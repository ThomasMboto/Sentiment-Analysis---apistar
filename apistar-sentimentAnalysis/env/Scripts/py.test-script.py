#!"c:\Users\mbototh1\Desktop\Zip Files\struct\struct\apistar-master\env\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pytest==3.5.0','console_scripts','py.test'
__requires__ = 'pytest==3.5.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pytest==3.5.0', 'console_scripts', 'py.test')()
    )
