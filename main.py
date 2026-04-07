from data_processor import elabora_dati_excel, mostra_statistiche
from email_service import crea_bozze_su_gmail

def avvia_programma():
    print("=" * 50)
    print("🚀 SCRIPT RECRUITING TEAM ASTRA AVVIATO 🚀")
    print("=" * 50)
    
    # Fase 1: Estrazione e pulizia dati
    dati_candidati = elabora_dati_excel()
    
    # Fase 2: Calcolo e stampa delle statistiche
    mostra_statistiche(dati_candidati)
    
    # Conferma prima di procedere (opzionale ma consigliato per evitare spam per errore)
    if dati_candidati:
        procedere = input("Vuoi procedere con la creazione delle bozze su Gmail? (s/n): ")
        if procedere.lower() == 's':
            # Fase 3: Creazione bozze via Email
            crea_bozze_su_gmail(dati_candidati)
        else:
            print("🛑 Operazione annullata dall'utente. Nessuna bozza creata.")

if __name__ == "__main__":
    avvia_programma()