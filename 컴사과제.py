from tkinter import *
x=0
d=[]
win = Tk()
win.title("일정표")
win.geometry("800x600")
win.resizable(width=False,height=False)

#일정표 추가 창
lb1 = Label(win,text="년도/월/날짜 순으로 입력하세요")
lb1.grid(row=0,column=0,sticky=N)

sc_input_date = Text(width=30,height=3)
sc_input_date.grid(row=1,column=0,sticky=N)

lb2 = Label(win,text="일정을 입력하세요")
lb2.grid(row=2,column=0,sticky=N)

sc_input_plan = Text(width=30,height=3)
sc_input_plan.grid(row=3,column=0,sticky=N)


lb3 = Label(win,text="세부사항을 입력하세요")
lb3.grid(row=4,column=0,sticky=N)

sc_input_de = Text(width=30,height=3)
sc_input_de.grid(row=5,column=0,sticky=N)

#일정표 추가 버튼
def 일정추가 () :
    global x
    global d
    
    a= sc_input_date.get("1.0",END)  
    #addf=Label(win,text=a)
    #addf.grid(row=x,column=1,padx=5,sticky=N)
    b= sc_input_plan.get("1.0",END)  
    #addf1=Label(win,text=b)
    #addf1.grid(row=x,column=2,padx=5,sticky=N)
    c= sc_input_de.get("1.0",END)  
    #addf2=Label(win,text=c)
    #addf2.grid(row=x,column=3,padx=5,sticky=N)
    
    d.append([a,b,c])
    
    addf=Label(file_frame,text=d[x][0])
    addf.grid(row=(x+1),column=0,padx=5,sticky=N)
    
    addf1=Label(file_frame,text=d[x][1])
    addf1.grid(row=(x+1),column=1,padx=5,sticky=N)
    
    addf2=Label(file_frame,text=d[x][2])
    addf2.grid(row=(x+1),column=2,padx=5,sticky=N)
    x+=1

    sc_input_date.delete("1.0",END)
    sc_input_plan.delete("1.0",END)
    sc_input_de.delete("1.0",END)

btn_add = Button(width=20, height=2,text='추가하기')
btn_add.config(command=일정추가)
btn_add.grid(row=6,column=0) 

#일정표 형식 프레임
file_frame = Frame(win)
file_frame.grid(row=0, column=1,columnspan=400,rowspan=400,sticky=N)

label1=Label(file_frame,text="날짜",bg='#FFBF00')
label1.grid(row=0, column=0,padx=30,sticky=N)

label2=Label(file_frame,text="일정")
label2.grid(row=0, column=1,padx=40,sticky=N)

label3=Label(file_frame,text="세부사항")
label3.grid(row=0, column=2,padx=60,sticky=N)

#일정표 삭제 창
lb4 =Label(win,text="삭제하고 싶은 줄을 입력하세요(1)")
lb4.grid(row=7,column=0,sticky=N)

sc_input_delete = Entry(width=30)
sc_input_delete.grid(row=8,column=0,sticky=N)


#일정표 삭제 버튼
def 삭제하기 () :
    global x
    global d

    c=sc_input_delete.get()
    s=int(c)
    h=len(d)
    if h==s :
        
        
        d.remove(d[s-1])
        
        widget =file_frame.grid_slaves(row=(x), column=0)
        widget[0].destroy()
        widget1 =file_frame.grid_slaves(row=(x), column=1)
        widget1[0].destroy()
        widget2 =file_frame.grid_slaves(row=(x), column=2)
        widget2[0].destroy()
        
        x-=1
        
       
    if s<h :
        
        d.remove(d[s-1])
        
        f=len(d)
    
        
        
        for i in range (f) :
            addf=Label(file_frame,text=d[i][0])
            addf.grid(row=(i+1),column=0,padx=5,sticky=N)
        
            addf1=Label(file_frame,text=d[i][1])
            addf1.grid(row=(i+1),column=1,padx=5,sticky=N)
        
            addf2=Label(file_frame,text=d[i][2])
            addf2.grid(row=(i+1),column=2,padx=5,sticky=N)
        widget =file_frame.grid_slaves(row=(x), column=0)
        widget[0].destroy()
        widget1 =file_frame.grid_slaves(row=(x), column=1)
        widget1[0].destroy()
        widget2 =file_frame.grid_slaves(row=(x), column=2)
        widget2[0].destroy()
        x-=1



btn_delete = Button(width=20, height=2,text='삭제하기')
btn_delete.config(command=삭제하기)
btn_delete.grid(row=9,column=0,sticky=N) 













win.mainloop()





