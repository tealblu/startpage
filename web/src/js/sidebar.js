document.addEventListener("DOMContentLoaded", function () {
  const hamburgerMenu = document.getElementById("hamburger-menu");
  const hamburgerIcon = hamburgerMenu.querySelector(".hamburger-icon");
  const sidebar = document.getElementById("sidebar");

  // Stop event propagation to prevent immediate closure
  hamburgerMenu.addEventListener("click", function (event) {
    event.stopPropagation();
    hamburgerIcon.classList.toggle("active");
    sidebar.classList.toggle("active");
  });

  // Prevent sidebar from closing when clicking inside it
  sidebar.addEventListener("click", function (event) {
    event.stopPropagation();
  });

  // Close sidebar when clicking outside
  document.addEventListener("click", function () {
    hamburgerIcon.classList.remove("active");
    sidebar.classList.remove("active");
  });
});
