import platform
import sys

test_class_path = sys.argv[1]

os_name = platform.system().lower()

separator = "/"
tests_folder_name = "tests"
path_param = test_class_path
idea_projects_path = (
    f"{path_param.split(f'IdeaProjects{separator}')[0]}IdeaProjects{separator}"
)

path_to_project = f"{idea_projects_path}PROJECT_NAME{separator}"
path_to_test_classes = (
    path_to_project + tests_folder_name + separator + "CLASS_NAMETest.java"
)


def get_instance_call(class_name: str, is_singleton: bool) -> str:
    """
    Returns the instance call for a given class name.

    Args:
        class_name (str): The name of the class.
        is_singleton (bool): Indicates if the class is a Singleton.

    Returns:
        str: The instance call for the given class name.
    """
    return f"{class_name}.getInstance" if is_singleton else f"new {class_name}"


def create_standard_test(
    function_in_name: str,
    test_number: str,
    return_type: str,
    class_name: str,
    java_function: str,
    sending_params: str,
    params: str,
    is_singleton: bool,
    existing_tests: str = None
) -> str:
    """
    Generates a standard test template for a given Java function.

    Args:
        function_in_name (str): The name of the function, capitalized for test method naming.
        test_number (str): A unique identifier for the test.
        return_type (str): The return type of the function being tested.
        class_name (str): The name of the class containing the function.
        function (str): The name of the function being tested.
        sending_params (str): The parameters to be passed to the function during the test.
        params (str): Additional test parameters.
        is_singleton (bool): Indicates if the class is a Singleton.
        existing_tests (str, optional): Existing tests to avoid duplicates. Defaults to None.

    Returns:
        str: A formatted Java test method as a string.

    Notes:
        - If the function is "getInstance" or the same as the class name, an empty string is returned.
        - Handles both Singleton and non-Singleton class instantiation.
    """
    declaration = "public void test{function_in_name}Standard{test_number}()"
    # used to determine whether the test is a duplicate

    # returns an empty string if the function is "getInstance" or the same as the class name because we don't want to test constructors
    # and we don't want to test the same function twice so we check if the existing tests already contain the declaration
    if java_function in ["getInstance", class_name] or (existing_tests is not None and existing_tests.__contains__(declaration)):
        return ""

    return f"""
\t@Test
\t{declaration} {{
\t\tfinal {return_type} EXPECTED = ?;
{params}
\t\tfinal {return_type} RESULT = {get_instance_call(class_name, is_singleton)}().{java_function}({sending_params});
\t\tassertEquals(EXPECTED, RESULT);
\t}}\n"""


def create_edge_case_test(
    function_in_name: str,
    param_name: str,
    test_number: str,
    return_type: str,
    class_name: str,
    java_function: str,
    sending_params: str,
    params: str,
    is_singleton: bool,
    existing_tests: str = None
) -> str:
    """
    Generates an edge case test template for a given Java function.

    Args:
        function_in_name (str): The name of the function, capitalized for test method naming.
        param_name (str): The name of the parameter associated with the edge case.
        test_number (str): A unique identifier for the test.
        return_type (str): The return type of the function being tested.
        class_name (str): The name of the class containing the function.
        function (str): The name of the function being tested.
        sending_params (str): The parameters to be passed to the function during the test.
        params (str): Additional test parameters.
        is_singleton (bool): Indicates if the class is a Singleton.
        existing_tests (str, optional): Existing tests to avoid duplicates. Defaults to None.

    Returns:
        str: A formatted Java test method as a string.

    Notes:
        - If the function is "getInstance" or the same as the class name, an empty string is returned.
        - Handles both Singleton and non-Singleton class instantiation.
    """

    # returns an empty string if the function is "getInstance" or the same as the class name because we don't want to test constructors
    if java_function in ["getInstance", class_name]:
        return ""
    
    # used to determine whether the test is a duplicate
    declaration = "public void test{function_in_name}EdgeCase{param_name}{test_number}()"
    return f"""
\t@Test
\t{declaration} {{
\t\tfinal {return_type} EXPECTED = ?;
{params}
\t\tfinal {return_type} RESULT = {get_instance_call(class_name, is_singleton)}().{java_function}({sending_params});
\t\tassertEquals(EXPECTED, RESULT);
\t}}\n""" if existing_tests is None or not existing_tests.__contains__(declaration) else ""


def create_null_edge_case_test(
    function_in_name: str,
    param_name: str,
    test_number: str,
    return_type: str,
    class_name: str,
    java_function: str,
    sending_params: str,
    params: str,
    is_singleton: bool,
    param_type: str,
    existing_tests: str = None
) -> str:
    """
    Generates a null edge case test template for a given Java function.

    Args:
        function_in_name (str): The name of the function, capitalized for test method naming.
        param_name (str): The name of the parameter associated with the null edge case.
        test_number (str): A unique identifier for the test.
        return_type (str): The return type of the function being tested.
        class_name (str): The name of the class containing the function.
        function (str): The name of the function being tested.
        sending_params (str): The parameters to be passed to the function during the test.
        params (str): Additional test parameters.
        is_singleton (bool): Indicates if the class is a Singleton.
        param_type (str): The type of the parameter associated with the null edge case.
        existing_tests (str, optional): Existing tests to avoid duplicates. Defaults to None.

    Returns:
        str: A formatted Java test method as a string.

    Notes:
        - If the function is "getInstance" or the same as the class name, an empty string is returned.
        - Handles both Singleton and non-Singleton class instantiation.
        - If the parameter is a primitive type, an empty string is returned.
    """

    # primitive types cannot be null
    primitive_types = [
        "boolean",
        "char",
        "byte",
        "short",
        "int",
        "long",
        "float",
        "double",
    ]
    

    # returns an empty string if the function is "getInstance" or the same as the class name because we don't want to test constructors
    if java_function in ["getInstance", class_name] or param_type in primitive_types:
        return ""

    # lower the param name to match the test method naming convention
    lowered_param_name = (
        param_name.lower()
        if len(param_name) <= 1
        else param_name.lower()[0] + param_name.lower()[1:]
    )

    # remove the test param from the test method parameters
    params = ";\n".join(
        [
            param
            for param in params.split(";\n")
            if param == ""
            or param.split(" = ")[-2].split(" ")[-1] != lowered_param_name
        ]
    )

    # replace the param name with null in the test method parameters
    sending_params = sending_params.replace(lowered_param_name, "null")
    
    # used to determine whether the test is a duplicate
    declaration = "public void test{function_in_name}NullParam{param_name}{test_number}()"
    
    return f"""
\t@Test
\t{declaration} {{
\t\tfinal {return_type} EXPECTED = ?;
{params}
\t\tfinal {return_type} RESULT = {get_instance_call(class_name, is_singleton)}().{java_function}({sending_params});
\t\tassertEquals(EXPECTED, RESULT);
\t}}\n""" if existing_tests is None or not existing_tests.__contains__(declaration) else ""


def create_exception_test(
    function_in_name: str,
    exception: str,
    class_name: str,
    java_function: str,
    sending_params: str,
    test_number: str,
    params: str,
    is_singleton: bool,
    existing_tests: str = None,
) -> str:
    """
    Generates an exception-throwing test template for a given Java function.

    Args:
        function_in_name (str): The name of the function, capitalized for test method naming.
        exception (str): The exception expected to be thrown.
        class_name (str): The name of the class containing the function.
        java_function (str): The name of the function being tested.
        sending_params (str): The parameters to be passed to the function during the test.
        test_number (str): A unique identifier for the test.
        params (str): Additional test parameters.
        is_singleton (bool): Indicates if the class is a Singleton.
        existing_tests (str, optional): Existing tests to avoid duplicates. Defaults to None.

    Returns:
        str: A formatted Java test method for exception throwing as a string.
    """

    # used to determine whether the test is a duplicate
    declaration = "public void test{function_in_name}Throws{exception}{test_number}()"
    return f"""
\t@Test(expectedExceptions = {exception}.class)
\t{declaration} {{
{params}
\t\t{get_instance_call(class_name, is_singleton)}().{java_function}({sending_params});
\t}}""" if existing_tests is None or not existing_tests.__contains__(declaration) else ""


standard_test = """\t@Test
\tpublic void testFUNCTION_IN_NAMEStandardTEST_NUMBER() {
\t\tfinal RETURN_TYPE EXPECTED = ?;
\t\tPARAMS
\t\tfinal RETURN_TYPE RESULT = new CLASS_NAME().FUNCTION(SENDING_PARAMS);
\t\tassertEquals(EXPECTED, RESULT);
\t}"""

edge_case_test = """\t@Test
\tpublic void testFUNCTION_IN_NAMEEdgeCasePARAM_NAMETEST_NUMBER() {
\t\tfinal RETURN_TYPE EXPECTED = ?;
\t\tPARAMS
\t\tfinal RETURN_TYPE RESULT = new CLASS_NAME().FUNCTION(SENDING_PARAMS);
\t\tassertEquals(EXPECTED, RESULT);
\t}"""

null_case_test = """\t@Test
\tpublic void testFUNCTION_IN_NAMENullParamTEST_NUMBER() {
\t\tfinal RETURN_TYPE EXPECTED = ?;
\t\tPARAMS
\t\tfinal RETURN_TYPE RESULT = new CLASS_NAME().FUNCTION(SENDING_PARAMS);
\t\tassertEquals(EXPECTED, RESULT);
\t}"""

expected_error_test = """\t@Test(expectedExceptions = EXCEPTION.class)
\tpublic void testFUNCTION_IN_NAMEThrowsEXCEPTIONTEST_NUMBER() {
\t\tnew CLASS_NAME(?).FUNCTION(?);
\t}"""

final_param_for_test = "final PARAM_TYPE PARAM_NAME = ?;"

tear_down_function = """
    @AfterMethod
    public void tearDown() {

    }"""

before_test_function = """
    @BeforeClass
    public void beforeClass() {

    }

	@BeforeMethod
	public void beforeMethod() {

	}"""

tests_class = """import org.testng.annotations.*;
import static org.testng.Assert.*;

public class CLASS_NAMETest {
    BEFORE
    TEAR_DOWN
    TESTS
}
"""

eof = """
    /*
        End of tests - do not edit. if this text is changed or deleted, the file will be overwritten during the next generation.
    */
"""