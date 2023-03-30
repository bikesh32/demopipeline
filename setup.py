from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author= "Bikesh",
      author_email="bikeshsingh023@gmail.com",
      packages = find_packages(),
      install_rquires = ["pandas","numpy","flask"]
      )