from distutils.core import setup

setup(name='GitIgnore Creator',
      version='0.1.0',
      description='Creates .gitignore file based on Project type.',
      author='Arjun Adhikari',
      author_email='arjunadhikari@protonmail.com',
      url='https://github.com/theArjun/gitignore-creator',
      packages=['src'],
      license='GPL v3',
      package_data={'src': ['description.txt']
                    },
      entry_points={
          'console_scripts': [
              'gitignore=src.main:main']
      },
      requires=['pyperclip', 'requests'],
      classifiers=[
          'Development Status :: 1 Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Version Control',
      ],
      )

if __name__ == "__main__":
    setup()
