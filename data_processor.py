import pandas as pd
from config import FILE_EXCEL, INFO_SEZIONI, STATI_ACCETTATO

def ottieni_nome_completo(row):
    """Utility per gestire colonna 'Nome Completo' o 'Nome' e 'Cognome' separati"""
    if 'Nome Completo' in row:
        return str(row['Nome Completo']).strip()
    nome = str(row.get('Nome', '')).strip()
    cognome = str(row.get('Cognome', '')).strip()
    return f"{nome} {cognome}".strip()

def elabora_dati_excel():
    print("Lettura dei fogli Excel in corso...")
    candidati = {}
    
    try:
        # 1. Lettura del Primo Foglio (Tutti i candidati)
        try:
            df_tutti = pd.read_excel(FILE_EXCEL, sheet_name=0)
        except Exception as e:
            raise Exception(f"Errore nella lettura del Foglio 1. Dettagli: {e}")

        for _, row in df_tutti.iterrows():
            email = str(row.get('Email', '')).strip().lower()
            if '@' not in email:
                continue
                
            candidati[email] = {
                'nome_completo': ottieni_nome_completo(row),
                'esito': 'rifiuto',
                'sezione_estesa': None
            }

        # 2. Lettura del Secondo Foglio (Candidati ai colloqui)
        try:
            df_colloqui = pd.read_excel(FILE_EXCEL, sheet_name=1)
            foglio_2_esiste = True
        except Exception:
            print("⚠️ Avviso: Foglio 2 non trovato. Tutti considerati scartati.")
            foglio_2_esiste = False

        if foglio_2_esiste:
            for _, row in df_colloqui.iterrows():
                email = str(row.get('Email', '')).strip().lower()
                if '@' not in email:
                    continue
                
                nome = ottieni_nome_completo(row)
                stato = str(row.get('Stato', '')).strip().lower()
                sezione_acronimo = str(row.get('Sezione', '')).strip()
                # print(f"{nome} - {stato} - {sezione_acronimo}")
                if email not in candidati:
                    candidati[email] = {'nome_completo': nome, 'esito': 'rifiuto', 'sezione_estesa': None}
                    print(f"⚠️ ATTENZIONE: il candidato {nome} - {email} non era presente in ALL")
                
                # Sovrascrive con 'welcome' se trova uno stato di accettazione
                if stato in STATI_ACCETTATO:
                    if candidati[email]['esito'] == 'welcome':
                        print(f"⚠️ ATTENZIONE: {nome} ({email}) risulta accettato in più di una sezione!")
                    else:
                        candidati[email]['esito'] = 'welcome'
                        info = INFO_SEZIONI.get(sezione_acronimo, {'esteso': sezione_acronimo})
                        candidati[email]['sezione_estesa'] = info.get('esteso', sezione_acronimo)
                        # print(f"Acettato: {nome} - {stato} - {sezione_acronimo}")
                        

        return candidati

    except FileNotFoundError:
        print(f"❌ Errore critico: File {FILE_EXCEL} non trovato.")
        return {}
    except Exception as e:
        print(f"❌ Errore imprevisto durante l'elaborazione dei dati: {e}")
        return {}
    
# Aggiungi questa funzione in fondo a data_processor.py

def mostra_statistiche(candidati):
    """Calcola e stampa a schermo le statistiche dei candidati"""
    if not candidati:
        return

    totale_candidati = len(candidati)
    ammessi = sum(1 for info in candidati.values() if info['esito'] == 'welcome')
    rifiutati = totale_candidati - ammessi

    # Calcola il dettaglio per sezione
    statistiche_sezioni = {}
    for info in candidati.values():
        if info['esito'] == 'welcome':
            sezione = info['sezione_estesa']
            statistiche_sezioni[sezione] = statistiche_sezioni.get(sezione, 0) + 1

    # Stampa a schermo
    print("\n" + "=" * 30)
    print("      STATISTICHE RECRUITING")
    print("=" * 30)
    print(f"👥 Totale candidati anagrafati: {totale_candidati}")
    print(f"🎉 Totale AMMESSI:            {ammessi}")
    print(f"❌ Totale NON ammessi:        {rifiutati}")
    
    if ammessi > 0:
        print("\n📈 Dettaglio Ammessi per Sezione:")
        # Ordina le sezioni in ordine alfabetico per una lettura migliore
        for sezione, conteggio in sorted(statistiche_sezioni.items()):
            print(f"   - {sezione}: {conteggio} membri")
    
    print("=" * 30 + "\n")