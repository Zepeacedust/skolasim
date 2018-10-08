import pygame, humans, sys, menu
from random import randint

menu.valmynd()
skra = open("settings/exit.txt", "r")
for line in skra:
    if line == "True":
        sys.exit()
skra.close()
settings = (open("settings/settings.txt", "r").read()).split()

fps = int(settings[2])


pygame.init()
student_list = []
for stud_num in range(200):
    student_list.append(humans.student(randint(0,800), randint(0,800), randint(1,10), stud_num))

# student_list[1].image = pygame.image.load("./sprites/import.JPEG")

school = pygame.display.set_mode((800, 800))
school.fill((255,255,255))
while 1:#gameplay loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    target =randint(0,len(student_list) - 1)
    school.fill((255, 255, 255))
    for student in student_list:
        school.blit(student.image,student.rect)
        student.scan_surroundings(student_list)
        student.move(student.moveto(student.find_friend()))
        student.check_collide(student_list)
    pygame.display.flip()
    pygame.time.Clock().tick(fps)