def search(
    query,
    documents
):

    result = []

    for doc in documents:

        if query.lower() in \
                doc["content"].lower():

            result.append(doc)

    return result
