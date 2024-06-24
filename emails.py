import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time


smtp_server = 'smtp@teste.com'
smtp_port = 587
username = 'email@teste.com.br'
password = 'teste123'

def enviar_email(destinatario, assunto, corpo, anexo):
    try:
        # Cria a mensagem
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = destinatario
        msg['Subject'] = assunto

        # Adiciona o corpo do e-mail
        msg.attach(MIMEText(corpo, 'plain'))

        # Adiciona o anexo
        with open(anexo, 'rb') as file:
            mime_base = MIMEBase('application', 'octet-stream')
            mime_base.set_payload(file.read())
            encoders.encode_base64(mime_base)
            mime_base.add_header('Content-Disposition', f'attachment; filename={os.path.basename(anexo)}')
            msg.attach(mime_base)

        print(f'Conectando ao servidor SMTP para enviar {anexo}...')
        
        # Conecta ao servidor SMTP e envia o e-mail
        start_time = time.time()
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, destinatario, msg.as_string())
        server.close()
        end_time = time.time()

        tempo_execucao = end_time - start_time
        print(f'E-mail enviado com sucesso para {destinatario} com o anexo {anexo}')
        print(f'Tempo de execução: {tempo_execucao:.2f} segundos')

    except Exception as e:
        print(f'Falha ao enviar e-mail para {destinatario}. Erro: {str(e)}')

pasta_anexos = os.path.expanduser('~/Desktop/teste')

destinatario = 'destinatario@teste.com'

arquivos = os.listdir(pasta_anexos)
for anexo in arquivos:
    caminho_anexo = os.path.join(pasta_anexos, anexo)
    assunto = f"Assunto para {anexo}"
    corpo = f"Olá,\n\nSegue em anexo o arquivo {anexo}.\n\nAtenciosamente."
    enviar_email(destinatario, assunto, corpo, caminho_anexo)

