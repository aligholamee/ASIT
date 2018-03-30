from setuptools import setup

setup(
    name = 'sit',
    packages = ['sit'],
    version = '0.1',
    description = 'System Information Toolbox Python Library',
    author = 'Ali Gholami', 
    author_email = 'aligholami7596@gmail.com',
    url = 'https://github.com/aligholamee/sit',
    keywords = 'SYSTEM INFO CPU MEMORY OS PYTHON',
    platforms = ["any"],
    install_requires = [
        'codecov'
    ],
    python_requires = '>3.5',
    license = 'MIT'
)
