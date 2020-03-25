import requests
import pyperclip

URL = 'https://gitignore.io/api/{}'
project_query = input("Enter project type : ")
URL = URL.format(project_query)

request = requests.get(URL)
if request.status_code == 200:
    pyperclip.copy(request.text)
    print(".gitignore added to Clipboard.")
else:
    print("Please specify correct project type.")

