import platform
import sys
# import os
# idea_projects_path = os.getcwd()  # Example. fill with the path to your "IdeaProjects" directory

test_class_path = 'C:\\Users\\orkin\\IdeaProjects\\Testing\\src\\Weird.java'

os_name = platform.system().lower()
separator = "\\" if os_name.__contains__("windows") else "/"   # Designed for Windows and Linux
# path_param = sys.argv[1]
tests_folder_name = "tests"
path_param = test_class_path
idea_projects_path = path_param.split("IdeaProjects" + separator)[0] + "IdeaProjects" + separator
path_to_project = idea_projects_path + "PROJECT_NAME" + separator
path_to_test_classes = path_to_project + tests_folder_name + separator + "CLASS_NAMETest.java"


def create_standard_test(
    function_in_name: str, test_number: str, return_type: str,
    class_name: str, java_function: str, sending_params: str,
    params: str, is_singleton: bool) -> str:
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

    Returns:
        str: A formatted Java test method as a string.

    Notes:
        - If the function is "getInstance" or the same as the class name, an empty string is returned.
        - Handles both Singleton and non-Singleton class instantiation.
    """

    # returns an empty string if the function is "getInstance" or the same as the class name because we don't want to test constructors
    if java_function in ["getInstance", class_name]:
        return ""

    instance_call = f"{class_name}.getInstance" if is_singleton else f"new {class_name}"

    return f"""
\t@Test
\tpublic void test{function_in_name}Standard{test_number}() {{
\t\tfinal {return_type} EXPECTED = ?;
{params}
\t\tfinal {return_type} RESULT = {instance_call}().{java_function}({sending_params});
\t\tassertEquals(EXPECTED, RESULT);
\t}}\n"""


def create_edge_case_test(
    function_in_name: str, param_name: str, test_number: str,
    return_type: str, class_name: str, java_function: str,
    sending_params: str, params: str, is_singleton: bool) -> str:
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

    Returns:
        str: A formatted Java test method as a string.

    Notes:
        - If the function is "getInstance" or the same as the class name, an empty string is returned.
        - Handles both Singleton and non-Singleton class instantiation.
    """

    # returns an empty string if the function is "getInstance" or the same as the class name because we don't want to test constructors
    if java_function in ["getInstance", class_name]:
        return ""
    
    instance_call = f"{class_name}.getInstance" if is_singleton else f"new {class_name}"

    return f"""
\t@Test
\tpublic void test{function_in_name}EdgeCase{param_name}{test_number}() {{
\t\tfinal {return_type} EXPECTED = ?;
{params}
\t\tfinal {return_type} RESULT = {instance_call}().{java_function}({sending_params});
\t\tassertEquals(EXPECTED, RESULT);
\t}}\n"""


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
\tpublic void testFUNCTION_IN_NAMEThrowsEXCEPTION() {
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
