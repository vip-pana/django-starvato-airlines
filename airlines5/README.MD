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

