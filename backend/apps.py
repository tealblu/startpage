import configparser
import os

import eel

from .icon_helper import find_icon

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
    "/usr/share/pixmaps",
    os.path.expanduser("~/.icons"),
    os.path.expanduser("~/.local/share/icons"),
    *[f"{dir}/icons" for dir in XDG_DATA_DIRS],
]
app_list = []


@eel.expose
def run_app(exec):
    # trunk-ignore(bandit/B605)
    os.system(exec)


@eel.expose
def get_app_list():
    global app_list
    app_list.clear()

    for app_dir in app_dirs:
        if not app_dir or not os.path.isdir(app_dir):
            continue

        with os.scandir(app_dir) as entries:
            for entry in entries:
                if entry.name.endswith(".desktop"):
                    print(entry.path)
                    app_name, app_icon, launch_cmd = get_app_details(
                        os.path.join(app_dir, entry.name)
                    )
                    if app_name and not any(
                        app["name"] == app_name for app in app_list
                    ):
                        app_list.append(
                            {"name": app_name, "icon": app_icon, "exec": launch_cmd}
                        )

    # sort the list by name
    app_list.sort(key=lambda app: app["name"])
    return app_list


def get_app_details(desktop_file):
    config = configparser.ConfigParser(interpolation=None)
    config.read(desktop_file, encoding="utf-8")

    if "Desktop Entry" in config:
        app_name = config["Desktop Entry"].get("Name", None)
        icon_name = config["Desktop Entry"].get("Icon", None)
        launch_cmd = config["Desktop Entry"].get("Exec", None)
        if launch_cmd:
            launch_cmd += "> /dev/null 2>&1"  # Hide output
        app_icon_path = resolve_icon_path(icon_name) if icon_name else None

        if app_icon_path and os.path.exists(app_icon_path):
            # Copy the icon to src/images/icons
            icon_file_name = os.path.basename(app_icon_path)
            icon_dest_path = f"web/src/images/icons/{icon_file_name}"
            os.makedirs(os.path.dirname(icon_dest_path), exist_ok=True)
            # trunk-ignore(bandit/B605)
            os.system(f"cp {app_icon_path} {icon_dest_path}")
            # trunk-ignore(bandit/B605)
            os.system(
                f"magick convert {icon_dest_path} -resize 64x64 {icon_dest_path} > /dev/null 2>&1"
            )

            app_icon_path = f"src/images/icons/{icon_file_name}"
        else:
            app_icon_path = "src/images/icons/default.svg"

        return app_name, app_icon_path, launch_cmd
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

    # Check system icon themes
    icon_path = find_icon(icon_name)
    if icon_path:
        return icon_path

    # If no file is found, return the raw name (some environments can resolve it)
    return icon_name


def init():
    return


if __name__ == "__main__":
    get_app_list()
