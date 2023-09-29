#!/usr/bin/env python
import pika

rabbit_host = '10.128.0.2'
rabbit_user = 'broker_user'
rabbit_password = 'isis2503'
exchange = 'loginauthentication_users'
topic = 'LOGIN'

def send_authentication_message():

    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
        channel = connection.channel()

        channel.exchange_declare(exchange=exchange, exchange_type='topic')
        
        message = 'Inicio de sesión exitoso'

        channel.basic_publish(exchange=exchange, routing_key=topic, body=message)

        print('> Enviando autenticación. To exit press CTRL+C')

        connection.close()
    
    except Exception as e:
        print(f"Error al enviar autenticación: {str(e)}")

if __name__ == "__main__":
    send_authentication_message()
