from tkinter import *
root1 = Tk( )
fram1 = Frame(root1)
Label(fram1,text='Please enter the text to
search:').pack(side=LEFT)
edit1 = Entry(fram1)
edit1.pack(side=LEFT, fill=BOTH, expand=1)
edit1.focus_set( )
button = Button(fram1, text='Search')
button.pack(side=RIGHT)
fram1.pack(side=TOP)
text1 = Text(root1)
text1.insert('1.0',
'''India is a beautiful nation
''')
text1.pack(side=BOTTOM)
def find( ):
 text1.tag_remove('found', '1.0', END)
 search1 = edit1.get( )
 if search1:
 id = '1.0'
 while 1:
     id = text1.search(search1, id, nocase=1,
                       stopindex=END)
     if not id: break
     lastid = '%s+%dc' % (id, len(search1))
     text1.tag_add('found', id, lastid)
     id = lastid
     text1.tag_config('found', foreground='red')
     edit1.focus_set()
     button.config(command=find)
     root1.mainloop()