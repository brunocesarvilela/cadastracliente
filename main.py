import customtkinter
janela = customtkinter.CTk()

janela.geometry("800x400")
janela.title("Sistema de Cadastro")
janela.resizable(width=False, height=False)
janela._set_appearance_mode("light")

frame1 = customtkinter.CTkFrame(janela,width=570,height=330).place(x=10,y=30)
frame2 = customtkinter.CTkFrame(janela,width=180,height=180).place(x=590,y=30)

janela.mainloop()