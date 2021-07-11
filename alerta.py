import smtplib
from email.message import EmailMessage


def Alerta_gmail(endereco, titulo, mensagem):
    usuario = "alerta.email.gaspar@gmail.com"
    senha = "jgbfuvvxivhcjtrv"

    msg = EmailMessage()
    msg.set_content(mensagem)
    msg['subject'] = titulo
    msg['to'] = endereco
    msg['from'] = usuario

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(usuario, senha)
    server.send_message(msg)

    server.quit()


if __name__ == "__main__":
    Alerta_gmail("campos.gasapr@gmail.com", "Teste", "Olá Mundo")
