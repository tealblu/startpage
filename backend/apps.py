import configparser
import os

import eel

XDG_DATA_HOME = os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
XDG_DATA_DIRS = os.environ.get("XDG_DATA_DIRS", "/usr/local/share:/usr/share").split(
    ":"
)

app_dirs = [
    os.path.expanduser("~/.local/share/applications"),
    f"{XDG_DATA_HOME}/applications" if XDG_DATA_HOME else None,
    *[f"{dir}/applications" for dir in XDG_DATA_DIRS],
]
icon_dirs = [
    "/usr/share/icons",
    "/usr/local/share/icons",
    os.path.expanduser("~/.icons"),
    os.path.expanduser("~/.local/share/icons"),
]
app_list = []


@eel.expose
def get_app_list():
    global app_list
    app_list.clear()

    for app_dir in app_dirs:
        if not app_dir or not os.path.isdir(app_dir):
            continue

        print("Scanning " + app_dir)
        with os.scandir(app_dir) as entries:
            for entry in entries:
                if entry.name.endswith(".desktop"):
                    app_name, app_icon = get_app_details(
                        os.path.join(app_dir, entry.name)
                    )
                    if app_name and not any(
                        app["name"] == app_name for app in app_list
                    ):
                        app_list.append({"name": app_name, "icon": app_icon})

    # sort the list by name
    app_list.sort(key=lambda app: app["name"])
    return app_list


def get_app_details(desktop_file):
    config = configparser.ConfigParser(interpolation=None)
    config.read(desktop_file, encoding="utf-8")

    if "Desktop Entry" in config:
        app_name = config["Desktop Entry"].get("Name", None)
        icon_name = config["Desktop Entry"].get("Icon", None)
        app_icon = resolve_icon_path(icon_name) if icon_name else None
        return app_name, app_icon
    return None, None


def resolve_icon_path(icon_name):
    if not icon_name:
        return None

    # If it's an absolute path, return it directly
    if os.path.isabs(icon_name) and os.path.exists(icon_name):
        return icon_name

    # Check common icon directories
    for icon_dir in icon_dirs:
        for ext in ["png", "svg", "xpm"]:
            icon_path = os.path.join(icon_dir, icon_name + "." + ext)
            if os.path.exists(icon_path):
                return icon_path

    # If no file is found, return the raw name (some environments can resolve it)
    return icon_name


if __name__ == "__main__":
    get_app_list()
    print(app_list)
