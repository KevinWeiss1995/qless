from setuptools import setup, find_packages

setup(
    name="qless",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.20.0",  
        "typing-extensions>=4.0.0",
    ],
    entry_points={
        'console_scripts': [
            'qless=qless.cli:main',
        ],
    },
    python_requires=">=3.7",
    description="Q-Less game solver.",
    author="Kevin Weiss",
    author_email="kjweiss1995@gmail.com",
    url="https://github.com/KevinWeiss1995/qless",
) 