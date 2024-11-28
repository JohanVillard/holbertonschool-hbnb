import handleLoginFormSubmit from "./login.js";
import checkAuthentication from "./check_auth.js";

document.addEventListener("DOMContentLoaded", () => {
  // On login
  handleLoginFormSubmit();

  // On all pages
  checkAuthentication();
});
