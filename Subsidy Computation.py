import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Subsidy Compution")
root.geometry("600x400")



def Rice():
    global rice_window
    rice_window=tk.Toplevel(root)
    rice_window.title("RICE")
    rice_window.geometry("600x400")

    R_lable=tk.Label(rice_window,text="RICE")
    R_lable.grid()
    
    RiceL1=tk.Label(rice_window,text="Enter Your Yeild")
    RiceL1.grid()

    global rice_y
    rice_y = tk.Entry(rice_window, font=("Arial", 16))
    rice_y.grid()

    RiceL2=tk.Label(rice_window,text="Enter Your Market price")
    RiceL2.grid()

    global rice_mp
    rice_mp=tk.Entry(rice_window,font=("Arial", 16))
    rice_mp.grid()

    submitr=tk.Button(rice_window,text="Submit",command=subrice)
    submitr.grid()




def subrice():
    ricey=rice_y.get()
    ricey=int (ricey)
    ricemp=rice_mp.get()
    ricemp=int(ricemp)
    global subsidyr
    subsidyr=(ricey*ricemp)+100
    subsidyr=str(subsidyr)
    messagebox.showinfo("Subsidy","Your Subsidy on rice is ₹"+subsidyr)
    
    



def Wheat():

    wheat_window=tk.Toplevel(root)
    wheat_window.title("WHEAT")
    wheat_window.geometry("600x400")

    W_lable=tk.Label(wheat_window,text="WHEAT")
    W_lable.grid()
    
    wheatL1=tk.Label(wheat_window,text="Enter Your Yeild")
    wheatL1.grid()

    global wheat_y
    wheat_y = tk.Entry(wheat_window, font=("Arial", 16))
    wheat_y.grid()

    wheatL2=tk.Label(wheat_window,text="Enter Your Market price")
    wheatL2.grid()

    global wheat_mp
    wheat_mp=tk.Entry(wheat_window,font=("Arial", 16))
    wheat_mp.grid()

    submitW=tk.Button(wheat_window,text="Submit",command=subwheat)
    submitW.grid()


    
def subwheat():
    wheaty=wheat_y.get()
    wheaty=int(wheaty)
    wheatmp=wheat_mp.get()
    wheatmp=int(wheatmp)

    global subsidyw
    subsidyw=(wheaty*wheatmp)+200
    subsidyw=str(subsidyw)

    messagebox.showinfo("Subsidy","Your Subsidy on wheat is ₹"+subsidyw)



def Maize():
     
    Maize_window=tk.Toplevel(root)
    Maize_window.title("RICE")
    Maize_window.geometry("600x400")

    M_lable=tk.Label(Maize_window,text="MAIZE")
    M_lable.grid()
    
    MaizeL1=tk.Label(Maize_window,text="Enter Your Yeild")
    MaizeL1.grid()
    
    
    global Maize_y
    Maize_y = tk.Entry(Maize_window, font=("Arial", 16))
    Maize_y.grid()

    MaizeL2=tk.Label(Maize_window,text="Enter Your Market price")
    MaizeL2.grid()

    global Maize_mp
    Maize_mp=tk.Entry(Maize_window,font=("Arial", 16))
    Maize_mp.grid()

    submitM=tk.Button(Maize_window,text="Submit",command=subMaize)
    submitM.grid()
    


def subMaize():

    Maizey=Maize_y.get()
    Maizey=int(Maizey)
    Maizemp=Maize_mp.get()
    Maizemp=int(Maizemp)

    global subsidym
    subsidym=(Maizey*Maizemp)+300
    subsidym=str(subsidym)

    messagebox.showinfo("Subsidy","Your Subsidy on Maize is ₹"+subsidym)
    



def totsubsidy():
    subsidyr1=subsidyr.get()
    subsidyr1=int(subsidyr1)
    subsidyw1=subsidyw.get()
    subsidyw1=int(subsidyw1)
    subsidym1=subsidym.get()
    subsidym1=int(subsidym1)
    totsub=subsidym1+subsidyr1+subsidyw1
    totsub=str(totsub)

    ptotalsub=tk.Label(root,text="Your total subsidy getting by goverment is ₹ " + totsub)
    ptotalsub.grid()



def check():
    
    
    if subsidym and subsidyr and subsidyw :
        totsubsidy()
    else:
        messagebox.showinfo("ERROR","fill all the crop type")

main_lable=tk.Label(root,text="Choose the Crop") 
main_lable.grid()

button_rice=tk.Button(root,text="Rice",command=Rice,font=("Arial", 14))
button_rice.grid()
   
button_wheat=tk.Button(root,text="Wheat",command=Wheat,font=("Arial", 14))
button_wheat.grid()

button_maize=tk.Button(root,text="Maize",command=Maize,font=("Arial", 14))
button_maize.grid()

button_totsub=tk.Button(root,text="Total Subsidy",font=("Arial", 14),command=check)
button_totsub.grid()




root.mainloop()