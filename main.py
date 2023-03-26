import os
import subprocess
import json

def main(filenames):
    with open("./output/result.json", "w") as file:
        infos = getInfos(filenames)
        file.write(json.dumps(infos, indent=4))

def getInfos(filenames):
    def getInfo(filename):
        lines = execTransmission(filename)
        
        return {
            "filename": filename,
            "trackers": filterError(getTrackers(lines))
        }

    return list(map(getInfo, filenames))

def execTransmission(filename):
    cmd = f"transmission-show -s './torrents/{filename}'"
    return subprocess\
        .check_output(cmd, shell=True, encoding='utf-8')\
        .split("\n")

def getTrackers(lines):
    isTracker = lambda line: line.find(" ... ") != -1
    filtered = filter(isTracker, lines)

    def toTrackerObj(line):
        chunks = line.split(" ... ")
        return {
            "url": chunks[0],
            "state": chunks[1]
        }

    return list(map(toTrackerObj, filtered))

def filterError(trackers):
    isError = lambda tracker: tracker["state"].find("error") == -1
    return list(filter(isError, trackers))


main(os.listdir("./torrents"))
