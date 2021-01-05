from tkinter import *
from tkinter import filedialog
from tkinter import messagebox 
from Crypto import Random
from Crypto.Cipher import AES
import os
from pathlib import Path
from PIL import ImageTk, Image
import tkinter.font as tkFont

root= Tk()
root.title("Encryption & Decryption")
root.geometry("400x390")

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc" , 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)
        

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')


def showimg():
    window3 = Toplevel(window2)
    window3.title("Decrypted Image")
    im = Image.open(filename[:-4])
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(window3,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window3.mainloop()

def encrypt():
    password=pass1.get(1.0,END)
    f = open(s+r"\data.txt", "w+")
    f.write(password)
    f.close()
    enc.encrypt_file(s+r"\data.txt")
    enc.encrypt_file(filename)
    messagebox.showinfo("Success!", "Image encrypted successfully...")
    window1.destroy()
    sys.exit()

def decrypt():
    password2=pass2.get(1.0,END)
    enc.decrypt_file(s+r"\data.txt.enc")
    p = ''
    with open(s+r"\data.txt", "r") as f:
        p = f.readlines()
    if p[0] == password2:
        enc.encrypt_file(s+r"\data.txt")
        enc.decrypt_file(filename)
        messagebox.showinfo("Success!", "Image successfully decrypted!")
        print("Decryption done!")
        btn = Button(window2, text="Show File", width=14, height=2, command=showimg)
        btn.place(x= 163, y= 280)
    elif pass2.compare("end-1c", "==", "1.0"):
        enc.encrypt_file(s+r"\data.txt")
        messagebox.showwarning("Warning!", "Please enter password before proceed!")
    else:
        enc.encrypt_file(s+r"\data.txt")
        messagebox.showerror("Password Mismatched", "You've entered an incorrect password!")


def choosefile1():
    global filename,s
    file1= filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg')])
    if file1 is not None:
        filename= file1.name
        p = Path(filename)
        Label(window1, text = p.name, bg='#111111', fg='white' ).place(x=140,y=155)
        s= str(p.parent)

def choosefile2():
    global filename,s
    file1= filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg.enc')])
    if file1 is not None:
        filename= file1.name
        p = Path(filename)
        Label(window2, text = p.name, bg='#000', fg='#fff').place(x=140,y=75)
        s= str(p.parent)

def openEncrypt():
    global window1
    global pass1
    window1 = Toplevel(root)
    root.withdraw()
    window1.title("Encryption")
    window1.geometry("450x350")
    canv = Canvas(window1, width=445, height=345, bg='#111111')
    canv.grid(row=2, column=3)
    fontStyle = tkFont.Font(family="Lucida Grande", size=11)
    label_pass = Label(window1, text = "Create Password", bg='#111111', fg='white', font=fontStyle)
    label_pass.place(x = 75, y = 60)
    pass1= Text(window1, height=1, width=18)
    pass1.place(x=200,y=60)
    encryptbtn = Button(window1, text="Choose File to Encrypt", width=18, height=1, command=choosefile1)
    encryptbtn.place(x= 145, y= 130)
    btn = Button(window1, text="Encrypt", width=14, height=2, command=encrypt)
    btn.place(x= 160, y= 220)
    window1.mainloop()

def openDecrypt():
    global window2
    global pass2
    window2= Toplevel(root)
    root.withdraw()
    window2.title("Decryption")
    window2.geometry("450x370")
    canv = Canvas(window2, width=445, height=365, bg='#000')
    canv.grid(row=2, column=3)
    fontStyle = tkFont.Font(family="Lucida Grande", size=11)
    decryptbtn = Button(window2, text="Choose File to Decrypt", width=18, height=1, command=choosefile2)
    decryptbtn.place(x= 150, y= 50)
    label_pass = Label(window2, text = "Enter Password", bg='#000', fg='#fff', font=fontStyle)
    label_pass.place(x = 75, y = 130)
    pass2= Text(window2, height=1, width=18)
    pass2.place(x=195,y=130)
    btn = Button(window2, text="Decrypt", width=14, height=2, command=decrypt)
    btn.place(x= 163, y= 220)
    window2.mainloop()

clear()
print("Working on files...")
img=Image.open("bg/encry1.jpg")
img = img.resize((395, 385))
bg = ImageTk.PhotoImage(img)  
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 
btn1 = Button(root, text="Encrypt", width=14, height=2, command=openEncrypt)
btn1.place(x= 150, y= 127)
btn2 = Button(root, text="Decrypt", width=14, height=2, command=openDecrypt)
btn2.place(x= 150, y= 225)


root.mainloop()

