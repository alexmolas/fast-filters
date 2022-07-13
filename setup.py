import re
from setuptools import setup

with open("fast_filters/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


setup(version=version)
