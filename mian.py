from tkinter import *
from spider import getsougou
from tkinter import ttk

root = Tk()

  

root.minsize("350","200")
root.maxsize("350","200")
root.title("搜狗图片爬取系统(简单版)")

label = Label(text="关键词：       ")
label.place(x=0,y=40)

tips = Label(text="Tips:   爬取的图片已经默认保存在F:\\spider_photos")
tips.place(x=50,y=130)


number = Label(text="爬取的图片数量：")
number.place(x=0,y=70)


number_entry = Entry() # 爬取数量的输入框
number_entry.place(x=140,y=70) # 位置


comboxlist=ttk.Combobox(root,width=17,textvariable=number) #初始化,创建一个下拉列表
comboxlist["values"]=("美女有沟必火",'明星薛之谦')
comboxlist.place(x=140,y=40)
comboxlist.focus()
    



def spider():
    
    keyword = comboxlist.get()
    number = number_entry.get()

    getsougou(keyword, number)
    
    
button = Button(text="开始爬取",command = spider)
button.place( x=130, y=100)

mainloop()
