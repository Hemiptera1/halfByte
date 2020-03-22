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

/* FORMULARIO REGISTRO DE ANIMALES */

function poblar(s1, s2) {
    var s1 = document.getElementById(s1);
    var s1Value = s1.value;
    var s2 = document.getElementById(s2);
    var textoRaza = document.getElementById("textoRaza");
    s2.innerHTML = "";
    if(s1Value == "Perros") {
        var opcionesEspecie = ["elijaUno|Elija uno","cimarron|Cimarron","rottweiler|Rottweiler","ovejeroAleman|Ovejero Aleman","mixto|Mixto"];
        textoRaza.innerHTML = "¿De que raza es su perro?";
    } else if(s1Value == "Gatos") {
        var opcionesEspecie = ["elijaUno|Elija uno","largo|Largo","medio|Medio","largo|Corto","sinPelo|Sin pelo"]
        textoRaza.innerHTML = "¿Que tan largo es el pelaje de su gato?";
    } else if(s1Value == "Elija") {
        textoRaza.innerHTML = "Escoja una especie primero";
    }
    for(var opcion in opcionesEspecie) {
        var par = opcionesEspecie[opcion].split("|");
        var nuevaOpcion = document.createElement("option");
        nuevaOpcion.value = par[0];
        nuevaOpcion.innerHTML = par[1];
        s2.options.add(nuevaOpcion);
    }
}

const botonOriginal = document.getElementById("botonOriginal");
const botonFalso = document.getElementById("botonFalso");
const infoBoton = document.getElementById("infoBoton");

botonFalso.addEventListener("click", function() {
    botonOriginal.click();
})

botonOriginal.addEventListener("change", function() {
    if(botonOriginal.value) {
        infoBoton.innerHTML = "Subido :)";
    }
})

/*  FIN DEL FORMULARIO DE REGISTRO DE ANIMALES */