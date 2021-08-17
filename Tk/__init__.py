from tkinter import *

def horario():
    print()

def anti():
    print()


def stop():
   while horario() is True:
    break

janela = Tk()
janela.title("CONTROLE DE COMANDO DO MOTOR")
janela.geometry("350x60")
frame = Frame(master=janela)
frame.pack()
btacende = Button(master=frame, text="HORARIO", command=horario)
btacende.grid(row=0, column=0)

btapaga = Button(master=frame, text="ANTI-HORARIO", command=anti)
btapaga.grid(row=0, column=1)

btstop = Button(master=frame, text="STOP", command=stop)
btstop.grid(row=0, column=2)

janela.mainloop()
