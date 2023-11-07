from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt', 'r') as file:
    requirements = file.read().splitlines()

with open('version.txt', 'r') as file:
    version = file.read()

setup(
    name='DesktopAutomationFramework', 
    version=version,  
    packages=find_packages(),
    install_requires=requirements
)
