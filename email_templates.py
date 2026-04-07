from config import URL_LOGO, LINK_REGOLAMENTO, LINK_FORM_RICHIESTA_BADGE

def genera_testo_email_rifiuto(nome_completo):
    """Genera l'HTML dell'email di esito negativo generica"""
    colore_primario = "#9D84C6"
    colore_secondario = "#4A3B69"
    colore_sfondo = "#F4F4F9"
    colore_sfondo_card = "#FFFFFF"
    colore_testo = "#333333"

    testo_html = f"""
    <html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: {colore_testo}; line-height: 1.6; margin: 0; padding: 20px; background-color: {colore_sfondo};">
        <div style="max-width: 600px; margin: 0 auto; background-color: {colore_sfondo_card}; padding: 40px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.05); border-top: 6px solid {colore_primario};">
            
            <div style="text-align: center; margin-bottom: 30px;">
                <img src="{URL_LOGO}" alt="Logo Team ASTRA" style="max-width: 150px; height: auto; border: none;">
            </div>
            
            <h1 style="color: {colore_secondario}; text-align: center; font-size: 22px; margin-bottom: 20px;">
                Esito delle selezioni Team ASTRA
            </h1>
            
            <p style="font-size: 16px;">Ciao <strong>{nome_completo}</strong>,</p>
            
            <p style="font-size: 16px;">
                Ti scriviamo in merito alla tua recente candidatura per entrare a far parte del Team ASTRA.
            </p>

            <p style="font-size: 16px;">
                Innanzitutto, ci teniamo a ringraziarti per il tempo, l'energia e l'entusiasmo che hai dedicato al processo di selezione. Abbiamo avuto il piacere di incontrare tantissimi studenti motivati e appassionati, e il livello generale dei colloqui è stato davvero alto.
            </p>
            
            <p style="font-size: 16px;">
                Purtroppo, quest'anno i posti a nostra disposizione sono estremamente limitati. Dopo un'attenta valutazione di tutti i profili, siamo dispiaciuti di doverti comunicare che <strong>non possiamo accogliere la tua candidatura per questa stagione</strong>. 
            </p>
            
            <p style="font-size: 16px;">
                Ti invitiamo caldamente a continuare a seguire i nostri progetti e a riprovare durante le prossime sessioni di recruiting. Nel frattempo, ti auguriamo il meglio per il tuo percorso accademico e i tuoi progetti futuri!
            </p>
            
            <hr style="border: 0; border-top: 1px solid #eeeeee; margin: 30px 0;">
            
            <div style="text-align: center; font-size: 15px;">
                <strong style="color: {colore_primario}; font-size: 18px; display: inline-block; margin-top: 10px;">Team ASTRA</strong><br>
            </div>
        </div>
    </body>
    </html>
    """
    return testo_html

def genera_testo_email_welcome(email_destinatario, nome_completo, sezione_estesa):
    """Genera l'HTML dell'email di benvenuto"""
    colore_primario = "#9D84C6"
    colore_secondario = "#4A3B69"
    colore_sfondo = "#F4F4F9"
    colore_sfondo_card = "#FFFFFF"
    colore_testo = "#333333"

    avviso_email_istituzionale = ""
    if not email_destinatario.lower().endswith("@studenti.polito.it"):
        avviso_email_istituzionale = f"""
        <div style="background-color: #FFF3CD; border-left: 4px solid #FFC107; padding: 15px; border-radius: 0 8px 8px 0; margin: 20px 0; color: #856404;">
            <strong>⚠️ Azione richiesta:</strong> L'indirizzo fornito non è quello del Politecnico. <strong>Rispondi a questa email</strong> fornendoci la tua <strong>Matricola</strong> e la tua <strong>Email Istituzionale (@studenti.polito.it)</strong> per poter completare la tua anagrafica.
        </div>
        """

    return f"""
    <html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: {colore_testo}; line-height: 1.6; margin: 0; padding: 20px; background-color: {colore_sfondo};">
        <div style="max-width: 600px; margin: 0 auto; background-color: {colore_sfondo_card}; padding: 40px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.05); border-top: 6px solid {colore_primario};">
            <div style="text-align: center; margin-bottom: 30px;">
                <img src="{URL_LOGO}" alt="Logo Team ASTRA" style="max-width: 150px; height: auto; border: none;">
            </div>
            <h1 style="color: {colore_secondario}; text-align: center; font-size: 24px; margin-bottom: 20px;">
                Benvenuto a bordo, {nome_completo}! 🚀
            </h1>
            <p style="font-size: 16px;">Ciao <strong>{nome_completo}</strong>,</p>
            <p style="font-size: 16px;">
                Dopo gli ottimi colloqui di selezione, siamo felicissimi di comunicarti che <strong>sei ufficialmente parte del Team ASTRA</strong>! 
                Ti diamo il benvenuto all'interno della sezione <strong style="color: {colore_primario};">{sezione_estesa}</strong>.
            </p>
            <div style="background-color: #F9F6FE; border-left: 4px solid {colore_primario}; padding: 20px; border-radius: 0 8px 8px 0; margin: 30px 0;">
                <h3 style="color: {colore_secondario}; margin-top: 0; font-size: 18px;">Cosa succede ora?</h3>
                <ul style="padding-left: 20px; margin-bottom: 0; font-family: Arial, sans-serif;">
                    <li style="margin-bottom: 15px;">
                        <strong>📱 Community WhatsApp:</strong> Verrai aggiunto/a al nostro gruppo ufficiale.
                    </li>
                    
                    <li style="margin-bottom: 15px;">
                        <strong>🦺 Sicurezza in Laboratorio:</strong> Per l'accesso è necessario il corso sulla sicurezza. Dettagli nel regolamento.
                    </li>
                    
                    <li style="margin-bottom: 25px;">
                        <strong>🪪 Badge del TB:</strong> Per ottenere il badge per accedere agli spazi del team al TB è necessario compilare la richiesta <strong> entro Domenica 19 Aprile </strong>
                        
                        <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-top: 12px; margin-bottom: 5px;">
                            <tr>
                                <td align="center">
                                    <table border="0" cellspacing="0" cellpadding="0">
                                        <tr>
                                            <td align="center" bgcolor="{colore_primario}" style="background-color: {colore_primario}; border-radius: 6px;">
                                                <a href="{LINK_FORM_RICHIESTA_BADGE}" target="_blank" style="font-size: 15px; font-family: Arial, sans-serif; font-weight: bold; color: #ffffff; text-decoration: none; border-radius: 6px; padding: 12px 24px; border: 1px solid {colore_primario}; display: inline-block;">Richiesta Badge</a>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                        </li>
                    
                    <li style="margin-bottom: 15px;">
                        <strong>📖 Regolamento:</strong> Leggi con attenzione il regolamento del Team.
                        
                        <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-top: 12px; margin-bottom: 5px;">
                            <tr>
                                <td align="center">
                                    <table border="0" cellspacing="0" cellpadding="0">
                                        <tr>
                                            <td align="center" bgcolor="{colore_primario}" style="background-color: {colore_primario}; border-radius: 6px;">
                                                <a href="{LINK_REGOLAMENTO}" target="_blank" style="font-size: 15px; font-family: Arial, sans-serif; font-weight: bold; color: #ffffff; text-decoration: none; border-radius: 6px; padding: 12px 24px; border: 1px solid {colore_primario}; display: inline-block;">Leggi il Regolamento</a>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                        </li>
                </ul>
            </div>
            {avviso_email_istituzionale}
            <p style="font-size: 16px;">
                Siamo molto entusiasti di iniziare questo percorso insieme e non vediamo l'ora di vederti all'opera. Preparati per una stagione ricca di sfide, innovazione e tanto lavoro di squadra!
            </p>
            <p style="font-size: 15px; color: #666;">
                <em>Per qualsiasi dubbio o informazione, puoi sempre rispondere a questa email o contattare il referente della tua sezione una volta nei gruppi.</em>
            </p>
            <hr style="border: 0; border-top: 1px solid #eeeeee; margin: 30px 0;">
            <div style="text-align: center; font-size: 15px;">
                <strong style="color: {colore_primario}; font-size: 18px; display: inline-block; margin-top: 10px;">Team ASTRA</strong><br>
            </div>
        </div>
    </body>
    </html>
    """