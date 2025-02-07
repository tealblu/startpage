function populate_app_grid() {
  // Ensure you are getting the resolved value of the Promise
  eel
    .get_app_list()()
    .then((app_list) => {
      // Get the grid container where apps will be populated
      var grid = document.querySelector(".apps-grid");
      grid.innerHTML = ""; // Clear existing content

      // Iterate over the app list and create a grid item for each app
      app_list.forEach((app) => {
        // Create a container for each app
        var appItem = document.createElement("div");
        appItem.classList.add("app-item");

        // Create a name element for the app
        var appName = document.createElement("div");
        appName.classList.add("app-name");
        appName.textContent = app.name;

        // Append icon and name to the app item
        // first check if the icon is available
        if (app.icon) {
          // Create an image element for the app icon
          var appIcon = document.createElement("img");
          appIcon.classList.add("app-icon");
          appIcon.src = `/${app.icon}`;

          appItem.appendChild(appIcon);
        }

        appItem.appendChild(appName);

        // Add an event listener to run the app exec cmd when clicked
        appItem.addEventListener("click", () => {
          eel.run_app(app.exec)();
        });

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
