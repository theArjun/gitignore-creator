import sys

import pyperclip
import requests


def main():
    url = 'https://gitignore.io/api/{}'
    print('Separate the projects by comma without spaces.')
    project_query = input("Enter project type : ")

    f = open('.gitignore', 'w+')

    if project_query.strip() == '':
        f.write('')
        print('Empty gitignore created.')
        f.close()
        sys.exit(0)

    if ',' in project_query:
        projects = project_query.split(',')
        projects = [project.strip() for project in projects]
        project_query = ','.join(projects)

    url = url.format(project_query)

    request = requests.get(url)
    if request.status_code == 200 or request.ok:
        pyperclip.copy(request.text)
        print(".gitignore added to Clipboard.")
    else:
        print("Please specify correct project type.")

    f.write(request.text)
    f.close()
    

if __name__ == '__main__':
    main()

