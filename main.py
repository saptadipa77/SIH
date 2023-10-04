from appwrite.client  import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from appwrite.query import Query
import pprint
"""client is basically our computer and from where we send our database to the server and it stores all info from appwrite after creating new project"""
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('65190e566a551bf59b08')
client.set_key('a855deff07bbd40f81703bffd084aaeae1d3acb85bc6540a4c23fda3e21b7e5dde38c4d0013d71aad5bf98d066e1d969fb75e4d62d5bbbfaffa2410f99c18b1f214042c358bb6c42053a2b824a73c2982f418ccae3b557c8ca577565213d813e92aa039865569ff093c8f53ce74e5537a6be690b42027bcdc04eba1e721c4fd8')
"""receives all the info under the client part and recognizes in which project we need to perform crud operations"""
"""db basically has all the infos of client"""
db=Databases(client)
#response=db.create(database_id="demo_db",name="demodb")
"""after creating anything or doing any operation we should comment out the response thing so that it again does not create a collection pr perform the same thing"""
#response=db.create_collection(database_id="demo_db",collection_id="demo_collection",name="demo_collection")

#response=db.create_string_attribute(database_id="demo_db",collection_id="demo_collection",key="user_id",size=50,required=True)
#response=db.create_string_attribute(database_id="demo_db",collection_id="demo_collection",key="name",size=50,required=True)
#response=db.create_string_attribute(database_id="demo_db",collection_id="demo_collection",key="password",size=50,required=True)
"""here we are inserting documents into the table"""
# response=db.create_document(
#     database_id="demo_db",
#     collection_id="demo_collection",
#     document_id=ID.unique(),
#     data={"user_id":"ani","name":"Anindita Datta","password":"9884",
#           }
#     )
"""read operation means using the function list"""
"""lists all the things created in the project of appwrite"""
#response=db.list()
#print(response)
"""lists all the tables or collections that we created in the database"""
#response=db.list_collections(database_id="demo_db")
#print(response)
"""lists all the documents in the collection of database"""
#response=db.list_documents(database_id="demo_db",collection_id="demo_collection")
#print(response)
#response=db.update(
#    database_id="demo_db",
#    name="demo_new_collection",
#)
# response=db.update_collection(
#     database_id="demo_db",
#     collection_id="demo_collection",
#     name="demo_new_collection"
# )
# response=db.update_string_attribute(
#     database_id="demo_db",
#     collection_id="demo_collection",
#     key="user_id",
#     required=False,
#     default=""
# )
"""----Using query from here----"""
response=db.list_documents(
    database_id="demo_db",
    collection_id="demo_collection",
    queries=[
        Query.equal(attribute="user_id",value="navya")
    ]
    )
# """if we comment out the queries part and then execute then all the records that are entered in the documents will be printed"""
# pprint.pprint(response)
"""pprint basically prints the data of the dictionary in a beautiful way. We also need to import pprint in the beginning of the program"""
# def search(index):
#     print(index.search("name=krita"))

# fields=[
#     search.TextField(name='title',value='user_id')
# ]
# d=search.Document(fields=fields)
# search.Index(name="_INDEX_NAME").put(d)
# doc_id=d.doc_id
# results=search.Index(name='Navya Sri Thalluri').put(d)
# doc_id=results[0].id
# print(doc_id)
# pprint.pprint(response['documents'][0]['$id'])
#pprint.pprint(response)
pprint.pprint(response['documents'][0]['password'])











































