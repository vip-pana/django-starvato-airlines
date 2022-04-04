airlines v.3.0

ho ricreato il tutto per tenerlo piu' pulito e ho usato un altro database perche' avevo incasinato quello prima

domanda: dopo aver fatto un cambiamento tipo cambiare proprio il tipo di field di un modello cosa devo fare per salvare questa migrazione senza incasinare tutto o dover ricreare il db

ho creato l'app prenotazione che possiede i models airports collegato con chiave esterna a fly,
fly usa il file forms.py per dare un form visibile al template,
viene tutto inserito nel context della views che renderizza home.html

il form e' visibile con le sue modifiche grazie al modulo di django installato a parte 'widget_tweaks'
che permette di modificare direttamente sul html

PROBLEMI:
- dentro alle select non so come modificare i value delle option per dargli un ID cosi da usare per la search
-p.s. voglio capire come fare anche senza widget_tweaks a mettere i value nelle option

-capire come estrarre i dati utilizzando i widget_tweaks, senza e' fattibile ma con ho notato qualche problema

TO DO:
- estrarre i dati dal form di home.html
- pagina search dove vengono mostrati i dati filtrati su fly

MENO IMPORTANTE:
- creare una pagina di amministrazione per inserire dati non del superuser
-inserire gli under banners
- inserire carosello

_____________________________________________________________________________--
il form di ricerca base funziona quasi del tutto devo solo collegare come mettere
per farlo è un po un casino o creo la funzione dentro o metto nell'action che chiama la funzione o boh non ho capit


vedere urls per le app
vedere redirect