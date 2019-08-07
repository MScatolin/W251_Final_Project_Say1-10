#!/usr/bin/env bash

mkdir full_files
mkdir full_files/audios
mkdir full_files/transcriptions
mkdir full_files/videos

mkdir videos
mkdir videos/ZERO
mkdir videos/ONE
mkdir videos/TWO
mkdir videos/THREE
mkdir videos/FOUR
mkdir videos/FIVE
mkdir videos/SIX
mkdir videos/SEVEN
mkdir videos/EIGHT
mkdir videos/NINE

mkdir audios
mkdir audios/ZERO
mkdir audios/ONE
mkdir audios/TWO
mkdir audios/THREE
mkdir audios/FOUR
mkdir audios/FIVE
mkdir audios/SIX
mkdir audios/SEVEN
mkdir audios/EIGHT
mkdir audios/NINE

apt update

apt install ffmpeg

apt install python3

apt install python3-pip

apt install python3-opencv

pip3 install pydub

pip3 install requests
