# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:58:27 2017

@author: ZY
"""

#question 1.1.2
class Email:
    def __init__(self, msg, sender_name, recipient_name):
        self.msg=msg
        self.sender_name=sender_name
        self.recipient_name=recipient_name

        
class Postman:
    def __init__(self):
        self.clients = {}
        
    def send(self, email):
        self.clients[email.recipient_name].receive(email)
        
    
    def register_client(self, client, client_name):
        self.clients[client_name]=client
        
class Client:
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman=mailman
        self.name=name
        self.mailman.register_client(self,self.name)
        
    def compose(self, msg, recipient_name):
        email=Email(msg,self.name,recipient_name)
        self.mailman.sent(email)
        
    def receive(self, email):
        self.inbox.append(email)
        
        