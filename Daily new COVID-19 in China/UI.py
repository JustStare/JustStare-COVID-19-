from tkinter import *
from update import *
import webbrowser

def run_tk():

    root=Tk()
    root.geometry('300x440')
    b1 = Button(root,text='生成可视化图表',command=lambda : updateChart())
    b1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.2)
    # b2 = Button(root,text="具体查询某一天数据",command=lambda :chaxun_chart())
    # b2.place(relx=0.3 ,rely = 0.4 ,relwidth = 0.4,relheight=0.2)
    b3 = Button(root, text="退出", command=root.destroy)
    b3.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.15)
    root.mainloop()
    webbrowser.open('中国每日新冠病毒阳性人数.html')

if __name__ == '__main__':
    run_tk()