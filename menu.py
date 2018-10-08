from appJar import gui
import sys

def geraStrMedNull(strengur):
    if strengur < 10:
        return "0"+str(strengur)
    else:
        return str(strengur)

skra = open("settings/exit.txt", "w")
skra.write("False")
skra.close()

padding_in_X = 250
padding_in_Y = 10

def valmynd():
    menu = gui("Skóla simulator", "600x800")
    menu.setBg("lightblue")
    # menu.setSize("fullscreen")

    def main_menu(button):
        if button == "Spila":
            skra = open("settings/settings.txt")
            settings = {}
            for line in skra:
                settings[line[0:3]] = line[6:8]
            skra.close()

                # lina = list(lina)
                # lina[6] = tala_str[0]
                # lina[7] = tala_str[1]
                # lina = "".join(lina)

            settings["FPS"] = geraStrMedNull(menu.getScale("fps-tala"))
            settings["LFS"] = geraStrMedNull(menu.getScale("likur-samskipti"))
            settings["LAS"] = geraStrMedNull(menu.getScale("likur-spjall"))

            skra = open("settings/settings.txt", "w")
            for setting in settings:
                skra.write(str(setting)+" = "+str(settings[setting])+"\n")
            skra.close()
            
            menu.stop()
            
        elif button == "Hætta":
            skra = open("settings/exit.txt", "w")
            skra.write("True")
            skra.close()

            menu.stop()
    
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

    # menu.startFrame("MENU_RIGHT", row=0, column=1)#MENU_RIGHT

    # menu.startFrame("prufu_slider_1")
    # menu.setInPadding(padding_in_X,padding_in_Y)
    # menu.setSticky("s")
    # menu.addLabel("Prufu renna 1")
    # menu.setSticky("n")
    # menu.addScale("prufu_slider_1")
    # menu.showScaleValue("prufu_slider_1", show=True)
    # menu.stopFrame()

    # menu.stopFrame()#/MENU_RIGHT

    # menu.startFrame("MENU_RIGHT2", row=0, column=2)#MENU_RIGHT

    # menu.stopFrame()#/MENU_RIGHT

    menu.go()







