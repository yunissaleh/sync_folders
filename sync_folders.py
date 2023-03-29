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

    # traverse through the source folder
    for root, fldrs, files in os.walk(src):
        dest_path = root.replace(src, dest)

        # copy files to replica
        for file in files:
            file_src = os.path.join(root, file)
            file_dest = os.path.join(dest_path, file)
            shutil.copy(file_src, file_dest)
            log(f"[[ {getTime()} ]] File {file} copied to {file_dest}.")

        # copy directories to replica
        for fldr in fldrs:
            try:
                fldr_dest = os.path.join(dest_path, fldr)
                os.mkdir(fldr_dest)
                log(f"[[ {getTime()} ]] Folder {fldr} copied to {fldr_dest}.")
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
                log(f"[[ {getTime()} ]] File deleted: {file} from {file_dest}")

        # delete folders no longer present in src folder
        for fldr in fldrs:
            fldr_path = os.path.join(root, fldr)
            fldr_src = os.path.join(src_path, fldr)
            if not os.path.exists(fldr_src):
                shutil.rmtree(fldr_path)
                log(f"[[ {getTime()} ]] Folder deleted: {fldr_path}")


sync("src", "replica")
