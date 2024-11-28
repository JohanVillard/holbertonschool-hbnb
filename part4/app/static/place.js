export async function fetchPlaceDetails(token, placeId) {
  // Include the token in the Authorization header
  const headers = {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  };

  // Make a GET request to fetch place details
  const response = await fetch(
    `http://127.0.0.1:5000/api/v1/places/${placeId}`,
    {
      method: "GET",
      headers: headers,
    },
  );

  // Handle the response and pass the data to displayPlaceDetails function
  if (response.ok) {
    return await response.json();
  }
}

export function displayPlaceDetails(place) {
  if (!place) {
    console.error("No place details to display.");
    return;
  }

  const reviewList = document.querySelector("#review-cards-container");

  clearPlaceDetailsSection(reviewList);

  updatePlaceInfo(place);

  displayPlaceAmenity(place);

  // Have any reviews been posted?
  if (place.reviews.length) {
    createReviewCard(place, reviewList);
  } else {
    const noReviewMessage = document.createElement("p");
    noReviewMessage.textContent = "Be the first to leave a comment";
  }
}

function clearPlaceDetailsSection(reviewList) {
  // Clear the current content of the place details section
  const placeDetail = document.querySelector(".place-amenities");

  // Clear previous reviews
  if (!reviewList) {
    console.error("Review list not found in the DOM.");
  }
  // Clean the dom
  placeDetail.innerHTML = "";
  reviewList.innerHTML = "";
}

function updatePlaceInfo(place) {
  // Create elements to display the place details (name, description, price, amenities and reviews)
  document.querySelector(".place-title").textContent = place.title;
  document.querySelector(".place-owner").textContent =
    place.owner.first_name + " " + place.owner.last_name;
  document.querySelector(".place-price").textContent =
    place.price + "€ per day";
  document.querySelector(".place-description").textContent = place.description;
}

function displayPlaceAmenity(place) {
  // Append the created elements to the place details section
  place.amenities.forEach((amenity, index, array) => {
    const amenityCard = document.createElement("li");
    amenityCard.classList.add("amenity-card");

    // Add comma only if it is not the last element
    if (index < array.length - 1) {
      amenityCard.textContent = amenity.name + ",";
    } else {
      amenityCard.textContent = amenity.name;
    }
    amenityCard.style.display = "block";
    document.querySelector(".place-amenities").appendChild(amenityCard);
  });
}

function getReviewTemplate() {
  // Get the review template
  const reviewTemplate = document.querySelector("#review-template");
  if (!reviewTemplate) {
    console.error("Review template not found in the DOM.");
    return;
  }
  return reviewTemplate;
}

function createReviewCard(place, reviewList) {
  const reviewTemplate = getReviewTemplate();
  // Iterate in reviews place list
  place.reviews.forEach((review) => {
    // Create a new review card
    const reviewCard = reviewTemplate.content.cloneNode(true);

    // Fill in the card with the corresponding values
    reviewCard.querySelector(".review-user").textContent =
      review.user_first_name + " " + review.user_last_name + ":";
    reviewCard.querySelector(".review-description").textContent =
      review.description;

    // Get the stars of this card and convert rating into stars
    const starContainer = reviewCard.querySelector(".review-star-rating");
    setActiveStars(review.rating, starContainer);

    // Put the card in its container
    reviewList.appendChild(reviewCard);
  });
}

function setActiveStars(count, container) {
  const stars = container.querySelectorAll("i");

  stars.forEach((star, index) => {
    if (index < count) {
      star.classList.add("active");
    } else {
      star.classList.remove("active");
    }
  });
}
