установка rabbitmq в docker

sudo docker pull rabbitmq:management

Запуск контейнера

sudo docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq:management

Проверять по адресу 

localhost:15672
