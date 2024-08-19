import sys

from TestCreator import TestCreator
import Templates

if sys.argv.__len__() > 1:
    path_param = sys.argv[1]
    path = path_param.split("IdeaProjects" + Templates.separator)[1].split(Templates.separator)
    
else:
    print("Error! Cannot create relevant tests without a given file path!")