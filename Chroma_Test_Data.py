import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

class ChromaDBClient:

  def __init__(self, host="", port=8000, api_key="", model_name=""):
    """
    Initializes a ChromaDB client with connection details and embedding function

    Args:
        host (str, optional): ChromaDB server host. Defaults to "13.49.73.92".
        port (int, optional): ChromaDB server port. Defaults to 8000.
        api_key (str, optional): OpenAI API key for text embedding. Defaults to "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".
        model_name (str, optional): OpenAI text embedding model name. Defaults to "text-embedding-3-large".
    """
    self.host = host
    self.port = port
    self.chroma_client = chromadb.HttpClient(host=self.host, port=self.port)  # Initialize client in constructor
    self.embedding_function = OpenAIEmbeddingFunction(api_key=api_key, model_name=model_name)

  def get_collection(self, name=""):
    """
    Gets a collection from ChromaDB with the specified name and embedding function

    Args:
        name (str, optional): Name of the collection. Defaults to "Cash".

    Returns:
        chromadb.Collection: The retrieved collection object.
    """
    return self.chroma_client.get_collection(name=name, embedding_function=self.embedding_function)

  def query(self, query_text, collection_name, n_results=2, include=["distances", "documents"]):
    """
    Queries a ChromaDB collection with a text and returns documents with distances

    Args:
        query_text (str): Text to query the collection with.
        collection_name (str, optional): Name of the collection. Defaults to "Cash".
        n_results (int, optional): Number of results to retrieve. Defaults to 2.
        include (list, optional): List of fields to include in the results. Defaults to ["distances", "documents"].

    Returns:
        dict: Dictionary containing query results.
    """
    collection = self.get_collection(name=collection_name)
    results = collection.query(query_texts=[query_text], n_results=n_results, include=include)
    return results

  def delete_collection(self, collection_name):
    """
    Deletes a collection from ChromaDB

    Args:
        collection_name (str): Name of the collection to delete.

    Returns:
        None
    """
    try:
      # Use the existing `chroma_client` instance
      self.chroma_client.delete_collection(name=collection_name)
      print(f"Collection '{collection_name}' successfully deleted.")
    except Exception as e:
      print(f"Error deleting collection '{collection_name}': {e}")

  def list_collections(self):
    """
    Lists all collections in ChromaDB

    Returns:
        None
    """
    try:
      collections = self.chroma_client.list_collections()
      for collection in collections:
        self.get_collection_data(collection.name)  # Call new function
    except Exception as e:
      print(f"Error listing collections: {e}")

  def get_collection_data(self, collection_name,chromadb_host,chromadb_port):
    Document = []
    ids = []
    try:
      # Use chromadb client for collection access
      chroma_client = chromadb.HttpClient(host=chromadb_host, port=chromadb_port)
      collection = chroma_client.get_collection(name=collection_name)
      documents = collection.get()
      print(f"Collection: {collection_name}")
      for doc_id, doc in documents.items():
        if doc_id == "ids":
          ids.append(doc)
        elif doc_id == "documents":
          Document.append(doc)
      combined = zip(ids[0], Document[0])
      my_dict = dict(combined)
      return my_dict


    except Exception as e:
      print(f"Error getting data for collection '{collection_name}': {e}")


