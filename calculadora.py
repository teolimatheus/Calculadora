from tkinter import *
from tkinter import ttk


cor1 ="#080600" #preto
cor2 ="#ffffff" #branco
cor3 ="#803738" #vermelho
cor4 ="#7a807c" #cinza
cor5 ="#0e6782" #azul claro


janela = Tk()
janela.title("calculadora")
janela.geometry("250x250")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=250,height=50,bg=cor5)
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela,width=250,height=268)
frame_corpo.grid(row=1,column=0)

todos_valores=''

valor_texto=StringVar()

def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)

    
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado=eval(todos_valores)

    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores=''
    valor_texto.set ('')

app_label= Label(frame_tela,textvariable=valor_texto,width=25,height=3,padx=7,relief=FLAT, anchor="e",justify=RIGHT,font= ('Ivy 12'),bg=cor5,fg=cor2)
app_label.place(x=0,y=0)


b_1 = Button(frame_corpo,command=limpar_tela, text="C",width=20,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frame_corpo,command=lambda:entrar_valores('%'), text="%",width=5,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_2.place(x=150,y=0)
b_3 = Button(frame_corpo,command=lambda:entrar_valores('/'), text="/",width=7,height=2,bg=cor3,fg=cor2,relief=RAISED,overrelief=RIDGE)
b_3.place(x=195,y=0)

b_4 = Button(frame_corpo,command=lambda:entrar_valores('7'), text="7",width=8,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_4.place(x=0,y=40)
b_5 = Button(frame_corpo,command=lambda:entrar_valores('8'), text="8",width=8,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_5.place(x=60,y=40)
b_6 = Button(frame_corpo,command=lambda:entrar_valores('9'), text="9",width=9,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_6.place(x=125,y=40)

b_7 = Button(frame_corpo,command=lambda:entrar_valores('*'), text="*",width=7,height=2,bg=cor3,fg=cor2,relief=RAISED,overrelief=RIDGE)
b_7.place(x=195,y=40)

b_8 = Button(frame_corpo,command=lambda:entrar_valores('4'), text="4",width=8,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_8.place(x=0,y=80)
b_9 = Button(frame_corpo, command=lambda:entrar_valores('5'),text="5",width=8,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_9.place(x=60,y=80)
b_10 = Button(frame_corpo,command=lambda:entrar_valores('6'), text="6",width=9,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_10.place(x=125,y=80)

b_11 = Button(frame_corpo,command=lambda:entrar_valores('-'), text="-",width=7,height=2,bg=cor3,fg=cor2,relief=RAISED,overrelief=RIDGE)
b_11.place(x=195,y=80)

b_12 = Button(frame_corpo,command=lambda:entrar_valores('1'), text="1",width=9,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_12.place(x=0,y=120)
b_13 = Button(frame_corpo,command=lambda:entrar_valores('2'), text="2",width=8,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_13.place(x=60,y=120)
b_14 = Button(frame_corpo,command=lambda:entrar_valores('3'), text="3",width=9,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_14.place(x=125,y=120)

b_15 = Button(frame_corpo,command=lambda:entrar_valores('+'), text="+",width=7,height=2,bg=cor3,fg=cor2,relief=RAISED,overrelief=RIDGE)
b_15.place(x=195,y=120)

b_16 = Button(frame_corpo,command=lambda:entrar_valores('0'), text="0",width=18,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_16.place(x=0,y=160)
b_17 = Button(frame_corpo,command=lambda:entrar_valores('.'), text=".",width=9,height=2,bg=cor4,relief=RAISED,overrelief=RIDGE)
b_17.place(x=125,y=160)
b_18 = Button(frame_corpo,command=calcular, text="=",width=9,height=2,bg=cor3,fg=cor2,relief=RAISED,overrelief=RIDGE)
b_18.place(x=195,y=160)


janela.mainloop()
