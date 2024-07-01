import sqlite3
conn = sqlite3.connect('yt_project.db')
cursor=conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS yt_videos(
    id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    time TEXT NOT NULL)
''')

def list_all_videos():
    cursor.execute("SELECT * FROM yt_videos" )
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO yt_videos(name, time) values (?,?)", (name, time))
    conn.commit()

def update_video(video_id,new_name, new_time):
    cursor.execute("UPDATE yt_videos SET name=?,  time=? where id=?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM yt_videos WHERE id =?", (video_id,))
    conn.commit()

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

conn.close()



