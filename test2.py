#!/usr/bin/python

import boto3
import Adafruit_BMP.BMP085 as BMP085

import sys
import Adafruit_DHT
import platform
import time

hostname=platform.node()
ts=time.time()


sensor = BMP085.BMP085()
temp = sensor.read_temperature()
pressure = sensor.read_pressure()

print 'Pressure = {0:0.2f} Pa'.format(pressure)

humidity, temperature = Adafruit_DHT.read_retry(22, 4)
fahrenheit = (temperature * 9 /5 ) + 32

print 'Temp: {0:0.1f} F'.format(fahrenheit) 
print 'Humidity: {0:0.1f} %'.format(humidity)



temperature=str(fahrenheit)[:6]
humidity=str(humidity)[:6]
pressure=str(pressure)[:5]

print 'Temp: {} F'.format(temperature)
print 'Humidity: {} %'.format(humidity)
print 'Pressure = {} Pa'.format(pressure)




sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='saim_queue2')

#dict1={"temperature":str(temperature),"humidity":str(humidity),"pressure":str(pressure)}

for i in range(50):
	message_name=hostname+"|||"+str(ts)+"|||"+str(i)	
	response=queue.send_message(MessageBody=message_name, MessageAttributes={
	    'temperature': {
	        'StringValue': temperature,
	        'DataType': 'String'
	    },
	    'humidity': {
	        'StringValue': humidity,
	        'DataType': 'String'
	    },
	    'pressure': {
                'StringValue': pressure,
                'DataType': 'String'
            }

	})
	print(response.get('MessageId'))
	print(response.get('MD5OfMessageBody'))








