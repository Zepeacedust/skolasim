import pygame, humans, sys, menu
from random import randint

scan_delay = 300
coll_delay = 300
move_delay = 300

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

school = pygame.display.set_mode((800, 800))
school.fill((255,255,255))
while 1:#gameplay loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    target =randint(0,len(student_list) - 1)
    school.fill((255, 255, 255))
    for student in student_list:
        school.blit(student.image,student.rect)
        if scan_delay >= 10:
            student.scan_surroundings(student_list)
        if move_delay >= 10:
            student.move(student.moveto(student.find_friend()))
        else:
            student.move(student.move_angle)
        student.check_collide(student_list)
    if scan_delay >= 10:
        scan_delay = 0
    else:
        scan_delay += 1
    if move_delay >= 10:
        move_delay = 0
    else:
        move_delay += 1
    if coll_delay >= 1:
        coll_delay = 0
    else:
        coll_delay += 1
    pygame.display.flip()
    pygame.time.Clock().tick(fps)
