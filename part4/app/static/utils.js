export function getCookie(name) {
  // Get all cookies and separates them with ;
  const cookies = document.cookie.split(";");
  // Retrieves and return cookie by name
  for (let cookie of cookies) {
    if (cookie.startsWith(name + "=")) {
      return cookie.substring(name.length + 1);
    }
  }
  return null;
}

export function getPlaceIdFromURL() {
  // Extract the place ID from window.location.search
  return window.location.search.slice(4);
}

export function handleMessage(color, content) {
  const message = document.getElementById("message");

  message.style.display = "block";
  message.style.textAlign = "center";
  message.style.marginTop = "1rem";
  message.style.color = color;
  message.textContent = content;
}
