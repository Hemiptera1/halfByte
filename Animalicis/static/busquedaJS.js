const botonPerros = document.getElementById("botonPerros");
const botonGatos = document.getElementById("botonGatos");
const botonOtros = document.getElementById("botonOtros");
const botonRefugios = document.getElementById("botonRefugios");
const botonImagen = document.getElementById("botonImagen");
const panelRaza = document.getElementById("Raza");
const panelEdad = document.getElementById("Edad");
const panelSexo = document.getElementById("Sexo");
const porBarraSearch = document.getElementById("porBarraSearch");
const porBarraInput = document.getElementById("porBarraInput");

var opcionesPerros = ["razaCredo|Raza / Credo","cimarron|Cimarron","rottweiler|Rottweiler","ovejeroAleman|Ovejero Aleman","mixto|Mixto"];
var opcionesGatos = ["largoPelo|Largo del Pelo","largo|Largo","medio|Medio","largo|Corto","sinPelo|Sin pelo"];
var opcionesEdad = ["franajaEtaria|Franja Etaria","cachorro|Cachorro","joven|Joven","adulto|Adulto","mayor|Mayor"];
var opcionesSexo = ["optar|Opta por un Género","macho|Macho","hembra|Hembra"];
var opcionesRefugiosDistancia = ["distancia|Distancia del Refugio","10kilometros|10 Kilometros o menos","25kilometros|25 Kilometros o menos","50kilometros|50 kilometros o menos","sinLimite|Sin límite"]
var opcionesRefugiosAnimales = ["mascotaQueBusco|Mascota que Busco","perros|Perros","gatos|Gatos","otros|Otros"]
var opcionesAnimales = ["tipoDeMascota|Elije un tipo de mascota","aves|Aves","ofidios|Ofidios","roedores|Roedores","otros|Otros"];
botonPerros.classList.add("botonesActivos");


function cambiaActivos(argumento) {
    if(argumento === botonPerros.innerHTML) {
        botonPerros.classList.add("botonesActivos");
        botonGatos.classList.remove("botonesActivos");
        botonOtros.classList.remove("botonesActivos");
        botonRefugios.classList.remove("botonesActivos");
        botonImagen.src="/Animalicis/static/image/busquedaPerro3.png";
        botonImagen.style.width="100%";
        botonImagen.style.bottom="0";
        botonImagen.style.left="0";

        porBarraSearch.style.display = "grid";
        porBarraInput.style.width = "95%";
        panelRaza.style.display = "block";
        panelRaza.style.width = "95%";
        panelSexo.style.display = "block";
        panelSexo.style.width = "95%";
        panelEdad.style.width = "95%";

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

        botonImagen.src="/Animalicis/static/image/gato1.png";
        botonImagen.style.width="100%";
        botonImagen.style.bottom="-1.3rem";
        botonImagen.style.left="0rem";

        porBarraSearch.style.display = "grid";
        porBarraInput.style.width = "95%";
        panelRaza.style.display = "block";
        panelRaza.style.width = "95%";
        panelSexo.style.display = "block";
        panelSexo.style.width = "95%";
        panelEdad.style.width = "95%";

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

        porBarraSearch.style.display = "block";
        porBarraInput.style.width = "97%";
        panelRaza.style.width = "95%";
        panelSexo.style.display = "none";
        panelEdad.style.width = "95%";

        botonImagen.src="/Animalicis/static/image/parrot1.png";
        botonImagen.style.width="100%";
        botonImagen.style.left="0%";
        botonImagen.style.bottom="-20%";

        panelEdad.innerHTML = "";
        for(let opcion in opcionesAnimales) {
            let par = opcionesAnimales[opcion].split("|");
            let nuevoElemento = document.createElement("option");
            nuevoElemento.value = par[0];
            nuevoElemento.innerHTML = par[1];
            panelEdad.options.add(nuevoElemento);
        }
        panelRaza.innerHTML = "";
        for(let opcion in opcionesSexo) {
            let par = opcionesSexo[opcion].split("|");
            let elementoNuevo = document.createElement("option");
            elementoNuevo.value = par[0];
            elementoNuevo.innerHTML = par[1];
            panelRaza.options.add(elementoNuevo);
        }
    }
    else if(argumento === botonRefugios.innerHTML) {
        botonPerros.classList.remove("botonesActivos");
        botonGatos.classList.remove("botonesActivos");
        botonOtros.classList.remove("botonesActivos");
        botonRefugios.classList.add("botonesActivos");

        porBarraSearch.style.display = "block";
        porBarraInput.style.width = "97%";
        panelRaza.style.width = "95%";
        panelSexo.style.display = "none";
        panelEdad.style.width = "95%";

        panelEdad.innerHTML = "";
        for(let opcion in opcionesRefugiosAnimales) {
            let par = opcionesRefugiosAnimales[opcion].split("|");
            let nuevoElemento = document.createElement("option");
            nuevoElemento.value = par[0];
            nuevoElemento.innerHTML = par[1];
            panelEdad.options.add(nuevoElemento);
        }
        panelRaza.innerHTML = "";
        for(let opcion in opcionesRefugiosDistancia) {
            let par = opcionesRefugiosDistancia[opcion].split("|");
            let elementoNuevo = document.createElement("option");
            elementoNuevo.value = par[0];
            elementoNuevo.innerHTML = par[1];
            panelRaza.options.add(elementoNuevo);
        }

        botonImagen.src="{{ url_for('static', filename='image/shelter1.png') }}";
        botonImagen.style.width="70%";
        botonImagen.style.bottom="-1rem";
        botonImagen.style.left="20%";
    }
}
