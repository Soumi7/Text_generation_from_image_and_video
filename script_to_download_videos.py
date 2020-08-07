import youtube_dl

with open('./text_files/Vid2Url_Full.txt', 'r') as f:
    file_content = f.read() # Read whole file in the file_content string
print(file_content)

dic=dict(file_content)

for filename,youtube_addon in file_content :
    video_path = "/Data/YoutubeClips/" + filename + ".mp4"
    video_link = "https://www.youtube.com/watch?v=" + youtube_addon

    print(video_path)
    print(video_link)

    ydl_opts = {'outtmpl': video_path}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])