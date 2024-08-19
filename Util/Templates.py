import platform
import sys
# import os
# idea_projects_path = os.getcwd()  # Example. fill with the path to your "IdeaProjects" directory


os_name = platform.system().lower()
separator = "\\" if os_name.__contains__("windows") else "/"   # Designed for Windows and Linux
path_param = sys.argv[1]
idea_projects_path = path_param[1].split("IdeaProjects" + separator)[0] + "IdeaProjects" + separator
path_to_project = idea_projects_path + separator + "PROJECT_NAME" + separator
path_to_test_classes = path_to_project + "testClasses" + separator + "CLASS_NAMETest.java"

standard_test = """
    @Test
    public void testFUNCTION_IN_NAMEStandardTEST_NUMBER() {
        final String EXPECTED = ?;
        PARAMS
        final String RESULT = new CLASS_NAME().FUNCTIONS(SENDING_PARAMS);
        assertEquals(EXPECTED, RESULT);
    }"""

edge_case_test = """
    @Test
    public void testFUNCTION_IN_NAMENonStandardTEST_NUMBER() {
        final String EXPECTED = ?;
        PARAMS
        final String RESULT = new CLASS_NAME().FUNCTIONS(SENDING_PARAMS);
        assertEquals(EXPECTED, RESULT);
    }"""
    
null_case_test = """
    @Test
    public void testFUNCTION_IN_NAMENullParamTEST_NUMBER() {
        final String EXPECTED = ?;
        PARAMS
        final String RESULT = new CLASS_NAME().FUNCTIONS(SENDING_PARAMS);
        assertEquals(EXPECTED, RESULT);
    }"""
    
expected_error_test = """
    @Test(expectedExceptions = EXCEPTION.class)
    public void testFUNCTION_IN_NAMEThrowsEXCEPTION() {
        new CLASS_NAME(?).FUNCTION(?);
    }"""
    
final_param_for_test = "final PARAM_TYPE PARAM_NAME = ?;"

tear_down_function = """
    @AfterMethod
    public void tearDown() {

    }"""

before_test_function = """
    @BeforeTest
    public void beforeTest() {
        
    }"""
    
tests_class = """package testClasses;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import static org.testng.Assert.*;

public class CLASS_NAMETest {
    BEFORE
    
    TEAR_DOWN
    
    TESTS
}
"""


