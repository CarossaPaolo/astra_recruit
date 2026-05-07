"""
survey_email_service.py
-----------------------
Crea bozze Gmail per invitare i candidati a compilare
il questionario di feedback sul processo di recruit.

USO:
    python survey_email_service.py

INPUT ATTESO:
    Un file CSV (survey_destinatari.csv) con almeno due colonne:
        - email
        - nome_completo

    Oppure modifica la lista DESTINATARI direttamente in questo file
    se preferisci non usare un CSV.

REQUISITI:
    - Le credenziali email nel file .env (come il resto del progetto)
    - Il link al questionario impostato in survey_email_template.py
"""

import csv
import imaplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import (
    IL_TUO_INDIRIZZO_EMAIL,
    LA_TUA_PASSWORD,
    CARTELLA_BOZZE,
    CREA_SOLO_BOZZE_DI_PROVA,
    NUMERO_MASSIMO_BOZZE,
)
from survey_email_template import genera_email_questionario

# ==========================================
# ⚙️  CONFIGURAZIONE
# ==========================================

FILE_CSV_DESTINATARI = "survey_destinatari.csv"
"""
Il CSV deve avere l'intestazione nella prima riga.
Colonne minime richieste: email, nome_completo

Esempio:
    email,nome_completo
    mario.rossi@example.com,Mario Rossi
    giulia.bianchi@example.com,Giulia Bianchi
"""

# ─── Alternativa: lista hardcoded (usala se non hai un CSV) ─────────────────
# Decommenta e compila se vuoi bypassare il file CSV.
# DESTINATARI = [
#     {"email": "mario.rossi@example.com", "nome_completo": "Mario Rossi"},
#     {"email": "giulia.bianchi@example.com", "nome_completo": "Giulia Bianchi"},
# ]
DESTINATARI = None  # None = usa il CSV
# ────────────────────────────────────────────────────────────────────────────

OGGETTO_EMAIL = "La tua opinione sulle selezioni ASTRA 📋"


# ==========================================
# 📖  LETTURA DESTINATARI DA CSV
# ==========================================

def leggi_destinatari_da_csv(percorso: str) -> list[dict]:
    """Legge il CSV e restituisce una lista di dict {email, nome_completo}."""
    if not os.path.isfile(percorso):
        print(f"❌ File CSV non trovato: {percorso}")
        print("   Crea il file o usa la lista DESTINATARI nel codice.")
        return []

    destinatari = []
    with open(percorso, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for riga in reader:
            email = riga.get("email", "").strip()
            nome = riga.get("nome_completo", "").strip()
            if email and nome:
                destinatari.append({"email": email, "nome_completo": nome})
            else:
                print(f"⚠️  Riga saltata (campi mancanti): {riga}")
    return destinatari


# ==========================================
# 📧  CREAZIONE BOZZE
# ==========================================

def crea_bozze_questionario(destinatari: list[dict]) -> None:
    """
    Si connette a Gmail via IMAP e crea una bozza personalizzata
    per ogni destinatario nella lista.
    """
    if not destinatari:
        print("⚠️  Nessun destinatario da elaborare. Operazione annullata.")
        return

    totale = len(destinatari)
    print(f"\n📋 Trovati {totale} destinatari. Connessione a Gmail in corso...")

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(IL_TUO_INDIRIZZO_EMAIL, LA_TUA_PASSWORD)

        status, _ = mail.select(CARTELLA_BOZZE)
        if status != "OK":
            print(f"❌ Errore: impossibile aprire la cartella {CARTELLA_BOZZE}.")
            return

        print("✅ Connessione riuscita! Inizio creazione delle bozze...\n")
        bozze_create = 0

        for dest in destinatari:
            # Limite sicurezza test
            if CREA_SOLO_BOZZE_DI_PROVA and bozze_create >= NUMERO_MASSIMO_BOZZE:
                print(f"\n🛑 Modalità Test: mi fermo a {NUMERO_MASSIMO_BOZZE} bozze.")
                break

            email_dest = dest["email"]
            nome = dest["nome_completo"]

            # Costruzione messaggio MIME
            msg = MIMEMultipart("alternative")
            msg["From"] = IL_TUO_INDIRIZZO_EMAIL
            msg["To"] = email_dest
            msg["Subject"] = OGGETTO_EMAIL

            corpo_html = genera_email_questionario(nome)
            msg.attach(MIMEText(corpo_html, "html", "utf-8"))

            # Upload in bozze
            mail.append(
                CARTELLA_BOZZE,
                "",
                imaplib.Time2Internaldate(time.time()),
                msg.as_bytes(),
            )

            print(f"✅ Bozza creata per: {nome} ({email_dest})")
            bozze_create += 1

        mail.logout()

        print(f"\n🎉 Completato! {bozze_create}/{totale} bozze create.")
        if not CREA_SOLO_BOZZE_DI_PROVA:
            print("   Vai su Gmail → Bozze per rivedere e inviare le email.")

    except imaplib.IMAP4.error:
        print("❌ Errore di autenticazione. Controlla EMAIL_ASTRA e PASSWORD_ASTRA nel file .env.")
    except Exception as e:
        print(f"❌ Errore imprevisto: {e}")


# ==========================================
# 🚀  ENTRY POINT
# ==========================================

if __name__ == "__main__":
    # Scegli la fonte dei destinatari
    if DESTINATARI is not None:
        lista = DESTINATARI
        print(f"📌 Uso la lista hardcoded ({len(lista)} destinatari).")
    else:
        lista = leggi_destinatari_da_csv(FILE_CSV_DESTINATARI)
        print(f"📌 Letto il file: {FILE_CSV_DESTINATARI} ({len(lista)} destinatari validi).")

    crea_bozze_questionario(lista)
