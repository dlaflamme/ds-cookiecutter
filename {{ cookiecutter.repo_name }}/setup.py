from setuptools import setup

setup(name='{{ cookiecutter.repo_name }}',
      version='POC',
      url='https://github.com/rebuy-de/{{ cookiecutter.repo_name }}.git',
      author='{{ cookiecutter.author_name }}',
      author_email='{{ cookiecutter.email }}',
      packages=['src'],
      zip_safe=False)
