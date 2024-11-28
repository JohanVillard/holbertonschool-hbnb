import { getCookie, getPlaceIdFromURL, handleMessage } from "./utils.js";

export function collectReviewData() {
  const token = getCookie("token");
  return new Promise((resolve) => {
    // Select the form
    const reviewForm = document.getElementById("review-form");

    // Add a event listener
    reviewForm.addEventListener("submit", function (event) {
      event.preventDefault();

      // Get the value of fields
      const reviewText = document.getElementById("review-text").value;
      const reviewRating = document.getElementById("review-rating").value;

      // Create an object to send to server
      const reviewData = {
        text: reviewText,
        rating: reviewRating,
        place_id: getPlaceIdFromURL(),
        user_id: getSubFromToken(token)["sub"],
      };
      resolve(reviewData);
    });
  });
}

function getSubFromToken(token) {
  // Decode the token in base 64
  const arrayToken = token.split(".");
  const tokenPayload = JSON.parse(atob(arrayToken[1]));
  return tokenPayload;
}

export async function submitReview(reviewData) {
  const token = getCookie("token");

  const request = {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json; charset=UTF-8",
    },
    body: JSON.stringify({
      text: reviewData.text,
      rating: reviewData.rating,
      place_id: reviewData.place_id,
      user_id: reviewData.user_id,
    }),
  };

  try {
    const response = await fetch(
      `http://127.0.0.1:5000/api/v1/reviews`,
      request,
    );

    if (!response.ok) {
      const errorData = await response.json();
      const errorMessage =
        errorData.error || errorData.message || "An unknown error occurred";
      throw new Error(`Error: ${errorMessage}`);
    }

    handleMessage("green", "Thank you for your comments.");
  } catch (error) {
    handleMessage("red", error.message);
  }
  // Wait 2 seconds for the user to read the message
  setTimeout(() => {
    window.location.reload();
  }, 2000);
}
