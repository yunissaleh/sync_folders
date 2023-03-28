import os
import shutil
from datetime import datetime


# log to file and console
def log(message):
    f = open("log.txt", "a")
    f.write(message + "\n")
    f.close()

    print(message)


def getTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def sync(src, dest):
    for root, dirs, files in os.walk(src):

        # Synchronize files
        for file in files:
            src_path = root + '\\' + file
            dest_path = root.replace(src, dest)
            shutil.copy(src_path, dest_path)
            log(f"[[ {getTime()} ]] File copied: from: {root} to {dest_path}")

        # Synchronize directories
        for dir in dirs:
            try:
                dest_path = root.replace(src, dest) + "\\" + dir
                os.mkdir(dest_path)
                log(f"[[ {getTime()} ]] Folder copied: from: {root} to {dest_path}")
            except OSError:
                log(f"{getTime()}Cannot create folder when it already exists")


sync("src", "replica")
