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
const panelBusqueda = document.getElementById("panelBusqueda");
const panelRaza = document.getElementById("Raza");
const panelSalud = document.getElementById("Salud");
const panelEdad = document.getElementById("Edad");
const panelSexo = document.getElementById("Sexo");
const panelDisponible = document.getElementById("panelDisponible");

var opcionesPerros = ["razaCredo|Raza / Credo","cimarron|Cimarron","rottweiler|Rottweiler","ovejeroAleman|Ovejero Aleman","mixto|Mixto"];
var opcionesGatos = ["largoPelo|Largo del Pelo","largo|Largo","medio|Medio","largo|Corto","sinPelo|Sin pelo"];
var opcionesEdad = ["franajaEtaria|Franja Etaria","cachorro|Cachorro","joven|Joven","adulto|Adulto","mayor|Mayor"];
var opcionesSexo = ["optar|Opta por un Género","macho|Macho","hembra|Hembra"];
var opcionesRefugiosDistancia = ["distancia|Distancia del Refugio","10kilometros|10 Kilometros o menos","25kilometros|25 Kilometros o menos","50kilometros|50 kilometros o menos","sinLimite|Sin límite"]
var opcionesRefugiosAnimales = ["mascotaQueBusco|Mascota que Busco","perros|Perros","gatos|Gatos","otros|Otros"]
botonPerros.classList.add("botonesActivos");


function cambiaActivos(argumento) {
    if(argumento === botonPerros.innerHTML) {
        botonPerros.classList.add("botonesActivos");
        botonGatos.classList.remove("botonesActivos");
        botonOtros.classList.remove("botonesActivos");
        botonRefugios.classList.remove("botonesActivos");
        botonImagen.src="/Animalicis/static/image/perroDesktop.png";
        botonImagen.style.width="100%";
        botonImagen.style.bottom="0";
        botonImagen.style.left="0";

        panelDisponible.style.display="none";
        panelBusqueda.style.display="block";
        panelRaza.style.display = "block";
        panelSalud.style.display = "block";
        panelRaza.style.width = "45%";
        panelSalud.style.width = "45%";
        panelSexo.style.width = "45%";
        panelEdad.style.width = "45%";

        panelEdad.innerHTML = "";
        for(let opcion in opcionesEdad) {
            let par = opcionesEdad[opcion].split("|");
            let nuevoElemento = document.createElement("option");
            nuevoElemento.value = par[0];
            nuevoElemento.innerHTML = par[1];
            panelEdad.options.add(nuevoElemento);
        }
        panelSexo.innerHTML = "";
        for(let opcion in opcionesSexo) {
            let par = opcionesSexo[opcion].split("|");
            let elementoNuevo = document.createElement("option");
            elementoNuevo.value = par[0];
            elementoNuevo.innerHTML = par[1];
            panelSexo.options.add(elementoNuevo);
        } 
        panelRaza.innerHTML = "";
        for(let opcion in opcionesPerros) {
            let par = opcionesPerros[opcion].split("|");
            let nuevoElemento = document.createElement("option");
            nuevoElemento.value = par[0];
            nuevoElemento.innerHTML = par[1];
            panelRaza.options.add(nuevoElemento);
        }
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

        panelDisponible.style.display="none";
        panelBusqueda.style.display="block";
        panelRaza.style.display = "block";
        panelSalud.style.display = "block";
        panelRaza.style.width = "45%";
        panelSalud.style.width = "45%";
        panelSexo.style.width = "45%";
        panelEdad.style.width = "45%";

        panelEdad.innerHTML = "";
        for(let opcion in opcionesEdad) {
            let par = opcionesEdad[opcion].split("|");
            let nuevoElemento = document.createElement("option");
            nuevoElemento.value = par[0];
            nuevoElemento.innerHTML = par[1];
            panelEdad.options.add(nuevoElemento);
        }
        panelSexo.innerHTML = "";
        for(let opcion in opcionesSexo) {
            let par = opcionesSexo[opcion].split("|");
            let elementoNuevo = document.createElement("option");
            elementoNuevo.value = par[0];
            elementoNuevo.innerHTML = par[1];
            panelSexo.options.add(elementoNuevo);
        }
        panelRaza.innerHTML = "";
        for(let opcion in opcionesGatos) {
            let par = opcionesGatos[opcion].split("|");
            let nuevoElemento = document.createElement("option");
            nuevoElemento.value = par[0];
            nuevoElemento.innerHTML = par[1];
            panelRaza.options.add(nuevoElemento);
        }
    }
    else if(argumento === botonOtros.innerHTML) {
        botonPerros.classList.remove("botonesActivos");
        botonGatos.classList.remove("botonesActivos");
        botonOtros.classList.add("botonesActivos");
        botonRefugios.classList.remove("botonesActivos");

        botonImagen.src="/Animalicis/static/image/panelOtros.png";
        botonImagen.style.width="140%";
        botonImagen.style.left="-10rem";
        botonImagen.style.bottom="0";

        panelBusqueda.style.display="none";
        panelDisponible.style.display="block";
    }
    else if(argumento === botonRefugios.innerHTML) {
        botonPerros.classList.remove("botonesActivos");
        botonGatos.classList.remove("botonesActivos");
        botonOtros.classList.remove("botonesActivos");
        botonRefugios.classList.add("botonesActivos");

        panelDisponible.style.display="none";
        panelBusqueda.style.display="block";
        panelRaza.style.display = "none";
        panelSalud.style.display = "none";
        panelSexo.style.width = "95%";
        panelEdad.style.width = "95%";

        panelEdad.innerHTML = "";
        for(let opcion in opcionesRefugiosAnimales) {
            let par = opcionesRefugiosAnimales[opcion].split("|");
            let nuevoElemento = document.createElement("option");
            nuevoElemento.value = par[0];
            nuevoElemento.innerHTML = par[1];
            panelEdad.options.add(nuevoElemento);
        }
        panelSexo.innerHTML = "";
        for(let opcion in opcionesRefugiosDistancia) {
            let par = opcionesRefugiosDistancia[opcion].split("|");
            let elementoNuevo = document.createElement("option");
            elementoNuevo.value = par[0];
            elementoNuevo.innerHTML = par[1];
            panelSexo.options.add(elementoNuevo);
        }

        botonImagen.src="/Animalicis/static/image/refugioPanel2.png";
        botonImagen.style.width="170%";
        botonImagen.style.bottom="0rem";
        botonImagen.style.left="-10rem";
    }
}


/* FIN DE BOTONES DE SELECTORES */