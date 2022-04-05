Starvato Airlines v.4.0.

prenotazione ora puo filtrare la ricerca tramite un salvataggio della ricerca su db e per ogni volta che viene fatta una nuova ricerca fa l'update della vecchia ricerca senza crearne una nuova, 

ora urls della app funge a pulire urls del project

la pagina search filtra bene i risultati ottenuti dalla ricerca


requisiti per farlo girare:
    db con nome del db dato al file;
    aver installato widget tweaks;

TO-DO:
    re-inserire i media cosi da usare gli under_banners
    inserire carsello

    creare matrice per i posti,
    creare funzione per inviare email(servira un form per la mail)
    creare il modifica ricerca in search
    fare in modo che la ricerca non parta subito ma che aspetti la selezione da parte dell'utente(basterebbe settare la data su Null)
    vedere libreria per settare distanza da un punto all'altro, scoprire nome


    mettere un flycode univoco al volo
    stampare 'nessun risultato' sullo schermo a ricerca non valida

    assumiamo per ora che esiste una solo tipo di posti, in seguito aggiungiamo seconda, prima ed economy



devo creare la page prenotazione che è legata all'id del volo che quando da search clicchi 'vai al biglietto' ti porta alla pagina <id:pk>/prenotazione

devo vedermi i video sui detail delle pagine

to-do: 
crea pagina detail
in questa pagina mostrare matrice posti e dopo la selezione nella stessa pagina contact form per ricevere la mail
mettere nel for del filtro il bottone che è a href collegato alla pagina prenotazione con id
