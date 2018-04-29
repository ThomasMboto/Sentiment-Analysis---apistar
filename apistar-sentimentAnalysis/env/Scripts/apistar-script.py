#!"c:\Users\mbototh1\Desktop\Zip Files\struct\struct\apistar-master\env\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'apistar==0.3.9','console_scripts','apistar'
__requires__ = 'apistar==0.3.9'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('apistar==0.3.9', 'console_scripts', 'apistar')()
    )
