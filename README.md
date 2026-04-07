"""
# 🚀 Team ASTRA - Recruiting Automator

Questo progetto è un tool automatizzato sviluppato per gestire l'invio degli esiti (accettazione o rifiuto) ai candidati del **Team ASTRA**. 
Il sistema legge i dati da un file Excel, elabora gli stati dei candidati e genera automaticamente delle bozze su Gmail, evitando errori manuali e risparmiando tempo prezioso durante la fase di recruiting.

---

## 📁 Struttura del Progetto

Il progetto è diviso in moduli per facilitarne la manutenzione:

* `main.py`: Il punto di ingresso dell'applicazione. Coordina la lettura dei dati e la creazione delle email.
* `data_processor.py`: Gestisce la logica di lettura del file Excel e la pulizia dei dati.
* `email_service.py`: Si occupa della connessione ai server Gmail tramite IMAP e del salvataggio delle bozze.
* `email_templates.py`: Contiene i template HTML per le email di "Welcome" e di "Rifiuto".
* `config.py`: Centralizza tutte le configurazioni, i link e i parametri di test.
* `.env`: (Da creare) Contiene le credenziali sensibili (Email e Password).
* `requirements.txt`: Elenca le librerie Python necessarie.

---

## 🛠️ Requisiti e Installazione

1. **Clona o scarica** la cartella del progetto.
2. **Crea un ambiente virtuale** per isolare le dipendenze:
   ```bash
   python -m venv venv

   