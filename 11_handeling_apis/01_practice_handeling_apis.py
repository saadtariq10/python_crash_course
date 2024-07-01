import requests

def fetch_random_dogs_api():
    url = "https://api.freeapi.app/api/v1/public/dogs?page=1&limit=10&query=Affenpinscher"
    response = requests.get(url)
    data = response.json()
    if data ["success"] and "data" in data:
        user_data = data["data"]
        total_pages = user_data["totalPages"]
        name = user_data["data"][0]["name"]
        origin = user_data["data"][0]["origin"]
        height = user_data["data"][0]["height"]["imperial"]
        image_id=user_data["data"][0]["image"]["id"]
        image_url=user_data["data"][0]["image"]["url"]

        return total_pages,name, origin, height, image_id, image_url
    
def main():
        try:
            total_pages, name, origin, height, image_id, image_url = fetch_random_dogs_api()
            print(f"Total Pages: {total_pages} \nName: {name}  \nImage URL: {image_url} \nOrigin: {origin} \nHeight: {height} \nImage ID: {image_id} ")

        except Exception as e:
             print(str(e))

if __name__ == "__main__":
    main()




    