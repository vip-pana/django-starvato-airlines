questa e' la documentazione su definitive airlines

CONFIGURAZIONE:

VIRTUALENV:
ho creato un virtual enviroments dove installare le librerie di utilizzo e tenere pulito il pip di python:
attivare virtual env 'source venv/bin/activate'

usare il file 'requirements.txt' per installare dentro al virtual enviroments le librerie di utilizzo:
dopo aver attivato il venv, per installare 'pip install -r requirements.txt'

SETTINGS.PY:
dopo aver installato le librerie aprire definitive_airlines/settings.py e inserire in INSTALLED_APPS 'widget_tweaks'

widget_tweaks e' una shortcut di django per renderizzare i modelli presi da forms.py e inserire gli attributi direttamente sulla pagina html

modificare le impostazioni di DATABASES per usare PostgreSQL, di base e' in utilizzo SQLlite
--------------------------------------------------
il progetto e' svolto usando il framework django

APPLICAZIONE:
1)creo una app di nome starvato_airlines
2)inserisco i modelli creati nel modello ERD
inserisco come modelli anche uno per salvare le ricerche

---------------------------------------------------
attivare il modifica info e elimina prenotazione

creare andata e ritorno
#creare accesso per aggiungere voli
