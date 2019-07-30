import os
import cv2
import math
import time
from pydub import AudioSegment

# verify files path
save_dir = "data/"
list_of_words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
fps = 100  # according to dataset documentation
height = 640  # original height is 1920
width = 360  # original width is 1080
fourcc = cv2.VideoWriter_fourcc(*'mpg2')  # encoder case we want to convert to other file formats. Can lose quality.
logfile = save_dir + "logfile.txt"  # simple text file for logging and debugging.

for filename in os.listdir(save_dir + "full_files/transcripts"):  # filename example SPEAKER09_C1_AUD1.lab

    # open tanscriptions file
    f = open(save_dir + "full_files/transcripts/" + filename)

    # logging for debug
    print(time.asctime(), " - processing file: ", filename)
    print(time.asctime(), " - processing file: ", filename, file=open(logfile, "a"))

    try:  # case hidden files are created inside the dataset folders

        # iterate line by line, extract the word
        for line in f:
            line = line.strip()
            init_ts, end_ts, word = line.split(' ')

            # open the left video file with openCV
            captureL = cv2.VideoCapture(save_dir + "full_files/videos/" + filename.split('_')[0] + "_" +
                                        filename.split('_')[1] + "_STRL.mkv")

            # open the right video file with openCV
            captureR = cv2.VideoCapture(save_dir + "full_files/videos/" + filename.split('_')[0] + "_" +
                                        filename.split('_')[1] + "_STRR.mkv")

            # open audio file
            full_audio = AudioSegment.from_wav(save_dir + "full_files/audios/" + filename.split('_')[0] + "_" +
                                               filename.split('_')[1] + "_AUD2.wav")

            # check if current word is on the target words list
            if word in list_of_words:
                # calculate initial and final timestamps in microseconds, and frames to be iterated
                start_pos = math.floor(int(init_ts) / 10000)
                end_pos = math.ceil(int(end_ts) / 10000)
                frame_count = math.ceil((end_pos - start_pos)/10 + 1)

                # set a code based on time to avoid overwriting and match all files:
                filecode = str(int(time.time()))

                # logging for debug purposes
                print(time.asctime(), " - new word: ", word, start_pos/1000, "secs to", end_pos/1000,
                      "secs, filecode #: ", filecode)
                print(time.asctime(), " - new word: ", word, start_pos/1000, "secs to", end_pos/1000,
                      "secs, filecode #: ", filecode, file=open(logfile, "a"))

                # set decoders and initial time to start clipping videos
                captureL.set(cv2.CAP_PROP_FOURCC, fourcc)
                captureL.set(cv2.CAP_PROP_POS_MSEC, start_pos)
                captureR.set(cv2.CAP_PROP_FOURCC, fourcc)
                captureR.set(cv2.CAP_PROP_POS_MSEC, start_pos)

                # set up video output for left camera
                output_videoL = cv2.VideoWriter(save_dir + "videos/" + word + "/" + filename.split('_')[0] + "_" +
                                                filename.split('_')[1] + "_L_" + filecode + ".mkv", fourcc,
                                                fps, (width, height))

                # iterate through frames, saving to new short video
                for frame_num in range(frame_count):
                    ret, frame = captureL.read()
                    resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
                    output_videoL.write(resized)

                # set up video output for right camera
                output_videoR = cv2.VideoWriter(save_dir + "videos/" + word + "/" + filename.split('_')[0] + "_" +
                                                filename.split('_')[1] + "_R_" + filecode + ".mkv", fourcc,
                                                fps, (width, height))

                # iterate through frames, saving to new short video
                for frame_num in range(frame_count):
                    ret, frame = captureR.read()
                    resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
                    output_videoR.write(resized)

                # cut audio file and store it
                audio = full_audio[start_pos:end_pos]
                audio.export(save_dir + "audios/" + word + "/" + filename.split('_')[0] + "_" +
                             filename.split('_')[1] + "_" + filecode + ".wav", format="mp3")

                # release videos
                captureL.release()
                captureR.release()

            else:  # release video file after the last word was processed.
                captureL.release()
                captureR.release()

    except:  # case the file isn't a transcription, ignore it and move on.
        continue
