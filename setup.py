from setuptools import find_packages,setup
from typing import List

HYPEN = '-e .'

def requirements(file_path:str) -> List:
    requirement_info = []
    with open(file_path) as file_info:
        file_read = file_info.readlines()
        requirement_info = [i.replace('/n','') for i in file_read]
    
    if HYPEN in requirement_info:
        requirement_info.remove(HYPEN)

    return requirement_info

setup(
    name='MNIST-Digitrecognition',
    author='Padmaraj',
    version='0.0.1',
    packages=find_packages(),
    install_requires= requirements('requirements.txt')
)