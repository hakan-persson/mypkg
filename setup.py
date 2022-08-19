import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    reqs = fr.read().strip().split('\n')


setuptools.setup(
    name="mypkg",
    version="0.1",
    author="Håkan Persson",
    author_email="hakan.persson@haninge.se",
    description="A public github-hosted python package for test, with dependency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hakan-persson/mypkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=reqs,
)
