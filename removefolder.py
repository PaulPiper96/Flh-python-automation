# importing os module
import os
from pathlib import Path


def returnallfilesinDir(fontloc_path):
    # Directory nam
    textdirectory = Path(fontloc_path).expanduser()
    txt_files = list(textdirectory.glob("*"))
    return txt_files

def removeallfiles(filelist):
    if filelist: 
        for file in filelist:
            os.remove(file)
            print("all files removed")
    else:
        print("no files found")

def deletedir(filelist, fontloc_path):
    if filelist:
        print("filelist not empty")
    else:
        os.rmdir(fontloc_path)
        print("filelocation removed")


if __name__ == "__main__":
    fontloc_path = os.path.expanduser("~/Desktop/fontloc")
    files=returnallfilesinDir(fontloc_path)
    removeallfiles(files)