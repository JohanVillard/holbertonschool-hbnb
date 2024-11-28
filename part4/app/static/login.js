import { handleMessage } from "./utils.js";

export default function handleLoginFormSubmit() {
  // On login.html
  const loginForm = document.getElementById("login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
      event.preventDefault();

      // Retrieve user input (email and password)
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      clearMessage();

      try {
        // Await the login response from the server
        const response = await loginUser(email, password);

        if (response.ok) {
          const data = await response.json();

          setCookie(data);

          redirectToHomePage();
        } else {
          const errorData = await response.json();
          handleMessage("red", errorData.message || "login failed");
        }
      } catch (error) {
        // Display the error message in the form
        handleMessage("red", error.message);
      }
    });
  }
}

function clearMessage() {
  const messageElement = document.getElementById("message");

  // Reset message
  messageElement.style.display = "none";
  messageElement.textContent = "";
}

async function loginUser(email, password) {
  // Create a request and wait for server response for access and token
  if (!email) {
    throw new Error("An email is required");
  }

  if (!password) {
    throw new Error("A password is required");
  }

  // Create Request
  const request = {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  };

  // Fetch request
  const response = await fetch(
    "http://127.0.0.1:5000/api/v1/auth/login",
    request,
  );

  // Handle response
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(
      `Login failed: ${errorData.message || response.statusText}`,
    );
  }
  return response;
}

function setCookie(data) {
  // Creates and stores a cookie
  document.cookie = `token=${data.access_token}; path=/`;
}

function redirectToHomePage() {
  // Redirect user
  window.location.href = "/index.html";
}
