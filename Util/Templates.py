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
path_to_test_classes = path_to_project + tests_folder_name + separator + "testClasses" + separator + "CLASS_NAMETest.java"

standard_test = """\t@Test
\tpublic void testFUNCTION_IN_NAMEStandardTEST_NUMBER() {
\t\tfinal String EXPECTED = ?;
\t\tPARAMS
\t\tfinal String RESULT = new CLASS_NAME().FUNCTION(SENDING_PARAMS);
\t\tassertEquals(EXPECTED, RESULT);
\t}"""

edge_case_test = """\t@Test
\tpublic void testFUNCTION_IN_NAMENonStandardPARAM_NAMETEST_NUMBER() {
\t\tfinal String EXPECTED = ?;
\t\tPARAMS
\t\tfinal String RESULT = new CLASS_NAME().FUNCTION(SENDING_PARAMS);
\t\tassertEquals(EXPECTED, RESULT);
\t}"""
    
null_case_test = """\t@Test
\tpublic void testFUNCTION_IN_NAMENullParamTEST_NUMBER() {
\t\tfinal String EXPECTED = ?;
\t\tPARAMS
\t\tfinal String RESULT = new CLASS_NAME().FUNCTION(SENDING_PARAMS);
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
    
tests_class = """package testClasses;

import org.testng.annotations.*;
import static org.testng.Assert.*;

public class CLASS_NAMETest {
    BEFORE
    TEAR_DOWN
    TESTS
}
"""


