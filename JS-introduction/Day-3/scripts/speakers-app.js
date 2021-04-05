const speakersUL = document.getElementById("speakersUL");

for (let index = 0; index < speakers.length; index++) {
  let speaker = speakers[index];
  let speakerLi = `
    <li>
        ${speaker.name} - ${speaker.category}
    </li>
    `;
  speakersUL.insertAdjacentHTML("beforeend", speakerLi);
}
