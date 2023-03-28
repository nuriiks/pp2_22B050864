import pygame
import os
pygame.init()
screen = pygame.display.set_mode((500,700))
run=True
bg = pygame.image.load('TSIS7/greenjpg.jpg')
fir = pygame.image.load('TSIS7/myun.jpg')
index_of_sound = 0
music_dir ='C:\\Users\\nuriks\\Documents\\GitHub\\pp2_22B050864\\TSIS7\\music\\'
pictures_dir='C:\\Users\\nuriks\\Documents\\GitHub\\pp2_22B050864\\TSIS7\\pictures\\'
pic_files = os.listdir(pictures_dir)
current_pic=0
music_files = os.listdir(music_dir)
current_music = 0
picture = pygame.image.load(pictures_dir+pic_files[current_pic])
pygame.mixer.music.load(music_dir + music_files[current_music])
pygame.display.set_caption('Nuriksfy')
font = pygame.font.SysFont(None, 24)
key_play = pygame.K_SPACE
key_stop = pygame.K_ESCAPE
key_next = pygame.K_RIGHT
key_prev = pygame.K_LEFT

labels = {
    key_play: "Play",
    key_stop: "Stop",
    key_next: "Next",
    key_prev: "Previous",
}

label_pos = {
    key_play: (50, 650),
    key_stop: (150,650),
    key_next: (250, 650),
    key_prev: (350, 650),
}
for key in label_pos:
    label_text = labels[key]
    label_surface = font.render(label_text, True, (255, 255, 255))
    label_rect = label_surface.get_rect(center=label_pos[key])
    screen.blit(label_surface, label_rect)
picture = pygame.transform.scale(picture, (500,500)) 
screen.blit(picture,(0,0))
pygame.mixer.music.play()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == key_play:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == key_stop:
                pygame.mixer.music.stop()
            elif event.key == key_next:
                current_music = (current_music + 1)%len(music_files)
                current_pic =(current_pic + 1)%len(pic_files)
                pygame.mixer.music.load(music_dir + music_files[current_music])
                picture = pygame.image.load(pictures_dir+pic_files[current_pic])
                picture = pygame.transform.scale(picture, (500,500)) 
                screen.blit(picture,(0,0))
                pygame.mixer.music.play()
                pygame.display.flip()
            elif event.key == key_prev:
                current_music = (current_music - 1)%len(music_files)
                current_pic = (current_pic + 1)%len(pic_files)
                pygame.mixer.music.load(music_dir + music_files[current_music])
                picture = pygame.image.load(pictures_dir+pic_files[current_pic])
                picture = pygame.transform.scale(picture, (500,500)) 
                screen.blit(picture,(0,0))
                pygame.mixer.music.play()
                pygame.display.flip()
                
             

    pygame.display.update()
   

    
   
    
   
    ##