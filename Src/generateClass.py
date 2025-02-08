from Src.TestCreator import TestCreator
from Util import Templates

def generateClass(path_param):
    path = path_param.split(f"IdeaProjects{Templates.separator}")[1].split(Templates.separator)
    try:
        with open(path_param, 'r') as f:
            class_full_text = f.read()      
    except Exception as e:
        print(e)

    project_name = path[0]
    test_creator = TestCreator(project_name, class_full_text)
    test_creator.create_file()
    print("Done!")
        
    
        
