from tkinter import *
from random import randint
from tkinter import messagebox

a = []

def generate_array():
    
    try:
        n = edit1.get()
        if not n:
            messagebox.showerror('Помилка', 'Розмірність масиву не вказана.')
            return

        n = int(n)
        if n <= 0:
            messagebox.showerror('Помилка', 'Розмірність масиву має бути додатним цілим числом.')
            return

        a.clear()  # Очищення масиву перед заповненням новими значеннями
        listbox1.delete(0, END) 
        label4['text'] = 'Сума = ' 

        for _ in range(n):
            a.append(randint(-50, 50))
            listbox1.insert(END, a[-1]) 

        count_positive_elements() 

    except ValueError:
        messagebox.showerror('Помилка вводу', 'Будь ласка, введіть дійсне ціле число для розмірності масиву.')

def sort_array_descending():
    """Сортує масив за спаданням за допомогою бульбашкового сортування."""
    if not a:
        messagebox.showwarning('Попередження', 'Будь ласка, спочатку згенеруйте масив.')
        return

    n = len(a)
    # Створюємо копію для сортування, щоб вихідний масив 'a' залишався незмінним
    # для розрахунку суми, якщо це необхідно.
    sorted_copy_of_a = a[:] # Створює поверхневу копію масиву для сортування

    # Бульбашкове сортування за спаданням
    for j in range(n - 1):
        for i in range(n - j - 1):
            if sorted_copy_of_a[i] < sorted_copy_of_a[i + 1]:
                sorted_copy_of_a[i + 1], sorted_copy_of_a[i] = sorted_copy_of_a[i], sorted_copy_of_a[i + 1]

    listbox2.delete(0, END)
    for element in sorted_copy_of_a:
        listbox2.insert(END, element)

def compute_sum():
    """Обчислює та відображає суму елементів масиву."""
    if not a:
        messagebox.showwarning('Попередження', 'Будь ласка, спочатку згенеруйте масив.')
        return
    s = sum(a)
    label4['text'] = 'Сума = ' + str(s)

def count_positive_elements():
    """Підраховує та відображає кількість додатних елементів у масиві."""
    if not a:
        messagebox.showwarning('Попередження', 'Будь ласка, спочатку згенеруйте масив.')
        return
    positive_count = sum(1 for x in a if x > 0)
    messagebox.showinfo('Додатні елементи', f'Кількість додатних елементів: {positive_count}')

def about_author():
    
    messagebox.showinfo('Про автора', 'Автор: Сичук Ангеліна Email: sychuk.angelina123@gmail.com')

def problem_statement():
    """Відображає умову задачі."""
    messagebox.showinfo('Умова задачі',
                        'Підрахувати кількість додатних елементів у даному одновимірному масиві.Виконати сортування елементів масиву за спаданням, використовуючи методекстремальних елементів')

# --- Функції для зміни теми ---
def set_light_theme():
   
    root['bg'] = 'lightgray'
    listbox1['bg'] = 'white'
    listbox2['bg'] = 'white'
    label1['bg'] = 'lightgray'
    label2['bg'] = 'lightgray'
    label3['bg'] = 'lightgray'
    label4['bg'] = 'lightgray'
    label1['fg'] = 'black'
    label2['fg'] = 'black'
    label3['fg'] = 'black'
    label4['fg'] = 'black'
    edit1['bg'] = 'white'


def set_dark_theme():
    
    root['bg'] = 'black'
    listbox1['bg'] = 'gray80'
    listbox2['bg'] = 'gray80'
    label1['bg'] = 'black'
    label2['bg'] = 'black'
    label3['bg'] = 'black'
    label4['bg'] = 'black'
    label1['fg'] = 'white'
    label2['fg'] = 'white'
    label3['fg'] = 'white'
    label4['fg'] = 'white'
    edit1['bg'] = 'gray80'

def set_default_theme():
    
    root['bg'] = '#F0F0F0'
    listbox1['bg'] = '#FFFFFF'
    listbox2['bg'] = '#FFFFFF'
    label1['bg'] = '#F0F0F0'
    label2['bg'] = '#F0F0F0'
    label3['bg'] = '#F0F0F0'
    label4['bg'] = '#F0F0F0'
    label1['fg'] = '#F0F0F0'
    label2['fg'] = '#F0F0F0'
    label3['fg'] = '#F0F0F0'
    label4['fg'] = '#F0F0F0'
    edit1['bg'] = '#FFFFFF'
   

x = y = 0
    
def do_popup(event):
    """Відображає контекстне меню при натисканні правої кнопки миші."""
    try:
        popupmenu.tk_popup(event.x_root, event.y_root)
    finally:
        popupmenu.grab_release()

root = Tk()
root.title('Масиви')
root.geometry('600x320') 

label1 = Label(text='Вихідний масив')
label2 = Label(text='Посортований масив')
label1.place(x=20, y=30)
label2.place(x=200, y=30)

listbox1 = Listbox(height=10, width=20)
listbox2 = Listbox(height=10, width=20)
listbox1.place(x=20, y=70)
listbox2.place(x=200, y=70)

label3 = Label(text='Кількість елементів масиву:')
label3.place(x=400, y=30)

edit1 = Entry()
edit1.place(x=400, y=70)

button1 = Button(text='Згенерувати', width=20, command=generate_array)
button1.place(x=400, y=100)

button2 = Button(text='Сортувати (спадання)', width=20, command=sort_array_descending)
button2.place(x=400, y=130)

button3 = Button(text='Обчислити суму', width=20, command=compute_sum)
button3.place(x=400, y=160)

label4 = Label(text='Сума =', font=("Arial", 10, "bold"))
label4.place(x=400, y=210)

# --- Головне меню ---
main_menu = Menu(root)
root.config(menu=main_menu)

# Підменю "Дії з масивом"
array_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Дії з масивом', menu=array_menu)
array_menu.add_command(label='Згенерувати', command=generate_array)
array_menu.add_command(label='Сортувати (спадання)', command=sort_array_descending)
array_menu.add_command(label='Обчислити суму', command=compute_sum)

# Підменю "Про програму"
about_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Про програму', menu=about_menu)
about_menu.add_command(label='Про автора', command=about_author)
about_menu.add_command(label='Умова задачі', command=problem_statement)

# --- Контекстне меню ---
popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label="Світлий", command=set_light_theme)
popupmenu.add_command(label="Темний", command=set_dark_theme)
popupmenu.add_command(label="Відновити початкові кольори", command=set_default_theme)
root.bind("<Button-3>", do_popup)

root.mainloop()