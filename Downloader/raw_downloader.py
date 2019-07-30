import zipfile
import io
import requests
import time
import os
import shutil

# verify string for directory where the files are supposed to be downloaded.
root_dir = "data/"
logfile = root_dir + "logfile.txt"
download_root = "http://153.19.49.27/MODALITY/"
test_speakers = [3, 4, 5, 7, 8, 9, 10, 13, 17, 21, 22, 23, 25, 26, 32, 33, 35]
training_speakers = [1, 2, 14, 19, 24, 27, 28, 29, 30, 31, 34, 36, 37, 38, 39, 40, 41, 42]
missing = [6, 11, 12, 15, 16, 18, 20]

# http://153.19.49.27/MODALITY/SPEAKER05/SPEAKER05_C1_test.zip

print(time.asctime(), "download starting")
print(time.asctime(), "download starting", file= open(logfile,"a"))

for spk in range(1, 43):
    for file_num in range(1, 7):

        if spk in test_speakers:
            download_url = download_root + "SPEAKER" + "{:02d}".format(spk) + "/SPEAKER" + "{:02d}".format(spk) + "_C" + \
                       str(file_num) + "test.zip"

        elif spk in training_speakers:
            download_url = download_root + "SPEAKER" + "{:02d}".format(spk) + "/SPEAKER" + "{:02d}".format(spk) + "_C" + \
                       str(file_num) + ".zip"

        else: break

        # test_url = "http://153.19.49.27/MODALITY/SPEAKER03/SPEAKER03_S5_h265.zip"

        # get data from web page to memory
        result = requests.get(download_url)
        file_stream = io.BytesIO(result.content)
        zip_file = zipfile.ZipFile(file_stream, 'r')
        archive_files = zip_file.namelist()

        print(time.asctime(), "parsing url: ", download_url[-16:], "file list: ", archive_files)
        print(time.asctime(), "parsing speaker: ", download_url[-16:], file= open(logfile,"a"))

        if archive_files[1][-4:] == ".lab":

            for zip_name in archive_files:
                if zip_name[-4:] == ".lab":

                    filename = os.path.basename(zip_name)

                    # copy file (taken from zipfile's extract)
                    source = zip_file.open(zip_name)
                    target = open(os.path.join(root_dir + "full_files/transcriptions/", filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)

                    print(time.asctime(), "extracting transcriptions")
                    print(time.asctime(), "extracting transcriptions", file= open(logfile,"a"))


                elif zip_name[-8:] == "AUD2.wav":

                    filename = os.path.basename(zip_name)

                    # copy file (taken from zipfile's extract)
                    source = zip_file.open(zip_name)
                    target = open(os.path.join(root_dir + "full_files/audios/", filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)

                    print(time.asctime(), "extracting audio")
                    print(time.asctime(), "extracting audio", file= open(logfile,"a"))

                elif zip_name[-8:] == "STRL.mkv":

                    filename = os.path.basename(zip_name.split('.')[0] + "_L." + zip_name.split('.')[1])

                    # copy file (taken from zipfile's extract)
                    source = zip_file.open(zip_name)
                    target = open(os.path.join(root_dir + "full_files/videos/", filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)

                    print(time.asctime(), "extracting video left")
                    print(time.asctime(), "extracting video left", file= open(logfile,"a"))

                elif zip_name[-8:] == "STRR.mkv":

                    filename = os.path.basename(zip_name.split('.')[0] + "_R." + zip_name.split('.')[1])

                    # copy file (taken from zipfile's extract)
                    source = zip_file.open(zip_name)
                    target = open(os.path.join(root_dir + "full_files/videos/", filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)

                    print(time.asctime(), "extracting video right")
                    print(time.asctime(), "extracting video right", file= open(logfile,"a"))

        else:
            zip_file.close()
