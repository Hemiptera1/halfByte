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

/* BOTONES DE SELECTORES */

const botonPerros = document.getElementById("botonPerros");
const botonGatos = document.getElementById("botonGatos");
const botonOtros = document.getElementById("botonOtros");
const botonRefugios = document.getElementById("botonRefugios");
const botonImagen = document.getElementById("botonImagen");

function cambiaActivos(argumento) {
    console.log(argumento);
    console.log(botonGatos.innerHTML);
    if(argumento === botonPerros.innerHTML) {
        botonPerros.classList.add("botonesActivos");
        botonGatos.classList.remove("botonesActivos");
        botonOtros.classList.remove("botonesActivos");
        botonRefugios.classList.remove("botonesActivos");
        botonImagen.src="/Animalicis/static/image/perroDesktop.png";
        botonImagen.style.width="100%";
        botonImagen.style.bottom="0";
        botonImagen.style.left="0";
    }
    else if(argumento === botonGatos.innerHTML) {
        botonPerros.classList.remove("botonesActivos");
        botonGatos.classList.add("botonesActivos");
        botonOtros.classList.remove("botonesActivos");
        botonRefugios.classList.remove("botonesActivos");
        botonImagen.src="/Animalicis/static/image/gatoSelectores.png";
        botonImagen.style.width="115%";
        botonImagen.style.bottom="-1.3rem";
        botonImagen.style.left="-5.5rem";
    }
    else if(argumento === botonOtros.innerHTML) {
        botonPerros.classList.remove("botonesActivos");
        botonGatos.classList.remove("botonesActivos");
        botonOtros.classList.add("botonesActivos");
        botonRefugios.classList.remove("botonesActivos");
    }
    else if(argumento === botonRefugios.innerHTML) {
        botonPerros.classList.remove("botonesActivos");
        botonGatos.classList.remove("botonesActivos");
        botonOtros.classList.remove("botonesActivos");
        botonRefugios.classList.add("botonesActivos");
    }
}


/* FIN DE BOTONES DE SELECTORES */