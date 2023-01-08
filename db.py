class db():
    def __init__(self):
        import pymongo
        import pymongo

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        dblist = myclient.list_database_names()
        if "database" in dblist:
            pass
        else:
            mydb = myclient["database"]
    def search(self):
        print("hi")
    def collection(self,collection_name):
        import pymongo

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["database"]
        collist = mydb.list_collection_names()
        if collection_name in collist:
            pass
        else:
            mycol = mydb[collection_name]
    def new_element(self,collection_name,element_name,element_content):
        import pymongo

        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['database']
        mycol = mydb[collection_name]

        mydict = { element_name: element_content}

        x = mycol.insert_one(mydict)
    def see(self,collection_name):
        import pymongo

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["database"]
        mycol = mydb[collection_name]

        for x in mycol.find():
            print(x)