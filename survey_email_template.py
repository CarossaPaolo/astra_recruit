from config import URL_LOGO

# ==========================================
# 📋 TEMPLATE EMAIL QUESTIONARIO RECRUIT
# ==========================================

LINK_QUESTIONARIO = "https://tally.so/r/SOSTITUISCI_CON_IL_TUO_LINK"  # ⚠️ Sostituisci con il link reale al tuo form


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
    <body style="margin:0; padding:0; background-color:#f4f4f4; font-family: Arial, sans-serif;">

      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4; padding: 32px 16px;">
        <tr>
          <td align="center">

            <!-- Card principale -->
            <table role="presentation" width="600" cellpadding="0" cellspacing="0"
                   style="background:#ffffff; border-radius:12px; overflow:hidden;
                          box-shadow: 0 4px 16px rgba(0,0,0,0.08); max-width:600px; width:100%;">

              <!-- Header con logo -->
              <tr>
                <td align="center" style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
                           padding: 32px 24px;">
                  <img src="{URL_LOGO}" alt="Logo Team ASTRA" width="80" height="80"
                       style="border-radius:50%; border: 3px solid rgba(255,255,255,0.2); display:block;">
                  <p style="color:#ffffff; font-size:20px; font-weight:bold; margin:16px 0 4px;
                            letter-spacing:2px; text-transform:uppercase;">Team ASTRA</p>
                  <p style="color:rgba(255,255,255,0.65); font-size:13px; margin:0;
                            letter-spacing:1px;">Politecnico di Torino</p>
                </td>
              </tr>

              <!-- Corpo -->
              <tr>
                <td style="padding: 40px 40px 32px;">

                  <h2 style="color:#1a1a2e; font-size:22px; margin:0 0 16px; font-weight:700;">
                    La tua opinione conta, {nome_breve}! 📋
                  </h2>

                  <p style="color:#4a4a4a; font-size:15px; line-height:1.7; margin:0 0 16px;">
                    Grazie per aver partecipato alle selezioni del <strong>Team ASTRA</strong>!
                    Indipendentemente dall'esito, il tuo percorso durante il recruit è stato
                    prezioso per noi.
                  </p>

                  <p style="color:#4a4a4a; font-size:15px; line-height:1.7; margin:0 0 24px;">
                    Per aiutarci a migliorare il processo di selezione nelle edizioni future,
                    ti chiediamo di dedicare <strong>5 minuti</strong> alla compilazione di un breve
                    questionario anonimo.
                  </p>

                  <!-- Box highlight -->
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"
                         style="background:#f0f7ff; border-left:4px solid #0f3460;
                                border-radius:0 8px 8px 0; margin-bottom:28px;">
                    <tr>
                      <td style="padding:16px 20px;">
                        <p style="color:#1a1a2e; font-size:14px; line-height:1.6; margin:0;">
                          🎯 <strong>Cosa ci aiuta a migliorare:</strong> chiarezza delle prove,
                          organizzazione dei colloqui, comunicazione e gestione dei tempi.
                        </p>
                      </td>
                    </tr>
                  </table>

                  <!-- CTA button -->
                  <table role="presentation" cellpadding="0" cellspacing="0" style="margin: 0 auto 32px;">
                    <tr>
                      <td align="center">
                        <a href="{LINK_QUESTIONARIO}"
                           style="display:inline-block; background:linear-gradient(135deg, #0f3460, #1a1a2e);
                                  color:#ffffff; text-decoration:none; font-size:15px; font-weight:bold;
                                  padding:14px 36px; border-radius:8px;
                                  letter-spacing:0.5px;">
                          Compila il Questionario →
                        </a>
                      </td>
                    </tr>
                  </table>

                  <p style="color:#888888; font-size:13px; line-height:1.6; margin:0 0 8px; text-align:center;">
                    Il questionario è <strong>anonimo</strong> e richiede circa 5 minuti.
                  </p>
                  <p style="color:#aaaaaa; font-size:12px; margin:0; text-align:center;">
                    Se il pulsante non funziona, copia e incolla questo link nel browser:<br>
                    <a href="{LINK_QUESTIONARIO}" style="color:#0f3460; word-break:break-all;">{LINK_QUESTIONARIO}</a>
                  </p>

                </td>
              </tr>

              <!-- Footer -->
              <tr>
                <td style="background:#f8f8f8; padding:20px 40px; border-top:1px solid #e8e8e8;">
                  <p style="color:#aaaaaa; font-size:12px; margin:0; text-align:center; line-height:1.6;">
                    © 2025 Team ASTRA – Politecnico di Torino<br>
                    Hai ricevuto questa email perché hai partecipato alle selezioni del Team ASTRA.
                  </p>
                </td>
              </tr>

            </table>
            <!-- Fine card -->

          </td>
        </tr>
      </table>

    </body>
    </html>
    """
    return html
