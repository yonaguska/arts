import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arts",
    version="0.0.1",
    author="Kirk Franks",
    author_email="kirk@theatrolabs.com",
    description="An Automated Regrassion Test System (ARTS)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yonaguska/arts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
)
