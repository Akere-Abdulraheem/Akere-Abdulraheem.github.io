from pypaystack import Transaction, Customer, Plan

"""
All Response objects are a tuple containing status_code, status, message and data
"""

#Instantiate the transaction object to handle transactions.  
#Pass in your authorization key - if not set as environment variable PAYSTACK_AUTHORIZATION_KEY

transaction = Transaction(authorization_key="sk_myauthorizationkeyfromthepaystackguys")
response = transaction.charge("customer@domain.com", "CustomerAUTHcode", 10000) #Charge a customer N100.
response  = transaction.verify(refcode) #Verify a transaction given a reference code "refcode".


#Instantiate the customer class to manage customers

customer = Customer(authorization_key="sk_myauthorizationkeyfromthepaystackguys")
response = customer.create("customer2@gmail.com", "John", "Doe", phone="080123456789") #Add new customer
response = customer.getone("CUS_xxxxyy") #Get customer with customer code of  CUS_xxxxyy
response = customer.getall() #Get all customers


#Instantiate the plan class to manage plans

plan = Plan(authorization_key="sk_myauthorizationkeyfromthepaystackguys")
response = plan.create("Test Plan", 150000, 'Weekly') #Add new plan
response = plan.getone(240) #Get plan with id of 240
response = plan.getall() #Get all plans
