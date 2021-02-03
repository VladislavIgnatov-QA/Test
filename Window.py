import tkinter as tk
import tkinter.filedialog as fd

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text = tk.Text(self, height=10, width=50)
        self.btn_save = tk.Button(self, text="Сохранить", command=self.save_file)
        btn_file = tk.Button(self, text="Выбрать файл",
                             command=self.choose_file)
        btn_create = tk.Button(self, text="Создать файл",
                             command=self.create_file)
        self.text.pack()
        btn_file.pack(padx=60, pady=10)
        btn_create.pack(padx=60, pady=10)
        self.btn_save.pack(pady=10, ipadx=5)

    def save_file(self):
        contents = self.text.get(1.0, tk.END)
        new_file = fd.asksaveasfile(title="Сохранить файл", defaultextension=".txt",
                                    filetypes=(("Текстовый файл", "*.txt"),))
        if new_file:
            new_file.write(contents)
            new_file.close()

    def choose_file(self):
        filetypes = (("Текстовый файл", "*.txt"),
                     ("Изображение", "*.jpg *.gif *.png"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            print(filename)

    def create_file(self):
        contents = self.text.get(1.0, tk.END)
        new_file = fd.asksaveasfilename (title="Создать файл", defaultextension=".txt",
                                    filetypes=(("Текстовый файл", "*.txt"),))
        if new_file:
            new_file.write(contents)
            new_file.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()