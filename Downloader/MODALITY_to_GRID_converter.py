import glob
import os
import cv2
import math

root_dir = "/Users/marceloqueiroz/Documents/Berkeley/term5/w251/Final_project"
sources_path = os.path.join(root_dir, "video_modality_per_digit", "*", "*")
output_train_path = os.path.join(root_dir, "videos_modality_for_lipnet", "train")
output_eval_path = os.path.join(root_dir, "videos_modality_for_lipnet", "eval")
output_align_path = os.path.join(root_dir, "videos_modality_for_lipnet", "align")

fps = 100  # according to dataset documentation
height = 640  # original height is 1920
width = 360  # original width is 1080
fourcc = cv2.VideoWriter_fourcc(*'mpg2')

converter_dict = {"ZERO": 0,
                  "ONE": 1,
                  "TWO": 2,
                  "THREE": 3,
                  "FOUR": 4,
                  "FIVE": 5,
                  "SIX": 6,
                  "SEVEN": 7,
                  "EIGHT": 8,
                  "NINE": 9}

# define which speakers will go to evaluation dataset.
# Here we used 4 unseen speakers for evaluation.
eval_speakers = [1, 19, 27, 28]

# iterate through all videos, copying in the correct folder and generating align txt files for all
for video_path in glob.glob(sources_path):
    spoken_digit = video_path.split("/")[-2]
    split_name = os.path.splitext(video_path.split("/")[-1])[0]

    speaker_num = int(split_name.split("_")[0][-2:])

    cam_side = split_name.split("_")[-2]

    video_code = split_name.split("_")[-1]

    # use opencv to check for video frame count:
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    vid_length = int(math.ceil(frame_count) * 1000)

    # LipNet need 75 frames videos, so we will "pad" with frozen frames in the beginning and in the end of each video.
    init_padding = int((75 - frame_count)//2)
    end_padding = int(75 - frame_count - init_padding)

    if speaker_num in eval_speakers:

        os.makedirs(os.path.join(output_eval_path, "s" + str(speaker_num)), exist_ok=True)

        output_video = cv2.VideoWriter(os.path.join(output_eval_path, "s" + str(speaker_num), video_code + cam_side +
                                                    ".mpg"), fourcc, fps, (width, height))

        # insert initial padding
        for frame_num in range(init_padding):
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            ret, frame = cap.retrieve()
            resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
            output_video.write(resized)

        # now recording the video
        # cap.set(cv2.CAP_PROP_POS_FRAMES, init_padding)
        for frame_num in range(frame_count):
            ret, frame = cap.read()
            resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
            output_video.write(resized)

        # now freeze last frames
        cur_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        for frame_num in range(end_padding):
            cap.set(cv2.CAP_PROP_POS_FRAMES, cur_frame)
            ret, frame = cap.retrieve()
            resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
            output_video.write(resized)

        with open(os.path.join(output_align_path, video_code + cam_side + ".align"), "a+") as f:
            f.write("0 " + str(init_padding*1000) + " sil\n")
            f.write(str(init_padding*1000) + " " + str(vid_length) + " " + spoken_digit.lower() + "\n")
            f.write(str(vid_length) + " 75000 sil")

    else:

        os.makedirs(os.path.join(output_train_path, "s" + str(speaker_num)), exist_ok=True)

        output_video = cv2.VideoWriter(os.path.join(output_train_path, "s" + str(speaker_num), video_code + cam_side +
                                                    ".mpg"), fourcc, fps, (width, height))

        # insert initial padding
        for frame_num in range(init_padding):
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            ret, frame = cap.retrieve()
            resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
            output_video.write(resized)

        # now recording the video
        # cap.set(cv2.CAP_PROP_POS_FRAMES, init_padding)
        for frame_num in range(frame_count):
            ret, frame = cap.read()
            resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
            output_video.write(resized)

        # now freeze last frames
        cur_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        for frame_num in range(end_padding):
            cap.set(cv2.CAP_PROP_POS_FRAMES, cur_frame)
            ret, frame = cap.retrieve()
            resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
            output_video.write(resized)

        with open(os.path.join(output_align_path, video_code + cam_side + ".align"), "a+") as f:
            f.write("0 " + str(init_padding*1000) + " sil\n")
            f.write(str(init_padding*1000) + " " + str(vid_length) + " " + spoken_digit.lower() + "\n")
            f.write(str(vid_length) + " 75000 sil")

    cap.release()