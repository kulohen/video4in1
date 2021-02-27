from moviepy.editor import *

clip1 = VideoFileClip("myHolidays.mp4").subclip(50,60)

getlength = VideoFileClip("myHolidays.mp4").end
time_1 = int(getlength *1/4)
time_2 = int(getlength *2/4)
time_3 = int(getlength *3/4)
time_4 = int(getlength *4/4)

clip_1 = VideoFileClip("myHolidays.mp4").subclip(0,time_1) #读取视频，并截取
clip_2 = VideoFileClip("myHolidays.mp4").subclip(time_1,time_2) #读取视频，并截取
clip_3 = VideoFileClip("myHolidays.mp4").subclip(time_2,time_3) #读取视频，并截取
clip_4 = VideoFileClip("myHolidays.mp4").subclip(time_3,time_4) #读取视频，并截取

final_clip = clips_array([[clip_1, clip_2],[clip_3, clip_4]]) #ok 可行
# final_clip = CompositeVideoClip([[clip_1, clip_2],[clip_3, clip_4]])


# result = CompositeVideoClip([clip1, clip2]) # Overlay text on video
# result.write_videofile("hebing.mp4") # Many options...
final_clip.write_videofile("hebing2.mp4") # Many options...