# 🤖 ZITYHUB AUTO-BOOKING

Sistema automático para reservar tu escritorio en Zityhub cada día a las 00:01, para 14 días adelante.

---

## 📋 LO QUE HACE

- ✅ Se ejecuta automáticamente a las **00:01** cada día
- ✅ Reserva tu escritorio (ID: 37196) para **14 días adelante**
- ✅ Horario: **8:00 - 20:00** (Madrid)
- ✅ Te envía notificaciones por email (opcional)
- ✅ Guarda logs de cada reserva

---

## 🚀 INSTALACIÓN EN LA NUBE (GRATIS)

### Opción 1: RENDER.COM (Recomendado - Más fácil)

1. **Crea una cuenta gratis en Render**
   - Ve a https://render.com
   - Regístrate con tu email o GitHub

2. **Sube el código a GitHub**
   - Ve a https://github.com/new
   - Crea un repositorio público llamado `zityhub-booking`
   - Sube los 3 archivos: `zityhub_auto_booking.py`, `requirements.txt`, `README.md`

3. **Despliega en Render**
   - En Render, haz clic en **"New +"** → **"Cron Job"**
   - Conecta tu repositorio de GitHub
   - Configuración:
     - **Name**: `zityhub-booking`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Command**: `python zityhub_auto_booking.py`
     - **Schedule**: `1 0 * * *` (a las 00:01 cada día)
   - Haz clic en **"Create Cron Job"**

4. **Listo** ✅
   - El script se ejecutará automáticamente cada día a las 00:01


### Opción 2: RAILWAY.APP

1. **Crea cuenta en Railway**
   - Ve a https://railway.app
   - Regístrate con GitHub

2. **Sube el código a GitHub** (igual que opción 1)

3. **Despliega en Railway**
   - En Railway, crea un **"New Project"** → **"Deploy from GitHub repo"**
   - Selecciona tu repositorio
   - Añade un **"Cron Schedule"**:
     - Command: `python zityhub_auto_booking.py`
     - Schedule: `1 0 * * *`

---

## ⚙️ CONFIGURACIÓN IMPORTANTE

### 1. Actualizar las Cookies (CRÍTICO)

**Cuando las cookies expiren**, necesitarás actualizarlas:

1. Abre Chrome, ve a Zityhub (logueado)
2. Presiona **F12** → pestaña **Application** → **Cookies**
3. Copia los valores de `_ga` y `_ga_EF1J2HPK9Z`
4. Actualiza el archivo `zityhub_auto_booking.py`:

```python
COOKIES = {
    '_ga': 'TU_NUEVO_VALOR_AQUI',
    '_ga_EF1J2HPK9Z': 'TU_NUEVO_VALOR_AQUI'
}
```

5. Haz commit y push a GitHub (se actualizará automáticamente en Render/Railway)


### 2. Activar Notificaciones por Email (OPCIONAL)

Si quieres recibir emails cuando se haga cada reserva:

1. Edita `zityhub_auto_booking.py`:

```python
SEND_EMAIL_NOTIFICATIONS = True
EMAIL_FROM = "tu_email@gmail.com"
EMAIL_PASSWORD = "tu_contraseña_app_gmail"  # Ver nota abajo
EMAIL_TO = "tu_email@gmail.com"
```

2. **Contraseña de aplicación de Gmail:**
   - Ve a https://myaccount.google.com/apppasswords
   - Genera una contraseña de aplicación
   - Úsala en `EMAIL_PASSWORD`

---

## 🧪 PRUEBA MANUAL (Antes de automatizar)

Para probar que funciona antes de subirlo a la nube:

```bash
# Instala Python si no lo tienes
python --version  # Debería mostrar Python 3.x

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el script
python zityhub_auto_booking.py
```

Deberías ver:
```
✅ ¡RESERVA EXITOSA!
📅 Fecha objetivo: 24/02/2026
```

---

## 📊 VER LOGS

Para ver si las reservas se están haciendo correctamente:

1. En Render: Ve a tu Cron Job → pestaña **"Logs"**
2. Verás el output de cada ejecución
3. También se guarda un archivo `booking_log.txt` (opcional)

---

## ❓ SOLUCIÓN DE PROBLEMAS

### Error 401 / 403
- **Causa**: Cookies expiradas
- **Solución**: Actualiza las cookies (ver arriba)

### Error 500
- **Causa**: Problema del servidor de Zityhub
- **Solución**: El script reintentará al día siguiente

### No se ejecuta a las 00:01
- **Causa**: Zona horaria del servidor
- **Solución**: Ajusta el cron schedule si es necesario

---

## 📅 CALENDARIO DE RESERVAS

| Día ejecuta | Día reserva |
|-------------|-------------|
| 10/02 00:01 | 24/02       |
| 11/02 00:01 | 25/02       |
| 12/02 00:01 | 26/02       |
| ...         | ...         |

---

## 🔒 SEGURIDAD

- ✅ Las cookies se guardan en variables de entorno (no públicas)
- ✅ No se comparten credenciales de Google
- ✅ El código es open source y revisable

---

## 💡 CONSEJOS

1. **Revisa los logs** la primera semana para confirmar que funciona
2. **Actualiza las cookies** si notas que fallan las reservas
3. **Activa las notificaciones** por email para estar tranquilo

---

## 📞 SOPORTE

Si algo no funciona:
1. Revisa los logs en Render/Railway
2. Verifica que las cookies estén actualizadas
3. Prueba ejecutar el script manualmente en tu PC

---

¡Listo! 🎉 Ahora tendrás tu escritorio reservado automáticamente cada día.
