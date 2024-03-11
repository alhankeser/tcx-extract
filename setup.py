from setuptools import setup, find_packages

setup(
    name='tcx-extract',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "ziglang"
    ]
)