from Util import Config
from Util import Templates
from Representations.JavaClassRepresentation import JavaClassRepresentation
from Representations.JavaFunctionRepresentation import JavaFunctionRepresentation


import os


def capitalize_first_letter(text: str) -> str:
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


def create_test_parameters(java_function: JavaFunctionRepresentation) -> str:
    """
    Create test parameters based on the JavaFunctionRepresentation object.

    Args:
        java_function (JavaFunctionRepresentation): An object representing a Java function.

    Returns:
        str: A string containing the final test parameters based on the function's parameters.
    """

    result = ""
    for parameter_name in java_function.params.keys():
        final_param_text = (
            Templates.final_param_for_test.replace(
                "PARAM_TYPE", java_function.params[parameter_name]
            ).replace("PARAM_NAME", parameter_name)
            + "\n"
        )
        result += (
            final_param_text
            if "\t\t" in final_param_text
            else "\t\t" + final_param_text
        )
    return result


def create_sending_params(test_params: str) -> str:
    """
    Create sending parameters from test parameters.

    Args:
        test_params (str): A string containing test parameters.

    Returns:
        str: A string containing only the parameters marked as "final".
    """

    params = [
        param.split(" ")[2] for param in test_params.split(" = ") if "final" in param
    ]

    return ", ".join(params)


def create_standard_tests_for_function(
    func: JavaFunctionRepresentation,
    class_name: str,
    test_params: str,
    is_singleton: bool,
) -> str:
    """
    Generates multiple standard test templates for a Java function.

    Args:
        func (JavaFunctionRepresentation): The Java function representation object.
        class_name (str): The name of the class containing the function.
        test_params (str): A string containing test parameters.
        is_singleton (bool): Indicates if the class is a Singleton.

    Returns:
        str: A string containing multiple formatted Java test methods.
    """

    function_name = capitalize_first_letter(func.name)
    function_tests = ""
    for number in range(1, Config.number_of_standard_tests_per_function + 1):
        sending_params = create_sending_params(test_params=test_params)
        function_tests += Templates.create_standard_test(
            function_in_name=function_name,
            test_number=number,
            return_type=func.return_type,
            class_name=class_name,
            java_function=func.name,
            sending_params=sending_params,
            params=test_params,
            is_singleton=is_singleton,
        )
    return function_tests


def create_edge_case_test_for_function(
    func: JavaFunctionRepresentation,
    class_name: str,
    test_params: str,
    is_singleton: bool,
) -> str:
    """
    Generates edge case test templates for a Java function.

    Args:
        func (JavaFunctionRepresentation): The Java function representation object.
        class_name (str): The name of the class containing the function.
        test_params (str): A string containing test parameters.
        is_singleton (bool): Indicates if the class is a Singleton.

    Returns:
        str: A string containing formatted Java test methods.
    """

    function_name = capitalize_first_letter(func.name)
    function_tests = ""
    for param in func.params.keys():
        for number in range(
            1, Config.number_of_edge_case_tests_per_function_parameter + 1
        ):
            param_name = capitalize_first_letter(param)
            sending_params = create_sending_params(test_params=test_params)
            function_tests += Templates.create_edge_case_test(
                function_in_name=function_name,
                param_name=param_name,
                test_number=number,
                return_type=func.return_type,
                class_name=class_name,
                java_function=func.name,
                sending_params=sending_params,
                params=test_params,
                is_singleton=is_singleton,
            )

    return function_tests


class TestCreator:
    """
    Creates test cases and test classes for a Java class.

    This class provides methods to generate standard and edge case test templates for each function in the Java class representation. It also handles the creation of test classes directories and test files.

    Attributes:
        project_name (str): The name of the project.
        full_text (str): The full text of the Java class.
        class_representation (JavaClassRepresentation): The representation of the Java class.

    Methods:
        create_tests(): Generates test templates for each function in the Java class.
        create_test_classes_dir(): Creates the directory structure for test classes.
        create_file(): Creates the test file with the formatted test classes.
        __init__(): Initializes the TestCreator object with the project name and full text of the Java class.
    """

    project_name = ""
    full_text = ""
    class_representation = None

    def create_tests(self) -> str:
        """
        Generates test templates for each function in the Java class representation.

        Returns:
            str: A string containing formatted test templates for standard and edge case tests.
        """

        tests = ""
        for func in self.class_representation.functions:
            test_params = create_test_parameters(java_function=func)
            if func.return_type != "void":
                test = create_standard_tests_for_function(
                    func=func,
                    class_name=self.class_representation.name,
                    test_params=test_params,
                    is_singleton=self.class_representation.is_singleton,
                )
                tests += test

        for func in self.class_representation.functions:
            test_params = create_test_parameters(java_function=func)
            if func.return_type != "void":
                test = create_edge_case_test_for_function(
                    func=func,
                    class_name=self.class_representation.name,
                    test_params=test_params,
                    is_singleton=self.class_representation.is_singleton,
                )
                tests += test

        return tests

    def create_test_classes_dir(self) -> None:
        """
        Creates the directory structure for test classes.

        This method constructs the directory path for test classes based on the project name and class name. It then checks if the directory already exists and creates it if not present.
        """

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

    def create_file(self) -> None:
        """
        Creates a test file with formatted test classes.

        This method replaces placeholders in the test class template with actual test functions, setup, teardown, class name, and project name. It then creates the necessary directory structure for the test classes and writes the formatted test classes to a new file
        """

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

    def __init__(self, project_name: str, full_text: str) -> None:
        """
        Initializes the TestCreator object with the provided project name and full text of the Java class

        Parameters:
        - project_name (str): The name of the project.
        - full_text (str): The full text of the Java class.
        """

        self.full_text = full_text
        self.class_representation = JavaClassRepresentation(full_text=full_text)
        self.project_name = project_name
