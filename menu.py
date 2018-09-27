from appJar import gui

def valmynd():
    menu = gui("Skóla simulator", "800x500")
    menu.setBg("lightblue")
    menu.setFont(18)

    def main_menu(button):
        if button == "Spila":
            fps = menu.getScale("fps-tala")
            print(fps)
            
        elif button == "Hætta": menu.stop()

    menu.setSticky("nwe")
    menu.addLabel("title", "Skóla simulator")
    
    menu.startFrame("MENU")#MENU
    menu.addButton("Spila", main_menu, 0, 0, 2)

    row = menu.getRow() # get current row
    menu.addLabel("fps-text", "Rammar á sekúndu", 1, 0)
    menu.addScale("fps-tala", 1, 1)
    menu.showScaleValue("fps-tala", show=True)

    menu.addButton("Hætta", main_menu, 2, 0, 2)
    
    menu.stopFrame()#/MENU

    menu.go()







