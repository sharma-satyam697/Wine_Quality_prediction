import setuptools

with open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()


REPO_NAME  = 'Ml_end_to_end_project'
AUTHER_USER_NAME = 'codedestructed007'
SRC_REPO = 'mlproject'
AUTHER_EMAIL = 'codexistslonglastingnotfog@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    author=AUTHER_USER_NAME,
    author_email=AUTHER_USER_NAME,
    description= "A small python package for machine learning app",
    long_description=long_description,
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    packages = setuptools.find_packages(where='src')

)
