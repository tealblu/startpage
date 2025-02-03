// Image is opacity 0 and text is translated off screen by default
// Add the loaded class to the image and text to animate them in
window.onload = function () {
  document.getElementById("image").classList.add("loaded");
  document.getElementById("text").classList.add("loaded");
  document.getElementsByTagName("html")[0].classList.add("loaded");
};

// Image is opacity 0 and text is translated off screen by default
// Add the loaded class to the image and text to animate them in
window.onload = function () {
  // Try to ping localhost:8069
  fetch('http://localhost:8069')
    .then(response => {
      if (response.ok) {
        // If the ping is successful, add the loaded class to the image and text
        document.getElementById("image").classList.add("loaded");
        document.getElementById("text").classList.add("loaded");
        document.getElementsByTagName("html")[0].classList.add("loaded");
      } else {
        throw new Error('Failed to load');
      }
    })
    .catch(error => {
      // If the ping fails, show an error page
      document.body.innerHTML = `
        <div style="text-align: center; margin-top: 20px;">
          <h1 style="color: red;">Error: Unable to connect to pywal-webserver</h1>
          <p>Please check the server at <code>localhost:8069</code>. Check the README for more info.</p>
        </div>
      `;
    });
};
