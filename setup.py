from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Fredy Somy",
    author_email="fredysomy@gmail.com",
    python_requires=">=3",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="A Python JSON and/or YAML based lightweight Database.",
    install_requires=["fire", "beautifultable", "filelock"],
    license="MIT License",
    long_description=readme,
    long_description_content_type="text/markdown",
    version="1.1.6",
    keywords="pysondb,database,json,yaml",
    name="pysondb",
    packages=["pysondb"],
    entry_points={"console_scripts": ["pysondb=pysondb.cli:main"]},
    setup_requires=[],
    url="https://github.com/fredysomy/pysonDB",
    zip_safe=False,
)
