import os

import eel
from watchdog.events import FileSystemEventHandler

from backend import pywal_interface

pywal_directory = "/home/indigo/.cache/wal"
wallpaper_path = f"{pywal_directory}/wallpaper.txt"
css_path = f"{pywal_directory}/colors.css"


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
def cache_colors(path):
    # Cache the colors in a file in the app directory
    with open(path, "r") as f:
        colors = f.read()

    with open("./web/src/css/colors.css", "w") as f:
        f.write(colors)


@eel.expose
def cache_wallpaper(path):
    # Cache the wallpaper in a file in the app directory
    with open(path, "r") as f:
        wallpaper_path = f.read().strip()

    with open("./web/src/images/wallpaper.jpg", "wb") as f:
        with open(wallpaper_path, "rb") as wallpaper_file:
            f.write(wallpaper_file.read())


if __name__ == "__main__":
    print("\ncaching...\n")

    cache_colors("/home/indigo/.cache/wal/colors.css")
    cache_wallpaper("/home/indigo/.cache/wal/wallpaper.txt")

    with open("/home/indigo/.cache/wal/wallpaper.txt", "r") as f:
        print(f"wallpaper path: {f.read()}\n")

    with open("./web/src/css/colors.css", "r") as f:
        print(f.read())

    print("\n")
else:
    cache_colors(css_path)
    cache_wallpaper(wallpaper_path)
