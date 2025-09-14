""" import os

import eel

eel.init('www')

os.system('open GoogleChrome.exe --app=http://localhost:8000/index.html')

eel.start('index.html', mode=None, host='localhost', block=True) """

import os
import time
import eel

# Initialize Eel (but you are using Live Server at port 5500, so no need to run eel server)
eel.init('www')

# Wait 1 sec so that your Live Server is ready (optional if you are using VS Code live server)
time.sleep(1)

# URL you want to open
url = "http://127.0.0.1:5500/www/index.html"

# Open Chrome in app mode (macOS)
os.system('open -na "Google Chrome" --args --app="http://127.0.0.1:5500/www/index.html"')
