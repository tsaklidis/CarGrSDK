import os
from shutil import copyfile
from .base import *


try:
    from .local import *
    main_hdrs = {
        'User-Agent': 'CarGrSDK v1.0',
    }
except ImportError as e:
    ans = input('local.py not found. Create with default values? y/n: ')
    if ans in ['y', 'Y', '']:
        path = os.path.dirname(os.path.abspath(__file__))
        copyfile(path + '/local.py.example', path + '/local.py')
        from .local import *
    else:
        quit('Crete your settings/local.py based on example file.')
