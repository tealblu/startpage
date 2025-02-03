const dateElement = document.getElementById("date");

function showTime() {
  const date = new Date();

  const options = {
    weekday: "long",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    day: "2-digit",
    month: "2-digit",
    year: "2-digit",
  };

  const formattedDate = date.toLocaleString("en-GB", options).toLowerCase();
  const [dayOfWeek, dateStr, time] = formattedDate.split(", ");

  dateStrISO = date.toISOString().split("T")[0];

  dateElement.innerHTML = `${dateStrISO} | ${dayOfWeek}, ${time}`;
}

setInterval(showTime, 1000);
showTime();
