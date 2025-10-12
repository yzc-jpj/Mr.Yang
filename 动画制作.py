from CodeVideoRenderer import*
import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title('动画')
root.geometry('300x400+100+100')

def new():
    textget=text.get('1.0','end-1c')
    video=CodeVideo(code_string=textget,language='Python')
    video.render()

label=tk.Label(root,text='编程动画生成',font='苹方,10')
label.pack()
notebook=ttk.Notebook(root)
notebook.pack(fill='both', expand=True)
frame=tk.Frame(notebook)
frame_2=tk.Frame(notebook)
notebook.add(frame,text='文本')
notebook.add(frame_2,text='渲染')
text=tk.Text(frame,font='苹方,9')
text.pack()
button=ttk.Button(frame_2,text='开始渲染',command=new)
button.pack()
root.mainloop()