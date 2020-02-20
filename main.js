let toggleMenuEmergente = false;

let toggleMenEme = function() {
    let getMenuEmergente = document.querySelector(".menuEmergente");

    if (toogleMenuEmergente === false) {
        getMenuEmergente.style.visibility = "visible";

        toggleMenuEmergente = true;
    }
}