print('[-- Faça um programa em Python que abra e reproduza o Áudio de um arquivo MP3. --]\n')
import playsound
playsound('C:\Users\Roberto\Documents\MeusProjetos\Exercicios-Python')
import pygame
pygame.init()
pygame.mixer.music.load('Sleep Away.mp3')
pygame.mixer.music.play()
pygame.event.wait()


