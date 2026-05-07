from config import URL_LOGO

# ==========================================
# 📋 TEMPLATE EMAIL QUESTIONARIO RECRUIT
# ==========================================

LINK_QUESTIONARIO = "https://tally.so/r/SOSTITUISCI_CON_IL_TUO_LINK"  # ⚠️ Sostituisci con il link reale al tuo form

# Palette personalizzata
COLORE_PRIMARIO = "#9D84C6"
COLORE_SECONDARIO = "#4A3B69"
COLORE_SFONDO = "#F4F4F9"
COLORE_SFONDO_CARD = "#FFFFFF"
COLORE_TESTO = "#333333"


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
    <!DOCTYPE html>
    <html lang="it">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Questionario Recruit – Team ASTRA</title>
    </head>
    <body style="margin:0; padding:0; background-color:{COLORE_SFONDO}; font-family: Arial, sans-serif;">

      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{COLORE_SFONDO}; padding: 32px 16px;">
        <tr>
          <td align="center">

            <table role="presentation" width="600" cellpadding="0" cellspacing="0"
                   style="background:{COLORE_SFONDO_CARD}; border-radius:12px; overflow:hidden;
                          box-shadow: 0 4px 16px rgba(74,59,105,0.12); max-width:600px; width:100%;">

              <tr>
                <td align="center" style="background: linear-gradient(135deg, {COLORE_PRIMARIO} 0%, {COLORE_SECONDARIO} 100%);
                           padding: 32px 24px;">
                  <img src="{URL_LOGO}" alt="Logo Team ASTRA" width="80" height="80"
                       style="border-radius:50%; border: 3px solid rgba(255,255,255,0.25); display:block; background:#ffffff;">
                  <p style="color:#ffffff; font-size:20px; font-weight:bold; margin:16px 0 4px;
                            letter-spacing:2px; text-transform:uppercase;">Team ASTRA</p>
                  <p style="color:rgba(255,255,255,0.78); font-size:13px; margin:0;
                            letter-spacing:1px;">Politecnico di Torino</p>
                </td>
              </tr>

              <tr>
                <td style="padding: 40px 40px 32px;">

                  <h2 style="color:{COLORE_SECONDARIO}; font-size:22px; margin:0 0 16px; font-weight:700;">
                    La tua opinione conta, {nome_breve}! 📋
                  </h2>

                  <p style="color:{COLORE_TESTO}; font-size:15px; line-height:1.7; margin:0 0 16px;">
                    Grazie per aver partecipato alle selezioni del <strong>Team ASTRA</strong>!
                    Indipendentemente dall'esito, il tuo percorso durante il recruit è stato
                    prezioso per noi.
                  </p>

                  <p style="color:{COLORE_TESTO}; font-size:15px; line-height:1.7; margin:0 0 24px;">
                    Per aiutarci a migliorare il processo di selezione nelle edizioni future,
                    ti chiediamo di dedicare <strong>5 minuti</strong> alla compilazione di un breve
                    questionario anonimo.
                  </p>

                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"
                         style="background:#EFEAF7; border-left:4px solid {COLORE_PRIMARIO};
                                border-radius:0 8px 8px 0; margin-bottom:28px;">
                    <tr>
                      <td style="padding:16px 20px;">
                        <p style="color:{COLORE_SECONDARIO}; font-size:14px; line-height:1.6; margin:0;">
                          🎯 <strong>Cosa ci aiuta a migliorare:</strong> chiarezza delle prove,
                          organizzazione dei colloqui, comunicazione e gestione dei tempi.
                        </p>
                      </td>
                    </tr>
                  </table>

                  <table role="presentation" cellpadding="0" cellspacing="0" style="margin: 0 auto 32px;">
                    <tr>
                      <td align="center">
                        <a href="{LINK_QUESTIONARIO}"
                           style="display:inline-block; background:{COLORE_SECONDARIO};
                                  color:#ffffff; text-decoration:none; font-size:15px; font-weight:bold;
                                  padding:14px 36px; border-radius:8px;
                                  letter-spacing:0.5px; box-shadow: 0 4px 12px rgba(74,59,105,0.18);">
                          Compila il Questionario →
                        </a>
                      </td>
                    </tr>
                  </table>

                  <p style="color:{COLORE_TESTO}; font-size:13px; line-height:1.6; margin:0 0 8px; text-align:center; opacity:0.85;">
                    Il questionario è <strong>anonimo</strong> e richiede circa 5 minuti.
                  </p>
                  <p style="color:{COLORE_TESTO}; font-size:12px; margin:0; text-align:center; opacity:0.7;">
                    Se il pulsante non funziona, copia e incolla questo link nel browser:<br>
                    <a href="{LINK_QUESTIONARIO}" style="color:{COLORE_PRIMARIO}; word-break:break-all;">{LINK_QUESTIONARIO}</a>
                  </p>

                </td>
              </tr>

              <tr>
                <td style="background:#F8F7FC; padding:20px 40px; border-top:1px solid #E6E0F0;">
                  <p style="color:{COLORE_TESTO}; font-size:12px; margin:0; text-align:center; line-height:1.6; opacity:0.65;">
                    © 2025 Team ASTRA – Politecnico di Torino<br>
                    Hai ricevuto questa email perché hai partecipato alle selezioni del Team ASTRA.
                  </p>
                </td>
              </tr>

            </table>

          </td>
        </tr>
      </table>

    </body>
    </html>
    """
    return html
