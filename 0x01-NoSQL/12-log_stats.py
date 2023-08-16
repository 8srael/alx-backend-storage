#!/usr/bin/env python3

""" Task 12. Log stats """

from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    for http_method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        count = nginx_collection.count_documents({'method': http_method})
        print("\t method {}: {}".format(http_method, count))
    status_check = nginx_collection.count_documents(
            {'method': 'GET', 'path': '/status'}
    )
    print("{} status check".format(status_check))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    # db_name = my_db ; collection_name = nginx
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
 