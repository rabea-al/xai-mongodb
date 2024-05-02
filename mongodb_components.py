from xai_components.base import InArg, InCompArg, OutArg, Component, xai_component
import pymongo

@xai_component
class InitMongoDBConnection(Component):
    """
    Component to initialize and store a MongoDB connection in the context.
    
    ##### inPorts:
    - uri: MongoDB URI string required to connect to the database. Example: "mongodb://localhost:27017/"
    
    ##### outPorts:
    - client: Outputs the MongoDB client object for use in other components.
    """
    uri: InCompArg[str]
    client: OutArg[pymongo.MongoClient]

    def execute(self, ctx) -> None:
        client = pymongo.MongoClient(self.uri.value)
        self.client.value = client
        ctx['mongo_client'] = client
        print("MongoDB connection initialized and stored in context.")

def check_mongo_client(ctx):
    if 'mongo_client' in ctx:
        return ctx['mongo_client']
    else:
        raise Exception("MongoDB client not found in context. Please ensure the InitMongoDBConnection component is executed first.")

@xai_component
class MongoDBInsertDocument(Component):
    """
    Component to insert a document into MongoDB.
    
    ##### inPorts:
    - client: The MongoDB client object (optional).
    - database_name: The name of the database to insert the document into.
    - collection_name: The name of the collection to insert the document into.
    - document: The document to be inserted as a dictionary.
    """
    client: InArg[pymongo.MongoClient]
    database_name: InArg[str]
    collection_name: InArg[str]
    document: InCompArg[dict]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else check_mongo_client(ctx)
        db = client[self.database_name.value]
        collection = db[self.collection_name.value]
        result = collection.insert_one(self.document.value)
        print("Document inserted, ID:", result.inserted_id)

@xai_component
class MongoDBFindDocuments(Component):
    """
    Component to find documents in MongoDB.
    
    ##### inPorts:
    - client: The MongoDB client object (optional).
    - database_name: The name of the database from which to retrieve documents.
    - collection_name: The name of the collection from which to retrieve documents.
    - query: A dictionary defining the query criteria to locate the documents.
    
    ##### outPorts:
    - found_documents: Outputs the list of documents found by the query.
    """
    client: InArg[pymongo.MongoClient]
    database_name: InArg[str]
    collection_name: InArg[str]
    query: InCompArg[dict]
    found_documents: OutArg[list]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else check_mongo_client(ctx)
        db = client[self.database_name.value]
        collection = db[self.collection_name.value]
        documents = list(collection.find(self.query.value))
        self.found_documents.value = documents
        print("Documents retrieved.")

@xai_component
class MongoDBUpdateDocument(Component):
    """
    Component to update documents in MongoDB.
    
    ##### inPorts:
    - client: The MongoDB client object (optional).
    - database_name: The name of the database where the documents will be updated.
    - collection_name: The name of the collection where the documents will be updated.
    - filter: A dictionary defining the criteria to select the documents to be updated.
    - update: A dictionary defining the changes to apply to the selected documents.
    """
    client: InArg[pymongo.MongoClient]
    database_name: InArg[str]
    collection_name: InArg[str]
    filter: InCompArg[dict]
    update: InCompArg[dict]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else check_mongo_client(ctx)
        db = client[self.database_name.value]
        collection = db[self.collection_name.value]
        result = collection.update_many(self.filter.value, self.update.value)
        print("Documents updated:", result.modified_count)

@xai_component
class MongoDBDeleteDocument(Component):
    """
    Component to delete documents from MongoDB.
    
    ##### inPorts:
    - client: The MongoDB client object (optional).
    - database_name: The name of the database from which documents will be deleted.
    - collection_name: The name of the collection from which documents will be deleted.
    - query: A dictionary defining the criteria to select the documents to be deleted.
    """
    client: InArg[pymongo.MongoClient]
    database_name: InArg[str]
    collection_name: InArg[str]
    query: InCompArg[dict]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else check_mongo_client(ctx)
        db = client[self.database_name.value]
        collection = db[self.collection_name.value]
        result = collection.delete_many(self.query.value)
        print("Documents deleted:", result.deleted_count)


