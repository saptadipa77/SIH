from appwrite.client  import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from appwrite.query import Query
import pprint
"""client is basically our computer and from where we send our database to the server and it stores all info from appwrite after creating new project"""
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('65190e54854144c213e3')
client.set_key('dd0297f256aed3eb659e9100bf62af805ce7cfdd3bdae14fc7b01d415702a415fc62bb8089790c309bd3124f87f8bc52164e184e9f836c935cfa00bd468c0c54f788bc9f22a6f6cf1e052375da629c438f5e9e36ca86bf70453881fd12df0db0d5e57be3019b33c7e4deba50017d75a7035f3eaa98078fb38496bb2ace21e130')


# response=db.create_collection(database_id="demo_db",collection_id="demo_collection",name="demo_collection")

db=Databases(client)
#response=db.create_collection(database_id="demo_db",collection_id="demo_collection",name="demo_collection")

# def login(username,password):
#     # username=input("Enter your username")
#     # password=input("Enter your password")
    
#     response=db.list_documents(
#     database_id="demo_db",
#     collection_id="demo_collection",
#     queries=[
#         Query.equal(attribute="user_id", value=username),
#         Query.equal(attribute="password",value=password)
#     ])
#     while True:
#         if username in (response['documents'][0]['user_id']) and password in (response['documents'][0]['password']):
#             return True;
#         else:
#             return False;
# user=input("Enter your username")
# pwd=input("Enter your password")
#def login(username,password):
    # username=input("Enter your username")
    # password=input("Enter your password")

user=input("Enter your username")
passw=input("Enter your password")
response=db.list_documents(
database_id="demo_db",
collection_id="demo_collection",
queries=[
Query.equal(attribute="user_id", value=user),
Query.equal(attribute="password",value=passw)
])  
# response=db.list_documents(
#     database_id="demo_db",
#     collection_id="demo_collection",
#     queries=[
#     Query.equal(attribute="user_id", value=user),
#     Query.equal(attribute="password",value=passw)
# ])
    # while True:
    #     if username!=(response['documents'][0]['user_id']) and password!=(response['documents'][0]['password']):
    #         user=input("Enter your username")
    #         pwd=input("Enter your password")
    #         login(user,pwd)
    #     # else:
    #     #     login(user,pwd)

while response['total']!=1:
        # if (username!=(response['documents'][0]['user_id']) and password!=(response['documents'][0]['password'])):
    user=input("Enter your username")
    passw=input("Enter your password")
    # # response=db.list_documents(
    # # database_id="demo_db",
    # # collection_id="demo_collection",
    # # queries=[
    # # Query.equal(attribute="user_id", value=user),
    # # Query.equal(attribute="password",value=passw)
    # # ])
    # res(user,passw)
    response=db.list_documents(
    database_id="demo_db",
    collection_id="demo_collection",
    queries=[
    Query.equal(attribute="user_id", value=user),
    Query.equal(attribute="password",value=passw)
    ])  
    continue;

    
        
print("correct details entered");   
           

# user=input("Enter your username")
# pwd=input("Enter your password")
# login(user,pwd)
# response=db.list_documents(database_id="demo_db",collection_id="demo_collection")
# pprint.pprint(response)



        

    
