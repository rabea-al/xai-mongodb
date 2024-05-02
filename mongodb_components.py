from xai_components.base import InArg, OutArg, Component, xai_component
import pymongo

@xai_component(color="green")
class MongoDBConnection(Component):
    """
    Component to establish a MongoDB connection.
    
    ##### inPorts:
    - uri: MongoDB URI string required to connect to the database. Example: "mongodb://localhost:27017/"
    """
    uri: InArg[str]  # MongoDB URI

    def execute(self, ctx) -> None:
        self.client = pymongo.MongoClient(self.uri.value)
        print("MongoDB connection established.")

@xai_component
class MongoDBInsertDocument(Component):
    """
    Component to insert a document into MongoDB.
    
    ##### inPorts:
    - client: The MongoDB client object.
    - database_name: The name of the database to insert the document into.
    - collection_name: The name of the collection to insert the document into.
    - document: The document to be inserted as a dictionary.
    """
    client: InArg[pymongo.MongoClient]
    database_name: InArg[str]
    collection_name: InArg[str]
    document: InArg[dict]

    def execute(self, ctx) -> None:
        db = self.client.value[self.database_name.value]
        collection = db[self.collection_name.value]
        result = collection.insert_one(self.document.value)
        print("Document inserted, ID:", result.inserted_id)

@xai_component
class MongoDBFindDocuments(Component):
    """
    Component to find documents in MongoDB.
    
    ##### inPorts:
    - client: The MongoDB client object.
    - database_name: The name of the database from which to retrieve documents.
    - collection_name: The name of the collection from which to retrieve documents.
    - query: A dictionary defining the query criteria to locate the documents.
    ##### outPorts:
    - found_documents: Outputs the list of documents found by the query.
    """
    client: InArg[pymongo.MongoClient]
    database_name: InArg[str]
    collection_name: InArg[str]
    query: InArg[dict]
    found_documents: OutArg[list]

    def execute(self, ctx) -> None:
        db = self.client.value[self.database_name.value]
        collection = db[self.collection_name.value]
        documents = list(collection.find(self.query.value))
        self.found_documents.value = documents
        print("Documents retrieved.")

@xai_component
class MongoDBUpdateDocument(Component):
    """
    Component to update documents in MongoDB.
    
    ##### inPorts:
    - client: The MongoDB client object.
    - database_name: The name of the database where the documents will be updated.
    - collection_name: The name of the collection where the documents will be updated.
    - filter: A dictionary defining the criteria to select the documents to be updated.
    - update: A dictionary defining the changes to apply to the selected documents.
    """
    client: InArg[pymongo.MongoClient]
    database_name: InArg[str]
    collection_name: InArg[str]
    filter: InArg[dict]
    update: InArg[dict]

    def execute(self, ctx) -> None:
        db = self.client.value[self.database_name.value]
        collection = db[self.collection_name.value]
        result = collection.update_many(self.filter.value, self.update.value)
        print("Documents updated:", result.modified_count)

@xai_component
class MongoDBDeleteDocument(Component):
    """
    Component to delete documents from MongoDB.
    
    ##### inPorts:
    - client: The MongoDB client object.
    - database_name: The name of the database from which documents will be deleted.
    - collection_name: The name of the collection from which documents will be deleted.
    - query: A dictionary defining the criteria to select the documents to be deleted.
    """
    client: InArg[pymongo.MongoClient]
    database_name: InArg[str]
    collection_name: InArg[str]
    query: InArg[dict]

    def execute(self, ctx) -> None:
        db = self.client.value[self.database_name.value]
        collection = db[self.collection_name.value]
        result = collection.delete_many(self.query.value)
        print("Documents deleted:", result.deleted_count)
