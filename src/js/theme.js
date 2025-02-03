document.addEventListener("DOMContentLoaded", () => {
  setTimeout(() => {  // Ensures CSS is loaded
    let rootStyle = getComputedStyle(document.documentElement);
    let wallpaper = rootStyle.getPropertyValue("--wallpaper").trim();

    if (wallpaper) {
      // Extract the actual URL from `url("...")`
      wallpaper = wallpaper.replace(/^url\(["']?|["']?\)$/g, "");
      console.log("Extracted Wallpaper URL:", wallpaper);  // Debugging
      document.querySelector(".wallpaper").src = wallpaper;
    }
  }, 100);
});



// Image is opacity 0 and text is translated off screen by default
// Add the loaded class to the image and text to animate them in
window.onload = function () {
  document.getElementById("image").classList.add("loaded");
  document.getElementById("text").classList.add("loaded");
  document.getElementsByTagName("html")[0].classList.add("loaded");
};
