import logging
import os
import sys

import pyperclip
import requests

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():

    url = 'https://gitignore.io/api/{}'
    print('Separate the projects separated by comma.')
    project_query = input("Enter project type : ")

    if project_query.strip() == '':
        os.system('touch .gitignore')
        logger.info('Empty gitignore created.')
        sys.exit(0)

    if ',' in project_query:
        projects = project_query.split(',')
        projects = [project.strip() for project in projects]
        project_query = ','.join(projects)

    url = url.format(project_query)

    request = requests.get(url)
    logger.info('Connecting to server ...')
    if request.status_code == 200 or request.ok:
        logger.info('Fetched successully.')

        print('\nEnter GitIgnore Loaction : \n1. File\n2. Clipboard')
        try:
            choice = int(input('Enter (1 / 2) : '))
            if choice == 1:
                with open('.gitignore', 'w') as file_ptr:
                    file_ptr.write(request.text)
                    logger.info(f'Stored in file at {os.getcwd()}/.gitignore')
            if choice == 2:
                pyperclip.copy(request.text)
                logger.info(".gitignore added to Clipboard.")
        except ValueError:
            logger.error('Invalid Choice')

    else:
        logger.error("Please specify correct project type.")


if __name__ == '__main__':
    main()
