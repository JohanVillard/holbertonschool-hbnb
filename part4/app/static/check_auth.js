import { getCookie, getPlaceIdFromURL } from "./utils.js";
import { fetchPlaces, displayPlaces } from "./index.js";
import { fetchPlaceDetails, displayPlaceDetails } from "./place.js";
import { collectReviewData, submitReview } from "./add-review.js";

export default function checkAuthentication() {
  const token = getCookie("token");
  const loginLink = document.getElementById("login-link");

  // Handle login display
  if (!token && window.location.pathname !== "/login.html") {
    loginLink.style.display = "block";
  } else {
    loginLink.style.display = "none";
  }

  const currentPage = window.location.pathname;

  // Performs an action according to the page
  if (currentPage === "/index.html") {
    // Fetch places data if the user is authenticated ??? Une erreur du concepteur ??? Pourquoi ne pas afficher les places sans être connecté
    fetchPlaces(token).then((places) => {
      displayPlaces(places);
    });
  } else if (currentPage === "/place.html") {
    const addReviewSection = document.querySelector("#add-review");
    if (!token) {
      addReviewSection.style.display = "none";
    } else {
      addReviewSection.style.display = "block";
    }
    const placeId = getPlaceIdFromURL(token);

    // Display details of the place
    fetchPlaceDetails(token, placeId).then((place) => {
      displayPlaceDetails(place);
    });

    // User can create a review
    collectReviewData().then(submitReview);
  }
}
