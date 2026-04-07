import os
from dotenv import load_dotenv

# Carica le variabili dal file .env
load_dotenv()

# ==========================================
# ⚙️ CONFIGURAZIONI EMAIL E LINK
# ==========================================
IL_TUO_INDIRIZZO_EMAIL = os.getenv("EMAIL_ASTRA")
LA_TUA_PASSWORD = os.getenv("PASSWORD_ASTRA")
CARTELLA_BOZZE = '"[Gmail]/Bozze"' 
FILE_EXCEL = 'candidati_selezioni.xlsx' 

LINK_REGOLAMENTO = "https://drive.google.com/file/d/1C1ENevbnOvJ9U_jWUVjvrSFJqJ_QcihA/view?usp=sharing"
URL_LOGO = "https://media.licdn.com/dms/image/v2/D4D0BAQFOYGheeYaYMg/company-logo_200_200/company-logo_200_200/0/1680595545550?e=2147483647&v=beta&t=C7s8e5Du4lKyFZBJSdcHMMP3jdltwf3sDrOWUlw-Xf0"
LINK_FORM_RICHIESTA_BADGE = "https://tally.so/r/rjLPW2"

# --- MODALITÀ SICUREZZA / TEST ---
CREA_SOLO_BOZZE_DI_PROVA = False
NUMERO_MASSIMO_BOZZE = 10

# ==========================================
# 🏢 CONFIGURAZIONI SEZIONI E STATI
# ==========================================
INFO_SEZIONI = {
    'COM': {'esteso': 'Communication and Management'},
    'PROT_F': {'esteso': 'Prototyping FIRE'},
    'PROT_S': {'esteso': 'Prototyping SCOUT'},   
    'MT_F': {'esteso': 'Mechatronics FIRE'},
    'MT_S': {'esteso': 'Mechatronics SCOUT'},
    'GNC': {'esteso': 'GNC'},
    'STR': {'esteso': 'Structure'}    
}

# Parole chiave che determinano se un candidato è stato preso
STATI_ACCETTATO = ['ammesso', 'acettato/a', 'idoneo', 'preso', 'selezionato', 'si']