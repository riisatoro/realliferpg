def save_to_db(collection, instance):
    collection.insert_one(instance)
    return


def find_in_db(collection, **kwargs):
    return list(collection.find(kwargs))


def count_existed_in_db(collection, **kwargs):
    return collection.count_documents(kwargs)
