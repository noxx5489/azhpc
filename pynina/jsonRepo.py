import pydocumentdb.document_client as document_client

class jsonrepo():
    """ use to save a json document into CosmosDB """
    def __init__(self, endpoint, key, database, collection):
        self.client = document_client.DocumentClient(endpoint, {'masterKey': key})
        self.database = database
        self.collection = collection
        self.coll_link = self.GetDocumentCollectionLink(self.database, self.collection)

    """ save a json doc """
    def UpdateDocument(self, doc):        
        self.client.UpsertDocument(self.coll_link, doc)

    def GetDatabaseLink(self, database):
        return 'dbs/' + database

    def GetDocumentCollectionLink(self, database, collection):
        return self.GetDatabaseLink(database) + '/colls/' + collection

    def GetDocumentLink(self, database, collection, docId):
        return self.GetDocumentCollectionLink(database, collection) + '/docs/' + docId
