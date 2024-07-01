from pymongo import MongoClient
from bson import ObjectId

Client = MongoClient("mongodb+srv://saadtariq:saadtariq@cluster0.ntrbfk3.mongodb.net/", tlsAllowInvalidCertificates=True)
db = Client["ytmanager"]
video_collection = db["videos"]

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
        result = video_collection.delete_one({"_id": video_id})
        
def main():
    while True:
        print("\n")
        print("YouTube Manager | Choose an option:")
        print("=" * 70)
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        print("=" * 70)

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video id to update: ")
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)

        elif choice == '5':
            print("Exiting the YouTube Manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
            print("=" * 70)


if __name__ == "__main__":
    main()