import sys
import os

from Src.generateClass import generateClass

def create_tests_recursively(path_param):
    for item in os.listdir(path=path_param):
        try:    
            item_path = os.path.join(path_param, item)
            if os.path.isdir(item_path):
                create_tests_recursively(item_path)
            else:
                generateClass(item_path)
        except Exception as e:
            print(e)
    
if sys.argv.__len__() > 1:
    path_param = sys.argv[1]
    if os.path.isdir(path_param):
        create_tests_recursively(path_param)
    else:
        generateClass(path_param)
else:
    print("Error! Cannot create relevant tests without a given file path!")