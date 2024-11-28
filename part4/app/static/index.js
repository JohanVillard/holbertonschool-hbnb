export async function fetchPlaces(token) {
  const headers = {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  };

  // Make a GET request to fetch places data
  const response = await fetch("http://127.0.0.1:5000/api/v1/places", {
    method: "GET",
    headers: headers,
  });

  // Handle the response and pass the data to displayPlaces function
  if (response.ok) {
    return await response.json();
  }
}

export function displayPlaces(places) {
  // On index.html
  if (!places) {
    throw new Error("No places to display");
  }

  // Get the card place container
  const placeCardsContainer = document.querySelector("#place-cards-container");

  placeCardsContainer.innerHTML = "";
  // Create card for each place
  places.forEach((place) => {
    const placeCard = CreatePlaceCard(place);
    // Put the card in the container
    placeCardsContainer.appendChild(placeCard);
  });
  // Set #place-cards-container the display to grid. none by default
  placeCardsContainer.style.display = "grid";
  filterPlaceByPrice(places);
}

function CreatePlaceCard(place) {
  // Get the card place template
  const placeCardTemplate = document.querySelector("#place-card-template");

  // Create a card from the template
  const placeCard = placeCardTemplate.content.cloneNode(true);

  // Get the place details button
  const detailsButton = placeCard.querySelector(".details-button");

  // Set place infos
  placeCard.querySelector(".place-title").textContent = place.title;
  placeCard.querySelector(".place-price").textContent =
    "Price per night: €" + place.price;

  // Defines the button to be sent to the location detail when clicked
  detailsButton.addEventListener("click", () => {
    window.location.href = "/place.html?id=" + place.id;
  });
  return placeCard;
}

function filterPlaceByPrice(places) {
  // On index.html
  if (!places) {
    throw new Error("No places to filter");
  }

  // Get the place filter
  const priceFilter = document.getElementById("price-filter");

  priceFilter.addEventListener("change", (event) => {
    // Get the selected price value
    const maxPrice = event.target.value;

    // Get all the place card
    const placeCards = document.querySelectorAll(".place-card");

    // Iterate over the places and show/hide them based on the selected price
    placeCards.forEach((placeCard, index) => {
      // Get the actual place
      const place = places[index];
      // Manages card display in relation to filter price
      if (maxPrice === "all" || maxPrice >= place.price) {
        placeCard.style.display = "flex";
      } else {
        placeCard.style.display = "none";
      }
    });
  });
}
