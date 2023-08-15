#!/usr/bin/env python3
""" Task 8. List all mongoDB documents in Python """

import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection """
    return [doc for doc in mongo_collection.find()]
