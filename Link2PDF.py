import os
from os import path
import pdfkit
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import move


def pdfThat(name, input_path, output_path, PATH_wkhtmltopdf):
    option = {'encoding': 'UTF-8', 'enable-local-file-access': True}
    config = pdfkit.configuration(wkhtmltopdf=PATH_wkhtmltopdf)
    path_name = path.join(output_path, name + ".pdf")
    path_default = path.join(output_path, "temporary.pdf")

    pdfkit.from_url(extractURL(input_path), path_default, options=option, configuration=config)
    move(path_default, path_name)
    print("{} done converting".format(name))


def extractURL(path):
    filename = r'C:\Users\regev\Desktop\Google.url'
    with open(path, "r", encoding='utf8') as infile:
        for line in infile:
            if (line.startswith('URL')):
                url = line[4:]
                break
    return url


class OnMyWatch:
    # Set the directory on watch
    watchDirectory = r"C:\Users\regev\Desktop\מתכונים"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
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
            folder_file = r"C:\Users\regev\Desktop\מתכונים"
            dir_list = os.listdir(folder_file)
            PATH_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
            output_path = r"C:\Users\regev\Desktop\New folder"
            for file_name in dir_list:
                if file_name.split('.')[-1] != "url":
                    continue
                # print(file_name.split(".")[0])
                input_path = path.join(folder_file, file_name)
                pdfThat(file_name.split(".")[0], input_path, output_path, PATH_wkhtmltopdf)
                if os.path.isfile(input_path):
                    os.remove(input_path)
        elif event.event_type == 'deleted':
            # Event is modified, you can process it now
            print("File has deleted!")


if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()