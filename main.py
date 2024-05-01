import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
# Configuración del servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'noeliapantigoso2@gmail.com'
password = os.environ.get('password')  # Leer de variable de entorno

# Creación del mensaje
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Prueba'
msg['From'] = username
msg['To'] = 'noeliapantigoso@gmail.com'

# Datos para personalizar el correo
nombre_usuario = "Noelia"
area_de_mejora = "tu desarrollo profesional"

# Crear el cuerpo del mensaje en HTML
html = f"""\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="initial-scale=1, width=device-width" />

    <link rel="stylesheet" href="./global.css" />
    <link rel="stylesheet" href="./index.css" />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap"
    />
  </head>
  <body>
    <div class="bienvenidos-variante-1">
      <section class="header"></section>
      <section class="email-content-wrapper">
        <div class="email-content">
          <div class="hola-nombre-hola-container">
            <p class="hola-nombre">
              <span class="hola">Hola, </span>
              <b class="nombre">{{nombre}}</b>
              <span>,</span>
            </p>
            <p class="blank-line">&nbsp;</p>
            <p class="hola-soy-fran-encantada-de-co">
              <span
                >¡Hola soy FRAN! encantada de conocerte y acompañarte en tu
                viaje para mejorar tu
              </span>
              <b class="rea-de-mejora">{{área de mejora}}</b>
              <span class="tengo-estas-funciones"
                >, tengo estas funciones para lograrlo.</span
              >
            </p>
          </div>
          <div class="email-content-inner">
            <div class="frame-parent">
              <div class="frame-group">
                <div class="more-people-speak-wrapper">
                  <button class="more-people-speak">
                    <div class="ellipse-parent">
                      <div class="frame-child"></div>
                      <img
                        class="icon"
                        loading="lazy"
                        alt=""
                        src="./public/1-1@2x.png"
                      />
                    </div>
                  </button>
                </div>
                <div class="recordatorios">Recordatorios</div>
              </div>
              <div class="frame-container">
                <div class="frame-wrapper">
                  <button class="frame">
                    <div class="ellipse-group">
                      <div class="frame-item"></div>
                      <img class="icon1" alt="" src="./public/2-1@2x.png" />
                    </div>
                  </button>
                </div>
                <div class="calendario">Calendario</div>
              </div>
              <div class="frame-div">
                <button class="frame1">
                  <div class="master-button-instance-parent">
                    <div class="master-button-instance"></div>
                    <img class="icon2" alt="" src="./public/3-1@2x.png" />
                  </div>
                </button>
                <div class="diario-wrapper">
                  <div class="diario">Diario</div>
                </div>
              </div>
            </div>
          </div>
          <div class="ms-de-5000">
            Más de 5000 personas hablan conmigo, cada una tiene una razón
            diferente. Siempre recuerda la tuya y déjame guiarte. ¡Estoy muy
            feliz de acompañarte! ¡Empecemos!
          </div>
        </div>
      </section>
      <section class="descuento-wrapper">
        <div class="descuento">
          <div class="content">
            <div class="text">
              <div class="por-cierto-de">
                Por cierto, de bienvenida. Te regalo un 10% de descuento en tus
                suscripción.
              </div>
            </div>
            <button class="master-button">
              <img
                class="arrows-down-arrow-2"
                alt=""
                src="./public/arrows--down-arrow-2.svg"
              />

              <b class="cta">¡Quiero mi descuento!</b>
              <img
                class="arrows-down-arrow-21"
                alt=""
                src="./public/arrows--down-arrow-2.svg"
              />
            </button>
          </div>
        </div>
      </section>
      <section class="email-template-footer">
        <footer class="email-template-footer1">
          <div class="content1">
            <div class="social-icons">
              <img
                class="instagram-line-icon"
                loading="lazy"
                alt=""
                src="./public/instagramline@2x.png"
              />

              <img
                class="frame-icon"
                loading="lazy"
                alt=""
                src="./public/frame@2x.png"
              />

              <img
                class="frame-icon1"
                loading="lazy"
                alt=""
                src="./public/frame-1@2x.png"
              />
            </div>
            <img
              class="fran-logo-png-1"
              loading="lazy"
              alt=""
              src="./public/fran-logo-png-1@2x.png"
            />

            <div class="fran-ai-all-container">
              <p class="fran-ai-all">© FRAN AI. All rights reserved.</p>
              <p class="si-tienes-consultas">
                Si tienes consultas, contactanos por correo:
                fran.ai.contacto@gmail.com
              </p>
            </div>
          </div>
        </footer>
      </section>
    </div>
  </body>
</html>
"""

# Adjunta el cuerpo HTML
part = MIMEText(html, 'html')
msg.attach(part)

# Conexión al servidor SMTP y envío
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()  # Identificación con el servidor
    server.starttls()  # Iniciar conexión segura
    server.ehlo()
    server.login(username, password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

print("Correo enviado exitosamente!")
