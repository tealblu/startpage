import asyncio
import signal
import webbrowser

import eel
from jinja2 import Environment, FileSystemLoader
from watchdog.observers import Observer

from backend import apps
from backend.pywal_interface import PywalHandler, pywal_directory

eel.init("web")
env = Environment(loader=FileSystemLoader("web"), autoescape=True)


def shutdown():
    asyncio.get_event_loop().stop()
    print("Shutting down gracefully...")


async def background_processing():
    await asyncio.to_thread(apps.init)


@eel.expose
def open_google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)  # Opens in default web browser


def start():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(background_processing())  # Run apps.init() in the background
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
    signal.signal(signal.SIGINT, lambda signum, frame: shutdown())

    try:
        start()
    except (KeyboardInterrupt, SystemExit):
        shutdown()
