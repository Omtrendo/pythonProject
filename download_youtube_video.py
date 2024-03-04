from pytube import YouTube
link = input("Enter URL of the Video ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
#Please don't steal the intelectual property, pay to the authors fair. This is only for the test