import configparser
import os
from pathlib import Path


def find_icon(icon_name):
    """
    Find an icon by name in the system icon themes.

    Args:
        icon_name: Name of the icon to find (without extension)

    Returns:
        str: Full path to the icon file if found, None otherwise
    """
    # Default base directories according to spec
    base_dirs = [
        os.path.expanduser("~/.icons"),  # For backwards compatibility
        os.path.expanduser("~/.local/share/icons"),  # XDG_DATA_HOME/icons
        "/usr/local/share/icons",
        "/usr/share/icons",
        "/usr/share/pixmaps",
    ]

    # Extensions in order of preference
    extensions = ["png", "svg", "xpm"]

    def get_theme_inheritance(theme_name):
        """Get list of parent themes for a given theme."""
        theme_parents = []

        for base_dir in base_dirs:
            theme_path = os.path.join(base_dir, theme_name, "index.theme")
            if os.path.exists(theme_path):
                config = configparser.ConfigParser()
                config.read(theme_path)

                if "Icon Theme" in config and "Inherits" in config["Icon Theme"]:
                    # Get inherited themes, splitting on comma and stripping whitespace
                    parents = [
                        p.strip() for p in config["Icon Theme"]["Inherits"].split(",")
                    ]
                    theme_parents.extend(parents)
                break

        return theme_parents

    def find_in_theme(theme_name):
        """Look for icon in specific theme."""
        for base_dir in base_dirs:
            theme_path = Path(base_dir) / theme_name

            if not theme_path.exists():
                continue

            # Check theme subdirectories
            for subdir in theme_path.glob("**"):
                if not subdir.is_dir():
                    continue

                # Try each supported extension
                for ext in extensions:
                    icon_path = subdir / f"{icon_name}.{ext}"
                    if icon_path.exists():
                        return str(icon_path)

        return None

    def find_icon_helper(theme_name):
        """Recursive helper to search theme and its parents."""
        # Try current theme
        result = find_in_theme(theme_name)
        if result:
            return result

        # Try parent themes
        for parent in get_theme_inheritance(theme_name):
            result = find_icon_helper(parent)
            if result:
                return result

        return None

    # First try current theme (assuming default)
    result = find_icon_helper("hicolor")
    if result:
        return result

    # Finally try unthemed icons in pixmap directories
    for base_dir in base_dirs:
        for ext in extensions:
            icon_path = Path(base_dir) / f"{icon_name}.{ext}"
            if icon_path.exists():
                return str(icon_path)

    return None
