import pygame

print('===== EXERCICIO 021 =====')
print('- Faça um programa em python que abra e reproduza o áudio de um arquivo MP3 -')

pygame.init()
pygame.mixer.music.load('aa.ogg')
pygame.mixer.music.play()
pygame.event.wait()
