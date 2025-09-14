import os

import eel

eel.init('www')

os.system('open -a "Google Chrome" --args --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)