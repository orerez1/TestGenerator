import sys

from Src.TestCreator import TestCreator
from Util import Templates
print("1. System arguments:")
print(sys.argv)
print("\n")
test_class_path = 'C:\\Users\\orkin\\IdeaProjects\\Testing\\src\\Exampleton .java'
if True or sys.argv.__len__() > 1:
    # path_param = sys.argv[1]
    path_param = test_class_path
    print("2. Isolated class path:")
    print(path_param)
    print("\n")
    path = path_param.split(f"IdeaProjects{Templates.separator}")[1].split(Templates.separator)
    print("3. Broken param:")
    print(path)
    print("\n")
    try:
        with open(path_param, 'r') as f:
            class_full_text = f.read()
        print("4. Class full text:")
        print(class_full_text)         
    except Exception as e:
        print(e)

    project_name = path[0]
    test_creator = TestCreator(project_name, class_full_text)
    print("5. TestCreator:")
    print(test_creator)
    test_creator.create_file()
    
else:
    print("Error! Cannot create relevant tests without a given file path!")