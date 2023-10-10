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
db=Databases(client)
userid=input("Enter your username: ")
emailid=input("Enter your emailid: ")
pwd1=input("Enter your password1: ")
pwd2=input("Enter your password2: ")

response1=db.list_documents(
database_id="demo_db",
collection_id="demo_collection",
queries=[
Query.equal(attribute="user_id", value=userid),
# Query.equal(attribute="password",value=pwd1),
# Query.equal(attribute="password", value=pwd2),
]
)  
response2=db.list_documents(
database_id="demo_db",
collection_id="demo_collection",
queries=[
Query.equal(attribute="email_id", value=emailid),
# Query.equal(attribute="password",value=pwd1),
# Query.equal(attribute="password", value=pwd2),
]
)  
# if response['documents'][0]['pwd1'] == response['documents'][0]['pwd2']:
if response1['total']==1 or response2['total']==1:
    print("Userid and emailid exists")
else:
    while pwd1!=pwd2:
        print("Password not matched")
        pwd1=input("Enter your password: ")
        pwd2=input("Enter your password: ")

        # response=db.list_documents(
        # database_id="demo_db",
        # collection_id="demo_collection",
        # queries=[
        # # Query.equal(attribute="user_id", value=userid),
        # # Query.equal(attribute="email_id", value=emailid),
        # Query.equal(attribute="password",value=pwd1),
        # Query.equal(attribute="password", value=pwd2),
        # ]
        # )
        continue;
    response=db.create_document(
        database_id="demo_db",
        collection_id="demo_collection",
        document_id=ID.unique(),
        data={"user_id":userid,"email_id":emailid,"password":pwd1
            }
        )
    print("Account created successfully")
