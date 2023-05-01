const container = document.getElementById("bicker");
const bickerButton = document.getElementById("bickerButton");
const containerReal = document.getElementById("bicker-container");
const name = document.getElementById("name").value;
const email = document.getElementById("email").value;
const submitInformation = get.getElementById("submit");

let messages = [];

function displayChatBot() {
  container.style.display = "block";
  bickerButton.style.display = "none";
}
