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


def pdfHendler():
    folder_file = SOURCE_PATH
    dir_list = os.listdir(folder_file)
    for file_name in dir_list:
        if file_name.split('.')[-1] == "url":
            print("Start converting.")
            input_path = path.join(folder_file, file_name)
            try:
                pdfThat(file_name.split(".")[0], input_path, output_path)
            except:
                except_orig_path=path.join(SOURCE_PATH, file_name)
                except_dust_path=path.join(SOURCE_PATH,"Couldent Convert", file_name)
                move(except_orig_path, except_dust_path)
                print("Couldn't convert.")
                toast.show_toast("Link2PDF", "Couldn't convert \"{}\" URL.".format(str(file_name.split(".")[0])))
            
            if os.path.isfile(input_path):
                path_name=path.join(output_path,"URL", file_name)
                move(input_path, path_name)
                toast.show_toast("Link2PDF", "\"{}\" has been converted.".format(str(file_name.split(".")[0])))
            
            
def pdfThat(name, input_path, output_path):
    option = {'encoding': 'UTF-8', 'enable-local-file-access': True}
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    path_name = path.join(output_path,"PDF", name + ".pdf")
    path_default = path.join(output_path,"PDF", "temporary.pdf")

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
        print("Now listening {} directory.".format(SOURCE_PATH.split("\\")[-1]))
        try:
            while True:
                time.sleep(60)
        except:
            self.observer.stop()
            print("Observer Stopped")
            toast.show_toast("Link2PDF", "The program has stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created' or event.event_type == 'modified':
            # Event is created, you can process it now
            pdfHendler()
            
        elif event.event_type == 'deleted':
            print("File has deleted!")


if __name__ == '__main__':
    SOURCE_PATH = argv[1]  # source directory
    output_path = argv[2]  # target directory

    print("Link2PDF now running.")
    toast = ToastNotifier()
    toast.show_toast("Link2PDF", "The program has started")

    if not os.path.exists(path.join(output_path, "URL")):
        os.makedirs(path.join(output_path, "URL"))
    if not os.path.exists(path.join(output_path, "PDF")):
        os.makedirs(path.join(output_path, "PDF"))
    if not os.path.exists(path.join(SOURCE_PATH, "Couldent Convert")):
        os.makedirs(path.join(SOURCE_PATH, "Couldent Convert"))
    
    if len(os.listdir(path.join(SOURCE_PATH, "Couldent Convert"))) != 0:
        print("directory is not empty, your attention is required")
        toast.show_toast("Link2PDF", "You have few URLs that couldent convert, your attention is required.")
    
    pdfHendler()
    
    watch = OnMyWatch(SOURCE_PATH)
    watch.run()
