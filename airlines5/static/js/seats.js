const pyPosti =  40 /* non va perche' e' in una pagina a se */

let pySection = ['A','B','C','D','E','F']

let pyFile = parseInt(pyPosti/pySection.length) /* prende i posti e li divide in file per la lunghezza di section */

/* con questo prendevo la lista delle prenotazioni da python inserita in for loop sull'html
con display=none... */

/* ...lo prendevo e inserivo dentro una nuova lista */


/* prendo il container dove inserire i posti */
const containera = document.getElementsByClassName('containera');
const tcontainer = document.querySelector('.containera');
const tseats = document.querySelectorAll('.rowe .seat:not(.occupied)');
const count = document.getElementById('count');
let selectedSeats = document.querySelectorAll('.rowe .seat.selected');
let selectedSeatsCount = selectedSeats.length;
let inputField = document.getElementById('code');

for(let i = 0; i!=pyFile; i++){                     /* per ogni fila */
    let rowe = document.createElement('div')
    rowe.classList.add('rowe')                      /* inserisco una nuova riga */
    for(let j = 0; j!=pySection.length; j++){       /* per ogni elemento della sezione */
        seat = document.createElement('div')        /* creo un posto */
        seat.classList.add('seat')
        seat.id = i + '' + pySection[j] 
        /* gli do l'id di css del numero piu' la sezione */
        rowe.appendChild(seat)
    }
    containera[0].appendChild((rowe))
}

function updateSelectedCount(){
    selectedSeats = document.querySelectorAll('.rowe .seat.selected')
    selectedSeatsCount = selectedSeats.length
    count.innerText = selectedSeatsCount
}

tcontainer.addEventListener('click', (e)=> { 
    if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')){
        try {
            selectedSeats[0].classList.remove('selected')
            e.target.classList.toggle('selected');
            
            inputField.value = e.target.id /* questo non va */

        } catch (error) {
            console.log('ua')
            e.target.classList.toggle('selected')
        }
    }
    updateSelectedCount();
});