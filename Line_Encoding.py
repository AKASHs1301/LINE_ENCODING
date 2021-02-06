# ██╗░░░░░  ██╗  ███╗░░██╗  ███████╗              
# ██║░░░░░  ██║  ████╗░██║  ██╔════╝              
# ██║░░░░░  ██║  ██╔██╗██║  █████╗░░              
# ██║░░░░░  ██║  ██║╚████║  ██╔══╝░░              
# ███████╗  ██║  ██║░╚███║  ███████╗              
# ╚══════╝  ╚═╝  ╚═╝░░╚══╝  ╚══════╝              

# ███████╗  ███╗░░██╗  ░█████╗░  ░█████╗░  ██████╗░  ██╗  ███╗░░██╗  ░██████╗░
# ██╔════╝  ████╗░██║  ██╔══██╗  ██╔══██╗  ██╔══██╗  ██║  ████╗░██║  ██╔════╝░
# █████╗░░  ██╔██╗██║  ██║░░╚═╝  ██║░░██║  ██║░░██║  ██║  ██╔██╗██║  ██║░░██╗░
# ██╔══╝░░  ██║╚████║  ██║░░██╗  ██║░░██║  ██║░░██║  ██║  ██║╚████║  ██║░░╚██╗
# ███████╗  ██║░╚███║  ╚█████╔╝  ╚█████╔╝  ██████╔╝  ██║  ██║░╚███║  ╚██████╔╝
# ╚══════╝  ╚═╝░░╚══╝  ░╚════╝░  ░╚════╝░  ╚═════╝░  ╚═╝  ╚═╝░░╚══╝  ░╚═════╝░

# ░██████╗  ░█████╗░  ██╗░░██╗  ███████╗    ███╗░░░███╗  ███████╗  ░██████╗
# ██╔════╝  ██╔══██╗  ██║░░██║  ██╔════╝    ████╗░████║  ██╔════╝  ██╔════╝
# ╚█████╗░  ██║░░╚═╝  ███████║  █████╗░░    ██╔████╔██║  █████╗░░  ╚█████╗░
# ░╚═══██╗  ██║░░██╗  ██╔══██║  ██╔══╝░░    ██║╚██╔╝██║  ██╔══╝░░  ░╚═══██╗
# ██████╔╝  ╚█████╔╝  ██║░░██║  ███████╗    ██║░╚═╝░██║  ███████╗  ██████╔╝
# ╚═════╝░  ░╚════╝░  ╚═╝░░╚═╝  ╚══════╝    ╚═╝░░░░░╚═╝  ╚══════╝  ╚═════╝░

import matplotlib.pyplot as plt
import numpy as np
from tkinter import * 
from tkinter.font import Font
import tkinter as tk

__author__ = “Akash Sivakumar”
__copyright__ = “Copyright 2021, line_encoding_schemes”
__credits__ = [“Rajkumar”]
__version__ = “0.1.0”
__maintainer__ = “Akash Sivakumar”
__email__ = “akashiva1301@gmail.com”
__status__ = “Dev”

#Unipolar - NRZ
def Unipolar_NRZ():
    bit_stream = ['0']+list(input.get(1.0, tk.END+"-1c"))
    check=1
    for i in range(len(bit_stream)):
        if bit_stream[i] == '1' or bit_stream[i] == '0':
            continue
        else:
            print("Enter valid values")
            warning_display()
            check = 0
            break
    if check!=0 :
        print("--Unipolar NRZ-- ",bit_stream)
        x_axis = [x for x in range(len(bit_stream))]
        return bit_stream,x_axis;
        
def plot1():
    bit_stream,x_axis=Unipolar_NRZ() 
    plt.step(x_axis,bit_stream,'k',linewidth=2)
    plt.plot(x_axis,[0]*len(bit_stream),'b',linewidth=0.8)
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.title('Unipolar - NRZ')
    plt.xticks(np.arange(0,len(bit_stream),step=1))
    #plt.show()

#polar - NRZ - L
def polar_NRZ_L():
    bit_stream = ['0']+list(input.get(1.0, tk.END+"-1c"))
    check = 1
    for i in range(len(bit_stream)):
        if bit_stream[i] == '1' or bit_stream[i] == '0':
            if bit_stream[i] == '0':
                bit_stream[i] = 1
            else:
                bit_stream[i] = -1
        else:
            print("Enter valid values")
            warning_display()
            check = 0
            break
    if check!=0 :
        print("--Polar NRZ L--  ",bit_stream)
        x_axis = [x for x in range(len(bit_stream))]
        return bit_stream,x_axis;

def plot2():
    bit_stream,x_axis=polar_NRZ_L()
    plt.step(x_axis,bit_stream,'k',linewidth=2)
    plt.plot(x_axis,[0]*(len(bit_stream)),'b',linewidth=1.5)
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.title('Polar NRZ-L')
    plt.xticks(np.arange(0,len(bit_stream),step=1))
    plt.yticks(np.arange(-1,2,step=1))
    #plt.show()

#polar - NRZ - L
def polar_NRZ_I():
    bit_stream = ['0']+list(input.get(1.0, tk.END+"-1c"))
    previous = 1
    check = 1
    for i in range(len(bit_stream)):
        if bit_stream[i] == '1' or bit_stream[i] == '0':
            if bit_stream[i] == '0':
                bit_stream[i] = previous
            else :
                previous = 1-previous
                bit_stream[i] = previous
        else:
            print("Enter valid values")
            warning_display()
            check = 0
            break
    if check!=0 :
        print("--Polar NRZ I--  ",bit_stream)
        x_axis = [x for x in range(len(bit_stream))]
        return bit_stream,x_axis;

def plot3():
    bit_stream,x_axis=polar_NRZ_I()
    plt.step(x_axis,bit_stream,'k',linewidth=2)
    plt.plot(x_axis,[0]*len(bit_stream),'b',linewidth=0.8)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.title('Polar NRZ-I')
    plt.grid(True)
    plt.xticks(np.arange(0,len(bit_stream),step=1))
    plt.yticks(np.arange(0,2,step=1))
        #plt.show()

#polar - RZ
def polar_RZ():
    input_stream = list(input.get(1.0, tk.END+"-1c"))
    bit_stream = []
    check=1
    for i in range(len(input_stream)):
        if input_stream[i] == '1' or input_stream[i] == '0':
            if input_stream[i] == '0':
                bit_stream.extend(['-1','0'])
            else :
                bit_stream.extend(['1','0'])
        else:
            print("Enter valid values")
            warning_display()
            check=0
            break
    if check!=0 :    
        bit_stream=[bit_stream[0]]+bit_stream
        x_axis = [x for x in range(len(bit_stream))]
        print("--Polar RZ--   ",bit_stream)
        return bit_stream,x_axis;

def plot4():
    bit_stream,x_axis=polar_RZ()
    plt.step(x_axis,bit_stream,'k',linewidth=2)
    #plt.plot(x_axis,[0]*len(bit_stream),'b',linewidth=0.8)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.title('Polar RZ')
    plt.xticks(np.arange(0,len(bit_stream),step=2),np.arange(0,int(len(bit_stream)/2)+1,step=1))
    #plt.yticks([-1,0,1])

#Bipolar - pseudoternary
def Bipolar_pseudoternary():
    input_stream = list(input.get(1.0, tk.END+"-1c"))
    bit_stream = []
    previous = -1
    check = 1
    for i in range(len(input_stream)):
        if input_stream[i] == '1' or input_stream[i] == '0':
            if input_stream[i] == '1':
                bit_stream.append(0)
            else :
                bit_stream.append(-previous)
                previous = -previous
        else:
            print("Enter valid values")
            warning_display()
            check = 0
            break
    if check != 0:
        print("--Bipolar pseudoternary--   ",bit_stream)
        bit_stream = [bit_stream[0]] + bit_stream
        x_axis = [x for x in range(len(bit_stream))]
        return bit_stream,x_axis;

def plot5():
    bit_stream,x_axis=Bipolar_pseudoternary()
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.title("Bipolar pseudoternary")
    plt.yticks([-1,0,1])
    plt.plot(x_axis,[0]*len(bit_stream),'b',linewidth=0.8)
    plt.step(x_axis,bit_stream,'k',linewidth=2)
    #plt.show()

#Bipolar - AMI
def Bipolar_AMI():
    input_stream = list(input.get(1.0, tk.END+"-1c"))
    bit_stream = []
    previous = -1
    check = 1
    for i in range(len(input_stream)):
        if input_stream[i] == '1' or input_stream[i] == '0':
            if input_stream[i] == '0':
                bit_stream.append(0)
            else :
                bit_stream.append(-previous)
                previous = -previous
        else:
            print("Enter valid values")
            warning_display()
            check = 0
            break
    if check != 0:
        print("--Bipolar AMI--   ",bit_stream)
        bit_stream = [bit_stream[0]] + bit_stream
        x_axis = [x for x in range(len(bit_stream))]
        return bit_stream,x_axis;

def plot6():
    bit_stream,x_axis=Bipolar_AMI()
    plt.title("Bipolar AMI")
    plt.step(x_axis,bit_stream,'k',linewidth=2)
    plt.plot(x_axis,[0]*len(bit_stream),'b',linewidth=0.8)
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.yticks([-1,0,1])
    #plt.show()

#Biphase - differntial - manchester
def Biphase_diff_manchester():
    input_stream = list(input.get(1.0, tk.END+"-1c"))
    bit_stream = []
    previous = 1
    check = 1
    for i in range(len(input_stream)):
        if input_stream[i] == '1' or input_stream[i] == '0':
            if input_stream[i] == '0':
                bit_stream.extend([-previous,previous])
            else :
                bit_stream.extend([previous,-previous])
                previous = -previous
        else:
            print("Enter valid values")
            warning_display()
            check = 0
            break
    if check != 0 :
        print("--Biphase Differntial Manchester--   ",bit_stream)
        bit_stream = [1] + bit_stream
        x_axis = [x for x in range(len(bit_stream))]
        return bit_stream,x_axis;

def plot8():
    bit_stream,x_axis=Biphase_diff_manchester()
    plt.title("Biphase Differntial Manchester")
    plt.step(x_axis, bit_stream,'k',linewidth=2)
    plt.plot(x_axis,[0]*len(bit_stream),'b',linewidth=0.8)
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.xticks(np.arange(0,len(bit_stream),step=2),np.arange(0,len(bit_stream)/2,step=1))
    plt.yticks([-1,0,1])
    #plt.show()

#Biphase - manchester
def Biphase_manchester():
    input_stream = list(input.get(1.0, tk.END+"-1c"))
    bit_stream = []
    check = 1
    for i in range(len(input_stream)):
        if input_stream[i] == '1' or input_stream[i] == '0':
            if input_stream[i] == '0':
                bit_stream.extend([1,-1])
            else :
                bit_stream.extend([-1,1])
        else:
            print("Enter valid values")
            warning_display()
            check = 0
            break
    if check != 0 :
        print("--Biphase Manchester--   ",bit_stream)
        bit_stream = [bit_stream[0]] + bit_stream
        x_axis = [x for x in range(len(bit_stream))]
        return bit_stream,x_axis;

def plot7():
    bit_stream,x_axis=Biphase_manchester()
    plt.title("Biphase Manchester")
    plt.step(x_axis, bit_stream,'k',linewidth=2)
    plt.plot(x_axis,[0]*len(bit_stream),'b',linewidth=0.8)
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.xticks(np.arange(0,len(bit_stream),step=2),np.arange(0,len(bit_stream)/2,step=1))
    plt.yticks([-1,0,1])
    #plt.show()

#to plot single method
def plot():
    plt.show()

def plot_in():
    bit_stream = ['0']+list(input.get(1.0, tk.END+"-1c"))
    x_axis=[x for x in range(len(bit_stream))]
    plt.step(x_axis,bit_stream,'g',linewidth=2)
    plt.plot(x_axis,[0]*len(bit_stream),'b',linewidth=0.8)
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.title("INPUT")

#to plot all methods
def all_plot():
    print("\n------------------ ALL METHODS ------------------")
    plt.subplots_adjust(wspace=0.3,hspace=0.6)
    plt.subplot(3,4,1)
    plot1()
    plt.ylabel('Amplitude')

    plt.subplot(3,4,2,)
    plot2()
    plt.ylabel('Amplitude')

    plt.subplot(3,4,3)
    plot3()

    plt.subplot(3,4,4)
    plot4()

    plt.subplot(3,4,5)
    plot5()
    plt.ylabel('Amplitude')

    plt.subplot(3,4,6)
    plot6()
    plt.ylabel('Amplitude')

    plt.subplot(3,4,7)
    plot7()

    plt.subplot(3,4,8)
    plot8()

    plt.subplot(3,4,(9,12))
    plot_in()
    #plt.show()

# to clear entry
def clear():
    input.delete("1.0","end")
    warning['text']=""

def warning_display():
    warning['text']="Check Input!"
#to render GUI window
window = Tk()
window.geometry('750x500')
window.title("LINE ENCODING SCHEMES")
window.iconbitmap(r'icon.ico')

main_frame=Frame(window,bg='#a3bff0')
main_frame.place(relwidth=1,relheight=1)

method_frame=Frame(main_frame,bg='#f5aec3')
method_frame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.4)

warning = Label( main_frame,width=50,pady=5,bg='#a3bff0',font="Arial 12 bold")
warning.place(relx=0.5,rely=0.125,anchor='n')

input = Text(main_frame,width=20,height=1,bd=3,bg='#edf3fc',highlightcolor='black',highlightthickness=0)
input.place(relx=0.5,rely=0.05,anchor='n')
font1 = Font(family="Times New Roman", size=15)
input.configure(font=font1)

clear_entry = Button(main_frame, text ="CLEAR",padx=10,height=1,bd=3,bg='#4572f7',font="Arial 10 bold",command = clear)
clear_entry.place(relx=0.7,rely=0.05,anchor='n')

Uni_NRZ = Button(method_frame, text ="Unipolar-NRZ",bd=5,font="Arial 10", command = plot1)
Uni_NRZ.place(relx=0.1,rely=0.4,anchor='n')

B_polar_NRZ_L = Button(method_frame, text ="Polar-NRZ-L",bd=5,font="Arial 10", command = plot2)
B_polar_NRZ_L.place(relx=0.35,rely=0.2,anchor='n')

B_polar_NRZ_I = Button(method_frame, text ="Polar-NRZ-I",padx=2,bd=5,font="Arial 10", command = plot3)
B_polar_NRZ_I.place(relx=0.35,rely=0.4,anchor='n')

B_polar_RZ = Button(method_frame, text ="Polar-RZ",padx=10,bd=5,font="Arial 10", command = plot4)
B_polar_RZ.place(relx=0.35,rely=0.6,anchor='n')

B_Bipolar_pseudoternary=Button(method_frame,text="Bipolar-pseudoternary",bd=5,font="Arial 10", command =plot5)
B_Bipolar_pseudoternary.place(relx=0.58,rely=0.6,anchor='n')

B_Bipolar_AMI=Button(method_frame,text="Bipolar-AMI",padx=27,bd=5,font="Arial 10", command =plot6)
B_Bipolar_AMI.place(relx=0.58,rely=0.2,anchor='n')

B_Biphase_manchester=Button(method_frame,text="Biphase-manchester",padx=11,bd=5,font="Arial 10", command =plot7)
B_Biphase_manchester.place(relx=0.85,rely=0.2,anchor='n')

B_Biphase_diff_manchester=Button(method_frame,text="Biphase-diff-manchester",bd=5,font="Arial 10", command =plot8)
B_Biphase_diff_manchester.place(relx=0.85,rely=0.6,anchor='n')

B_plot = Button(main_frame,text="PLOT",padx=30,pady=5,bd=7,bg='silver',font="Arial 12 bold",command=plot)
B_plot.place(relx=0.2,rely=0.8,anchor='s')

all_plots=Button(main_frame,text="ALL",padx=30,pady=5,bd=7,bg='gold',font="Arial 12 bold",command=all_plot)
all_plots.place(relx=0.5,rely=0.8,anchor='s')

quit = Button(main_frame,text="EXIT",padx=30,pady=5,bd=7,bg='red',font="Arial 12 bold",command=window.quit)
quit.place(relx=0.8,rely=0.8,anchor='s')
window.mainloop()
