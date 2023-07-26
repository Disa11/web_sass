var preloader = document.getElementById("preloader");
const element = document.getElementsByClassName("tagvisibility");

window.addEventListener("load", () => {
  preloader.style.display = "none";
  document.getElementById('body_id').classList.remove('hidden');

  for (let i = 0; i < element.length; i++) {
    element[i].style.visibility = "visible"
  }
})