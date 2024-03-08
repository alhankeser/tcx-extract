from setuptools import setup, find_packages
import subprocess
import sys
import os

VERSION = '0.0.1'
MODULE_PATH = "tcx_extract"
DESCRIPTION = 'A super-fast extractor of data from tcx files.'
LONG_DESCRIPTION = 'Usage: `extract_tag("myfile.tcx", "Time")`'


def build_zig():
    print("Building zig...")
    p = subprocess.call(["zig",
                         "build",
                         "--summary",
                         "all"
                         ])
    if p != 0:
        raise RuntimeError("[ERROR] Building zig failed!")

def move_zig():
    print("Moving zig executable...")
    os.rename("./zig-out/bin/extract", f"{MODULE_PATH}/zig/extract")

build_zig()
move_zig()


setup(
    name=MODULE_PATH,
    version=VERSION,
    author="Alhan Keser",
    author_email="hello@alhan.co",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=["zig>=0.12.0-dev"],
    keywords=["tcx", "extraction", "zig"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing :: Markup :: XML"
    ]
)

