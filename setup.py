from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='dhana',
    author_email='dhanakeerthid3@gmail.com',
    install_requires=["huggingface_hub","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
) 