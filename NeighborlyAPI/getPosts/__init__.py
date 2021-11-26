import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:

        url = "mongodb://cosmosdblab2:7OGwUstWlFr41tH0D67ttTTj42v6Yiuqp8tKipeBR7VFagkBQtf7wX7QsrFJQjlexC9RoGj2JtPM8MPdd7Gs3w==@cosmosdblab2.mongo.cosmos.azure.com:10255/lab2?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdblab2@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['lab2']
        collection = database['posts']
    



        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)