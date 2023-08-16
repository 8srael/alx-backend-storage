#!/usr/bin/env python3

""" Task 12. Log stats """

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    # db_name = my_db ; collection_name = nginx
    nginx_collection = client.logs.nginx
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    for http_method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_collection.count_documents({"method": http_method})
        print("\t method {}: {}".format(http_method, count))
    status_check = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))
