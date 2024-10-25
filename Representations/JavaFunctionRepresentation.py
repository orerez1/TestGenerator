import re
from Util import Regexs

class JavaFunctionRepresentation:
    """
    Represents a Java function and provides methods to extract its properties.

    Attributes:
        full_text (str): The full text of the Java function.
        return_type (str): The type of the function's returned value.
        params (dict[str, str]): Function parameters, where the key is the parameter name and the value is its type.
        exceptions_thrown (list[str]): The exceptions that the function declares it could throw.
        declaration (str): The function's declaration.
        access_type (str): The function's access type (e.g. public, private, protected).
        is_static (bool): Whether the Java function is static.
        name (str): The name of the Java function.

    Methods:
        extract_params(): Extracts the function's parameters and saves them in the [params] attribute.
        extract_function_types(): Extracts the function's return type and access type and saves them in the `return_type` and `access_type` attributes.
        extract_exceptions(): Extracts the exceptions that the function declares it could throw and saves them in the `exceptions_thrown` attribute.
        extract_name(): Extracts the function's name and saves it in the [name] attribute.
    """
    
    full_text = ""  # The full text of the function
    return_type = ""  # The type of the function's returned value
    params = dict[str, str]  # Function parameters. The param's name would be the key and the value would be its type
    exceptions_thrown = list[str]  # The exceptions that the function declares it could throw
    declaration = ""  # The function's declaration
    access_type = ""  # The function's access type (eg. public, private, protected)
    is_static = False  # Represents whether the java function is static 
    name = ""  # The name of the java function      
    def extract_params(self):
        """
        This function extracts the parameters given to the function,
        turns it into a dictionary where the parameter's name is the key and its type is the value
        and then saves it int the "params" member
        """
        
        params = re.search(Regexs.find_parameters, self.declaration).group().split(", ")  # Extracting the parameters from the declaration
        try:
            if params[0] != '':  # The first parameter would be an empty string if the function doesn't receive parameters
                for param in params:
                    broken_param = param.split(" ")  # Splitting the parameter into its type and name
                    self.params[broken_param[1]] = broken_param[0]  # Saving the parameter with its name as the key and its type as the value
        except IndexError as e:
            print(e)

            
    def extract_function_types(self):
        """
        This function extracts the following pieces of information from a function's declaration and saves it into the mentioned members:
        - Whether the function is static -> "is_static"
        - Access type (public|private|protected) -> "access_type"
        - The type of the function's return value -> "return_type"
        """
        declaration_parts = self.declaration.split(" ")
        while declaration_parts.__contains__(''):  # There could be irrelevant spaces in the declaration which'll result in empty elements
            declaration_parts.remove('')  # Removing the empty string elements for easier navigation and use of the different parts
        
        for part in declaration_parts:  # Breaking down the declaration and getting the data for the relevant class members
            access = re.search(Regexs.find_access_type, part)  # Finding the access type with a regex
            if access:
                self.access_type = access.group()
                continue
            
            is_static = part.__contains__("static")
            if is_static:
                self.is_static = True
                continue
            
            if not is_static and not access and not part.__contains__('\t'):
                if self.is_static: 
                    declaration_parts.remove("static")
                declaration_parts.remove(declaration_parts[0])
                self.return_type = declaration_parts[0]
                if len(declaration_parts) >= 2 and declaration_parts[1].__contains__(">"):
                    self.return_type += f" {declaration_parts[1]}"
                break
        
        
    def extract_exceptions(self):
        """
        This function extracts intentional exception throws from the function's declaration
        and saves them in the "exceptions_thrown" member
        """
        
        if "throws" in self.declaration:
            exceptions = self.declaration.split("throws")[-1].split(", ")  # Separating the exceptions list from the declaration
            exceptions[0] = exceptions[0].replace(' ', '')  # Removing an irrelevant space created in the separation process
            self.exceptions_thrown = exceptions
            
    
    def extract_name(self):
        """
        This function extracts the name of the funciton from its declaration
        and saves it in the "name" member
        """
        
        self.name = self.declaration.split("(")[0].split(" ")[-1]
        
    def __init__(self, full_text: str) -> None:
        """
        An initiating function.
        Divided into 3 parts

        Args:
            full_text (str): The full text of the function
        """

        # # Part 1: Deep copying the lists and dictionaries so they'll get different pointers per instance
        self.params = {}
        self.exceptions_thrown = []
        
        # Part 2 Setting the parameters to the equivalent properties
        self.full_text = full_text
        self.declaration = full_text.split('\n')[0].split('{')[0]
        while self.declaration.__contains__('\t'):
            self.declaration = self.declaration.replace('\t', '')
        
        # Part 3: Calling the methods that initialize the rest of the properties based on the parameters received
        self.extract_params()
        self.extract_function_types()
        self.extract_exceptions()
        self.extract_name()