from tkinter import *

class Todolist:
    def __init__(self,root):
        self.root = root
        self.root.title("To-Do-List")
        self.root.geometry("650x450+300+150")
        self.root.configure(bg="black")

        self.label1 = Label(self.root,text="TO-DO LIST",font=("Calibri light",15,"bold"),width=8,bd=5,bg="black",fg="red")
        self.label1.pack(side="top", fill=BOTH)

        self.label2 = Label(self.root, text="Enter the task:", font=("Montserrat", 15, "bold"), width=10, bd=10,
                            bg="black", fg="red")
        self.label2.place(x=20, y=80)

        self.label3= Label(self.root, text="Tasks", font=("calibri", 15 ,"bold"), width=10, bd=10,
                            bg="black", fg="red")
        self.label3.place(x=350, y=70)

        self.text = Text(self.root, height=2, bd=5, width=23, font="ariel 12",bg="red", fg= "black")
        self.text.place(x=20, y=120)

        self.main_text = Listbox(self.root, height=10, bd=5, width=27, font="ariel 18",bg="red", fg= "black")
        self.main_text.place(x=260, y=120)

        try:
            with open("todo.txt", "r") as f:
                readLine = f.readlines()
                for i in readLine:
                    self.main_text.insert(END,i)
        except FileNotFoundError:
            with open("todo.txt", "w") as f:
                pass

        def addTask():
            item = ""
            item = self.text.get(1.0, END)
            if item.strip():
                self.main_text.insert(END, item)
                with open("todo.txt","a") as f:
                    f.write(item)
                self.text.delete(1.0, END)

        def deleteTask():
            item_to_delete= self.main_text.curselection()
            selected_item = self.main_text.get(item_to_delete)
            with open("todo.txt","r") as f:
                list_of_tasks = f.readlines()
            with open("todo.txt","w") as f:
                for item in list_of_tasks:
                    if item.strip() != selected_item[0].strip():
                        f.write(item)
            self.main_text.delete(item_to_delete)

        def deleteAllTasks():
            self.main_text.delete(0 , END)
            open("todo.txt", "w").close()

        def exitApp():
            root.destroy()

        self.button1 = Button(self.root, text="Add Task", font= "calibri 12 bold",width= 14, bd=3,bg="red",fg="black",command=addTask)
        self.button1.place(x=50,y=210)

        self.button2 = Button(self.root, text="Delete Task", font="calibri 12 bold", width=14, bd=3, bg="red", fg="black",
                              command=deleteTask)
        self.button2.place(x=50,y=267)

        self.button3 = Button(self.root, text="Delete All Task", font="calibri 12 bold", width=14, bd=3, bg="red", fg="black",
                              command=deleteAllTasks)
        self.button3.place(x=50, y=324)

        self.button4 = Button(self.root, text="Exit", font="calibri 12 bold", width=14, bd=3, bg="red", fg="black",
                              command=exitApp)
        self.button4.place(x=50,y=381)

if __name__== "__main__":
    root = Tk()
    obj= Todolist(root)
    root.mainloop()




