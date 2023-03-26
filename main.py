import os
import subprocess
import json

def main():
    if not os.path.exists("./output"):
        os.mkdir("./output")

    filenames = os.listdir("./torrents")

    with open("./output/result.json", "w") as file:
        result = getResult(filenames)
        file.write(json.dumps(result, indent=4))

def getResult(filenames):
    def toInfo(filename):
        lines = execTransmission(filename)
        return {
            "filename": filename,
            "trackers": filterError(getTrackers(lines))
        }

    return list(map(toInfo, filenames))

def execTransmission(filename):
    cmd = f"transmission-show -s './torrents/{filename}'"
    return subprocess\
        .check_output(cmd, shell=True, encoding='utf-8')\
        .split("\n")

def getTrackers(lines):
    def isTracker(line):
        return line.find(" ... ") != -1

    def toTrackerObj(line):
        chunks = line.split(" ... ")
        return {
            "url": chunks[0],
            "state": chunks[1]
        }

    return list(map(toTrackerObj, filter(isTracker, lines)))

def filterError(trackers):
    isNotError = lambda tracker: tracker["state"].find("error") == -1
    return list(filter(isNotError, trackers))


main()
