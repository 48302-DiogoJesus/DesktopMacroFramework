from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt', 'r') as file:
    requirements = file.read().splitlines()

print("Requirements HE", requirements)

setup(
    name='DesktopAutomationFramework', 
    version='0.0.1',  
    packages=find_packages(),
    install_requires=requirements
)
