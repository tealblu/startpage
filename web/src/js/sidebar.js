document.addEventListener("DOMContentLoaded", function () {
  const sidebarContainer = document.getElementById("sidebar-container");
  if (!sidebarContainer) {
    console.error('Element with ID "sidebar-container" not found.');
    return;
  }

  fetch("/src/components/sidebar.html")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((html) => {
      sidebarContainer.innerHTML = html;

      document.querySelector(".ham").addEventListener("click", function () {
        document.querySelector(".sidebar").classList.toggle("active");
      });
    })
    .catch((error) => console.error("Error loading sidebar:", error));
});
