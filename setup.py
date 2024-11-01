from setuptools import setup, find_packages

setup(
    name="algofromscratch",
    version="0.1.0",
    description="A collection of machine learning algorithms implemented from scratch",
    author="Dhayananth B",
    author_email="dhayananthtn@gmail.com.com",  # Replace with your email
    url="https://github.com/DhayananthB/algofromscratch",  # Replace with your GitHub URL
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        "numpy",  # List dependencies here
        "scipy",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
