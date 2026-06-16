from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="sensor",
    version="0.0.1",
    author="Vivek Sasane",
    author_email="viveksasane9978@gmail.com",
    description="End-to-End Sensor Fault Detector Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Viveksasane/Sensor_Fault_Detector",

    package_dir={"": "src"},
    packages=find_packages(where="src"),

    install_requires=get_requirements("requirements.txt"),

    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
)