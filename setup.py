from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)-> List[str]:
    """
    this function will return the list of packages to be installed
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        for a in requirements:
            a =  a.replace("\n","")
        # requirements [ a.replace("\n","") for a in requirements ]


        if '-e .'in requirements:
            requirements.remove('-e .')

    return requirements



setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Sujith',
    author_email= ' narayanamsujith55@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)