import json
import pika
from sys import path
from os import environ
import django

rabbit_host = 'host'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'loginauthentication_users'
topics = ['AUTENTICACION']


path.append('loginauthentication/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'loginauthentication.settings')
django.setup()

from users.logic.logic_users import get_users

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

for topic in topics:
    channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=topic)

print('> Esperando autenticacion. To exit press CTRL+C')

def callback(ch, method, properties, body):
    try:
        # Aquí puedes implementar la lógica para verificar el usuario
        usuario = json.loads(body.decode('utf-8'))
        resultado = verificar_usuario(usuario)
        print(f'Recibido: {usuario}')
        print(f'Resultado de verificación: {resultado}')
    except Exception as e:
        print(f"Error en el callback: {str(e)}")

def verificar_usuario(usuario):
    # Implementa tu lógica de verificación de usuario aquí
    # Puedes utilizar la función get_users de acuerdo a tus necesidades
    pass

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
