
function changesource(source){
    let lbl = document.getElementById('source');
    lbl.innerHTML = source
}

function navbarfunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
