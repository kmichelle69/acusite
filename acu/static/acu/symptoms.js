// WOLOLOLOLO

// ok

var hurt, hurts
hurt = document.getElementById("symptom").value
hurts = []

// doIt collects the hurts as they are selected
// da buttons will call doIt
// yes
function doIt() {
  hurts.push(hurt);
}

function showIt() {
  document.getElementById("allTheHurts").innerHTML = hurts.length;
}
