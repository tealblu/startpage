import webbrowser

import eel
from jinja2 import Environment, FileSystemLoader
from watchdog.observers import Observer

from backend import apps
from backend.pywal_interface import PywalHandler, pywal_directory

eel.init("web")
env = Environment(loader=FileSystemLoader("web"), autoescape=True)


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

    try:
        eel.start("index.html", port=8069, size=(1200, 800))
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    start()
