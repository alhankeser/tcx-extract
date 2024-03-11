import subprocess
import os

def get_tag(filepath: str, tag_name: str) -> str:
    cwd = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(cwd, 'zig', 'extract')
    return subprocess.check_output([abs_path, filepath, tag_name]).decode('utf-8')

def extract(filepath: str, tag_name: str) -> list[str]:
    result = get_tag(filepath=filepath, tag_name=tag_name)
    if len(result) > 0:
        return result.split('\n')[:-1]
    else:
        return []