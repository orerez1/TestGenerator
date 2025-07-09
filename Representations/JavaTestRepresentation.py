import re
from Util import Regexs
class JavaTestRepresentation:
    class JavaVariableRepresentation:
        def __init__(self, name: str, type: str) -> None:
            self.name = name
            self.type = type
        
        def __str__(self):
            return f"Type: {self.type}, Name: {self.name}"
        
        def __eq__(self, other):
            if isinstance(other, JavaTestRepresentation.JavaVariableRepresentation):
                return self.name == other.name and self.type == other.type
            return False
            
    def __init__(self, text: str) -> None:
        self.text = text
        self.variables = []
        self.declaration = ""
        self.function_name = ""
        self.extract_variables()
        self.extract_declaration()
        self.extract_function_name()
        
    def set_text(self, text: str) -> None:
        self.__init__(text)
        
    
    def extract_function_name(self) -> None:
        """
        Extracts the function name from the test text.
        
        This method uses a regex to find the function name in the test text and sets it to the 'function_name' attribute.

        Parameters: None
        Returns: None
        """
        matches = re.findall(Regexs.find_method_from_test, self.text)
        self.function_name = matches[2] if matches else ""
    
    def extract_variables(self) -> None:
        """
        Extracts the variables declared within a Java test method from the test text.

        This method uses a regex to find all variable declarations in the test text and then creates a new JavaVariableRepresentation for each match, adding it to the "variables" list.

        Parameters: None
        Returns: None
        """
        matches = re.findall(Regexs.find_function_variable_types_from_test, self.text)
        for match in matches:
            var_type, var_name = match
            self.variables.append(self.JavaVariableRepresentation(var_name, var_type))
            
    def extract_declaration(self) -> None: 
        """
        Extracts the declaration of a Java test method from the test text.
        This method sets the 'declaration' attribute of the JavaTestRepresentation object by extracting the second line of the test text (after splitting by newline characters).

        Parameters: None
        Returns: None
        """
        text_lines = self.text.split("\n")
        self.declaration = text_lines[1]
        
    def get_overloaded_num_from_declaration(declaration) -> int:
        """
        Extracts the number of overloaded methods from a Java test method declaration.

        This method counts the occurrences of the word "Overloaded" in the declaration string and returns that count.

        Parameters:
            declaration (str): The declaration string of a Java test method.

        Returns:
            int: The number of times "Overloaded" appears in the declaration.
        """
        return declaration.split("Overloaded")[1].index(0) if "Overloaded" in declaration else None
            
    def __eq__(self, other):
        """
        Checks if two JavaTestRepresentations are equal.

        This method checks if two JavaTestRepresentation objects are equal by comparing their declaration and variables.

        Parameters:
            other (JavaTestRepresentation): The other JavaTestRepresentation object to compare with.

        Returns:
            bool: True if the two objects are equal, False if not.
        """

        if isinstance(other, JavaTestRepresentation):
            overloaded_num_self = self.get_overloaded_num_from_declaration(self.declaration)
            all_variables_equal = (all(var in other.variables for var in self.variables) and all(var in self.variables for var in other.variables))
            if overloaded_num_self:
                overloaded_num_other = self.get_overloaded_num_from_declaration(other.declaration)
                if overloaded_num_other:
                    return self.function_name == other.function_name and all_variables_equal
            return self.declaration == other.declaration and all_variables_equal
        overloaded_num_other = self.get_overloaded_num_from_declaration(other)
        if overloaded_num_other:
            return other.split("Overloaded")[0] in self.declaration # checking if other is an overloaded version of the same test
        return other in self.declaration if isinstance(other, str) else False # if other is a string, compare with declaration directly
    
    def __str__(self):
        return f"Declaration: {self.declaration}, Function Name: {self.function_name}, Variables: {[str(var) for var in self.variables]}"


