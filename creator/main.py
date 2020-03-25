import pyperclip
import requests

URL = 'https://gitignore.io/api/{}'
project_query = input("Enter project type : ")
URL = URL.format(project_query)

request = requests.get(URL)
if request.status_code == 200 or request.ok:
    pyperclip.copy(request.text)
    print(".gitignore added to Clipboard.")
else:
    print("Please specify correct project type.")

f = open('.gitignore', 'w+')
f.write(request.text)
f.close()
