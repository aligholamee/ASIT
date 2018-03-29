from setuptools import setup

setup(
    name = 'pysys',
    packages = ['pysys'],
    version = '0.1',
    description = 'Python library to extract machine resources information',
    author = 'Ali Gholami', 
    author_email = 'aligholami7596@gmail.com',
    url = 'https://github.com/aligholamee/pysys',
    keywords = 'SYSTEM INFO CPU MEMORY OS PYTHON',
    platforms = ["any"],
    install_requires = [
        'codecov'
    ],
    python_requires = '>3.5',
    license = 'MIT'
)
