function populate_app_grid() {
  // Ensure you are getting the resolved value of the Promise
  eel
    .get_app_list()()
    .then((app_list) => {
      console.log(app_list); // Check the app list data

      // Get the grid container where apps will be populated
      var grid = document.querySelector(".apps-grid");
      grid.innerHTML = ""; // Clear existing content

      // Iterate over the app list and create a grid item for each app
      app_list.forEach((app) => {
        // Create a container for each app
        var appItem = document.createElement("div");
        appItem.classList.add("app-item");

        // Create an image element for the app icon
        var appIcon = document.createElement("img");
        appIcon.classList.add("app-icon");
        appIcon.src = app.icon
          ? `/path/to/icons/${app.icon}.png`
          : "/path/to/default-icon.png"; // Default icon if none provided

        // Create a name element for the app
        var appName = document.createElement("div");
        appName.classList.add("app-name");
        appName.textContent = app.name;

        // Append icon and name to the app item
        // appItem.appendChild(appIcon);
        appItem.appendChild(appName);

        // Append the app item to the grid
        grid.appendChild(appItem);
      });
    })
    .catch((error) => {
      console.error("Error fetching app list:", error);
    });
}

// Call the function to populate the app grid
populate_app_grid();
