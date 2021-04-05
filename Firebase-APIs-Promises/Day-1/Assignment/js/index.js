const dataURL = "http://www.omdbapi.com/?s=batman&apikey=ba7aec68";
const selectionWrapper = document.getElementById("selectionWrapper");
const selectedWrapper = document.getElementById("selectedWrapper");
let request = new XMLHttpRequest();

function filmIDGet(filmID) {
  let filmURL = `http://www.omdbapi.com/?i=${filmID}&apikey=ba7aec68`;
  let filmByID = new XMLHttpRequest();
  filmByID.addEventListener("load", function () {
    let filmResult = JSON.parse(this.responseText);
    let filmOutput = `
                <article class="media is-flex is-flex-wrap-wrap">
            <figure class="media-left">
              <p>
                <img class='image' src="${filmResult.Poster}">
              </p>
            </figure>
            <div class="media-content">
              <div class="content">
                <p>
                  <strong>${filmResult.Title}</strong>
                  <br>
                  <strong>Year:</strong> ${filmResult.Year}
                  <br>
                  <strong>Rated:</strong> ${filmResult.Rated}
                  <br>
                  <strong>Released:</strong> ${filmResult.Released}
                  <br>
                  <strong>Director:</strong> ${filmResult.Director}
                </p>
              </div>
            </div>
          </article>
                `;
    selectedWrapper.innerHTML = filmOutput;
  });
  filmByID.open("GET", filmURL);
  filmByID.send();
}

request.addEventListener("load", function () {
  let result = JSON.parse(this.responseText);
  let output = result.Search.map(function (film) {
    return `
        <div class='column'>
        <img class='selectionIcon' src='${film.Poster}'>
        <p>${film.Title}</p>
        <button onclick='filmIDGet("${film.imdbID}")'>Select</button>
        </div>
        `;
  });
  selectionWrapper.innerHTML = output.join("");
});

request.open("GET", dataURL);
request.send();

/*
<article class="media is-flex is-flex-wrap-wrap">
            <figure class="media-left">
              <p>
                <img class='image' src="https://m.media-amazon.com/images/M/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg">
              </p>
            </figure>
            <div class="media-content">
              <div class="content">
                <p>
                  <strong>Batman Begins</strong>
                  <br>
                  <strong>Year:</strong> 2005
                  <br>
                  <strong>Rated:</strong> PG-13
                  <br>
                  <strong>Released:</strong> 15 Jun 2005
                  <br>
                  <strong>Director:</strong> Christopher Nolan
                </p>
              </div>
            </div>
          </article>
*/
