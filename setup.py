import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="danecode",
    version="0.0.6",
    author="Moship",
    author_email="opensource@moship.io",
    description="A simple util to get dane codes by department and municipality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moship",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "jellyfish"
    ]
)