from Util import Config
from Util import Templates
from Representations.JavaClassRepresentation import JavaClassRepresentation
from Representations.JavaFunctionRepresentation import JavaFunctionRepresentation


import os

def capitalize_first_letter(text: str):
    """
    Capitalize the first letter of a given text.

    Args:
        text (str): The input text to capitalize.

    Returns:
        str: The capitalized text.
    """
    if not text:
        return text
    return text[0].upper() + text[1:]

def create_test_params(func: JavaFunctionRepresentation):
    # type: (JavaFunctionRepresentation) -> str
    """
    Create test parameters based on the JavaFunctionRepresentation object.

    Args:
        func (JavaFunctionRepresentation): An object representing a Java function.

    Returns:
        (str): A string containing the final test parameters based on the function's parameters.
    """

    result = ""
    for param in func.params.keys():
        final_param_text = (
            Templates.final_param_for_test.replace(
                "PARAM_TYPE", func.params[param]
            ).replace("PARAM_NAME", param)
            + "\n"
        )
        result += (
            final_param_text
            if "\t\t" in final_param_text
            else "\t\t" + final_param_text
        )
    return result


def create_sending_params(test_params):
    # type: (str) -> str
    params = [
        param.split(" ")[2] for param in test_params.split(" = ") if "final" in param
    ]

    return ", ".join(params)


def create_standard_test(func: JavaFunctionRepresentation, class_name: str, test_params: str):
    # type: (JavaFunctionRepresentation, str, str) -> str
    function_name = capitalize_first_letter(func.name)
    function_tests = ""
    for number in range(1, Config.number_of_standard_tests_per_function + 1):
        sending_params = create_sending_params(test_params=test_params)
        function_tests += (
            Templates.standard_test.replace(
                "FUNCTION_IN_NAME", capitalize_first_letter(function_name)
            )
            .replace("FUNCTION", func.name)
            .replace("TEST_NUMBER", str(number))
            .replace("CLASS_NAME", class_name)
            .replace("\t\tPARAMS\n", test_params)
            .replace("SENDING_PARAMS", sending_params)
            .replace("RETURN_TYPE", func.return_type)
        )
        function_tests += "\n\n"
    return function_tests[:-2]


def create_edge_case_test(
    func: JavaFunctionRepresentation, class_name: str, test_params: str
):
    # type: (JavaFunctionRepresentation, str, str) -> str
    function_name = capitalize_first_letter(func.name)
    function_tests = ""
    for param in func.params.keys():
        for number in range(1, Config.number_of_edge_case_tests_per_function_parameter + 1):
            param_name = capitalize_first_letter(param)
            sending_params = create_sending_params(test_params=test_params)
            function_tests += (
                Templates.edge_case_test.replace("FUNCTION_IN_NAME", function_name)
                .replace("FUNCTION", func.name)
                .replace("TEST_NUMBER", str(number))
                .replace("CLASS_NAME", class_name)
                .replace("\n\t\tPARAMS\n", "\n" + test_params)
                .replace("PARAM_NAME", param_name)
                .replace("SENDING_PARAMS", sending_params)
                .replace("RETURN_TYPE", func.return_type)
                + "\n\n"
                )

    return function_tests[:-2]


class TestCreator:
    project_name = ""
    full_text = ""
    class_representation = None

    # todo: documentation

    def create_tests(self):
        tests = ""
        first = True
        for func in self.class_representation.functions:
            test_params = create_test_params(func=func)
            if func.return_type != "void":
                test = create_standard_test(
                    func=func,
                    class_name=self.class_representation.name,
                    test_params=test_params,
                )
                if not first:
                    test = "\n" + test
                else:
                    first = False
                tests += "\n" + test

        first = True
        for func in self.class_representation.functions:
            test_params = create_test_params(func=func)
            if func.return_type != "void":
                test = create_edge_case_test(
                    func=func,
                    class_name=self.class_representation.name,
                    test_params=test_params,
                )
                if not first:
                    test = "\n" + test
                else:
                    first = False
                tests += "\n" + test

        
        return tests

    # todo: documentation

    def create_test_classes_dir(self):
        dir = Templates.separator + Templates.tests_folder_name
        path_to_dir, end_dir = Templates.path_to_test_classes.replace(
            "PROJECT_NAME", self.project_name
        ).split(dir + Templates.separator)
        path_to_dir += dir
        end_dir = (
            Templates.separator + end_dir.split(Templates.separator + "CLASS_NAME")[0]
        )
        if not os.path.exists(path_to_dir):
            os.mkdir(path_to_dir)


    # todo: documentation and code
    def create_file(self):
        self.create_test_classes_dir()
        result = (
            Templates.tests_class.replace("TESTS", self.create_tests())
            .replace("BEFORE", Templates.before_test_function)
            .replace("TEAR_DOWN", Templates.tear_down_function)
            .replace("CLASS_NAME", self.class_representation.name)
            .replace("PROJECT_NAME", self.project_name.upper())
        )

        folder = Templates.path_to_test_classes.replace(
            "PROJECT_NAME", self.project_name
        ).split(Templates.separator + "CLASS_NAME")[0]

        if not os.path.exists(folder):
            os.mkdir(folder)
        f = open(
            Templates.path_to_test_classes.replace(
                "PROJECT_NAME", self.project_name
            ).replace("CLASS_NAME", self.class_representation.name),
            "w",
        )
        f.write(result)

    def __init__(self, project_name: str, full_text: str):
        # type: (str, str, str) -> None
        self.full_text = full_text
        self.class_representation = JavaClassRepresentation(full_text=full_text)
        self.project_name = project_name
