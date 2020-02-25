
/* MENU EXPANDIBLE */

function visible() {
    let getMenuEmergente = document.querySelector(".menuEmergente");
    getMenuEmergente.style.width = "100%";
    getMenuEmergente.style.opacity = "1";
}

function visibleDesktop() {
    let getMenuEmergente = document.querySelector(".menuEmergente");
    getMenuEmergente.style.width = "20%";
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

function visibleLoginDesktop() {
    let getLoginButton = document.querySelector(".loginExpandido");
    getLoginButton.style.width = "100%";
    getLoginButton.style.opacity = "1";

    let getLoginFondo = document.querySelector(".loginFondoExterior");
    getLoginButton.style.display = "contents";
}

function invisibleLogin() {
    let getLoginButton = document.querySelector(".loginExpandido");
    getLoginButton.style.width = "0%";
    getLoginButton.style.opacity = "0.5";
}

/* FIN LOGIN */