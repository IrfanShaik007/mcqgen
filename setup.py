from setuptools import setup, find_packages
setup(
    name="mcqgenerator",
    version="0.1.0",
    author="Shaik Irfan",
    author_email="Irfanshareefs067@gmail.com",
    install_requires=["langchain","langchain-google-genai","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
