from tkinter import *
#import pickle

checkpoint = []

#Recupera los datos guardados en el formulario
def send_data():
  username_info = username.get()
  password_info = password.get()
  fullname_info = fullname.get()
  age_info = str(age.get())

  #Se imprimen en la consola
  print(username_info,"\t", password_info,"\t", fullname_info,"\t", age_info)
  
  #Se escriben los datos en un txt
  file = open("formulario.txt", "a")
  file.write(username_info)
  file.write("\t")
  file.write(password_info)
  file.write("\t")
  file.write(fullname_info)
  file.write("\t")
  file.write(age_info)
  file.write("\t\n")
  file.close()
  print("Nuevo usuario registrado. Username: {} | FullName: {}   ".format(username_info, fullname_info))

  #Se limpian los campos
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  fullname_entry.delete(0, END)
  age_entry.delete(0, END)


#Formulario con Class Tk()  
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Formulario")
mywindow.resizable(False,False)
mywindow.config(background = "#49A")
main_title = Label(text = "Formulario de registro", font = ("Cambria", 14), bg = "#0059b3", fg = "black", width = "500", height = "2")
main_title.pack()

#Se crean los labels
username_label = Label(text = "Nombre de usuario", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Contraseña", bg = "#FFEEDD")
password_label.place(x = 22, y = 130)
fullname_label = Label(text = "Nombre completo", bg = "#FFEEDD")
fullname_label.place(x = 22, y = 190)
age_label = Label(text = "Edad", bg = "#FFEEDD")
age_label.place(x = 22, y = 250)
 
#Variables que almacenan los datos introducidos por el usuario
username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()

#Se asocian los label con las variables
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*") #Se oculta la contraseña
fullname_entry = Entry(textvariable = fullname, width = "40")
age_entry = Entry(textvariable = age, width = "40")

#Se posicionan los campos en la interfaz
username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)
fullname_entry.place(x = 22, y = 220)
age_entry.place(x = 22, y = 280)
 
#Boton
submit_btn = Button(mywindow,text = "Registrar", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)

#Al cerrar la ventana
def handler():
    print("Saliendo")
    #pickle_file = file('checkpoint.pickle', 'w')
    #pickle.dump(checkpoint, pickle_file)
    mywindow.quit()

mywindow.protocol("WM_DELETE_WINDOW", handler)

mywindow.mainloop()