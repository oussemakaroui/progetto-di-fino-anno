# **Documento dei requisiti - Progetto Meteo e info città - Lorenzi,Karoui**

## **1. Titolo del progetto**
 - Meteo e Info Città

## **2. Obiettivo**
 - Il programma chiede all'utenete di inserire il nome di una città. Di seguito il programma offre un menù che permette all'utente di scegliere se leggere i dati meteorologi e urbani o se visualizzare un grafico del meteo della città scelta.

## **3. Attori**
 - **Utente** → inserisce la città,visualizza meteo e grafici
 - **Sistema** → recupera dati meteo e li elabora

## **4. Requisiti funzionali**
 - Avviare il programma con un menu principale
 - Consentire all’utente di inserire il nome di una città
 - Recuperare i dati meteo tramite API esterna
 - Mostrare temperatura e descrizione del meteo
 - Salvare i dati raccolti in un file CSV
 - Permettere la visualizzazione di un grafico delle temperature

 - Filtrare i dati per città selezionata
 - Gestire errori (città non trovata, file mancante, ecc.)
 - Offrire la possibilità di tornare al menu principale o uscire

## **5. Requisiti non  funzionali**
 - Gestione degli errori per input non validi
- Codice organizzato e modulare
- Utilizzo di librerie esterne affidabile

- Prestazioni adeguate (risposta veloce alle richieste API)
- Salvataggio dei dati tramite file CSV

## **6. Scelta dei package python**
- **requests** → per effettuare richieste HTTP all’API meteo
- **pandas** → per gestire e salvare i dati in formato tabellare

- **matplotlib** → per creare grafici delle temperature

## **7. Suddivisione del lavoro**
- **Lorenzi** → sviluppo menù principale, gestione input/output e implementazione della chiamata API

- **Karoui** → gestione dati meteo,salvataggoio dati e creazione grafici

## **8. Flusso del programma** 
![alt text](image.png)

## **9. Cronoprogramma**

# Diagramma di Gantt - App Meteo

```mermaid
gantt
    title PROGRAMMA DI SVILUPPO - APP METEO
    dateFormat YYYY-MM-DD
    axisFormat Settimana %W
    tickInterval 1week

    %% La timeline parte esattamente con la settimana 1
    section Lorenzi
    Analisi e Requisiti     :a1, 2026-01-05, 7d
    Struttura Base          :a2, after a1, 7d
    Gestione I/O            :a3, after a2, 7d
    Menù Principale         :a4, after a3, 4d
    API Meteo               :a5, after a4, 4d

    section Karoui
    Ricerca API             :b1, 2026-01-05, 7d
    Analisi Dati            :b2, after b1, 7d
    Salvataggio Dati        :b3, after b2, 7d
    Grafici Meteo           :b4, after b3, 4d
    Integrazione e Test     :b5, after b4, 4d
    Documentazione          :b6, after b5, 4d
```