#!/usr/bin/env python
# coding: utf-8
import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
from data_preprocess import txt_preprocess
from model import preprocess_input, detect


def pop_up():
    if text.get(1.0, tk.END+"-1c"):
        result = text.get(1.0, tk.END+"-1c")
        result = txt_preprocess(result)
        result = preprocess_input(result)
        output = detect(result)
    # 彈出視窗
    messagebox.showinfo("評估結果", output)
    #括號裡面的兩個字串分別代表彈出視窗的標題(title)與要顯示的文字(index)


root = tk.Tk()

# 印出螢幕資訊
print(root.winfo_screenwidth()) # 印出螢幕寬度
print(root.winfo_screenheight()) # 印出螢幕高度

# 根據螢幕資訊 設定視窗大小及位置

# 350*200 -> 視窗大小 寬*高
# +200 -> 與螢幕左上x的距離
# +300 -> 與螢幕左上y的距離
root.geometry("500x300+300+150")

# 設定長寬鎖定, 可以用true or false去設定可否改變長寬
root.resizable(0,0)

# 設定標題名稱
root.title('AI假新聞辨識系統')

# 設定視窗顏色
root.configure(bg="#F2E6E6") 

# 設定標題圖示, 要用ico檔喔~
root.iconbitmap("標題icon.ico")

# 設定內文
label_1 = tk.Label(root,
                   text='請輸入欲查詢的內容',
                   height=1,width=15, # padding長寬
                   bg='#FCFCFC', #背景顏色
                   fg="#984B4B", # 前景顏色
                   font=("Algerian",20,"bold")) #字形

# 使用place定位來顯示label
label_1.place(x=110, y=10)

# 設定輸入框
text = Text(root, height=15, width = 60)
text.place(x = 40, y = 50)


# 設定確認的按鈕
btn_check = tk.Button(root, height=1, width=10, text="確認送出", command=pop_up)
btn_check.place(x=205, y = 260)


#讓程式繼續執行, 視窗按X就可以結束執行
root.mainloop() 




