# Startpage for Firefox

This repository contains a custom new tab page for Firefox, designed to be used in conjunction with the `pywal` color scheme generator. The page is highly customizable and can be personalized to reflect your unique preferences. It requires the use of `pywal` and a script called `pywal-webserver.py` to function properly.

## Requirements

- Python 3
- `pywal` (for color scheme generation)
- Firefox (or another modern browser)
- A local server running on your home PC

## Setup Instructions

Follow the steps below to set up and use the "startpage" on your home PC.

### 1. Install Dependencies

First, you need to install `pywal` and ensure that Python 3 is installed on your system.


Let me know if you'd like me to make any adjustments to this!
    - On most systems, you can install `pywal` using `pip`:
      ```bash
      pip install pywal
      ```

- **Install Python dependencies for the webserver**:
    - In the root of the repository, you'll find a script `pywal-webserver.py` which will serve your "startpage". You might need to install additional dependencies:
      ```bash
      pip install flask
      ```

### 2. Customize the Color Scheme

Before starting the webserver, run `pywal` to generate your color scheme.

- Generate a color scheme using any of `pywal`'s available themes. For example:
  ```bash
  wal -i /path/to/image.jpg
  ```
  This will generate a color scheme based on the provided image.

### 3. Configure the Webserver

- Inside the repository, navigate to the directory containing `pywal-webserver.py`. 
- Open the script in a text editor, and make sure the paths are correctly set up (e.g., for the location of your pywal colors).

### 4. Start the Webserver

Run the following command to start the local webserver:

```bash
python pywal-webserver.py
```

By default, this will host the site on `http://localhost:5000`.

### 5. Set the Startpage in Firefox

Now that your local webserver is running, you need to set the new tab page in Firefox to the hosted site.

- Open Firefox and go to `about:config`.
- Search for the setting `browser.newtab.url`.
- Set it to your local server URL: 
  ```
  http://localhost:5000
  ```

### 6. Accessing the Startpage

Once everything is set up, open a new tab in Firefox, and you'll see your custom startpage with the pywal-generated color scheme.

### 7. Customizing the Startpage

You can further customize the content of your startpage by modifying the files in the repository. Edit the HTML, CSS, and JavaScript as needed to fit your preferences. The color scheme will automatically adjust based on the `pywal` colors.

### 8. Accessing the Startpage Remotely (Optional)

If you want to use the startpage on other devices in your home network:

- Find your local IP address using a command like `ip a` (on Linux) or `ipconfig` (on Windows).
- Edit `pywal-webserver.py` to bind the server to your local IP by changing `host='localhost'` to `host='0.0.0.0'` or your specific IP address.
- Now, on other devices connected to the same network, you can access the startpage by going to `http://<your-ip>:5000`.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.