import customtkinter
janela = customtkinter.CTk()

janela.geometry("800x400")
janela.title("Sistema de Cadastro")
janela.resizable(width=False, height=False)
janela._set_appearance_mode("light")

def novatela():
    novajanela = customtkinter.CTkToplevel(janela,fg_color="teal")
    novajanela.geometry("500x260")
    novajanela.attributes("-topmost", True)

btn_novatela = customtkinter.CTkButton(master=janela, text="Abrir nova janela",command=novatela).place(x=300,y=100)

janela.mainloop()