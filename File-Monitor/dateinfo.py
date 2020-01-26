import os
import datetime
import hashlib


def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


def modification_date(path_to_file):
    t = os.path.getmtime(path_to_file)
    return str(datetime.datetime.fromtimestamp(t))


def creation_date(path_to_file):
    t = os.path.getctime(path_to_file)
    return str(datetime.datetime.fromtimestamp(t))


def size(path_to_file):
    t = os.path.getsize(path_to_file)
    return str(t)


def recurse():
    files = []
    for r, d, f in os.walk("."):
        for file in f:
            if ".git" in os.path.join(r, file):
                pass
            else:
                files.append(os.path.join(r, file))

    for filename in files:
        try:
            print()
            print(f"path={os.path.abspath(filename)}", end=" ")
            print("filename=" + filename, end=" ")
            print("file_size=" + size(filename), end=" ")
            print("files_hash=" + hash_file(filename), end=" ")
            print("creation_date=" + str(creation_date(filename)), end=" ")
            print("last_modification_date=" + str(modification_date(filename)), end=" ")
            print("device_identifier=" + str(os.stat(filename).st_dev), end=" ")
            print("userid=" + str(os.stat(filename).st_uid), end=" ")
            print("permissions=" + str(os.stat(filename).st_mode))
        except:
            pass
