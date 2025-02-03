import http.server
import os
import socketserver
from pathlib import Path
import sys

def create_static_file_server(directory='.', port=8000):
    """
    Create a lightweight static file server.
    
    Args:
        directory (str): Directory to serve files from
        port (int): Port to run the server on
    """
    # Validate directory exists
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
        print(f"Error: Cannot bind to port {port}. Try a different port.")
    except KeyboardInterrupt:
        print("\nServer stopped.")

def main():
    directory = "/home/indigo/.cache/wal"
    create_static_file_server(directory, 8000)

if __name__ == "__main__":
    main()