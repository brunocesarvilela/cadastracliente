import customtkinter

janela = customtkinter.CTk()
janela.geometry("800x400")
janela.title("Sistema de Cadastro")
janela.resizable(width=False, height=False)
janela._set_appearance_mode("light")

frame1 = customtkinter.CTkFrame(janela,width=570,height=330).place(x=10,y=30)
frame2 = customtkinter.CTkFrame(janela,width=180,height=180).place(x=590,y=30)

labelnome = customtkinter.CTkLabel(janela,text="Nome: ")
labelnome.place(x=15,y=37)

textbox = customtkinter.CTkTextbox(janela,width=300,height=30,border_spacing=2)
textbox.place(x=65,y=35)
textbox.insert("0.0","Bruno César Vilela")

botao1 = customtkinter.CTkButton(frame1, text="Novo", corner_radius=10).place(x=615,y=40)

janela.mainloop()