from tkinter import *  #importing tkinter and tkcalendar with their whole modoules
from tkcalendar import *
#Creating main tkinter window
ins=Tk()

#Creating calendar widget
mycal=Calendar(ins)
mycal.pack(fill='both',expand=True,padx=20,pady=20)

#Setting the size, title and backgroung colour of the wondow
ins.geometry("430x300")
ins.title("CALENDAR")
ins.configure(bg="light green")

#Creating a function for fetching selected date
def selected_date():
    date.config(text="Selected date is: "+mycal.get_date())
    
#Creating a button named "Get Data"
my_button=Button(ins, text = "Get Date",bg="lightblue",font=('Calibri',10,'bold'),command = selected_date)
my_button.pack(pady = 10)

# Create a label to display the selected date      
date =Label(ins,text='',bg="gold",font=('Comic Sans MS',14,'bold'))
date.pack(pady =4)


ins.mainloop()


   



 

