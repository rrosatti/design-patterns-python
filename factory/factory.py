class Button(object):
    html = ''
    def getHtml(self):
        return self.html

class Image(Button):
    html = '<img></img>'

class Input(Button):
    html = '<input></input>'

class Flash(Button):
    html = '<obj></obj>'

class ButtonFactory():
    def createButton(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()

button_obj = ButtonFactory()
buttons = ['image', 'input', 'flash']
for b in buttons:
    print button_obj.createButton(b).getHtml()
