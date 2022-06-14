from tkinter import *
import delhi_house_price as dp
new_input=[1000.0,2,2.0,19,1,70,0,667.0]
#print(dp.pred[0])

#main
window = Tk()

def click():
    entered_text1 = text1entry.get()
    entered_text2 = text2entry.get()
    entered_text3 = text3entry.get()
    entered_text4 = text4entry.get()
    entered_text5 = text5entry.get()
    entered_text6 = text6entry.get()
    entered_text7 = text7entry.get()
    entered_text8 = text8entry.get()
    #l1 = list(entered_text.split(' '))
    new_input=[entered_text1,entered_text2,entered_text3,entered_text4,entered_text5,entered_text6,entered_text7,entered_text8]
    #print(prediction[0])
    output.delete(0.0,END)
    dp.user[0][0] = float(new_input[0])
    dp.user[0][1] = int(new_input[1])
    dp.user[0][2] = float(new_input[2])
    dp.user[0][3] = int(new_input[3])
    dp.user[0][4] = int(new_input[4])
    dp.user[0][5] = int(new_input[5])
    dp.user[0][6] = int(new_input[6])
    dp.user[0][7] = float(new_input[7])
    prediction = dp.rf.predict(dp.user)
    # try:
    #     definition = my_dict[entered_text]
    # except:
    #     definition = 'Sorry didnt get ya'
    output.insert(END,prediction[0])
    #print(entered_text)

def close_window():
    window.destroy()
    exit(0)


window.title("TeeHee")
window.configure(bg="#585F65")
#image
#photo1 = PhotoImage(file="image1.gif")
#Label (window,image=photo1,bg="#585F65").grid(row=0,column=0,sticky=W)
#------------body for inputs-------------------------------------------
Label(window,text="Status:almost ready=0, ready=1\nTransaction: new=0, resale=1\nType:apartment=0,Floor Build=1",bg="black",fg="white",font="none 9 bold").grid(row=0,column=1,sticky=W)
Label(window,text="Area", bg= "#585F65",fg = "white",font=" none 14 bold").grid(row=1,column=0,sticky=W)
text1entry= Entry(window,width = 20,bg="white")
text1entry.grid(row=2,column=0,sticky=W)

Label(window,text="BHK", bg= "#585F65",fg = "white",font=" none 14 bold").grid(row=1,column=1,sticky=W)
text2entry= Entry(window,width = 20,bg="white")
text2entry.grid(row=2,column=1,sticky=W)

Label(window,text="Bathrooms", bg= "#585F65",fg = "white",font=" none 14 bold").grid(row=1,column=2,sticky=W)
text3entry= Entry(window,width = 20,bg="white")
text3entry.grid(row=2,column=2,sticky=W)

Label(window,text="Locality", bg= "#585F65",fg = "white",font=" none 14 bold").grid(row=1,column=3,sticky=W)
text4entry= Entry(window,width = 20,bg="white")
text4entry.grid(row=2,column=3,sticky=W)

Label(window,text="Status", bg= "#585F65",fg = "white",font=" none 14 bold").grid(row=3,column=0,sticky=W)
text5entry= Entry(window,width = 20,bg="white")
text5entry.grid(row=4,column=0,sticky=W)

Label(window,text="Transaction", bg= "#585F65",fg = "white",font=" none 14 bold").grid(row=3,column=1,sticky=W)
text6entry= Entry(window,width = 20,bg="white")
text6entry.grid(row=4,column=1,sticky=W)

Label(window,text="Type", bg= "#585F65",fg = "white",font=" none 14 bold").grid(row=3,column=2,sticky=W)
text7entry= Entry(window,width = 20,bg="white")
text7entry.grid(row=4,column=2,sticky=W)

Label(window,text="Per SqFt", bg= "#585F65",fg = "white",font=" none 14 bold").grid(row=3,column=3,sticky=W)
text8entry= Entry(window,width = 20,bg="white")
text8entry.grid(row=4,column=3,sticky=W)
#------------inputs end here-------------------------------------------
#--------------button-------------------------------------------------
Button(window,text="Submit",bg="#585F60",width=6,command=click).grid(row=5,column=0,sticky=W)
#--------------button ends here------------------------------------------
Label(window,text="\nOutput:",bg="#585F65",fg="white",font="none 14 bold").grid(row=6,column=0,sticky=W)
output = Text(window,width=20,height=5,bg="white",wrap=WORD)
output.grid(row=7,column=0,sticky=W)

#dictionary
#my_dict = {'itsy':'bitsy','chuddy':'buddy','son':'pari','golu':'molu','bjp':'communist'}
#exit
Label(window,text="Press to exit(or for fun)",bg="#585F65",font="none 10 bold").grid(row=8,column=0,sticky=W)
Button(window,text="Exit",width=4,bg="#585F65",command=close_window).grid(row=9,column=0,sticky=W)


window.mainloop()


#Area	BHK	Bathroom	Locality	Status	Transaction	Type	Per_Sqft
#                                   ready               builder_floor
#                                   almost ready        apartment
#                                            new_property
#                                             resale                                                