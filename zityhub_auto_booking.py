import requests
import os
from datetime import datetime, timedelta
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ========================
# CONFIGURACIÓN
# ========================

# Tus cookies de Zityhub (ACTUALIZA ESTOS VALORES)
COOKIES = {
    '_ga': 'GA1.1.920178878.1761125390',
    '_ga_EF1J2HPK9Z': 'GS2.1.s1770627657653s43sg19t1770628094s18s1030s0'
}

# Tu configuración de reserva
PERSON_ID = 16962
SPACE_ID = 37188
DESK_ID = 37196
BOOKING_TYPE = "desk"

# Horario (en UTC)
HORA_INICIO = 7  # 8am Madrid = 7am UTC
HORA_FIN = 19    # 8pm Madrid = 7pm UTC

# Configuración de email (OPCIONAL - para recibir notificaciones)
SEND_EMAIL_NOTIFICATIONS = False  # Cambia a True si quieres emails
EMAIL_FROM = "tu_email@gmail.com"  # Tu email
EMAIL_PASSWORD = "tu_contraseña_app"  # Contraseña de aplicación de Gmail
EMAIL_TO = "tu_email@gmail.com"  # Donde quieres recibir notificaciones

# ========================
# FUNCIONES
# ========================

def enviar_notificacion(asunto, mensaje):
    """Envía email de notificación"""
    if not SEND_EMAIL_NOTIFICATIONS:
        return
    
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = asunto
        
        msg.attach(MIMEText(mensaje, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_FROM, EMAIL_TO, text)
        server.quit()
        
        print("✅ Email enviado correctamente")
    except Exception as e:
        print(f"⚠️ Error al enviar email: {str(e)}")


def calcular_fecha_reserva():
    """Calcula la fecha para reservar (14 días desde hoy)"""
    hoy = datetime.now()
    fecha_reserva = hoy + timedelta(days=14)
    return fecha_reserva


def crear_reserva():
    """Crea la reserva en Zityhub"""
    
    # Calcular fecha
    fecha_reserva = calcular_fecha_reserva()
    
    # Formatear fechas en UTC
    fecha_inicio = fecha_reserva.replace(hour=HORA_INICIO, minute=0, second=0, microsecond=0)
    fecha_fin = fecha_reserva.replace(hour=HORA_FIN, minute=0, second=0, microsecond=0)
    
    # Formato ISO 8601
    from_time = fecha_inicio.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    to_time = fecha_fin.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    
    # Payload de la reserva
    payload = {
        "person": PERSON_ID,
        "space": SPACE_ID,
        "deskId": DESK_ID,
        "from": from_time,
        "to": to_time,
        "type": BOOKING_TYPE,
        "isDraft": True
    }
    
    # Headers
    headers = {
        'Content-Type': 'application/json',
        'Origin': 'https://app.zityhub.com',
        'Referer': 'https://app.zityhub.com/app/booking'
    }
    
    # URL del API
    url = "https://app.zityhub.com/api/v1/booking"
    
    print(f"\n{'='*50}")
    print(f"🕐 Ejecutando reserva automática...")
    print(f"📅 Fecha objetivo: {fecha_reserva.strftime('%d/%m/%Y')}")
    print(f"🕐 Horario: {HORA_INICIO+1}:00 - {HORA_FIN+1}:00 (hora Madrid)")
    print(f"💺 Escritorio ID: {DESK_ID}")
    print(f"{'='*50}\n")
    
    try:
        # Hacer la petición
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            cookies=COOKIES,
            timeout=30
        )
        
        # Verificar respuesta
        if response.status_code == 201:
            print(f"✅ ¡RESERVA EXITOSA!")
            print(f"📋 Respuesta: {response.text}")
            
            mensaje = f"""
¡Reserva exitosa! ✅

Fecha: {fecha_reserva.strftime('%d/%m/%Y')}
Horario: 8:00 - 20:00
Escritorio: {DESK_ID}
Ejecutado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
            """
            enviar_notificacion("✅ Zityhub - Reserva exitosa", mensaje)
            
            # Guardar log
            with open('booking_log.txt', 'a') as f:
                f.write(f"{datetime.now()} - SUCCESS - Reservado {fecha_reserva.strftime('%d/%m/%Y')}\n")
            
            return True
            
        else:
            print(f"❌ ERROR: Status {response.status_code}")
            print(f"📋 Respuesta: {response.text}")
            
            mensaje = f"""
Error en la reserva ❌

Status: {response.status_code}
Respuesta: {response.text}
Fecha objetivo: {fecha_reserva.strftime('%d/%m/%Y')}

Puede que necesites actualizar las cookies.
            """
            enviar_notificacion("❌ Zityhub - Error en reserva", mensaje)
            
            # Guardar log
            with open('booking_log.txt', 'a') as f:
                f.write(f"{datetime.now()} - ERROR {response.status_code} - {response.text}\n")
            
            return False
            
    except Exception as e:
        print(f"❌ EXCEPCIÓN: {str(e)}")
        
        mensaje = f"""
Error crítico en la reserva ❌

Error: {str(e)}
Fecha objetivo: {fecha_reserva.strftime('%d/%m/%Y')}

Revisa el servicio y las cookies.
        """
        enviar_notificacion("❌ Zityhub - Error crítico", mensaje)
        
        # Guardar log
        with open('booking_log.txt', 'a') as f:
            f.write(f"{datetime.now()} - EXCEPTION - {str(e)}\n")
        
        return False


# ========================
# EJECUCIÓN PRINCIPAL
# ========================

if __name__ == "__main__":
    print("\n🤖 ZITYHUB AUTO-BOOKING INICIADO")
    print(f"⏰ Hora actual: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    crear_reserva()
    
    print("\n✨ Proceso completado\n")
