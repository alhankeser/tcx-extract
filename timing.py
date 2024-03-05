import timeit
import subprocess
from bs4 import BeautifulSoup

def zig_get_values(filepath, tag_name) -> None:
    return subprocess.check_output(["./parse", filepath, tag_name])

def py_get_values(filepath, tag_name):
    with open(f"{filepath}", "rb") as file:
        soup = BeautifulSoup(file, features="lxml-xml")
        track_points = soup.find_all('Trackpoint')
        if len(track_points) == 0:
            return False
        data = []
        for track_point in track_points:
            time_point = track_point.find(tag_name).text
            data.append(time_point)
    return data

def py2_get_values(filepath, tag_name):
    with open(f"{filepath}", "rb") as file:
        soup = BeautifulSoup(file, features="lxml-xml")
        track_points = soup.find_all("Time")
        data = []
        for track_point in track_points:
            data.append(track_point.text)
    return data

def py3_get_values(filepath, tag_name):
    with open(f"{filepath}", "rb") as file:
        soup = BeautifulSoup(file, features="lxml-xml")
        track_points = soup.find_all("Time")
        data = list(map(lambda x: x.text, track_points))
    return data

def get_timing(func, args, iterations=1):
    total_time = timeit.timeit(lambda: func(**args), number=iterations)
    mean_time = total_time / iterations
    return mean_time

args = {
    "filepath": "example.tcx",
    "tag_name": "Time"
}

iterations = 3

print("zig: ", get_timing(zig_get_values, args, iterations))
print("py: ", get_timing(py_get_values, args, iterations))
print("py2: ", get_timing(py2_get_values, args, iterations))
print("py3: ", get_timing(py3_get_values, args, iterations))

