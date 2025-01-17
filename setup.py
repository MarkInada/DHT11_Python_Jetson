from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dht11j",
    version="0.1.0",
    author="MarkInada",
    author_email="",
    description="Pure Python library for reading DHT11 sensor on Jetson Nano",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkInada/DHT11_Python_Jetson",
    packages=find_packages(),
    install_requires=["Jetson.GPIO"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
