import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="danecode",
    version="0.2.7",
    author="santiagofep",
    description="A simple util to get dane codes by department and municipality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"danecode": ["files/**", "services/**"]},
    python_requires=">=3.6",
    install_requires=["jellyfish", "pandas", "unidecode"],
)
