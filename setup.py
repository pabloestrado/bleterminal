from setuptools import setup, find_packages

setup(
    name="bleterminal",
    version="1.0.0",
    description="A command-line tool for interacting with BLE devices",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Pavlo Romaniuk",
    author_email="pabloestrado@gmail.com",
    url="https://github.com/pabloestrado/bleterminal",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "bleak",
        "prompt_toolkit"
    ],
    entry_points={
        "console_scripts": [
            "bleterminal=bleterminal.bleterminal:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
