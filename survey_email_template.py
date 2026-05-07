from config import URL_LOGO

# ==========================================
# 📋 TEMPLATE EMAIL QUESTIONARIO RECRUIT
# ==========================================

LINK_QUESTIONARIO = "https://tally.so/r/SOSTITUISCI_CON_IL_TUO_LINK"  # ⚠️ Sostituisci con il link reale al tuo form

# Palette (stessa delle altre email)
colore_primario = "#9D84C6"
colore_secondario = "#4A3B69"
colore_sfondo = "#F4F4F9"
colore_sfondo_card = "#FFFFFF"
colore_testo = "#333333"


def genera_email_questionario(nome: str) -> str:
    """
    Genera il corpo HTML della mail che invita il candidato
    a compilare il questionario di feedback sul processo di recruit.

    Args:
        nome: Nome e cognome del candidato.

    Returns:
        Stringa HTML pronta da allegare al messaggio MIME.
    """
    nome_breve = nome.split()[0] if nome else "candidato"

    html = f"""
    <html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: {colore_testo}; line-height: 1.6; margin: 0; padding: 20px; background-color: {colore_sfondo};">
        <div style="max-width: 600px; margin: 0 auto; background-color: {colore_sfondo_card}; padding: 40px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.05); border-top: 6px solid {colore_primario};">

            <div style="text-align: center; margin-bottom: 30px;">
                <img src="{URL_LOGO}" alt="Logo Team ASTRA" style="max-width: 150px; height: auto; border: none;">
            </div>

            <h1 style="color: {colore_secondario}; text-align: center; font-size: 22px; margin-bottom: 20px;">
                La tua opinione conta, {nome_breve}! 📋
            </h1>

            <p style="font-size: 16px;">Ciao <strong>{nome_breve}</strong>,</p>

            <p style="font-size: 16px;">
                Grazie per aver partecipato alle selezioni del <strong>Team ASTRA</strong>!
                Indipendentemente dall'esito, il tuo percorso durante il recruit è stato prezioso per noi.
            </p>

            <p style="font-size: 16px;">
                Per aiutarci a migliorare il processo di selezione nelle edizioni future,
                ti chiediamo di dedicare <strong>5 minuti</strong> alla compilazione di un breve
                questionario anonimo.
            </p>

            <div style="background-color: #F9F6FE; border-left: 4px solid {colore_primario}; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 24px 0; color: {colore_secondario};">
                🎯 <strong>Cosa ci aiuta a migliorare:</strong> chiarezza delle prove,
                organizzazione dei colloqui, comunicazione e gestione dei tempi.
            </div>

            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin: 28px 0 24px;">
                <tr>
                    <td align="center">
                        <table border="0" cellspacing="0" cellpadding="0">
                            <tr>
                                <td align="center" bgcolor="{colore_primario}" style="background-color: {colore_primario}; border-radius: 6px;">
                                    <a href="{LINK_QUESTIONARIO}" target="_blank"
                                       style="font-size: 15px; font-family: Arial, sans-serif; font-weight: bold;
                                              color: #ffffff; text-decoration: none; border-radius: 6px;
                                              padding: 12px 28px; border: 1px solid {colore_primario}; display: inline-block;">
                                        Compila il Questionario →
                                    </a>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>

            <p style="font-size: 13px; text-align: center; color: #888888; margin: 0 0 8px;">
                Il questionario è <strong>anonimo</strong> e richiede circa 5 minuti.
            </p>
            <p style="font-size: 12px; text-align: center; color: #aaaaaa; margin: 0;">
                Se il pulsante non funziona, copia e incolla questo link nel browser:<br>
                <a href="{LINK_QUESTIONARIO}" style="color: {colore_primario}; word-break: break-all;">{LINK_QUESTIONARIO}</a>
            </p>

            <hr style="border: 0; border-top: 1px solid #eeeeee; margin: 30px 0;">

            <div style="text-align: center; font-size: 15px;">
                <strong style="color: {colore_primario}; font-size: 18px; display: inline-block; margin-top: 10px;">Team ASTRA</strong>
            </div>

        </div>
    </body>
    </html>
    """
    return html
