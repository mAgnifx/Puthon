import customtkinter as ctk

def todo():
    todoz = entry.get()
    label = ctk.CTkLabel(scroll, text=todoz)
    label.pack()
    entry.delete(0,ctk.END)




root = ctk.CTk()
root.geometry("700x850")
root.title('My Todo App')
ctk.set_appearance_mode("dark") 

#text 1
title = ctk.CTkLabel(root,text='Your tasks', font=ctk.CTkFont(size=30,weight='bold'))
title.pack(padx=10,pady=(40,20))

#sroll
scroll = ctk.CTkScrollableFrame(root, width=500,height=500)
scroll.pack()

#button
buton =  ctk.CTkButton(root,width=500,text='Add',command=todo)
buton.pack(pady=20)



#entry

entry = ctk.CTkEntry(scroll,placeholder_text="Add tasks")
entry.pack(fill='x')






root.mainloop()