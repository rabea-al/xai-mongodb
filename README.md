# Xircuits MongoDB Component Library

This library provides components for managing MongoDB operations within Xircuits, such as establishing connections and handling data manipulation.

## Installation

To install this component library in Xircuits, you can use the [tray library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface) or use the following command:

```bash
xircuits install mongodb
```

Alternatively, for manual setup:

```bash
git clone https://github.com/XpressAI/xai-mongodb xai_components/xai_mongodb
cd xai_components/xai_mongodb
pip install -r requirements.txt
```

## Database Local Setup
If you prefer to set up MongoDB locally for development or testing, follow these steps:

1. Download and install MongoDB from [MongoDB Downloads](https://www.mongodb.com/try/download/community). Choose the version compatible with your operating system.
2. Run MongoDB. Ensure the MongoDB service is accessible via the connection URI used in your components, typically something like mongodb://localhost:27017.
3. Create the database and collection if it is the first run, then run the xircuits example.

## Components

- **InitMongoDBConnection**: Establishes a MongoDB connection and provides a client instance.
- **MongoDBInsertDocument**: Inserts a document into a specified MongoDB collection.
- **MongoDBFindDocuments**: Retrieves documents based on a query from a MongoDB collection.
- **MongoDBUpdateDocument**: Updates documents in a MongoDB collection based on a specified filter.
- **MongoDBDeleteDocument**: Deletes documents from a MongoDB collection based on a specified query.
