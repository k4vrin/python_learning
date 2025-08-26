from setuptools import setup, find_packages

setup(
    name="kavlibrary",                     # Package name
    version="0.1.0",                       # First version
    description="A simple book management library",  # Description
    author="Mostafa Hosseini",             # Your name
    packages=find_packages(),             # Automatically find all packages
    install_requires=[],                  # Add dependencies here if needed
    python_requires=">=3.8",              # Minimum Python version
)