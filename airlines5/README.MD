airlines 5.0.

requisiti per farlo girare:
    db con nome del db dato al file;
    aver installato widget tweaks;

TO-DO:
- re-inserire gli STATIC cosi da:
    - inserire carosello
- creare function per mandare email()
- vedere geopy(possibile libreria per distanza)
- iMPORTANTE inserire un unique_code a Fly, Aircraft, Booking cosi da:
    - creare pagina cerca volo legata alle prenotazioni dei voli

- cambiare il select option in quella cosa bella che ha maria



make_id in utils.py:
'''cosciente del fatto che non sia sicuro
devo trovare un modo per confrontare tutti gli id creati e
se è uguale a qualcuno ricrearlo'''



ho avuto problemi col caricamento di detail, spero non riaccadano

studiare le API REST, sembra mi servano proprio


-----------------------------------------------
risolti problemi,nuovi problemi

le api posso farle come ultima cosa e non le devo richiamare per forz, usarle solo per richiamare i dati

problemi:
- creare unique id con sha256 o minore detto da bruno da decriptare, tengo il model, lo carico sul form per il biglietto che puo essere blank o con valore 0 e lo mando a django, poi modifico il save in modo che utilizzi sha256

- creare pop up visibile solo con errore aggiungengdo nel context un error visibile sull'html solo se entra nell'except FATTO

-creare tutti i collegamenti alla fine di tutto

-mandare mex per il successo dell'operazione e vedere se fare pagamento fittizio

-fare search come maria


-------------------------------------------------------

sembra che unique id non crei veri problemi devo solo renderli unici effettivamente dovrei creare un model di id in cui se esiste gia me ne riformula un altro

TODO:
creare search come maria
mandare email per fine di tutto(controllare se bruno ha creato pagamento fittizio) EMAIL FATTA IN PARTE
creare lista unique id
aggiungere carosello

----------------------------------------------------------
aggiornamento, il save funziona e rende unici gli ordini
riesco a inviare email di conferma dell'ordine alle persone, vorrei inserire html nelle email ma non ho capito ancora bene come si fa

TODO:
    -MOLTO IMPORTANTI:
    usare geopy per la distanza dei luoghi e il tempo di arrivo da punto A a punto B, molto importante
    creare prenotazione per più persone insieme, è un casino
    creare prenotazione andata e ritorno, credo sia meno un casino
    creare api per interrogare il codice, non ho ancora capito bene come fare
    creare login con meno privilegi per chi vuole inserire i voli, più importante

    MEDIA IMPORTANZA:
    creare pagina di ricerca prenotazione, più importante
    creare ulteriori variabili di manutenzione ecc, non ho capito se effettivamente le dovremmo fare

    MENO IMPORTANTE:
    creare search come maria (aspetto di tornare a lezione)
    inserire pagamento fittizio (aspetto bruno)
    sistemare estetica sito, meno importante
    creare email html da inviare, meno importante perché estetica

----------------------------------------------------------------
continuato da infobasic,
adesso gli aerei si scelogono per disponibilita di posti anche

adesso voglio selezionare tot posti per ogni persona che chiede di prenotare

devo rendere la scelta degli aereoporti possibile solo con il primo che connette il secondo e non tutti gli aereoporti

e poi tutti gli errori del caso

devo ricaricare la pagina con i biglietti da prendere per ogni persona che li deve prendere


posso mettere una choice field che se e' un numero maggiore di 1 deve mettere come stato pending
e poi mando la mail a tutte le pending 


---------------------------------------------------------------------

sto provando a prendere i biglietti per tot posti per persona

praticamente funziona che e' una prenotazione singola che si fa ricorrente fino a che le persone che hanno prenotato i posti sono finite,
problemi:
- invia la mail a ogni persona subito e non quando hanno finito di prendere i biglietti, questo costringe ogni utente ad aver gia preso un biglietto prima di terminare tutte le persone della prenotazione

dovrei prendere le persone a cui inviare la mail direttamente dal model booking

- sto provando a inserire uno status alla prenotazioni cosi da inviare la mail a chi ha lo status di pending e dopo averlo fatto cambiarlo in completed 

aggiornamento, non ho trovato un modo efficace per cambiare lo status(choiceField) dalla views.py, appena lo trovo dovrebbe essere fattibile sistemare molte cose

---------------------------------------------------------------------
ho sistemato la prenotazione per più persone ora tocca alla andata e ritorno

creo un boolean


swagger

ho un campo ritorno ma e' un problema farlo funzionare

devo controllare all'inizio se il campo ritorno e' selezionato

------------------------------------------------------------------------
sto lavorano sull'andata e ritorno e non con pochi problemi, ho problemi sul comunicare alla views quando attivare andata e quando invece sia andata che ritorno

devo provare con un campo charfield che si scrive

poi devo capire come fare la scelta dei voli, chiedero a lorenzo come ha gestito la sua

TO-DO:
- PIU IMPORTANTI:
-- finire andata e ritorno
-- creare API
-- creare slides di spiegazione (molto easy)


- MEDIA IMPORTANZA
-- geopy
-- creare sezione admin per creare voli
-- creare trova prenotazione


- MENO IMPORTANTI
-- creare ricerca come maria
-- non far trovare partenza scelta in arrivo scelta
-- sistemare problema delle prenotazioni multiple se esco dalle scelte mentre sto scegliendo


devo inserire un campo nel model che e' andata e farlo checkare quando seleziono l'andata nel primo search poi salvarmi da qualche parte obj selezionato tramite id o unique id e poi richiamarlo dopo aver selezionato il primo 



--------------------------------------------
sto bestemmiando parecchio

comunque il mio problema ora e' riuscire a mandare i dati al modello di andata e ritorno con is valid e dopo di che deve fare la ricerca del primo ticket e dopo se riesce del secondo

sono fermo a errori con il javascript quindi poi vedimao di aggiustare quello