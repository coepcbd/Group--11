#!/usr/bin/env python
import os
from novaclient.v1_1 import client
def get_nova_creds():
	d = {}
	d['username'] = os.environ['OS_USERNAME']
	d['api_key'] = os.environ['OS_PASSWORD']
	d['auth_url'] = os.environ['OS_AUTH_URL']
	d['project_id'] = os.environ['OS_TENANT_NAME']
	return d

creds = get_nova_creds()
mynova = client.Client(**creds)

def one():
	print mynova.floating_ip_pools.list()
def two():
	print mynova.floating_ips.list()
def three():
	print "Creating new floating ip for admin tenant"
	#Allocate a floating ip to a tenant
	new_ip = mynova.floating_ips.create()

def four():
	#Get floating ip information from the floating ip id
	new_ip = raw_input('Enter Floating ip id: ')
	float_ip_info = mynova.floating_ips.find(id=new_ip)
	print float_ip_info

def five():
	new_ip = raw_input('Enter Floating ip id: ')
	float_ip_info = mynova.floating_ips.find(id=new_ip)
	mynova.floating_ips.delete(float_ip_info)

def six():
	#Add a floating ip to an instance created 
	inst_name = raw_input("Enter name of instance: ")
	instance = mynova.servers.find(name=inst_name)
	ip_input = raw_input("Enter ip to be allocated: ")
	ip_allocate = mynova.floating_ips.find(ip=ip_input)
	instance.add_floating_ip(ip_allocate)

def seven():
	#Remove ip allocated to an instance 
	inst_name = raw_input("Enter name of instance: ")
	instance = mynova.servers.find(name=inst_name)
	print "Removing floating ip just created"
	to_remove = mynova.floating_ips.find(instance_id=(instance.id))
	instance.remove_floating_ip(to_remove.ip)

options = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven}
choice = 0
while(choice != 8):
	print 'Select an option'
	print '1. List all floating ip pools'
	print '2. List ip addresses associated with tenant/account'
	print '3. Allocate a new ip address to tenant/account'
	print '4. List details of the floating IP address associated with floating_IP_address_ID'
	print '5. Deallocated the floating IP address associated with floating_IP_address_ID'
	print '6. Add a floating IP address to an instance'
	print '7. Remove a floating IP address to an instance'
	print '8. Exit'
	choice = int(input('Enter a choice: '))
	if choice < 1 or choice > 8:
		print 'Incorrect option. Please enter a valid option.'
	elif choice == 8:
		exit()
	else:
		options[choice]()
	print ""
