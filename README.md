# Monitor de Puertos con Alertas por Telegram

Monitor automático que escanea un puerto cada 10 segundos y envía una alerta a Telegram cuando su estado cambia (abierto ↔ cerrado).

## Características

- Escanea un puerto específico de una IP
- Intervalo de 10 segundos entre escaneos
- Envía alerta a Telegram con fecha y hora
- Configurable para cualquier IP y puerto

## Requisitos

```bash
pip install requests

Configuración de Telegram

    Crear un bot en Telegram con @BotFather

    Obtener tu Chat ID

    Reemplazar TOKEN y CHATID en el código

USO
python monitorPuertosAlerta.py

EJEMPLO

Introduce la direccion IP: 127.0.0.1
Introduce puerto asociado: 135
--- MONITOREANDO PUERTO ---
El puerto 135 en 127.0.0.1 ahora está ABIERTO
✅ Alerta enviada a Telegram
