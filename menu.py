from appJar import gui

padding_in_X = 250
padding_in_Y = 10

def valmynd():
    menu = gui("Skóla simulator", "1600x800")
    menu.setBg("lightblue")
    menu.setSize("fullscreen")

    def main_menu(button):
        if button == "Spila":
            fps = menu.getScale("fps-tala")
            print(fps)
            
        elif button == "Hætta": menu.stop()
    
    menu.setInPadding(padding_in_X,padding_in_Y)
    menu.setSticky("")
    menu.startFrame("MENU_LEFT", row=0, column=0)#MENU_LEFT
    menu.startFrame("UPPI_1")#UPPI_1
    menu.setInPadding(padding_in_X,padding_in_Y)

    menu.setSticky("")
    menu.addLabel("title", "Skóla simulator")

    menu.setSticky("s")
    menu.addButton("Spila", main_menu)
    menu.stopFrame()#/UPPI_1

    menu.startFrame("NIDRI_1")#NIDRI_1
    menu.setInPadding(padding_in_X,padding_in_Y)

    menu.startFrame("rammar_a_sekundu")
    menu.setInPadding(padding_in_X,padding_in_Y)
    menu.setSticky("s")
    menu.addLabel("fps-text", "Rammar á sekúndu")
    menu.setSticky("n")
    menu.addScale("fps-tala")
    menu.showScaleValue("fps-tala", show=True)
    menu.stopFrame()

    menu.startFrame("likur_a_samskiptum")
    menu.setInPadding(padding_in_X,padding_in_Y)
    menu.setSticky("s")
    menu.addLabel("Líkur á fyrstu samskiptum")
    menu.setSticky("n")
    menu.addScale("likur-samskipti")
    menu.showScaleValue("likur-samskipti", show=True)
    menu.stopFrame()

    menu.startFrame("likur_a_spjalli")
    menu.setInPadding(padding_in_X,padding_in_Y)
    menu.setSticky("s")
    menu.addLabel("Líkur á spjalli")
    menu.setSticky("n")
    menu.addScale("likur-spjall")
    menu.showScaleValue("likur-spjall", show=True)
    menu.stopFrame()

    menu.setSticky("")
    menu.addButton("Hætta", main_menu)
    
    menu.stopFrame()#/NIDRI_1
    menu.stopFrame()#/MENU_LEFT

    menu.startFrame("MENU_RIGHT", row=0, column=1)#MENU_RIGHT

    menu.startFrame("prufu_slider_1")
    menu.setInPadding(padding_in_X,padding_in_Y)
    menu.setSticky("s")
    menu.addLabel("Prufu renna 1")
    menu.setSticky("n")
    menu.addScale("prufu_slider_1")
    menu.showScaleValue("prufu_slider_1", show=True)
    menu.stopFrame()

    menu.stopFrame()#/MENU_RIGHT

    menu.startFrame("MENU_RIGHT2", row=0, column=2)#MENU_RIGHT

    menu.stopFrame()#/MENU_RIGHT

    menu.go()







