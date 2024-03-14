from setuptools import find_packages
from setuptools import setup

with open("requirements_backend.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='musicbrain',
      version="0.0.1",
      description="Music Brain Model (api_pred)",
      license="MIT",
      author="Le Wagon",
      author_email="contact@lewagon.org",
      url="https://github.com/Jojoooo1/lewagon-final-project",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      include_package_data=True,
      zip_safe=False)
