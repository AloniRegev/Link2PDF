import os
from os import path
from sys import argv

import pdfkit
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import move
import pywintypes
from win10toast import ToastNotifier


def pdfThat(name, input_path, output_path, PATH_wkhtmltopdf):
    option = {'encoding': 'UTF-8', 'enable-local-file-access': True}
    config = pdfkit.configuration(wkhtmltopdf=PATH_wkhtmltopdf)
    path_name = path.join(output_path, name + ".pdf")
    path_default = path.join(output_path, "temporary.pdf")

    pdfkit.from_url(extractURL(input_path), path_default, options=option, configuration=config)
    move(path_default, path_name)
    print("{} done converting".format(name))


def extractURL(path):
    with open(path, "r", encoding='utf8') as infile:
        for line in infile:
            if (line.startswith('URL')):
                url = line[4:]
                break
    return url


class OnMyWatch:
    # Set the directory on watch
    def __init__(self, watchDirectory):
        self.observer = Observer()
        self.watchDirectory = watchDirectory

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(60)
        except:
            toast.show_toast("Link2PDF", "The program has stopped")
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created' or event.event_type == 'modified':
            # Event is created, you can process it now
            print("starting converting.")
            folder_file = SOURCE_PATH
            dir_list = os.listdir(folder_file)
            for file_name in dir_list:
                if file_name.split('.')[-1] != "url":
                    continue
                input_path = path.join(folder_file, file_name)
                pdfThat(file_name.split(".")[0], input_path, output_path, PATH_wkhtmltopdf)
                if os.path.isfile(input_path):
                    os.remove(input_path)
                    toast.show_toast("Link2PDF", "\"{}\" has converted.".format(str(file_name.split(".")[0])))
        elif event.event_type == 'deleted':
            print("File has deleted!")


if __name__ == '__main__':
    SOURCE_PATH = argv[1]  # source directory
    output_path = argv[2]  # target directory
    PATH_wkhtmltopdf = argv[3]  # wkhtmltopdf.exe path in your computer

    print("Link2PDF now running.")
    toast = ToastNotifier()
    toast.show_toast("Link2PDF", "The program has started")

    watch = OnMyWatch(SOURCE_PATH)
    watch.run()
