import http.server
import os
import signal
import socketserver
import sys
from pathlib import Path

import psutil


def kill_existing_instances():
    """Kill existing instances of this script."""
    current_pid = os.getpid()
    for proc in psutil.process_iter(["pid", "cmdline"]):
        try:
            # Check if it's the same script and not the current process
            if (
                proc.info["cmdline"]
                and sys.argv[0] in proc.info["cmdline"]
                and proc.info["pid"] != current_pid
            ):
                print(f"Killing existing instance (PID {proc.info['pid']})")
                os.kill(proc.info["pid"], signal.SIGTERM)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def create_static_file_server(directory=".", port=8069):
    """Create a static file server on port 8069 with file watching."""
    # Kill existing instances
    kill_existing_instances()

    # Validate directory
    serve_path = Path(directory).absolute()
    if not serve_path.is_dir():
        print(f"Error: {serve_path} is not a valid directory")
        sys.exit(1)

    # Change to serving directory
    os.chdir(serve_path)

    # Use Python's built-in SimpleHTTPRequestHandler
    Handler = http.server.SimpleHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Serving files from {serve_path} at http://localhost:{port}")
            httpd.serve_forever()
    except PermissionError:
        print(f"Error: Cannot bind to port {port}.")
    except KeyboardInterrupt:
        print("\nServer stopped.")


def start(directory="/home/indigo/.cache/wal", port=8069):
    create_static_file_server(directory, port)


if __name__ == "__main__":
    start()
