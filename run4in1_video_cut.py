from moviepy.editor import *

def run4in1(target_ad , result_ad):

    getlength = VideoFileClip(target_ad).end
    time_1 = int(getlength *1/4)
    time_2 = int(getlength *2/4)
    time_3 = int(getlength *3/4)
    time_4 = int(getlength *4/4)

    clip_1 = VideoFileClip(target_ad).subclip(0,time_1) #读取视频，并截取
    clip_2 = VideoFileClip(target_ad).subclip(time_1,time_2) #读取视频，并截取
    clip_3 = VideoFileClip(target_ad).subclip(time_2,time_3) #读取视频，并截取
    clip_4 = VideoFileClip(target_ad).subclip(time_3,time_4) #读取视频，并截取

    final_clip = clips_array([[clip_1, clip_2],[clip_3, clip_4]]) #ok 可行
    # final_file_name = result_ad + '/' +

    final_clip.write_videofile(result_ad) # Many options...

def run4in1_thread(target_ads , result_ads ):
    for i, exec_file in enumerate(result_ads):
        run4in1(target_ads[i], exec_file)
        print(i+1,"/",len(result_ads)," 完成！")


if __name__ == '__main__':
    run4in1("myHolidays.mp4", "hebing3.mp4")