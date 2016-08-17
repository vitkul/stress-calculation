import tkinter as tk
from math import pi


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.grid()
        self.title("Расчет на прочность")
        self.geometry("600x600")
        self.resizable(False,False)

        Frame1 = tk.Frame(relief="flat")
        Frame1.grid(row=0, column=1, columnspan=5, sticky="ew")
        tk.Label(Frame1,text="Площади, моменты инерции, моменты сопротивления").pack()#grid(row=0, column=3, columnspan=5)

        Frame5 = tk.Frame(self,relief="sunken")
        Frame5.grid(row=3, column=0, rowspan=8, columnspan=7, sticky="senw")


        self.frames = {}

        for i in (PageZero, PageOne, PageTwo, PageThee, PageFour, PageFive):
            frame = i(Frame5, self)
            self.frames[i] = frame
            frame.grid(row=1, column=1, sticky="senw")

        self.show_frame(PageZero)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
   
        
class PageZero(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page 0')
        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=1, columnspan=6)

        self.ractangle_photo = tk.PhotoImage(file="i1.gif")
        self.rac_tube_photo = tk.PhotoImage(file="i2.gif")
        self.isection_photo = tk.PhotoImage(file="i11.gif")
        self.tube_photo = tk.PhotoImage(file="i19.gif")
        self.circle_photo = tk.PhotoImage(file="i18.gif")
        main0_button = tk.Button(button_frame, text='Main', relief="sunken", command=lambda: controller.show_frame(PageZero))
        main1_button = tk.Button(button_frame, image=self.ractangle_photo, command=lambda: controller.show_frame(PageOne))
        main2_button = tk.Button(button_frame, image=self.rac_tube_photo, command=lambda: controller.show_frame(PageTwo))
        main3_button = tk.Button(button_frame, image=self.isection_photo, command=lambda: controller.show_frame(PageThee))
        main4_button = tk.Button(button_frame, image=self.tube_photo, command=lambda: controller.show_frame(PageFour))
        main5_button = tk.Button(button_frame, image=self.circle_photo, command=lambda: controller.show_frame(PageFive))                   
        
        label.grid(row=5,column=3)

        picture_frame = tk.Frame(self, bd=4, height=300, width=300)
        picture_frame.grid(row=3, column=0, rowspan=8, columnspan=3, sticky="senw")

        right_frame = tk.Frame(self, bd=4, height=300, width=300)
        right_frame.grid(row=3, column=3, rowspan=8, columnspan=4, sticky="senw")
        
        main0_button.grid(row=1,column=1)
        main1_button.grid(row=1,column=2)
        main2_button.grid(row=1,column=3)
        main3_button.grid(row=1,column=4)
        main4_button.grid(row=1,column=5)
        main5_button.grid(row=1,column=6)
        

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page 1')
        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=1, columnspan=6)
        
        self.ractangle_photo = tk.PhotoImage(file="i1.gif")
        self.rac_tube_photo = tk.PhotoImage(file="i2.gif")
        self.isection_photo = tk.PhotoImage(file="i11.gif")
        self.tube_photo = tk.PhotoImage(file="i19.gif")
        self.circle_photo = tk.PhotoImage(file="i18.gif")

        main1_button = tk.Button(button_frame, image=self.ractangle_photo, relief="sunken", command=lambda: controller.show_frame(PageOne))
        main2_button = tk.Button(button_frame, image=self.rac_tube_photo, command=lambda: controller.show_frame(PageTwo))
        main3_button = tk.Button(button_frame, image=self.isection_photo, command=lambda: controller.show_frame(PageThee))
        main4_button = tk.Button(button_frame, image=self.tube_photo, command=lambda: controller.show_frame(PageFour))
        main5_button = tk.Button(button_frame, image=self.circle_photo, command=lambda: controller.show_frame(PageFive))                   
        main1_button.grid(row=1,column=2)
        main2_button.grid(row=1,column=3)
        main3_button.grid(row=1,column=4)
        main4_button.grid(row=1,column=5)
        main5_button.grid(row=1,column=6)
   
        label.grid(row=5,column=3)

        picture_frame = tk.Frame(self, bd=4, height=300, width=300, relief="raised")
        picture_frame.grid(row=3, column=0, rowspan=8, columnspan=3, sticky="senw")
        right_frame = tk.Frame(self, bd=4, height=300, width=300, relief="raised")
        right_frame.grid(row=3, column=3, rowspan=8, columnspan=4, sticky="senw")

        self.photo_image = tk.PhotoImage(file="m1.gif")
        label_picture = tk.Label(picture_frame, image=self.photo_image)
        label_picture.grid(row=5, column=1, sticky="senw")

        text1_label = tk.Label(right_frame, text="Ширина прямоугольника b =")
        text2_label = tk.Label(right_frame,text="Высота прямоугольника h =")
        main1_entry = tk.Entry(right_frame,width=10)
        main2_entry = tk.Entry(right_frame,width=10)
        
        text1_label.grid(row=3, column=3)
        text2_label.grid(row=5, column=3)
        main1_entry.grid(row=3, column=4)
        main2_entry.grid(row=5, column=4)

        def ractangle():
            b = float(main1_entry.get())
            h = float(main2_entry.get())
            main_Area_text.delete(1.0,"end")# 1.0 - first sumbol to the end "end"
            main_Jx_text.delete(1.0,"end")
            main_Jy_text.delete(1.0,"end")
            main_Wx_text.delete(1.0,"end")
            main_Wy_text.delete(1.0,"end")
            main_Ix_text.delete(1.0,"end")
            main_Iy_text.delete(1.0,"end")
            main_Area_text.insert("end",b*h)#area
            main_Jx_text.insert("end",b*(h**3)/12)#jx
            main_Jy_text.insert("end",h*(b**3)/12)#jy
            main_Wx_text.insert("end",b*(h**2)/6)#Wx
            main_Wy_text.insert("end",h*(b**2)/6)#Wy
            main_Ix_text.insert("end",h/(12**0.5))#Ix
            main_Iy_text.insert("end",b/(12**0.5))#Iy

        button = tk.Button(self,text="Расчитать", command=lambda:ractangle())
        button.grid(row=13, column=3, sticky="ew")

        frame_results = tk.Frame(self)
        frame_results.grid(row=15, column=0, columnspan=7, rowspan=2, sticky="ew")

        for i,j in enumerate(("F", "Jx", "Jy", "Wx", "Wy", "Ix", "Iy")):
            frame_results.columnconfigure(i,weight=1)         
            tk.Label(frame_results, text="{0}".format(j),relief="ridge").grid(row=14, column=i)
            
        main_Area_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Area_text.grid(row=15, column=0)
        main_Jx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jx_text.grid(row=15, column=1)
        main_Jy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jy_text.grid(row=15, column=2)
        main_Wx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wx_text.grid(row=15, column=3)
        main_Wy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wy_text.grid(row=15, column=4)
        main_Ix_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Ix_text.grid(row=15, column=5)
        main_Iy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Iy_text.grid(row=15, column=6)
                      
        
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page 2')
        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=1, columnspan=6)
        
        self.ractangle_photo = tk.PhotoImage(file="i1.gif")
        self.rac_tube_photo = tk.PhotoImage(file="i2.gif")
        self.isection_photo = tk.PhotoImage(file="i11.gif")
        self.tube_photo = tk.PhotoImage(file="i19.gif")
        self.circle_photo = tk.PhotoImage(file="i18.gif")

        main1_button = tk.Button(button_frame, image=self.ractangle_photo, command=lambda: controller.show_frame(PageOne))
        main2_button = tk.Button(button_frame, image=self.rac_tube_photo, relief="sunken", command=lambda: controller.show_frame(PageTwo))
        main3_button = tk.Button(button_frame, image=self.isection_photo, command=lambda: controller.show_frame(PageThee))
        main4_button = tk.Button(button_frame, image=self.tube_photo, command=lambda: controller.show_frame(PageFour))
        main5_button = tk.Button(button_frame, image=self.circle_photo, command=lambda: controller.show_frame(PageFive))                   

        label.grid(row=5,column=3)
     
        right_label = tk.Label(self, text="Text")
        right_label.grid(row=3, column=3, rowspan=8, columnspan=4, sticky="senw")
        main1_button.grid(row=1, column=2)
        main2_button.grid(row=1, column=3)
        main3_button.grid(row=1, column=4)
        main4_button.grid(row=1, column=5)
        main5_button.grid(row=1, column=6)

        picture_frame = tk.Frame(self, bg="red")
        picture_frame.grid(row=3, column=0, rowspan=8, columnspan=3, sticky="senw")
        
        self.photo_image = tk.PhotoImage(file="m2.gif")
        label_picture = tk.Label(picture_frame, image=self.photo_image)
        label_picture.grid(row=5, column=1, sticky="senw")        

        right_frame = tk.Frame(self)
        right_frame.grid(row=3, column=3, rowspan=8, columnspan=4, sticky="senw")

        text1_label = tk.Label(right_frame, text="Ширина прямоугольника b =")
        text2_label = tk.Label(right_frame, text="Высота прямоугольника h =")
        main1_entry = tk.Entry(right_frame, width=10)
        main2_entry = tk.Entry(right_frame, width=10)
        text3_label = tk.Label(right_frame, text="Толщина sb1 =")
        text4_label = tk.Label(right_frame, text="Толщина sh1 =")
        main3_entry = tk.Entry(right_frame, width=10)
        main4_entry = tk.Entry(right_frame, width=10)
        text1_label.grid(row=3, column=3)
        text2_label.grid(row=5, column=3)     
        text3_label.grid(row=7, column=3)
        text4_label.grid(row=8, column=3)
        main3_entry.grid(row=7, column=4)
        main4_entry.grid(row=8, column=4)
        main1_entry.grid(row=3, column=4)
        main2_entry.grid(row=5, column=4) 

        def rac_tube():
            b = float(main1_entry.get())
            h = float(main2_entry.get())
            b1 = float(main3_entry.get())
            h1 = float(main4_entry.get())

            main_Area_text.delete(1.0,"end")# 1.0 - first sumbol to the end "end"
            main_Jx_text.delete(1.0,"end")
            main_Jy_text.delete(1.0,"end")
            main_Wx_text.delete(1.0,"end")
            main_Wy_text.delete(1.0,"end")
            main_Ix_text.delete(1.0,"end")
            main_Iy_text.delete(1.0,"end")
    
            main_Area_text.insert("end",((b*h)-(b1*h1)))#area
            main_Jx_text.insert("end",((b*(h**3)-(b1*(h1**3))))/12)#jx
            main_Jy_text.insert("end",((h*(b**3)-(h1*(b1**3))))/12)#jy
            main_Wx_text.insert("end",(b*(h**3)-b1*(h1**3))/(6*h))#Wx 
            main_Wy_text.insert("end",(h*(b**3)-h1*(b1**3))/6*b) #Wy
            main_Ix_text.insert("end",((b*(h**3)-b1*(h1**3))/(12*(b*h-b1*h1)))**0.5)#Ix 
            main_Iy_text.insert("end",((h*(b**3)-h1*(b1**3))/(12*(b*h-b1*h1)))**0.5)#Iy


        button = tk.Button(self,text="Расчитать", command=lambda:rac_tube())
        button.grid(row=13, column=3, sticky="ew")

        frame_results = tk.Frame(self)
        frame_results.grid(row=15, column=0, columnspan=7, rowspan=2, sticky="ew")

        for i,j in enumerate(("F", "Jx", "Jy", "Wx", "Wy", "Ix", "Iy")):
            frame_results.columnconfigure(i,weight=1)         
            tk.Label(frame_results, text="{0}".format(j),relief="ridge").grid(row=14, column=i)
            
        main_Area_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Area_text.grid(row=15, column=0)
        main_Jx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jx_text.grid(row=15, column=1)
        main_Jy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jy_text.grid(row=15, column=2)
        main_Wx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wx_text.grid(row=15, column=3)
        main_Wy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wy_text.grid(row=15, column=4)
        main_Ix_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Ix_text.grid(row=15, column=5)
        main_Iy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Iy_text.grid(row=15, column=6)    


class PageThee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page 3')
        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=1, columnspan=6)
        
        self.ractangle_photo = tk.PhotoImage(file="i1.gif")
        self.rac_tube_photo = tk.PhotoImage(file="i2.gif")
        self.isection_photo = tk.PhotoImage(file="i11.gif")
        self.tube_photo = tk.PhotoImage(file="i19.gif")
        self.circle_photo = tk.PhotoImage(file="i18.gif")

        main1_button = tk.Button(button_frame, image=self.ractangle_photo, command=lambda: controller.show_frame(PageOne))
        main2_button = tk.Button(button_frame, image=self.rac_tube_photo, command=lambda: controller.show_frame(PageTwo))
        main3_button = tk.Button(button_frame, image=self.isection_photo, relief="sunken", command=lambda: controller.show_frame(PageThee))
        main4_button = tk.Button(button_frame, image=self.tube_photo, command=lambda: controller.show_frame(PageFour))
        main5_button = tk.Button(button_frame, image=self.circle_photo, command=lambda: controller.show_frame(PageFive))           

        label.grid(row=5,column=3)

        picture_frame = tk.Frame(self, bg="red")
        picture_frame.grid(row=3,column=0,rowspan=8, columnspan=3, sticky="senw")
        
        self.photo_image = tk.PhotoImage(file="m11.gif")
        label_picture = tk.Label(picture_frame, image=self.photo_image)
        label_picture.grid(row=5, column=1, sticky="senw")

        right_frame = tk.Frame(self)
        right_frame.grid(row=3, column=3, rowspan=8, columnspan=4, sticky="senw")

        text1_label = tk.Label(right_frame, text="Ширина двутавра B =")
        text2_label = tk.Label(right_frame,text="Высота двутавра H =")
        main1_entry = tk.Entry(right_frame,width=10)
        main2_entry = tk.Entry(right_frame,width=10)
        text3_label = tk.Label(right_frame, text="Толщина b1 =")
        text4_label = tk.Label(right_frame,text="Толщина h1 =")
        main3_entry = tk.Entry(right_frame,width=10)
        main4_entry = tk.Entry(right_frame,width=10)
        
        text1_label.grid(row=3, column=3)
        text2_label.grid(row=5, column=3)
        text3_label.grid(row=7, column=3)
        text4_label.grid(row=8, column=3)
        main1_entry.grid(row=3, column=4)
        main2_entry.grid(row=5, column=4)
        main3_entry.grid(row=7, column=4)
        main4_entry.grid(row=8, column=4)

        main1_button.grid(row=1,column=2)
        main2_button.grid(row=1,column=3)
        main3_button.grid(row=1,column=4)
        main4_button.grid(row=1,column=5)
        main5_button.grid(row=1,column=6)

        def isection():
            B = float(main1_entry.get())
            H = float(main2_entry.get())
            b1 = float(main3_entry.get())
            h1 = float(main4_entry.get())

            main_Area_text.delete(1.0,"end")# 1.0 - first sumbol to the end "end"
            main_Jx_text.delete(1.0,"end")
            main_Jy_text.delete(1.0,"end")
            main_Wx_text.delete(1.0,"end")
            main_Wy_text.delete(1.0,"end")
            main_Ix_text.delete(1.0,"end")
            main_Iy_text.delete(1.0,"end")
    
            main_Area_text.insert("end",(2*B*h1+b1*H))#area 
            main_Jx_text.insert("end",((B*(H**3)-2*B*(H**3))/12))#jx 
            main_Jy_text.insert("end",((H*(b1**3)+2*h1*(B**3))/12))#jy 
            main_Wx_text.insert("end",((B*(H**3)-2*B*(H**3))/(6*H)))#Wx 
            main_Wy_text.insert("end",((H*(b1**3)+2*h1*(B**3))/6*B)) #Wy  
            main_Ix_text.insert("end",(((B*(H**3)-2*B*(H**3))/12)/(2*B*h1+b1*H))**0.5)#Ix 
            main_Iy_text.insert("end",(((H*(b1**3)+2*h1*(B**3))/12)/(2*B*h1+b1*H))**0.5)#Iy 

        button = tk.Button(self,text="Расчитать", command=lambda:isection())
        button.grid(row=13, column=3, sticky="ew")

        frame_results = tk.Frame(self)
        frame_results.grid(row=15, column=0, columnspan=7, rowspan=2, sticky="ew")

        for i,j in enumerate(("F", "Jx", "Jy", "Wx", "Wy", "Ix", "Iy")):
            frame_results.columnconfigure(i,weight=1)         
            tk.Label(frame_results, text="{0}".format(j),relief="ridge").grid(row=14, column=i)
            
        main_Area_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Area_text.grid(row=15, column=0)
        main_Jx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jx_text.grid(row=15, column=1)
        main_Jy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jy_text.grid(row=15, column=2)
        main_Wx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wx_text.grid(row=15, column=3)
        main_Wy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wy_text.grid(row=15, column=4)
        main_Ix_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Ix_text.grid(row=15, column=5)
        main_Iy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Iy_text.grid(row=15, column=6)

class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page 4')

        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=1, columnspan=6)

        self.ractangle_photo = tk.PhotoImage(file="i1.gif")
        self.rac_tube_photo = tk.PhotoImage(file="i2.gif")
        self.isection_photo = tk.PhotoImage(file="i11.gif")
        self.tube_photo = tk.PhotoImage(file="i19.gif")
        self.circle_photo = tk.PhotoImage(file="i18.gif")

        main1_button = tk.Button(button_frame, image=self.ractangle_photo, command=lambda: controller.show_frame(PageOne))
        main2_button = tk.Button(button_frame, image=self.rac_tube_photo, command=lambda: controller.show_frame(PageTwo))
        main3_button = tk.Button(button_frame, image=self.isection_photo, command=lambda: controller.show_frame(PageThee))
        main4_button = tk.Button(button_frame, image=self.tube_photo, relief="sunken", command=lambda: controller.show_frame(PageFour))
        main5_button = tk.Button(button_frame, image=self.circle_photo, command=lambda: controller.show_frame(PageFive))   
               
        label.grid(row=5,column=3)
        picture_frame = tk.Frame(self, bg="red")
        picture_frame.grid(row=3,column=0,rowspan=8, columnspan=3, sticky="senw")
        
        self.photo_image = tk.PhotoImage(file="m19.gif")
        label_picture = tk.Label(picture_frame, image=self.photo_image)
        label_picture.grid(row=5, column=1, sticky="senw")

        right_frame = tk.Frame(self)
        right_frame.grid(row=3, column=3, rowspan=8, columnspan=4, sticky="senw")

        text1_label = tk.Label(right_frame, text="Наружный диаметр d =")
        text2_label = tk.Label(right_frame,text="Толщина стенки s =")
        main1_entry = tk.Entry(right_frame,width=10)
        main2_entry = tk.Entry(right_frame,width=10)
        
        text1_label.grid(row=3, column=3)
        text2_label.grid(row=5, column=3)
        main1_entry.grid(row=3, column=4)
        main2_entry.grid(row=5, column=4)
        
        main1_button.grid(row=1,column=2)
        main2_button.grid(row=1,column=3)
        main3_button.grid(row=1,column=4)
        main4_button.grid(row=1,column=5)
        main5_button.grid(row=1,column=6)

        def tube():
            d = float(main1_entry.get())
            s = float(main2_entry.get())
            d1 = d-2*s

            main_Area_text.delete(1.0,"end")# 1.0 - first sumbol to the end "end"
            main_Jx_text.delete(1.0,"end")
            main_Jy_text.delete(1.0,"end")
            main_Wx_text.delete(1.0,"end")
            main_Wy_text.delete(1.0,"end")
            main_Ix_text.delete(1.0,"end")
            main_Iy_text.delete(1.0,"end")
    
            main_Area_text.insert("end",(pi*((d**2)-(d1**2))/4))#area  
            main_Jx_text.insert("end",(pi*((d**4)-(d1**4))/64))#jx  
            main_Jy_text.insert("end",(pi*((d**4)-(d1**4))/64))#jy  
            main_Wx_text.insert("end", 2*(pi*((d**4)-(d1**4))/64)/d)#Wx  
            main_Wy_text.insert("end", 2*(pi*((d**4)-(d1**4))/64)/d)#Wy   
            main_Ix_text.insert("end",((1/4)*((d**2)+(d1**2))**0.5 ))#Ix 
            main_Iy_text.insert("end",((1/4)*((d**2)+(d1**2))**0.5))#Iy  

        button = tk.Button(self,text="Расчитать", command=lambda:tube())
        button.grid(row=13, column=3, sticky="ew")

        frame_results = tk.Frame(self)
        frame_results.grid(row=15, column=0, columnspan=7, rowspan=2, sticky="ew")

        for i,j in enumerate(("F", "Jx", "Jy", "Wx", "Wy", "Ix", "Iy")):
            frame_results.columnconfigure(i,weight=1)         
            tk.Label(frame_results, text="{0}".format(j),relief="ridge").grid(row=14, column=i)
            
        main_Area_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Area_text.grid(row=15, column=0)
        main_Jx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jx_text.grid(row=15, column=1)
        main_Jy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jy_text.grid(row=15, column=2)
        main_Wx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wx_text.grid(row=15, column=3)
        main_Wy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wy_text.grid(row=15, column=4)
        main_Ix_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Ix_text.grid(row=15, column=5)
        main_Iy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Iy_text.grid(row=15, column=6)
        
class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page 5')

        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=1, columnspan=6)

        self.ractangle_photo = tk.PhotoImage(file="i1.gif")
        self.rac_tube_photo = tk.PhotoImage(file="i2.gif")
        self.isection_photo = tk.PhotoImage(file="i11.gif")
        self.tube_photo = tk.PhotoImage(file="i19.gif")
        self.circle_photo = tk.PhotoImage(file="i18.gif")

        main1_button = tk.Button(button_frame, image=self.ractangle_photo, command=lambda: controller.show_frame(PageOne))
        main2_button = tk.Button(button_frame, image=self.rac_tube_photo, command=lambda: controller.show_frame(PageTwo))
        main3_button = tk.Button(button_frame, image=self.isection_photo, command=lambda: controller.show_frame(PageThee))
        main4_button = tk.Button(button_frame, image=self.tube_photo, command=lambda: controller.show_frame(PageFour))
        main5_button = tk.Button(button_frame, image=self.circle_photo, relief="sunken", command=lambda: controller.show_frame(PageFive))
        
        label.grid(row=5,column=3)

        picture_frame = tk.Frame(self)
        picture_frame.grid(row=3, column=0, rowspan=8, columnspan=3, sticky="senw")

        self.photo_image = tk.PhotoImage(file="m18.gif")
        label_picture = tk.Label(picture_frame, image=self.photo_image)
        label_picture.grid(row=5, column=1, sticky="senw")

        right_frame = tk.Frame(self)
        right_frame.grid(row=3, column=3, rowspan=8, columnspan=4, sticky="senw")

        text1_label = tk.Label(right_frame, text="Наружный диаметр d =")
        main1_entry = tk.Entry(right_frame,width=10)
     
        text1_label.grid(row=3, column=3)
        main1_entry.grid(row=3, column=4)
        main1_button.grid(row=1,column=2)
        main2_button.grid(row=1,column=3)
        main3_button.grid(row=1,column=4)
        main4_button.grid(row=1,column=5)
        main5_button.grid(row=1,column=6)

        def circle():
            d = float(main1_entry.get())
                                
            main_Area_text.delete(1.0,"end")# 1.0 - first sumbol to the end "end"
            main_Jx_text.delete(1.0,"end")
            main_Jy_text.delete(1.0,"end")
            main_Wx_text.delete(1.0,"end")
            main_Wy_text.delete(1.0,"end")
            main_Ix_text.delete(1.0,"end")
            main_Iy_text.delete(1.0,"end")
    
            main_Area_text.insert("end", (pi*(d**2)/4))#area   
            main_Jx_text.insert("end", (pi*(d**4)/64))#jx   
            main_Jy_text.insert("end", (pi*(d**4)/64))#jy   
            main_Wx_text.insert("end", (2*(pi*(d**4)/64)/d))#Wx   
            main_Wy_text.insert("end", (2*(pi*(d**4)/64)/d))#Wy  
            main_Ix_text.insert("end",d/4)#Ix  
            main_Iy_text.insert("end",d/4)#Iy

        button = tk.Button(self,text="Расчитать", command=lambda:circle())
        button.grid(row=13, column=3, sticky="ew")

        frame_results = tk.Frame(self)
        frame_results.grid(row=15, column=0, columnspan=7, rowspan=2, sticky="ew")

        for i,j in enumerate(("F", "Jx", "Jy", "Wx", "Wy", "Ix", "Iy")):
            frame_results.columnconfigure(i,weight=1)         
            tk.Label(frame_results, text="{0}".format(j),relief="ridge").grid(row=14, column=i)
            
        main_Area_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Area_text.grid(row=15, column=0)
        main_Jx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jx_text.grid(row=15, column=1)
        main_Jy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Jy_text.grid(row=15, column=2)
        main_Wx_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wx_text.grid(row=15, column=3)
        main_Wy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Wy_text.grid(row=15, column=4)
        main_Ix_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Ix_text.grid(row=15, column=5)
        main_Iy_text = tk.Text(frame_results, width=10, height=1, wrap="word")
        main_Iy_text.grid(row=15, column=6)


test = Main()
test.mainloop()


