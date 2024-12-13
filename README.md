<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>





<p align="center"><i>Xircuits Component Library to integrate with 
MongoDB! Seamlessly manage your database operations.</i></p>

---
## Xircuits Component Library for MongoDB

This library integrates MongoDB functionalities into Xircuits workflows, enabling database management, document operations, and seamless interaction with MongoDB collections and databases.

## Table of Contents

- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)

## Preview

### The Example:

<img src="https://github.com/user-attachments/assets/418c4d14-8000-40aa-932e-b6b9417411ea" alt="mongodb-example" />

### The Result:

<img src="https://github.com/user-attachments/assets/9a6a0218-854d-4c00-862c-78f8a3ab1a2d" alt="mongodb-example_result" />

## Prerequisites

Before you begin, you will need the following:

1. Python3.9+.
2. Xircuits.
3. MongoDB 

## Main Xircuits Components

## Main Xircuits Components

### MongoDBInsertDocument Component:
Inserts a document into a specified MongoDB collection.

<img src="https://github.com/user-attachments/assets/aa342e49-51e4-43c4-a2d8-e736838445b7" alt="MongoDBInsertDocument" width="200" height="150" />

### MongoDBUpdateDocument Component:
Updates documents in a MongoDB collection based on a specified filter.

<img src="https://github.com/user-attachments/assets/b004c43e-0fa7-4a8d-a6da-07b2de62ea0a" alt="MongoDBUpdateDocument" width="200" height="150" />

### InitMongoDBConnection Component:
Establishes a MongoDB connection and provides a client instance.

### MongoDBFindDocuments Component:
Retrieves documents based on a query from a MongoDB collection.

### MongoDBDeleteDocument Component:
Deletes documents from a MongoDB collection based on a specified query.

## Try The Examples

We have provided an example workflow to help you get started with the MongoDB component library. Give it a try and see how you can create custom MongoDB components for your applications.

### MongoDB example
This example demonstrates how to use Xircuits with MongoDB. It initializes a MongoDB connection, inserts a document into a collection, and retrieves documents matching a specific query. The retrieved results are then printed for verification.

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