import os
import shutil
import sys
import time
from datetime import datetime


# Log to file and console
def log(message, file):
    f = open(file, "a")
    f.write(message + "\n")
    f.close()

    print(message)


def getTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Sync folders
def sync(src, dest, log_f):
    # Traverse through the source folder
    for root, fldrs, files in os.walk(src):
        dest_path = root.replace(src, dest)

        # Copy files to replica
        for file in files:
            file_src = os.path.join(root, file)
            file_dest = os.path.join(dest_path, file)

            if os.path.exists(file_dest) and os.path.getmtime(file_dest) >= os.path.getmtime(file_src):
                # Destination file exists and is up-to-date, do nothing
                pass
            else:
                shutil.copy(file_src, file_dest)
                log(f"[[ {getTime()} ]] File {file} copied to {file_dest}.", log_f)

        # Copy directories to replica
        for fldr in fldrs:
            try:
                fldr_dest = os.path.join(dest_path, fldr)
                os.mkdir(fldr_dest)
                log(f"[[ {getTime()} ]] Folder {fldr} created in {fldr_dest}.", log_f)
            except OSError:
                pass

    # Traverse through replica folder
    for root, fldrs, files in os.walk(dest):
        src_path = root.replace(dest, src)

        # Delete files no longer present in src folder
        for file in files:
            file_src = os.path.join(src_path, file)
            file_dest = os.path.join(root, file)

            if not os.path.exists(file_src):
                os.remove(file_dest)
                log(f"[[ {getTime()} ]] File {file} deleted from {file_dest}", log_f)

        # Delete folders no longer present in src folder
        for fldr in fldrs:
            fldr_dest = os.path.join(root, fldr)
            fldr_src = os.path.join(src_path, fldr)
            if not os.path.exists(fldr_src):
                shutil.rmtree(fldr_dest)
                log(f"[[ {getTime()} ]] Folder {fldr} deleted from {fldr_dest}", log_f)
                

# Sync periodically
def syncInterval(src, dest, interval, log_f):
    while True:
        sync(src, dest, log_f)
        time.sleep(int(interval))


syncInterval(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

