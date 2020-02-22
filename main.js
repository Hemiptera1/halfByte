
/* MENU EXPANDIBLE */

function visible() {
    let getMenuEmergente = document.querySelector(".menuEmergente");
    getMenuEmergente.style.width = "100%";
    getMenuEmergente.style.opacity = "1";
}

function invisible() {
    let getMenuEmergente = document.querySelector(".menuEmergente");
    getMenuEmergente.style.width = "0%";
    getMenuEmergente.style.opacity = "0.5%";
}

/* FIN MENU EXPANDIBLE */

/* LOGIN */

function visibleLogin() {
    let getLoginButton = document.querySelector(".loginExpandido");
    getLoginButton.style.width = "100%";
    getLoginButton.style.opacity = "1";
}

function invisibleLogin() {
    let getLoginButton = document.querySelector(".loginExpandido");
    getLoginButton.style.width = "0%";
    getLoginButton.style.opacity = "0.5";
}

/* FIN LOGIN */