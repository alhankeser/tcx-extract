import sys
import subprocess
import os
from pathlib import PurePath

python_exe = sys.executable
cwd = os.path.dirname(os.path.realpath(__file__))
zig_filename = "extract.zig"
zig_executable = zig_filename.replace(".zig", "")
zig_filepath = f"{cwd}/zig/{zig_filename}"


def build_zig():
    """
    Finds and moves the output of zig build to an expected location
    """
    print("Building zig...")
    subprocess.run(
        [python_exe, "-m", "ziglang", "build-exe", zig_filepath, "-O", "ReleaseFast"]
    )
    try_path = [".", zig_executable]
    for d in PurePath(cwd).parts:
        zig_executable_filepath = os.path.join(*try_path)
        if os.path.isfile(zig_executable_filepath):
            os.rename(zig_executable_filepath, os.path.join(cwd, "zig", zig_executable))
            os.rename(
                zig_executable_filepath + ".o",
                os.path.join(cwd, "zig", zig_executable + ".o"),
            )
            break
        try_path.insert(0, "..")
