from tkinter import *
from connect import requestquery

#janela do aplicato
root = Tk()
#Cores do aplicativo
colorbg = '#816b48'
colorbt = '#cfe2f3'
color_frame_title = '#EEE9DC'

def rastreio():
    root.destroy()
    tracking_app = Tk()
    tracking_app.geometry("300x300")
    tracking_app.title('InterExpress')
    tracking_app.configure(bg=colorbg)

    tracking_title = Label(text='Rastreamento de Entrega', bg=colorbg)
    tracking_title.place(x=50, y=10)



def solicitar():
    def request():
        cep = cep_input.get()
        product = product_input.get()
        requestquery(cep, product)
    root.destroy()
    request_app = Tk()
    request_app.geometry("300x300")
    request_app.title('InterExpress')
    request_app.configure(bg=colorbg)

    request_title = Label(text='Solicite sua Entrega', bg=colorbg)
    request_title.place(x=50, y=10)

    cep_title = Label(text='CEP:', bg=colorbg)
    cep_title.place(x=30, y=40)

    cep_input = Entry(border=0)
    cep_input.place(x=60, y=40)

    product = Label(text='Produto:', bg=colorbg)
    product.place(x=30, y=70)

    product_input = Entry(border=0)
    product_input.place(x=82, y=70)

    confirm_button = Button(text="Confirmar", command=request, border=0)
    confirm_button.place(x=50, y=100)



root.title('InterExpress')
root.configure(bg=colorbg)

title_frame = Frame(root, bg=color_frame_title)
title_frame.place(y=10, width=200, height=50)

title_app = Label(title_frame, text='InterExpress', bg=color_frame_title, font=5)
title_app.place(x=50, y=10)

request_button_app = Button(text='Solicitar Entrega', command=solicitar, bg=colorbt, border=0)
request_button_app.place(x=50, y=80, width=100)

tracking_button_app = Button(text='Rastreamento', command=rastreio, bg=colorbt, border=0)
tracking_button_app.place(x=50, y=120, width=100)


root.geometry("200x250")
root.mainloop()