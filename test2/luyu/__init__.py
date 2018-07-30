import os
print("luyu__init__.py:",os.getcwd())
print(__path__)

from .module2 import *
from .module3 import *

# import module2
# from .module2 import test as module2test
# from .module3 import filepath as module3filepath
# import module1
# import imp
# imp.reload(module1)

# __all__ = ['module2']
# import module2
# import luyu.module2