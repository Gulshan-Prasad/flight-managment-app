import tkinter as tk
from tkinter import ttk
import csv
import random

window = tk.Tk()
window.title("Airline management system")
window.geometry("900x600")

def adminwindow():
    checkfltframe.pack_forget()
    viewframe.pack_forget()
    updateframe.pack_forget()
    frame1.pack_forget()
    frame2.pack(fill=tk.BOTH, expand=True)
def userwindow():
    viewframe.pack_forget()
    frame4.pack_forget()
    frame1.pack_forget()
    cancelframe.pack_forget()
    checkframe.pack_forget()
    frame3.pack(fill=tk.BOTH, expand=True)
def update_interface():
    frame2.pack_forget()
    updateframe.pack(fill=tk.BOTH, expand=True)
def flight_det_interface():
    frame2.pack_forget()
    checkfltframe.pack(fill=tk.BOTH, expand=True)
def submit_flight():
    f= open("Flight_details.csv", "a")
    flt_name_sub= flt_name.get()
    flt_origin_sub= flt_origin.get()
    flt_dest_sub=flt_dest.get()
    flt_arrival_sub=flt_arrival.get()
    flt_dep_time_sub=flt_dep_time.get()
    flt_fare_sub=flt_fare.get()
    sub_flight=[flt_name_sub,flt_origin_sub,flt_dest_sub,flt_arrival_sub,flt_dep_time_sub,flt_fare_sub]
    w=csv.writer(f)
    w.writerow(sub_flight)
    f.close()
    flt_add=tk.Button(disp_frame, text=(sub_flight), font=("Arial", 10),width=90,height=3)
    flt_add.grid()
def store_data(text):
    f=open("Booking_details.csv", "a")
    w=csv.writer(f)
    w.writerow(text)
    f.close()
def exitwindow():
    window.destroy()
def backtomenu():
    frame3.pack_forget()
    frame2.pack_forget()
    frame1.pack(fill=tk.BOTH, expand=True)
def booking_interface():
    frame3.pack_forget()
    frame4.pack(fill=tk.BOTH, expand=True)
def view_interface_user():
    frame3.pack_forget()
    viewframe.pack(fill=tk.BOTH, expand=True)
    back4 = tk.Button(viewframe, text="Go back to User menu", command=userwindow, font=("Arial", 10), bg=("white"),width=18).place(x=30,y=50)
def view_interface_admin():
    frame2.pack_forget()
    viewframe.pack(fill=tk.BOTH, expand=True)
    back5 = tk.Button(viewframe, text="Go back to Admin menu", command=adminwindow, font=("Arial", 10), bg=("white"),width=18).place(x=30,y=50)
def cancel_interface():
    frame3.pack_forget()
    cancelframe.pack(fill=tk.BOTH, expand=True)
def check_interface():
    frame4.pack_forget()
    checkframe.pack(fill=tk.BOTH, expand=True)
def summon_check():
    global user_id
    user_id= random.randrange(1000,9999)
    tk.Label(frame4, text="Login Successfull!!", font=("Arial", 25), fg="green").place(x=320,y=350)
    tk.Label(frame4, text=("Your user id is:", user_id), font=("Arial", 25), fg="red").place(x=300,y=400)
    tk.Button(frame4, text="Select your flight", command=check_interface, font=("Arial", 20)).place(x=350,y=470)
def submit_book(text):
    f=open("Booking_details.csv", "a")
    name_sub= name_input.get()
    phn_sub= phn_input.get()
    address_sub= address_input.get()
    summon_check()
    submission= [user_id, name_sub, phn_sub, address_sub, text]
    w=csv.writer(f)
    w.writerow(submission)
    f.close()
    popup = tk.Toplevel(window)
    popup_width = 300
    popup_height = 100
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    popup.title("Flight submitted")
    tk.Label(popup, text="BOOKED SUCCESSFULLY!!").pack(padx=20, pady=20)

def find_id():
    background= tk.Canvas(viewframe, width=700, height=350, bg="white")
    background.place(x=150, y=200)
    background.create_rectangle(5, 350, 700, 5, fill="#FFFDD0")
    user_id= id_entry.get()
    f1=open("Booking_details.csv", "r")
    flag=False
    r=csv.reader(f1)
    tk.Label(viewframe, font=("Arial",20), text="User id", bg="#FFFDD0").place(x=200, y=220)
    tk.Label(viewframe, font=("Arial",20), text="Name", bg="#FFFDD0").place(x=200, y=270)
    tk.Label(viewframe, font=("Arial",20), text="Phone no.", bg="#FFFDD0").place(x=200, y=320)
    tk.Label(viewframe, font=("Arial",20), text="Address", bg="#FFFDD0").place(x=200, y=370)
    for i in r:
        if len(i)>0 and i[0]==user_id:
            b=220
            tk.Label(viewframe, text=(i[3]), font=("Arial",15), bg="#FFFDD0").place(x=400,y=370)
            tk.Label(viewframe, text=(i[4]), font=("Arial",16), bg="#FFFDD0").place(x=180,y=450)
            for j in range(0,len(i)-2):
                a=tk.Label(viewframe, text=(i[j]), font=("Arial",20), bg="#FFFDD0")
                a.place(x=400, y=b)
                b=b+50
            flag=True
            break
    if flag==False:
        b=tk.Label(viewframe, text="Incorrect ID or ID not found")
    f1.close()
def delete_passenger():
    f=open("Booking_details.csv","a+")
    f.seek(0)
    d=id_entry_can.get()
    r=csv.reader(f)
    L=list(r)
    for i in range(0,len(L)):
        if len(L[i])>0 and str(L[i][0])==d:
            L[i]=[]
            tk.Label(cancelframe, text="TICKET CANCELED", font=("Arial", 20), fg="red").place(x=350,y=300)
        else:
            continue
    L1=[z for z in L if not isinstance(z,(list)) or z]
    f1=open("Booking_details.csv","w+")
    w=csv.writer(f1)
    w.writerows(L1)
    f1.close()
    f.close()



#main interferance
frame1 = tk.Frame(window)
heading = tk.Label(frame1, text="AIRLINE MANAGEMENT SYSTEM", borderwidth=5, relief="groove", font=("Rubik Doodle Shadow", 40), bg="lightblue", fg="red").pack(anchor="n")
label = tk.Label(frame1, text="Welcome to our airline management \n Let us know who's in", font=("Arial", 35), fg="indigo", width=15, height=6).pack(fill="x")
admin = tk.Button(frame1, text="ADMIN", command=adminwindow, font=("Arial", 30), bg="lightblue", fg="orange").pack(side="left", padx=100, pady=10)
User = tk.Button(frame1, text="USER", command=userwindow, font=("Arial", 30), bg="lightblue", fg="darkgreen").pack(side="right", padx=100, pady=10)
exitwindow = tk.Button(frame1, text="EXIT", command=exitwindow, font=("Arial", 20), bg="#FF5349").pack(side="bottom", padx=10, pady=10)

#admin interface
frame2 = tk.Frame(window)
label2= tk.Label(frame2, text="WELCOME ADMIN!!", font=("Arial", 25), width=15, height=6).pack(fill="both")
back2 = tk.Button(frame2, text="Go back to main menu", command=backtomenu, font=("Arial", 10), bg=("white")).place(x=30,y=50)
update= tk.Button(frame2, text="UPDATE FLIGHTS", command=update_interface, font=("Arial", 20),width=23).pack()
view_data= tk.Button(frame2, text="VIEW PASSENGER DATA", command=view_interface_admin, font=("Arial",20),width=23).pack(pady=10)
flight_details= tk.Button(frame2, text="FLIGHT DETAILS", command=flight_det_interface, font=("Arial",20),width=23).pack(pady=10)

#update flights interace
updateframe= tk.Frame(window)
upL1= tk.Label(updateframe, text="SELECT YOUR FLIGHT DETAILS", font=("Arial", 20)).place(x=260,y=50)
spacing= tk.Label(updateframe, text="      ").grid(row=1, column=0,pady=50, padx=100)
flt_name= tk.Label(updateframe, text="Enter Name", font=("Arial", 20)).grid(row=2, column=1, padx=10, pady=10, sticky="w")
flt_name= tk.Entry(updateframe, width=30)
flt_name.grid(row=2, column=2, padx=10)
flt_origin= tk.Label(updateframe, text="Enter Origin", font=("Arial", 20)).grid(row=3, column=1, padx=10, pady=10, sticky="w")
flt_origin= tk.Entry(updateframe, width=30)
flt_origin.grid(row=3, column=2, padx=20)
flt_dest= tk.Label(updateframe, text="Enter Destination", font=("Arial", 20)).grid(row=4, column=1, padx=10, pady=10, sticky="w")
flt_dest= tk.Entry(updateframe, width=30)
flt_dest.grid(row=4, column=2, padx=20)
flt_arrival= tk.Label(updateframe, text="Enter Arrival time", font=("Arial", 20)).grid(row=5, column=1, padx=10, pady=10, sticky="w")
flt_arrival= tk.Entry(updateframe, width=30)
flt_arrival.grid(row=5, column=2, padx=20)
flt_dep_time= tk.Label(updateframe, text="Enter Departure time", font=("Arial", 20)).grid(row=6, column=1, padx=10, pady=10, sticky="w")
flt_dep_time= tk.Entry(updateframe, width=30)
flt_dep_time.grid(row=6, column=2, padx=20)
flt_fare= tk.Label(updateframe, text="Enter Fare", font=("Arial", 20)).grid(row=7, column=1, padx=10, pady=10, sticky="w")
flt_fare= tk.Entry(updateframe, width=30)
flt_fare.grid(row=7, column=2, padx=10)

submit= tk.Button(updateframe,text="SUBMIT", command=submit_flight ,font=("arial", 15)).place(x=450,y=500)
back5 = tk.Button(updateframe, text="Go back to Admin menu", command=adminwindow, font=("Arial", 10), bg=("white")).place(x=30,y=50)

#check flights details
checkfltframe= tk.Frame(window)
tk.Label(checkfltframe, text="FLIGHT DETAILS", font=("Arial",30)).pack()
disp_flt_frame = tk.Frame(checkfltframe, width=800, height=500)
disp_flt_frame.place(x=100,y=100)
chk_flt_file= open("Flight_details.csv", "r")
r_flt=csv.reader(chk_flt_file)
chk_flt_details=["Name","Origin","Destination","Arrival_Time","Departure_Time","Fare"]
modchkflt="                    ".join(chk_flt_details)
tk.Button(disp_flt_frame, text=modchkflt,width=103).grid()
for i in r_flt:
    if len(i)>0:
        modi = "                ".join(i)
        flt=tk.Label(disp_flt_frame, text=modi,justify="left",font=("Arial", 10),width=90,height=3)
        flt.grid(pady=5)
chk_flt_file.close()
back5 = tk.Button(checkfltframe, text="Go back to Admin menu", command=adminwindow, font=("Arial", 10), bg=("white")).place(x=30,y=50)


#user interface
frame3 = tk.Frame(window)
label3= tk.Label(frame3, text="Welcome User!!", font=("Arial", 25), width=15, height=6).pack(fill="both")
back3 = tk.Button(frame3, text="Go back to main menu", command=backtomenu, font=("Arial", 10), bg=("white")).place(x=30,y=50)
booking = tk.Button(frame3, text="Book your tickets", command=booking_interface, font=("Arial",20),width=15).pack()
view_data= tk.Button(frame3, text="View your Ticket", command=view_interface_user, font=("Arial",20),width=15).pack(pady=5)
cancel_booking= tk.Button(frame3, text="Cancel Booking",command=cancel_interface, font=("Arial",20),width=15).pack(pady=5)

#booking interface
frame4= tk.Frame(window)
bookheading = tk.Label(frame4, text="Book your tickets here", font=("Arial", 30))
bookheading.pack(anchor="n")
background1=tk.Canvas(frame4, width=650, height=250, bg="#90EE90")
background1.place(x=70,y=85)
name=tk.Label(frame4, text="Name ", font=("Helvetica", 20),bg="#90EE90").place(x=100, y=120)
name_input=tk.Entry(frame4, width=30)
name_input.place(x=270, y=130)

phn=tk.Label(frame4, text="Phone no. ", font=("Helvetica", 20),bg="#90EE90").place(x=100, y=175)
phn_input = tk.Entry(frame4, width=30)
phn_input.place(x=270, y=185)

address= tk.Label(frame4, text="Address ", font=("Helvetica", 20),bg="#90EE90").place(x=100, y=225)
address_input = tk.Entry(frame4, width=70)
address_input.place(x=270, y=235)

submit = tk.Button(frame4, text="Submit",command=summon_check , font=("Arial", 20))
submit.pack(side="bottom")
back4 = tk.Button(frame4, text="Go back to User menu", command=userwindow, font=("Arial", 10), bg=("white")).place(x=30,y=50)

#check your flights
checkframe= tk.Frame(window)
tk.Label(checkframe, text="SELECT YOUR FLIGHT", font=("Arial",30)).pack()
disp_frame = tk.Frame(checkframe, width=800, height=500)
disp_frame.place(x=100,y=100)
chk_file= open("Flight_details.csv", "r")
r=csv.reader(chk_file)
flt_details=["Name","Origin","Destination","Arrival_Time","Departure_Time","Fare"]
modflt="                    ".join(flt_details)
tk.Button(disp_frame, text=modflt,width=103).grid()
for i in r:
    if len(i)>0:
        modi = "                ".join(i)
        flt=tk.Button(disp_frame,command=lambda text=modi: submit_book(text), text=modi,justify="left",font=("Arial", 10),width=90,height=3)
        flt.grid(pady=5)
chk_file.close()
back4= tk.Button(checkframe, text="Go back to User menu", command=userwindow, font=("Arial", 10), bg=("white")).place(x=30,y=50)


#view interface
viewframe= tk.Frame(window)
tk.Label(viewframe, text="View data",font=("arial",20))
enter_id= tk.Label(viewframe, text="Enter your ID: ", font=("Arial", 10)).place(x=100,y=150)
id_entry= tk.Entry(viewframe, width=30)
id_entry.place(x=200, y=150)
submit_id= tk.Button(viewframe, text="Submit", command=find_id , font=("Arial", 20)).pack(side="bottom")

#Cancel Booking
cancelframe= tk.Frame(window)
tk.Label(cancelframe, text="Cancel Your Booking here", font=("arial", 20))
enter_id_can= tk.Label(cancelframe, text="Enter your ID: ", font=("Arial", 10)).place(x=100,y=150)
id_entry_can= tk.Entry(cancelframe, width=30)
id_entry_can.place(x=200, y=150)
submit = tk.Button(cancelframe, text="Submit",command=delete_passenger , font=("Arial", 20)).pack(side="bottom")
back4= tk.Button(cancelframe, text="Go back to User menu", command=userwindow, font=("Arial", 10), bg=("white")).place(x=30,y=50)

current_frame = frame1
frame1.pack()

window.mainloop()
