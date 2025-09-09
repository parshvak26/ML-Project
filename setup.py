
from setuptools import find_packages, setup
from typing import List


hyphen_e_dot = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return list of requirement
    '''
    requirement =[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n', '') for req in requirement]

    if hyphen_e_dot in requirement:
        requirement.remove(hyphen_e_dot)

    return requirement


setup(
name='mlproject',
version='0.0.1',
author='Parshva',
author_email= 'parshvakarani26@gmail.com',
packages=find_packages(),
install_required=get_requirements('requirements.txt')

)