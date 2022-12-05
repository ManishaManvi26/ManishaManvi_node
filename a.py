from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
from tkinter import ttk
import random
from collections import Counter


# functions
#### this function is to open a file
def openFile():
    
    txtarea.delete("1.0",END)
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)
    file_cont = tf.read()
    ### the data in the file will be displayed in the text area
    txtarea.insert(END, file_cont)
    
    path=pathh.get()
    print(path)
    
    tf.close()


#### defination for dispalying all numbers and get count and average of numbers
def Total_Average_Numebers():
    txtarea.delete("1.0",END)
    list_data=[]
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf1 = open(tf)
    file_cont = tf1.read()
    txtarea.insert(END, file_cont)

    #### open the file and append to the list and get count and average
    with open(tf) as fa:
        lines = fa.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                list_data.append(int(word))
         
        
        count=0
        #### gets the count and average of the list data
        for ld in list_data:
            count += ld
            avg = count/len(list_data)
            avg = round(avg, 2)
        print(count,avg)
    
    txtarea.insert(END,' ' +'\n')
    txtarea.insert(END,' ' +'\n')
    txtarea.insert(END, 'Total count of dispalyed numbers : ' + str(count) + '\n')
    txtarea.insert(END,'Average of the dispalyed numbers :  ' + str(avg))
    print("-----")

    #### create a window to print the avearge and count of the numbers in the text file
    top= Toplevel(ws)
    top.geometry("700x150")
    top.title("Count and Average Number In the File")
    text = " Average of the dispalyed numbers :  " + str(avg) + "\n" +   "Total count of dispalyed numbers : " + str(count)
    Label(top, text= text , font=('Mistral 18 bold')).place(x=40,y=30)


### def for SortNumber where we will sort the numbers in file
def SortNumber():
    txtarea.delete("1.0",END)
    f = open("avg.txt", "r+")
    numbers = sorted(list(map(int, f.readlines())))
    print(numbers)
    for i in numbers:
        txtarea.insert(END, str(i) + '\n')
    print("sort numbers")


### def to search the number of types the entered number occured
def SearchNumber():

    result_file=txtarea.get("1.0","end")
    result_file_list=list(result_file)
    print(result_file_list)

    #### input from the entered textarea
    inp = txtarea1.get(1.0, "end-1c")
    print(inp)

    result_file_list.count(inp)
    print(result_file_list.count(inp))

    top= Toplevel(ws)
    top.geometry("750x250")
    top.title("Serached Number Occurance")
    Label(top, text= "The Searched Number   " + str(inp) + "   occured  in the file is :   " + str(result_file_list.count(inp)) , font=('Mistral 18 bold')).place(x=40,y=30)




    

### def for Encrypt and DecryptFile
def EncryptDecryptFile():
    txtarea.delete("1.0",END)

    txtarea.delete("1.0",END)
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf1 = open(tf)
    file_cont = tf1.read()
    
    txtarea.insert(END, file_cont)

    path=pathh.get()
    #### genearte the key to encryt the 
    key = Fernet.generate_key()
    with open('file_key.key', 'wb') as filekey:
        filekey.write(key)
        fernet = Fernet(key)
    with open(tf, 'rb') as f:
        file = f.read()
        ### Here the file will be encrypted with the file_key.key
    encrypt_file = fernet.encrypt(file)
    with open(tf, 'wb') as encrypted_file:
        encrypted_file.write(encrypt_file)
        
    print('File is encrypted')
    
    tf = open(tf)
    file_cont = tf.read()
    print(file_cont,"-------")
    
    txtarea.insert(END, file_cont)
    
    txtarea.delete("1.0",END)

##def DeEncryptFile():
##    txtarea.delete("1.0",END)
    
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    
    
    top= Toplevel(ws)
    top.geometry("750x250")
    top.title("File Been Encrypted")
    Label(top, text= "Encrypted File :" + file_cont , font=('Mistral 18 bold')).place(x=40,y=120)
    
    ##### The file will be decrypted with same file_key
    with open('file_key.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(tf, 'rb') as f:
        file = f.read()
    decrypt_file = fernet.decrypt(file)
    with open(tf, 'wb') as decrypted_file:
        decrypted_file.write(decrypt_file)
    print('File is decrypted')

    tf1 = open(tf)
    file_cont = tf1.read()
    txtarea.insert(END, file_cont)
    print(file_cont)
    

### def to get LargestNumber and displayed on the popup message  
def LargestNumber():
    txtarea.delete("1.0",END)
    
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    print(tf)
    tf1 = open(tf)
    myList = []
    for line in tf1:
       myList.append(line)
    print(myList)
    ### convert the numbers in the text file to the list to find the largest number
    lst = []
    for i in myList:
        i = i[:-1]
        lst.append(int(i))
    print(lst)
    top= Toplevel(ws)
    top.geometry("750x250")
    top.title("Largest Number")
    Label(top, text= "The Largest Number in the file is :" + str(lst[-1]) , font=('Mistral 18 bold')).place(x=40,y=30)


### def to get AppendNumber and displayed on the popup message   
def AppendNumber():
    txtarea.delete("1.0",END)
    result_file=txtarea.get("1.0","end")
    result_file_list=list(result_file)
    
    print(result_file_list)
    
    valueToBeRemoved = '\n'
     
    try:
        while True:
            result_file_list.remove(valueToBeRemoved)
    except ValueError:
        pass

    ### convert the list of numbers in file to the list and append the number to the text file
    print(result_file_list)        
    result_file_list.append(random.randrange(1, 101, 2))
    print (result_file_list)
    txtarea.delete("1.0","end")
    txtarea.insert(END, result_file_list)
    top= Toplevel(ws)
    top.geometry("700x150")
    top.title("APPENDED NUMBER TO FILE")
    Label(top, text= "The random Number that been appended is :" + str(result_file_list[-1]) , font=('Mistral 18 bold')).place(x=40,y=30)
    
    
    
#### we will define the tk frame here    
ws = Tk()
ws.title("UNH Scripting w/Python")
##ws.label("Manisha")

#### This is for window geometry and the background colour
ws.geometry("800x600")
ws['bg']='#2a636e'




# adding frame
frame = Frame(ws)
frame.pack(pady=80)

## adding a frame for serach tet box
frame1 = Frame(ws)
frame1.pack(pady=5,expand = True)

### text box to search the numberfrom the given list
txtarea1 = Text(frame1, width=8, height=3)
txtarea1.pack(padx=0,pady=5)

# adding scrollbars 
ver_sb = Scrollbar(frame, orient=VERTICAL)
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

# adding writing space
txtarea = Text(frame, width=40, height=20)#### to read data from the file
txtarea.pack(fill=X, padx=0,pady=5)

# binding scrollbar with text area
txtarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=txtarea.yview)

txtarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=txtarea.xview)

# adding path showing box
pathh = Entry(ws)
pathh.pack(expand=True, fill=X, padx=0,pady=5)




#### Add the buttons and pass the commands for which buttons the functions should trigger
#### Here will give the name on the button and pass the function names and place to give the position of the buttons

##Label1 = Label(ws,text = "UNH Scripting w/Python").place(x = 280,y = 20)

##photo = Tk.PhotoImage(file='images.png')
##image_label = ttk.Label(
##    ws,
##    image=photo,
##    compound='top'
##)
##image_label.place(x = 20,y = 20)

label1 = ttk.Label(
    ws,
    text='         UNH Scripting w/Python          ',
    font=("Arial Bold", 16))

label1.place(x = 280,y = 20)



Button(ws, text=" 1. openFile", command=openFile,width=14).place(x=30, y=70)

Button(ws, text=" 2. Total/Average", command=Total_Average_Numebers,width=14).place(x=30, y=110)

Button(ws, text=" 3. SearchNumber", command=SearchNumber,width=14).place(x=30, y=150)

Button(ws, text=" 4. SortNumber", command=SortNumber,width=14).place(x=30, y=190)

Button(ws, text=" 5. EncryptFile/DecryptFile", command=EncryptDecryptFile,width=14).place(x=30, y=230)

Button(ws, text=" 6.LargestNumber", command=LargestNumber,width=14).place(x=30, y=270)

Button(ws, text=" 7. AppendNumber", command=AppendNumber,width=14).place(x=30, y=310)

Button(ws, text=" 8. EXIT", command=lambda:ws.destroy(),width=14).place(x=30, y=350)

Search_Label = Label(ws, text = "Enter Number To Search and Press 4.SERACH BUTTON").place(x = 20,y = 490)

 

#### this is the mainloop of the  disaplayed window
ws.mainloop()
