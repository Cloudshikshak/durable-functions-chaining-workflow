import requests, os, random, logging
from azure.storage.blob import ContainerClient

def main(name: str) -> str:
    storage_connection_string = os.environ["AzureWebJobsStorage"]
    container = ContainerClient.from_connection_string(conn_str=storage_connection_string, container_name="images")
    try:
        response = requests.get('https://picsum.photos/300')
        image_name = "image" + str(random.randrange(100,1000)) + ".jpg"

        blob_client = container.get_blob_client(image_name)
        blob_client.upload_blob(response.content, overwrite=True)
        
    except requests.exceptions.HTTPError as errh:
        # HTTP error getting file
        logging.error(str(errh))
    except:
        # Unknown error getting file
        pass
    return image_name