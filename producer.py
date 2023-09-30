#!/usr/bin/env python
import pika

rabbit_host = '10.128.0.2'
rabbit_user = 'broker_user'
rabbit_password = 'isis2503'
exchange = 'loginauthentication_users'
topic = 'LOGIN'

def enviar_mensaje_autenticacion(mensaje):

    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
        channel = connection.channel()

        channel.exchange_declare(exchange=exchange, exchange_type='topic')
        
        channel.basic_publish(exchange=exchange, routing_key=topic, body=mensaje)

        print('> Respuesta de la solicitud enviada')

        connection.close()
    
    except Exception as e:
        print(f"Error al enviar autenticación: {str(e)}")

