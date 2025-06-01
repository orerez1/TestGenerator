find_classes_declarations = r'.*class .*[{]'# Matches class declarations in Java, e.g., "public class MyClass { ... }"
find_functions = r'.*[(].*[)].*\{[^}]*}'# Matches function declarations in Java, e.g., "public void myFunction() { ... }"
find_parameters = r'(?<=\()[^)]*(?=\))'# Matches function parameters in Java, e.g., "(int x, String y)"
find_access_type = r'public|private|protected'# Matches access types in Java, e.g., "public", "private", "protected"
find_private_constructor = r'private\s+\w+\s*\(\)'# Matches private constructor declarations, e.g., "private MyClass()"
find_get_instance_method = r'static\s+\w+\s+getInstance\s*\(\)'# Matches static getInstance() method
find_static_instance = r'private\s+static\s+\w+\s+\w+\s*;'# Matches static instance variable declarations, e.g., "private static MyClass instance;"
find_function_variable_types_from_test = r'final\s+(\w+)\s+(\w+)\s*='# Matches final variable declarations in tests, e.g., "final int x = 5;"
find_tests_within_test_class = r'@Test\s+public\s+void\s+\w+\s*\([\s\S]*?\}'# Matches @Test public void methodName() { ... }