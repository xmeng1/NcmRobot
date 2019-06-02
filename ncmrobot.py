import yaml
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
from os.path import expanduser
import ntpath
import subprocess

home = expanduser("~")

configFilePath = "./user_config.yml"
configTempFilePath = "./config/config.yml"

config = None
CONFIG_KEY_FOLDER = "folder"
CONFIG_KEY_LAST_TS = "last_timestamp"

if os.path.isfile(configFilePath):
    print("The user config file existing!! Use it.")
else:
    config = yaml.safe_load(open(configTempFilePath))

    userPathIni = home + "/Music/网易云音乐"
    config[CONFIG_KEY_FOLDER] = userPathIni
    with open(configFilePath, 'w', encoding='utf-8') as outfile:
        yaml.dump(config, outfile, default_flow_style=False, allow_unicode=True)

config = yaml.safe_load(open(configFilePath))

dirPath = config.get(CONFIG_KEY_FOLDER)
print(dirPath)

# get all entries in the directory w/ stats
entries = (os.path.join(dirPath, fn) for fn in os.listdir(dirPath) if fn.endswith(".ncm"))
entries = ((os.stat(path), path) for path in entries)

# leave only regular files, insert creation date
entries = ((stat[ST_CTIME], path)
           for stat, path in entries if S_ISREG(stat[ST_MODE]))
# NOTE: on Windows `ST_CTIME` is a creation date
#  but on Unix it could be something else
# NOTE: use `ST_MTIME` to sort by a modification date
lastTS = config[CONFIG_KEY_LAST_TS]
newLastTS = lastTS
sumHandle = 0
for cdate, path in sorted(entries):
    # print(cdate)
    # print(time.ctime(cdate), os.path.basename(path), os.name)
    if cdate > lastTS:
        fileToConvert = ntpath.basename(path)
        print("### Start to convert the file: ", cdate, "-", fileToConvert)
        subprocess.run(["./ncmdump", path])
        sumHandle = sumHandle + 1
    if cdate > newLastTS:
        newLastTS = cdate

print("new last time stamp: ", newLastTS, "time: ", time.ctime(newLastTS))
print("sum of handle this time: ", sumHandle)

config[CONFIG_KEY_LAST_TS] = newLastTS
with open(configFilePath, 'w', encoding='utf-8') as outfile:
    yaml.dump(config, outfile, default_flow_style=False, allow_unicode=True)