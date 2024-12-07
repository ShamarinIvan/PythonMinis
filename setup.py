from setuptools import setup, Extension

module = Extension("foreign", sources=["13_mini.c"])

setup(
    name="foreign",
    version="1.0",
    description="C Extension for matrix power",
    author="shimney",
    ext_modules=[module],
)