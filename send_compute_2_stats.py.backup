import psutil
import boto3
import time
import platform

# System Stats
mem_obj=psutil.virtual_memory()
mem_percent=str(mem_obj.percent)
cpu_percent=str(psutil.cpu_percent())
hostname=platform.node()
ts=time.time()

print(mem_percent)
print(cpu_percent)
print(hostname)


# AWS SQS

sqs = boto3.resource('sqs')

# Create a new queue 
#queue = sqs.create_queue(QueueName='saim_queue2', Attributes={'DelaySeconds': '5'})
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))

queue = sqs.get_queue_by_name(QueueName='saim_queue2')
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))

dict1={"cpu":str(cpu_percent),"mem":str(mem_percent)}
print(dict1)

for i in range(50):
	message_name=hostname+"|||"+str(ts)+"|||"+str(i)	
	response=queue.send_message(MessageBody=message_name, MessageAttributes={
	    'cpu': {
	        'StringValue': cpu_percent,
	        'DataType': 'String'
	    },
	    'mem': {
	        'StringValue': mem_percent,
	        'DataType': 'String'
	    }
	})
	print(response.get('MessageId'))
	print(response.get('MD5OfMessageBody'))

