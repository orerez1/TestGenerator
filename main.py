import sys

from Src.TestCreator import TestCreator
from Util import Templates
if True or sys.argv.__len__() > 1:
    path_param = sys.argv[1]
    print(path_param)
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
    
else:
    print("Error! Cannot create relevant tests without a given file path!")