import tkinter as tk

# Создаем главное окно
root = tk.Tk()

# Задаем размеры окна
root.geometry("500x200")

# Создаем метку для вывода информации о состоянии карьеры
status_label = tk.Label(root, text="Вы на самом дне карьерной лестницы", font=("Arial", 14))
status_label.pack()

# Создаем функцию для обновления информации о состоянии карьеры
def update_status():
    # Здесь можно добавить логику обновления информации о состоянии карьеры
    status_label.configure(text="Вы стали домохозяйкой", fg="orange")
update_button = tk.Button(root, text="Выйти замуж за бедного, но молодого", command=update_status, fg='blue')
update_button.pack()

def updte_status():
    # Здесь можно добавить логику обновления информации о состоянии карьеры
    status_label.configure(text="Ваш муж умер и оставил вам все свое наследство", fg="purple" )

# Создаем кнопку для обновления информации
update_button = tk.Button(root, text="Выйти замуж за богатого, но старого", command=updte_status, fg='green')
update_button.pack()



# Запускаем главный цикл обработки событий
root.mainloop()