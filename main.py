from menu import valmynd
import humans

valmynd()

x = humans.student()
y = humans.student()
x.connect(y, 200)
print(x.connections)
print(y.connections)