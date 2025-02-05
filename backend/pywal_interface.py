import eel


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
