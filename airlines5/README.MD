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

- creare pop uo visibile solo con errore aggiungengdo nel context un error visibile sull'html solo se entra nell'except

-creare tutti i collegamenti alla fine di tutto

-mandare mex per il successo dell'operazione e vedere se fare pagamento fittizio

-fare search come maria
