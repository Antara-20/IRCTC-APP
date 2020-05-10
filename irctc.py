from tkinter import*
import requests

class Irctc:

    def __init__(self):
        self.root=Tk()
        self.root.title("Train Route")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)

        self.root.configure(background="#00a65a")

        self.label1=Label(self.root,text="Train Route",bg="#00a65a",fg="#fff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(30,10))

        self.trainNo=Entry(self.root)
        self.trainNo.pack(ipadx=40,ipady=5)

        self.click=Button(self.root,text="Fetch Stations",bg="#fff",fg="#000",width=25,height=2,command=lambda:self.__fetch())
        self.click.configure(font=("Constantia",10))
        self.click.pack(pady=(10,20))


        self.result=Label(self.root,text="",bg="#00a65a",fg="#fff")
        self.result.configure(font=("Constantia",14))
        self.result.pack(pady=(5,10))


        self.root.mainloop()

    def __fetch(self):
        train=self.trainNo.get()
        print(train)
        url="https://api.railwayapi.com/v2/route/train/{}/apikey/ch7i0nwyve/".format(train)
        response=requests.get(url)
        data=response.json()



        stations=""
       
        for i in data['route']:
            stations+=i['station']['name']+"|"+ str(i['distance'])+"KM"+"|"+str(i['scharr'])+"|"+str(i['schdep'])+"\n"
            
      
        self.result.configure(text=stations)
        
        
        
obj=Irctc()
