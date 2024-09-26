from setuptools import setup, find_packages

setup(
    name="pydaggerjl",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "juliacall",
    ],
    author="Julian P Samaroo",
    author_email="jpsamaroo@gmail.com",
    description="A Python interface to Dagger.jl",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jpsamaroo/pydaggerjl",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
