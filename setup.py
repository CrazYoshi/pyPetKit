import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypetkit",
    version="0.0.4",
    author="CrazYoshi",
    author_email="crazyoshi1186@gmail.com",
    description="PetKit python integration library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CrazYoshi/pypetkit",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
