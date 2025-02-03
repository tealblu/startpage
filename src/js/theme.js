// try to load the colors
async function loadColors() {
  const defaultColors = {
      background: '#1E1E2E',
      foreground: '#CDD6F4',
      color0: '#181825',
      color1: '#F38BA8'
      // Add more default colors
  };

  try {
    console.log('Loading colors...');
    const response = await fetch('file:///home/indigo/.cache/wal/colors.json');
    const colors = await response.json();
    applyColors(colors);
  } catch (error) {
    console.warn('Color loading failed, using defaults');
    applyColors(defaultColors);
  }
}

function applyColors(colors) {
  // Special colors
  Object.entries(colors.special).forEach(([key, value]) => {
      document.documentElement.style.setProperty(`--pywal-${key}`, value);
  });

  // Numeric colors
  Object.entries(colors.colors).forEach(([key, value]) => {
      document.documentElement.style.setProperty(`--pywal-${key}`, value);
  });

  // Additional properties
  document.documentElement.style.setProperty('--pywal-wallpaper', colors.wallpaper);
  document.documentElement.style.setProperty('--pywal-alpha', colors.alpha);
}

document.addEventListener('DOMContentLoaded', loadColors);

document.addEventListener("DOMContentLoaded", () => {
  setTimeout(() => {  // Ensures CSS is loaded
    let rootStyle = getComputedStyle(document.documentElement);
    let wallpaper = rootStyle.getPropertyValue("--pywal-wallpaper").trim();

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
