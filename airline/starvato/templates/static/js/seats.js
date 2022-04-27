
let pySection = ['A','B','C','D','E','F']
let pyFile = parseInt(pyPosti/pySection.length) /* prende i posti e li divide in file per la lunghezza di section */
const array_bookings = []
for(let m = 0; m < py_saved_booking.length; m ++){
    array_bookings.push(py_saved_booking[m].textContent)
}
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
let airC_seat = document.getElementById('code');

let selectId = document.getElementById('selectId').textContent
let fly = document.getElementById('fly')
fly.value = selectId




for(let i = 0; i!=pyFile; i++){                     /* per ogni fila */
    let rowe = document.createElement('div')
    rowe.classList.add('rowe')                      /* inserisco una nuova riga */
    for(let j = 0; j!=pySection.length; j++){       /* per ogni elemento della sezione */
        seat = document.createElement('div')        /* creo un posto */
        seat.classList.add('seat')
        seat.id = i + '' + pySection[j] 
        for(let booked = 0; booked < array_bookings.length; booked++){
            if(seat.id == array_bookings[booked]){
                    seat.classList.add('occupied')
            }
        }
        /* gli do l'id di css del numero piu' la sezione */
        rowe.appendChild(seat)
    }
    containera[0].appendChild((rowe))
}

function updateSelectedSeat(){
    selectedSeats = document.querySelectorAll('.rowe .seat.selected')
    count.innerText = airC_seat.value
}

tcontainer.addEventListener('click', (e)=> { 
    if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')){
        try {
            selectedSeats[0].classList.remove('selected')
            e.target.classList.toggle('selected');
            airC_seat.value = e.target.id
        } catch (error) {
            e.target.classList.toggle('selected')
            airC_seat.value = e.target.id
        }
    }
    updateSelectedSeat();
});