import re

from Util import Regexs
from Representations.JavaFunctionRepresentation import JavaFunctionRepresentation


def get_is_singleton(java_class: str) -> bool:
    """
    Checks if a given Java class is a Singleton.

    Args:
        java_class (str): The Java class to check.

    Returns:
        bool: Whether the class is a Singleton or not.
    """
    try:
        private_constructor = re.search(Regexs.find_private_constructor, java_class)
        get_instance_method = re.search(Regexs.find_get_instance_method, java_class)
        static_instance = re.search(Regexs.find_static_instance, java_class)
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

    return bool(private_constructor and get_instance_method and static_instance)


# This class represents a Java class in Python.
class JavaClassRepresentation:
    """
    Represents a Java class and provides methods to extract its properties.

    Attributes:
        full_text (str): The full text of the Java class.
        text (str): The text of the Java class without nested classes.
        classes (list): A list of nested classes.
        functions (list[JavaFunctionRepresentation]): A list of functions in the Java class.
        full_lines (list[str]): A list of lines in the full text of the Java class.
        is_static (bool): Whether the Java class is static.
        name (str): The name of the Java class.
        declaration (str): The declaration of the Java class.
        is_singleton (bool): Whether the Java class is a Singleton.

    Methods:
        form_lines(lines: list) -> str: Concatenates a list of lines into a single string with each line separated by a newline character.
        remove_nested_classes(class_text: str, class_list: list) -> str: Removes the nested classes specified in the class_list from the given class_text.
    """
    
    full_text = ""
    text = "" 
    classes: list
    functions: list[JavaFunctionRepresentation]
    full_lines: list[str]
    is_static = None
    name = ""
    declaration = ""
    is_singleton = False
    
    @staticmethod
    def form_lines(lines: list) -> str:
        """
            Concatenates a list of lines into a single string with each line separated by a newline character.

            Parameters:
            - lines (list): A list of lines to concatenate.

            Returns:
            - str: A string containing all the lines concatenated with newline characters.
        """
        
        result = ""
        for line in lines:
            result += line + "\n"
        return result
    
    @staticmethod
    def remove_nested_classes(class_text: str, class_list: list) -> str:
        """
            Removes the nested classes specified in the class_list from the given class_text.

            Parameters:
            - class_text (str): The text of the class to remove nested classes from.
            - class_list (list): A list of nested classes to remove from the class_text.

            Returns:
            - str: The class_text with the nested classes removed.
        """
        
        for c in class_list:
            class_text = class_text.replace(c, "")
        return class_text     
    def extract_declaration(self) -> None:
        """
            Extracts the class declaration line from the full lines of the JavaClassRepresentation object.

            This method iterates through the full lines and assigns the first line containing " class " to the 'declaration' attribute of the JavaClassRepresentation object.
        """
        for line in self.full_lines:
            if " class " in line:
                self.declaration = line
                break
    
    def extract_classes(self) -> None:
        """
            Extracts nested classes from the full text of the JavaClassRepresentation object.

            This method finds and processes nested class declarations within the full text, updating the 'classes' attribute accordingly.
        """
        
        class_declarations = re.findall(Regexs.find_classes_declarations, self.full_text)
        class_list = []
        for declaration in class_declarations:
            spaces = re.split(Regexs.find_access_type, declaration)[0]
            declaration_index = self.full_lines.index(declaration)
            closing_brackets_index = self.full_lines[declaration_index:].index(spaces + '}') + declaration_index
            class_list.append(self.form_lines(lines=self.full_lines[declaration_index:closing_brackets_index]) + spaces + "}")
        self.classes = []
        if class_declarations.__len__() > 1:
            self.text =  self.remove_nested_classes(class_text=class_list[0], class_list=class_list[1:])
            for nested_class in class_list[1:]:
                self.classes.append(JavaClassRepresentation(nested_class))
        else:
            self.text = ""
            for line in self.full_lines[declaration_index:]:
                self.text += line + "\n"
    
    def extract_functions(self) -> None:
        """
            Extracts functions from the JavaClassRepresentation object's text.

            This method searches for function declarations in the text of the JavaClassRepresentation object, processes them, and adds JavaFunctionRepresentation objects to the 'functions' attribute.

            No parameters are required for this method.

            This method does not return any value.
        """
        self.functions = []
        functions_declarations = re.findall(Regexs.find_functions, self.text)
        for declaration in functions_declarations:
            declaration = re.split(r'\n', declaration)[0]
            if re.search(Regexs.find_access_type, declaration):
                spaces = re.split(Regexs.find_access_type, declaration)[0]
                declaration_index = self.lines.index(declaration)
                try:
                    closing_brackets_index = self.lines[declaration_index:].index(spaces + '}') + declaration_index
                    self.functions.append(JavaFunctionRepresentation(self.form_lines(lines=self.lines[declaration_index:closing_brackets_index]) + spaces + "}"))
                except ValueError as e:
                    print("Indentation error found in the closing bracket of the \"" + declaration.split("(")[0].split(" ")[-1] + "\" function.")
                    print("This function will be ignored as a result")
    
    def extract_name_from_declaration(self, declaration: str) -> None:
        """
            Extracts the name from the given declaration string.

            Parameters:
            - declaration (str): The declaration string to extract the name from.

            Returns:
            - None
        """
        
        declaration_parts = declaration.split(" ")
        while '' in declaration_parts:
            declaration_parts.remove('')
        name_index = 2 if 'static' not in declaration_parts else 3
        self.name = declaration_parts[name_index]
        
    def __init__(self, full_text: str) -> None:
        """
            Initializes a JavaClassRepresentation object with the provided full text of the Java class.

            Parameters:
            - full_text (str): The full text of the Java class.
        """
        
        # part 1 - getting the members from the parameters
        self.full_text = full_text
        
        # part 2 - calling setup functions that others depend on
        self.full_lines = self.full_text.split('\n')
        self.extract_declaration()
        self.extract_classes()
        self.is_singleton = get_is_singleton(full_text)
        
        # part 4 - calling initiating functions that depend on previous functions
        self.lines = self.text.split('\n')
        self.extract_functions()
        self.is_static = 'static' in self.declaration.split(" ")
        self.extract_name_from_declaration(self.declaration)
    
        
    
            
        