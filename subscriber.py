import json
import pika
from sys import path
from os import environ
import django

rabbit_host = '10.128.0.2'
rabbit_user = 'broker_user'
rabbit_password = 'isis2503'
exchange = 'loginauthentication_users'
topics = ['AUTENTICACION']

path.append('loginauthentication/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'loginauthentication.settings')
django.setup()

from loginauthentication import views
import producer

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

for topic in topics:
    channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=topic)

print('> Esperando autenticacion.')

def callback(ch, method, body):
    try:
        usuario, clave = body.decode('utf-8').split()
        resultado = verificar_usuario(usuario, clave)
        print(f'Recibido: {usuario}')
        print(f'Resultado de verificación: {resultado}')
    except Exception as e:
        print(f"Error en el callback: {str(e)}")

def verificar_usuario(usuario, clave):

    respuesta = views.verificar_usuario(usuario, clave)

    producer.enviar_mensaje_autenticacion(respuesta)
    
    pass

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
