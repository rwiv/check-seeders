import os
import subprocess
import json


def main():
    if not os.path.exists("./output"):
        os.mkdir("./output")

    filenames = os.listdir("./torrents")
    result, debug = get_result(filenames)

    with open("./output/result.json", "w") as file:
        file.write(json.dumps(result, indent=4))

    with open("./output/debug.json", "w") as file:
        file.write(json.dumps(debug, indent=4))


def get_result(filenames):
    result = []
    debug = []

    for filename in filenames:
        stdout, stderr = exec_transmission(filename)

        if len(stderr) > 0:
            raise Exception("exec error!", stderr)
        else:
            print(f"{filename} finished!")

        result.append({
            "filename": filename,
            "trackers": filter_error(get_trackers(stdout))
        })

        debug.append({
            "filename": filename,
            "stdout": stdout,
            "stderr": stderr
        })

    return result, debug


def exec_transmission(filename):
    p = subprocess.Popen(
        f'transmission-show -s "./torrents/{filename}"',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )

    return list(p.stdout), list(p.stderr)


def get_trackers(lines):
    def is_tracker(line):
        return line.find(" ... ") != -1

    def to_tracker_obj(line):
        chunks = line.split(" ... ")
        return {
            "url": chunks[0],
            "state": chunks[1]
        }

    return list(map(to_tracker_obj, filter(is_tracker, lines)))


def filter_error(trackers):
    def is_not_error(tracker):
        return tracker["state"].find("error") == -1

    return list(filter(is_not_error, trackers))


main()
