from setuptools import setup

"""
author: anggelomos
github: https://github.com/anggelomos/pyshot
"""
with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="pyshot",
    url="https://github.com/anggelomos/pyshot",
    version="0.0.2",
    author="anggelomos",
    author_email="anggelomos@outlook.com",
    description="Pytest plugin to facilitate screenshot taking with selenium webdriver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3.8",
    ],
    license="MIT License",
    py_modules=["pyshot", "webdriver_proxy", "webelement_proxy"],
    package_dir={'': 'src'},
    keywords=[
        "pytest", "py.test", "pyshot", "screenshot", "selenium", "test", "plugin"
    ],
    install_requires=[
        "pytest",
        "selenium",
    ],
    entry_points={
        "pytest11": [
            "pyshot = pyshot",
        ]
    }
)
