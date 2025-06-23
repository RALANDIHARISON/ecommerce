# Django E-commerce Store con Gestione Ordini (Multi-App)

Benvenuto nel repository del progetto E-commerce Store, realizzato con il framework Django. 
Questo progetto è stato sviluppato per dimostrare le capacità di un'applicazione web complessa, suddivisa in più app con funzionalità distinte e gestione avanzata degli utenti e dei permessi.

## Funzionalità Principali

Il progetto si compone di due app principali per separare le responsabilità e migliorare l'organizzazione:

1.  **App `store` (Frontend E-commerce):**
    * **Catalogo Prodotti:** Visualizzazione di un elenco di prodotti con dettagli (nome, prezzo, immagine).
    * **Carrello Acquisti:** Funzionalità completa di aggiunta/rimozione articoli e gestione quantità.
    * **Processo di Checkout:** Gestione delle informazioni di spedizione e finalizzazione dell'ordine.
    * **Gestione Clienti:** Supporto per utenti registrati e checkout come ospite.

2.  **App `orders` (Dashboard di Gestione Ordini per Manager):**
    * **Dashboard Manager:** Un'interfaccia dedicata per la gestione degli ordini, separata dall'admin di Django per un'esperienza utente più mirata.
    * **Elenco Ordini:** Visualizzazione di tutti gli ordini con informazioni chiave (ID, cliente, data, totale, stato).
    * **Dettagli Ordine:** Possibilità di visualizzare i dettagli completi di ciascun ordine, inclusi gli articoli e l'indirizzo di spedizione.
    * **Permessi Avanzati:** Accesso controllato a questa sezione tramite un sistema di permessi basato su gruppi, che distingue tra utenti clienti e utenti manager. Questa app utilizza Class-Based Views generiche.

## Requisiti Esame Soddisfatti

* **Due App Django:** Il progetto è chiaramente diviso in due app (`store` e `orders`) con responsabilità distinte.
* **Class-Based Views Generiche:** L'app `orders` utilizza Class-Based Views generiche (`ListView`, `DetailView`) per la gestione degli ordini.
* **Due Gruppi di Utenti con Permessi Diversi:** È implementato un sistema di permessi con almeno due gruppi di utenti (`Customers` implicito tramite la funzionalità e-commerce, e `Store Managers` esplicito per la dashboard di gestione).
* **Estensione e Personalizzazione della Classe User:** Il modello `Customer` è collegato al modello `User` di Django tramite `OneToOneField`, permettendo l'aggiunta di informazioni specifiche del cliente.
* **Database Pre-popolato:** Il repository include un database SQLite (`db.sqlite3`) con dati di esempio per prodotti, clienti e ordini, consentendo l'esplorazione immediata dell'applicazione.
* **`requirements.txt`:** Il file `requirements.txt` è fornito per facilitare l'installazione delle dipendenze.
* **`README.md`:** Questo file fornisce una descrizione del progetto e le istruzioni.

## Come Avviare il Progetto Localmente

Segui questi passaggi per configurare ed eseguire il progetto sul tuo ambiente locale:

1.  **Clona il Repository:**
    ```bash
    git clone [https://github.com/RALANDIHARISON/ecommerce.git]
    cd <ecommerce>
    ```

2.  **Crea e Attiva un Ambiente Virtuale :**
    ```bash
    python -m venv .venv
    # Su Windows:
    .\.venv\Scripts\activate
    # Su macOS/Linux:
    source ./.venv/bin/activate
    ```

3.  **Installa le Dipendenze:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Esegui le Migrazioni del Database:**
    (Il file `db.sqlite3` con i dati pre-popolati è già incluso).
    ```bash
    python manage.py migrate
    ```

5.  **Crea un Superuser (se non l'hai già fatto):**
    Questo utente ti darà accesso completo all'admin di Django per la configurazione.
    ```bash
    python manage.py createsuperuser
    ```
    Segui le istruzioni a schermo per username, email e password (es. `lalaina`).

6.  **Crea un Utente "Store Manager" per i test:**
    * Accedi all'admin di Django: `http://127.0.0.1:8000/admin/` con il tuo superuser (es. `lalaina`).
    * Vai su `Authentication and Authorization` > `Groups` > `Add Group`. Nomina il gruppo `Store Managers`.
    * Assegna al gruppo i permessi necessari per la gestione degli ordini e prodotti (es. `Can view order`, `Can change order`, `Can view order item`, `Can view shipping address`, `Can view customer`, `Can add product`, `Can change product`, `Can delete product`, `Can view product`). **SALVA**.
    * Vai su `Authentication and Authorization` > `Users` > `Add user`. Crea un nuovo utente (es. `manager_test` o `mariefatima@gmail.com`), **SENZA spuntare "Superuser status"**.
    * Assegna questo utente al gruppo `Store Managers` nella sezione `Groups`. **SALVA**.

7.  **Avvia il Server di Sviluppo:**
    ```bash
    python manage.py runserver
    ```

## Navigazione dell'Applicazione

* **Frontend E-commerce:** Accedi a `http://127.0.0.1:8000/`. Puoi navigare tra i prodotti, aggiungerli al carrello e procedere al checkout.
* **Dashboard di Gestione Ordini:** Accedi a `http://127.0.0.1:8000/orders-management/`. **Per accedere a questa sezione, devi prima loggarti** con un utente che appartiene al gruppo `Store Managers` (es. `manager_test` o `mariefatima@gmail.com` con la password che hai scelto).
* **Django Admin:** Accedi a `http://127.0.0.1:8000/admin/`. Richiede l'accesso di un utente con "Staff status" e i permessi necessari (es. il superuser `lalaina` o l'utente `manager_test` se ha staff status).

## Link al Deployment

**Il progetto è deployato e accessibile qui:**

**[]**

---

Ora puoi usare il comando `New-Item README.md -ItemType File` (o `ni README.md`) in PowerShell, poi aprire il file appena creato nel tuo editor e incollare questo contenuto, salvandolo.