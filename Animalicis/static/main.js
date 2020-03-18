/* MENU EXPANDIBLE */

function visible() {
    let getMenuEmergente = document.querySelector(".menuEmergente");
    getMenuEmergente.style.width = "100%";
    getMenuEmergente.style.opacity = "1";
}

function visibleDesktop() {
    let getMenuEmergente = document.querySelector(".menuEmergente");
    getMenuEmergente.style.width = "30rem";
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
        getLoginButton.style.width = "50%";
        getLoginButton.style.right = "25%";
        getLoginButton.style.borderRadius = "5rem";
        getLoginButton.style.opacity = "1";
}

function visibleLogin2() {
    let getLoginButton = document.querySelector(".loginExpandido");
        getLoginButton.style.width = "100%";
        getLoginButton.style.right = "0";
        getLoginButton.style.borderRadius = "0";
        getLoginButton.style.opacity = "1";
}

function invisibleLogin() {
    let getLoginButton = document.querySelector(".loginExpandido");
    getLoginButton.style.width = "0%";
    getLoginButton.style.right = "0%";
    getLoginButton.style.borderRadius = "0";
    getLoginButton.style.opacity = "0.5";
}

/* FIN LOGIN */