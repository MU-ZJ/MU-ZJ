let starters = document.getElementById("starters");
let entrees = document.getElementById("entrees");
let desserts = document.getElementById("desserts");
let starterWrapper = document.getElementById("starterWrapper");
let entreeWrapper = document.getElementById("entreeWrapper");
let dessertWrapper = document.getElementById("dessertWrapper");
let filter = document.getElementById("filter");

let starterPrint = dishes.map(function (dish) {
  if (dish.course == "Starters") {
    return `
        <div class="card is-mobile">
          <div class="card-image">
            <figure class="image is-square is-fullwidth">
              <img src=${dish.imageURL} alt="Placeholder image">
            </figure>
          </div>
          <div class="card-content is-mobile">
            <div class="media">
              <div class="media-content">
                <p class="title is-4">${dish.title} - $${dish.price}</p>
              </div>
            </div>
            <div class="content">
              ${dish.description}
            </div>
          </div>
        </div>
      </div>
        `;
  }
});

let entreePrint = dishes.map(function (dish) {
  if (dish.course == "Entrees") {
    return `
        <div class="card is-mobile">
          <div class="card-image">
            <figure class="image is-square is-fullwidth">
              <img src=${dish.imageURL} alt="Placeholder image">
            </figure>
          </div>
          <div class="card-content is-mobile">
            <div class="media">
              <div class="media-content">
                <p class="title is-4">${dish.title} - $${dish.price}</p>
              </div>
            </div>
            <div class="content">
              ${dish.description}
            </div>
          </div>
        </div>
      </div>
        `;
  }
});

let dessertPrint = dishes.map(function (dish) {
  if (dish.course == "Desserts") {
    return `
        <div class="card is-mobile">
          <div class="card-image">
            <figure class="image is-square is-fullwidth">
              <img src=${dish.imageURL} alt="Placeholder image">
            </figure>
          </div>
          <div class="card-content is-mobile">
            <div class="media">
              <div class="media-content">
                <p class="title is-4">${dish.title} - $${dish.price}</p>
              </div>
            </div>
            <div class="content">
              ${dish.description}
            </div>
          </div>
        </div>
      </div>
        `;
  }
});

starters.innerHTML = starterPrint.join("");
entrees.innerHTML = entreePrint.join("");
desserts.innerHTML = dessertPrint.join("");

filter.addEventListener("change", function () {
  if (filter.value == "1") {
    starterWrapper.classList.remove("hidden");
    entreeWrapper.classList.remove("hidden");
    dessertWrapper.classList.remove("hidden");
  } else if (filter.value == "2") {
    entreeWrapper.className = "hidden";
    dessertWrapper.className = "hidden";
    starterWrapper.classList.remove("hidden");
  } else if (filter.value == "3") {
    starterWrapper.className = "hidden";
    dessertWrapper.className = "hidden";
    entreeWrapper.classList.remove("hidden");
  } else if (filter.value == "4") {
    starterWrapper.className = "hidden";
    entreeWrapper.className = "hidden";
    dessertWrapper.classList.remove("hidden");
  }
});
