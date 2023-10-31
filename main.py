from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os, time
import yagmail

GMAIL_USERNAME = os.getenv("EMAIL_RECE")
GMAIL_SENDER = os.getenv("EMAIL_SENDER")
GMAIL_PASSWORD = os.getenv("PASSWORD_KEY")

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave segura
 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        # Get the form data
        fullname = request.form['fullname']
        email = request.form['email']
        message = request.form['message']
        subject_form = request.form['subject']


       
        # Create a yagmail.SMTP object
        yag = yagmail.SMTP(GMAIL_SENDER, GMAIL_PASSWORD)

        # Compose the email
        subject = f'{subject_form}. Contacto de {fullname}.'
        msg_body = f'Nombre: {fullname}\nCorreo electrónico: {email}\nMensaje: {message}'

        yag.send(to=[GMAIL_USERNAME], subject=subject, contents=msg_body)
        print()

        # Respuesta JSON en caso de éxito
        response = {"success": True, "message": "Tu mensaje ha sido enviado. ¡Gracias!"}
        return jsonify(response)

    except Exception as e:
        # Respuesta JSON en caso de error
        response = {"success": False, "message": "Ha ocurrido un error al enviar el mensaje. Por favor, inténtalo nuevamente."}
        return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)

