mountain-rehub
==============

Aggregatore di recensioni. Un progetto per imparare.

## Installazione


Per installare l'ambiente:

    $ git clone https://github.com/xavitorne/mountain-rehub.git
    $ cd mountain-rehub
    $ virtualenv env
    $ source env/bin/activate
    

Una volta che siamo nell'ambiente, per installare le dipendeze, basta fare:

    $ pip install -r requirements.txt

E per eseguire:

    $ python run.py

 
Per iniziare con il database, bisogna creare un user "rehub" e password "rehub", già che nel file config.py usa questo user per il database. 

Dopo per creare le tables dentro il db:

    $ python db_create.py
    $ python db_migrate.py
    


