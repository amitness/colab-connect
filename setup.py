from setuptools import setup, find_packages

setup(
    name="colabtunnel",
    version="0.0.7",
    license="MIT",
    description="Connect to Google Colab VM locally from VSCode",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
    author="Amit Chaudhary",
    author_email="meamitkc@gmail.com",
    url="https://github.com/amitness/colab-tunnel",
    packages=find_packages(),
)
