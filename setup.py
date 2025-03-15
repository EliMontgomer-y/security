from setuptools import setup, find_packages

setup(
    name="security",
    version="1.0.0",
    description="A simple encryption and decryption tool using the cryptography library.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=["cryptography>=3.4"],  # Ensures cryptography is installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)