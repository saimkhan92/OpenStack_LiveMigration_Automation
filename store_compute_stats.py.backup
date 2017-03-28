import psutil
import boto3

def add_to_database(message_name,mem_attribute,cpu_attribute):
        pass

#if __name__==main:if __name__==main:

#Return a float representing the current system-wide CPU utilization as a percentage
cpu_percent=psutil.cpu_percent()

#Return statistics about system memory usage as a named tuple including the following fields: total,available,percent etc.
mem_obj=psutil.virtual_memory()
mem_percent=mem_obj.percent

#print(mem_percent)
#print(cpu_percent)

client = boto3.resource('sqs')
queue = client.get_queue_by_name(QueueName='saim_queue2')

for message in queue.receive_messages(MaxNumberOfMessages=10,WaitTimeSeconds=5,AttributeNames=["All"],MessageAttributeNames=["mem","cpu"]):
    # Get the custom author message attribute if it was set
    message_name=message.body
    print("Received message name : "+message_name)
    if message.message_attributes is not None:
        #print("entered loop")
	mem_attribute = message.message_attributes.get('mem').get('StringValue')
        if mem_attribute:
            mem_text = ' ({0})'.format(mem_attribute)
	    print("received message memory utilization % : "+mem_text)
        cpu_attribute = message.message_attributes.get('cpu').get('StringValue')
        if cpu_attribute:
            cpu_text = ' ({0})'.format(cpu_attribute)
            print("received message cpu utilization % : "+cpu_text+"\n")
    add_to_database(message_name,mem_attribute,cpu_attribute)
    message.delete()


