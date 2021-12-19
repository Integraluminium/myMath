from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "My fist Python package"
LONG_DESCRIPTION = "Math module, which is my first Python package"

setup(
    name="myMath",
    version=VERSION,
    author="Integraluminium",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    # install_requires=['sys', 'math'],
    keywords=["myMath", "first package"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

    ]

)
