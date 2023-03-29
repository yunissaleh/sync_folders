import os
import shutil
import sys
import time
from datetime import datetime


# log to file and console
def log(message, file):
    f = open(file, "a")
    f.write(message + "\n")
    f.close()

    print(message)


def getTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def sync(src, dest, log_f):
    # traverse through the source folder
    for root, fldrs, files in os.walk(src):
        dest_path = root.replace(src, dest)

        # copy files to replica
        for file in files:
            file_src = os.path.join(root, file)
            file_dest = os.path.join(dest_path, file)
            shutil.copy(file_src, file_dest)
            log(f"[[ {getTime()} ]] File {file} copied to {file_dest}.", log_f)

        # copy directories to replica
        for fldr in fldrs:
            try:
                fldr_dest = os.path.join(dest_path, fldr)
                os.mkdir(fldr_dest)
                log(f"[[ {getTime()} ]] Folder {fldr} created in {fldr_dest}.", log_f)
            except OSError:
                pass

    # traverse through replica folder
    for root, fldrs, files in os.walk(dest):
        src_path = root.replace(dest, src)

        # delete files no longer present in src folder
        for file in files:
            file_src = os.path.join(src_path, file)
            file_dest = os.path.join(root, file)

            if not os.path.exists(file_src):
                os.remove(file_dest)
                log(f"[[ {getTime()} ]] File {file} deleted from {file_dest}", log_f)

        # delete folders no longer present in src folder
        for fldr in fldrs:
            fldr_dest = os.path.join(root, fldr)
            fldr_src = os.path.join(src_path, fldr)
            if not os.path.exists(fldr_src):
                shutil.rmtree(fldr_dest)
                log(f"[[ {getTime()} ]] Folder {fldr} deleted from {fldr_dest}", log_f)


def syncInterval(src, dest, interval, log_f):
    while True:
        sync(src, dest, log_f)
        time.sleep(int(interval))


syncInterval(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
