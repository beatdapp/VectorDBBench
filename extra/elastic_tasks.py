import json
from dotenv import dotenv_values, find_dotenv
from elasticsearch import Elasticsearch

config = dotenv_values(find_dotenv())
client = Elasticsearch(config["HOST_URL"], api_key=config["API_KEY"])

tasks = client.tasks.list()
print(json.dumps(dict(tasks), indent=2))
