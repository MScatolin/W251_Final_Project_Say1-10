from moviepy.tools import subprocess_call
from moviepy.config import get_setting
from pydub import AudioSegment
import os

# TODO: add IBM cloud object storage modules and connection strings.
save_dir = "/Users/marceloqueiroz/Documents/Berkeley/term5/w251/Final_project/data/output"

def extract_subclip(filename, t1, t2, targetname = None):
    """ Makes a new video file playing video file ``filename`` between
    the times ``t1`` and ``t2``. Timestamps in 100 ns multiples"""
    name, ext = os.path.splitext(filename.name)
    t1 = int(t1)/1000
    t2 = int(t2)/1000
    if not targetname:
        T1, T2 = [int(t) for t in [t1, t2]]
        targetname = "%sSUB%d_%d.%s" % (name, T1, T2, ext)

    cmd = [get_setting("FFMPEG_BINARY"),"-y",
           "-ss", "%0.2f"%t1,
           "-i", filename,
           "-t", "%0.2f"%(t2-t1),
           "-vcodec", "copy", "-acodec", "copy", targetname]

# open local files for testing:
transcription = open("/Users/marceloqueiroz/Documents/Berkeley/term5/w251/Final_project" + "/data/SPEAKER09_C1_AUD1_crop.lab")
audio = open("/Users/marceloqueiroz/Documents/Berkeley/term5/w251/Final_project" + "/data/SPEAKER09_C1_AUD2.wav")
vid_left = open("/Users/marceloqueiroz/Documents/Berkeley/term5/w251/Final_project" + "/data/SPEAKER09_C1_STRL_h265.mkv")
vid_right = open("/Users/marceloqueiroz/Documents/Berkeley/term5/w251/Final_project" + "/data/SPEAKER09_C1_STRL_h265.mkv")
list_of_words = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def clip_files(transcription, audio, vid_left, vid_right, list_of_words = None):
    """
    this function receives the downloaded files described below and split the two videos and the audio according to the
    timestamps available in the transcription and the required words

    :param transcription: text file where each line contains a initial and a final timestamp together with the
    spoken digit.
    :param audio: wav file for cropping
    :param vid_left: one of the mkv video files for cropping
    :param vid_right: the second mkv file for cropping
    :param list_of_words: list of words to be considered. If missing will consider all words in transcription
    :return: none
    """

for line in transcription:
    line = line.strip()
    init_ts, end_ts, word = line.split(' ')
    if list_of_words:
        if word.split("\\n")[0] in list_of_words:
            # TODO: split video1, split video2, split audio, save everything to file
            base_name = vid_left.name.split('/')[0]

            # clip the two video files and save
            extract_subclip(vid_left, init_ts, end_ts, save_dir + "/video/" + base_name + "_L.mkv")
            extract_subclip(vid_right, init_ts, end_ts, save_dir + "/video/" + base_name + "_R.mkv")

            # clip the audio file and save (twice to match the two video files)
            # wav_file = AudioSegment.from_wav(audio)[1000:2000]
            # wav_file.export(save_dir + "/audio/" + base_name + "_L.wav")
            # wav_file.export(save_dir + "/audio/" + base_name + "_R.wav")
    else:
        # clip the two video files and save
        extract_subclip(vid_left, init_ts, end_ts, save_dir + "/video/" + base_name + "_L.mkv")
        extract_subclip(vid_right, init_ts, end_ts, save_dir + "/video/" + base_name + "_R.mkv")

        # clip the audio file and save (twice to match the two video files)
        wav_file = AudioSegment.from_wav("/Users/marceloqueiroz/Documents/Berkeley/term5/w251/Final_project" + "/data/SPEAKER09_C1_AUD2.wav")[init_ts / 1000:end_ts / 1000]
        wav_file.export(save_dir + "/audio/" + base_name + "_L.wav")
        wav_file.export(save_dir + "/audio/" + base_name + "_R.wav")
