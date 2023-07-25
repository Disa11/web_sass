var preloader = document.getElementById("preloader");

window.addEventListener("load", () => {
  preloader.style.display = "none";
  document.getElementById('body_id').classList.remove('hidden')
})