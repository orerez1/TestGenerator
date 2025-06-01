import sys
import os

from Src.generateClass import generateClass
from Util import Templates

def create_tests_recursively(path_param: str) -> None:
    """
    Recursively generates test cases for Java classes within a directory.

    This function traverses through the given directory path and its subdirectories,
    generating test cases for each Java class file found. It skips directories and files
    specified in the excluded folders list.

    Args:
        path_param (str): The path of the directory to process for Java class files.

    Notes:
        - Directories listed in Templates.excluded_folders are skipped.
        - Test generation is initiated by calling generateClass on each Java file found.
    """

    directory_name = path_param.split(Templates.separator)[-1]
    if directory_name in Templates.excluded_folders:
        print(f"Skipping excluded folder: {directory_name}")
        return # If it's the tests folder, we can skip it
    for item in os.listdir(path=path_param):
        try:
            item_path = path_param + Templates.separator + item
            if os.path.isdir(item_path) and item not in Templates.excluded_folders:
                print(f"Recursively creating tests for: {item_path} directory")
                create_tests_recursively(item_path)
            elif item in Templates.excluded_folders:
                print(f"Skipping excluded folder: {item_path}")
            elif item.endswith(".java"):
                print(f"Generating tests for: {item_path} class")
                generateClass(item_path)
        except Exception as e:
            print(e)

if sys.argv.__len__() > 1:
    path_param = sys.argv[1]
    if os.path.isdir(path_param):
        # If it's a directory, we can create tests recursively
        create_tests_recursively(path_param)
    else:
        # If it's a file, we can create tests for that specific file
        generateClass(path_param)
else:
    print("Error! Cannot create relevant tests without a given file path!")