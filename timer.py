from tkinter import *
import myModule4
import myModule3
import timeit
import math
import threading


def cpp_simple():
    iteration = textentry.get()
    time3 = myModule3.boucle(int(iteration))
    output.delete(0.0, END)
    output.insert(END, time3)


def cpp_thread():
    iteration = textentry.get()
    time4 = myModule4.boucle(int(iteration))
    output.delete(0.0, END)
    output.insert(END, time4)


def python_thread(debut, fin):
    a = []
    for i in range(int(debut), int(fin)):
        a.append(math.tanh(i))
    return a


def python_simple():
    iteration = textentry.get()
    liste = []
    start = timeit.default_timer()
    for i in range(0, int(iteration)):
        liste.append(math.tanh(i))
    stop = timeit.default_timer()
    time1 = stop - start
    output.delete(0.0, END)
    output.insert(END, time1)


def python_threads():
    iteration = textentry.get()
    start = timeit.default_timer()
    
    t1 = threading.Thread(target = python_thread, args = (0, int(iteration)/4))
    t2 = threading.Thread(target = python_thread, args = (0, int(iteration)/4))
    t3 = threading.Thread(target = python_thread, args = (0, int(iteration)/4))
    t4 = threading.Thread(target = python_thread, args = (0, int(iteration)/4))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    
    stop = timeit.default_timer()
    time2 = stop - start
    output.delete(0.0, END)
    output.insert(END, time2)



window = Tk()
window.title("Calcul du temps d'exécution")
window.configure(background="black")

Label (window, text="Entrez le nombre d'iterations à faire (doit être un nombre entier):", bg="black", fg="white", font="none 11 italic") .grid(row=0, column=0, sticky=W)
Label (window, text="", bg="black", fg="white", font="none 11 italic") .grid(row=1, column=1, sticky=E)
Label (window, text="", bg="black", fg="white", font="none 11 italic") .grid(row=2, column=1, sticky=E)
Label (window, text="", bg="black", fg="white", font="none 11 italic") .grid(row=3, column=1, sticky=E)
Label (window, text="Choisissez le type de boucle:", bg="black", fg="white", font="none 11 italic") .grid(row=4, column=1, sticky=E)
Label (window, text="Le temps d'exécution:", bg="black", fg="white", font="none 11 italic") .grid(row=5, column=0, sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=0, column=1, sticky=W)

Button(window, text="Boucle simple en langage compilé", command=cpp_simple) .grid(row=4, column=2)
Button(window, text="Boucle 4 threads en langage compilé", command=cpp_thread) .grid(row=5, column=2)
Button(window, text="Boucle simple en langage interprété", command=python_simple) .grid(row=6, column=2)
Button(window, text="Boucle 4 threads en langage interprété", command=python_threads) .grid(row=7, column=2)
output = Text(window, width=30, height=1, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=1, sticky=E)

window.mainloop()
