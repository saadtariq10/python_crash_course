import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
                
    except  FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n" + "*" * 70)
    print(f"{'No.':<5}{'Name':<40}{'Duration':<10}")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index:<5}{video['name']:<40}{video['time']:<10}")
    print("*" * 70 + "\n")

def add_video(videos):
    print("\n" + "-" * 70)
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully")
    print("-" * 70 + "\n")


def update_video(videos):
    print("\n" + "-" * 70)
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))

    if 1 <= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print("Video details updated successfully")
    else:
        print("Invalid index selected")
    print("-" * 70 + "\n")

def delete_video(videos):
    print("\n" + "-" * 70)
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("Video deleted successfully")
    else:
        print("Invalid index selected")
    print("-" * 70 + "\n")


def main():
    videos = load_data()
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



        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting the YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice, please try again.")
        print("=" * 70)

if __name__ == "__main__":
    main()