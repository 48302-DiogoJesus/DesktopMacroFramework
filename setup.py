from setuptools import setup

# Read requirements from requirements.txt
with open('requirements.txt', 'r') as file:
    requirements = file.read().splitlines()

print("Requirements HE", requirements)

setup(
    name='DesktopAutomationFramework', 
    version='0.0.1',  
    include_dirs=["automation", "framework"],
    install_requires=requirements
)
