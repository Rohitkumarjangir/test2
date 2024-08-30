from setuptools import setup, find_packages

setup(
    name="my-package",
    version="0.0.1",
    packages=find_packages(),
    author="Rohit jangir",
    author_email="rohitkumarjangir79@gmail.com",
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "pyPDF2",
    ],
)