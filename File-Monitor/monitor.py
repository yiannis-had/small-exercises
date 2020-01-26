import time
import sys
import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import hashlib
import dateinfo


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


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        try:
            print(f"action={event.event_type}", end=" ")
            print(f"path={event.src_path}", end=" ")
            filename = os.path.split(event.src_path)[1]
            print("filename=" + filename, end=" ")
            print("file_size=" + size(filename), end=" ")
            print("files_hash=" + hash_file(filename), end=" ")
            print("creation_date=" + creation_date(filename), end=" ")
            print("device_identifier=" + str(os.stat(filename).st_dev), end=" ")
            print("userid=" + str(os.stat(filename).st_uid), end=" ")
            print("permissions=" + str(os.stat(filename).st_mode))
        except:
            print("\n")

    def on_moved(self, event):
        try:
            print(str(datetime.datetime.now()), end=" ")
            print(f"action={event.event_type}", end=" ")
            print(f"path={event.src_path}", end=" ")
            filename = os.path.split(event.src_path)[1]
            print("filename=" + filename, end=" ")
            print("file_size=" + size(filename), end=" ")
            print("file_hash=" + hash_file(filename), end=" ")
            print("last_modification_date=" + modification_date(filename))
        except:
            print("\n")

    def on_modified(self, event):
        try:
            print(str(datetime.datetime.now()), end=" ")
            print(f"action={event.event_type}", end=" ")
            print(f"path={event.src_path}", end=" ")
            filename = os.path.split(event.src_path)[1]
            print("filename=" + filename, end=" ")
            print("file_size=" + size(filename), end=" ")
            print("file_hash=" + hash_file(filename), end=" ")
            print("last_modification_date=" + modification_date(filename))
        except:
            print("\n")

    def on_deleted(self, event):
        try:
            print(str(datetime.datetime.now()), end=" ")
            print(f"action={event.event_type}", end=" ")
            print(f"path={event.src_path}", end=" ")
            filename = os.path.split(event.src_path)[1]
            print("file_hash=" + hash_file(filename), end=" ")
            print("filename=" + filename)
        except:
            print("\n")


if __name__ == "__main__":
    dateinfo.recurse()
    event_handler = MyHandler()
    observer = Observer()
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
