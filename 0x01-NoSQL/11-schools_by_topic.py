#!/usr/bin/env python3

""" Task 11. Where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """ return the list of school having a specific topic """
    return mongo_collection.find({"topics": topic})
