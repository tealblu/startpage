async function pingURL(url) {
  try {
    const response = await fetch(url, { method: "HEAD" });
    if (!response.ok) throw new Error("Network response was not ok");
  } catch (error) {
    const mainContent = document.querySelector(".main-content");
    if (mainContent) {
      mainContent.innerHTML = `
        <div style="text-align: center;">
          <h1 style="color: red;">error: unable to reach the backend</h1>
          <p>only the home page is supported for web mode.</p>
          <p>please use the desktop app or go to the home page.</p>
          <p>if you are using the desktop app, something is very wrong.</p>
        </div>
      `;
    }
  }
}

pingURL("http://localhost:8069");
