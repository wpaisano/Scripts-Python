'''Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3'''

from moviepy.editor import VideoFileClip

clip = VideoFileClip('/home/wpaisano/Downloads/videoplayback.mp4')
clip.preview()