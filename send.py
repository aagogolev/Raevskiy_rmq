
import pika

for i in range(11):

  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  channel.queue_declare(queue='hello')
  channel.basic_publish(exchange='', routing_key='hello', body="mas namber " + str(i))
  print ("Sent massage" + str(i))

connection.close()