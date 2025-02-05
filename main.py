import os
import webbrowser

import eel
from jinja2 import Environment, FileSystemLoader
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from backend import pywal_interface

pywal_directory = "/home/indigo/.cache/wal"
wallpaper_path = f"{pywal_directory}/wallpaper.txt"
css_path = f"{pywal_directory}/colors.css"

eel.init("web")
env = Environment(loader=FileSystemLoader("web"), autoescape=True)


class PywalHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path in [
            os.path.join(pywal_directory, "colors.css"),
            os.path.join(pywal_directory, "wallpaper.txt"),
        ]:
            pywal_interface.cache_wallpaper(wallpaper_path)
            pywal_interface.cache_colors(css_path)

            eel.reload_page()


@eel.expose
def open_google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)  # Opens in default web browser


def start():
    # Set up file watcher
    event_handler = PywalHandler()
    observer = Observer()
    observer.schedule(event_handler, pywal_directory, recursive=False)
    observer.start()

    pywal_interface.cache_wallpaper(wallpaper_path)
    pywal_interface.cache_colors(css_path)

    try:
        eel.start("index.html", port=8069, size=(1200, 800))
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    start()
