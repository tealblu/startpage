document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("search-form")
    .addEventListener("submit", function (event) {
      event.preventDefault(); // Stop normal form submission
      const searchInput = document.getElementById("search-input");
      const query = searchInput.value;

      if (query.trim() !== "") {
        // Only proceed if there's input
        eel.open_google_search(query);
        searchInput.value = ""; // Clear the search box
      }
    });
});
