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
        self.extract_variables()
        self.extract_declaration()
        
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
            return self.declaration == other.declaration and (all(var in other.variables for var in self.variables) and all(var in self.variables for var in other.variables))
        return False


