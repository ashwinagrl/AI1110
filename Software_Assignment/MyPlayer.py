import pygame
import numpy as np
pygame.init()

window_width = 500
window_height = 500

play_button_pos = (100, 100)
play_button_size = (100, 100)
pause_button_pos = (300, 100)
pause_button_size = (100, 100)
prev_button_pos = (100, 300)
prev_button_size = (100, 100)
next_button_pos = (300, 300)
next_button_size = (100, 100)

song_numbers = np.arange(1,21)

def play_audio(audio_file,no):
    if(no == (len(song_numbers)-1)):
        np.random.shuffle(song_numbers)
    pygame.mixer.music.load(audio_file)
    # print(f"{no}.mp3 is playing")
    pygame.mixer.music.play()

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("MyMusic")
color = (144, 238, 144)
window.fill(color)

play_button_image = pygame.image.load("Images/play_button.png")
pause_button_image = pygame.image.load("Images/pause_button.png")
prev_button_image = pygame.image.load("Images/prev_button.png")
next_button_image = pygame.image.load("Images/next_button.png")

play_button_rect = pygame.Rect(play_button_pos, play_button_size)
pause_button_rect = pygame.Rect(pause_button_pos, pause_button_size)
prev_button_rect = pygame.Rect(prev_button_pos, prev_button_size)
next_button_rect = pygame.Rect(next_button_pos, next_button_size)

clock = pygame.time.Clock()
np.random.shuffle(song_numbers)

current_index = 0

running = True
play_next_song = False
for_pause = True
pygame.display.update()
clock.tick(60)
play_audio(f"Audio/{song_numbers[current_index]}.mp3",current_index)
while running:
    window.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                play_audio(f"Audio/{song_numbers[current_index]}.mp3",current_index)
                for_pause = True
            elif pause_button_rect.collidepoint(event.pos):
                pygame.mixer.music.pause()
                for_pause = False
            elif prev_button_rect.collidepoint(event.pos):
                current_index = (current_index - 1) % len(song_numbers)
                play_audio(f"Audio/{song_numbers[current_index]}.mp3",current_index)
            elif next_button_rect.collidepoint(event.pos):
                current_index = (current_index + 1) % len(song_numbers)
                play_audio(f"Audio/{song_numbers[current_index]}.mp3",current_index)

    if pygame.mixer.music.get_busy() == 0 and not play_next_song and for_pause:
        play_next_song = True

    font = pygame.font.Font("font/arial.ttf", 30)
    text = font.render(f"Currently Playing: {song_numbers[current_index]}.mp3", True, (0, 0, 0))
    window.blit(text, (90, 50))

    if play_next_song:
        current_index = (current_index + 1) % len(song_numbers)
        play_audio(f"Audio/{song_numbers[current_index]}.mp3",current_index)
        play_next_song = False

    
    window.blit(play_button_image, play_button_rect)
    window.blit(pause_button_image, pause_button_rect)
    window.blit(prev_button_image, prev_button_rect)
    window.blit(next_button_image, next_button_rect)
    
    pygame.display.flip()

pygame.quit()



