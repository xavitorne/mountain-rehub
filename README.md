mountain-rehub
==============

Aggregatore di recensioni. Un progetto per imparare.

## Installazione


Per installare l'ambiente:

    $ git clone https://github.com/xavitorne/mountain-rehub.git
    $ cd mountain-rehub
    $ virtualenv env
    $ source env/bin/activate
    
Se non avete il pachetto libpq-dev, bisogna:

    $ sudo apt-get install libpq-dev
    
Una volta che siamo nell'ambiente, per installare le dipendeze, basta fare:

    $ pip install -r requirements.txt

E per eseguire:

    $ python run.py

 
Per iniziare con il database, se si usa postgres, , bisogna creare un user "rehub" e password "rehub", già che nel file config.py usa questo user per il database. Se si usa altri db, cambiare il file config.py per la configurazione corrispondente.

C'è un piccolo script chiamato rhdb, che controlla la creazione del database, e upgrades possibili. Per creare il database e le tables:

    $ python rhdb.py --help
    $ python rhdb.py --create

Una volta creato il database, dentro la shell env/bin/python, possiamo giocare e creare:

    $ from rehub import db
    $ from rehub.models import Report
    $ rep = Report()
    $ rep.title = 'ciao'
    $ rep.kind = '1'
    $ db.session.add(rep)
    $ db.session.commit()
    $ Report.query.all()
