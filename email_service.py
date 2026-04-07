import imaplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import (
    IL_TUO_INDIRIZZO_EMAIL, LA_TUA_PASSWORD, CARTELLA_BOZZE, 
    CREA_SOLO_BOZZE_DI_PROVA, NUMERO_MASSIMO_BOZZE
)
from email_templates import genera_testo_email_welcome, genera_testo_email_rifiuto

def crea_bozze_su_gmail(candidati):
    if not candidati:
        print("Nessun candidato da elaborare. Operazione annullata.")
        return

    print(f"\nTrovati {len(candidati)} candidati univoci in totale. Connessione a Gmail in corso...")
    
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(IL_TUO_INDIRIZZO_EMAIL, LA_TUA_PASSWORD)
        
        status, response = mail.select(CARTELLA_BOZZE)
        if status != 'OK':
            print(f"❌ Errore: Non riesco a trovare la cartella {CARTELLA_BOZZE}.")
            return
            
        print("Connessione riuscita! Inizio creazione delle bozze...\n")
        bozze_create = 0
        
        for email_destinatario, info in candidati.items():
            if CREA_SOLO_BOZZE_DI_PROVA and bozze_create >= NUMERO_MASSIMO_BOZZE:
                print(f"\n🛑 Modalità Test: Mi fermo a {NUMERO_MASSIMO_BOZZE} bozze create.")
                break

            msg = MIMEMultipart()
            msg['From'] = IL_TUO_INDIRIZZO_EMAIL
            msg['To'] = email_destinatario

            # Decide quale template usare
            if info['esito'] == 'welcome':
                msg['Subject'] = f"Benvenuto nel Team ASTRA, {info['nome_completo']}! 🚀"
                corpo_html = genera_testo_email_welcome(email_destinatario, info['nome_completo'], info['sezione_estesa'])
                etichetta = f"✅ Bozza WELCOME creata per: {info['nome_completo']} ({info['sezione_estesa']})"
            else:
                msg['Subject'] = f"Esito selezioni Team ASTRA - {info['nome_completo']}"
                corpo_html = genera_testo_email_rifiuto(info['nome_completo'])
                etichetta = f"✅ Bozza RIFIUTO creata per: {info['nome_completo']}"
            
            msg.attach(MIMEText(corpo_html, 'html'))
            mail.append(CARTELLA_BOZZE, '', imaplib.Time2Internaldate(time.time()), msg.as_bytes())
            print(etichetta)
            bozze_create += 1
            
        mail.logout()
        
        if not CREA_SOLO_BOZZE_DI_PROVA:
            print("\n🎉 Finito! Tutte le bozze sono state create. Vai su Gmail per inviarle.")
        
    except imaplib.IMAP4.error:
        print("❌ Errore di autenticazione con Gmail. Controlla email e password nel file .env.")
    except Exception as e:
        print(f"❌ Errore imprevisto durante l'upload su Gmail: {e}")