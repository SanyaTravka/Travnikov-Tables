from tkinter import *
import math
from PIL import Image, ImageDraw, ImageFont


celWidth = 70
celHeight = 70
x0 = 100
y0 = 100


def DrawTable(ms, ks, mod, nBeg, nEnd, tableSize):
    im = Image.new('RGB', (1500, 1500), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.rectangle((x0-celWidth, y0-celHeight, celWidth*(tableSize+1.425), y0), fill='lightBlue', outline=(0, 0, 0))
    draw.rectangle((x0-celWidth, y0-celHeight, x0, celHeight*(tableSize+1.425)), fill='lightBlue', outline=(0, 0, 0))
    for i in range(tableSize+1):
        draw.line((x0+i*celWidth, y0-celHeight, x0+i*celWidth, y0+celHeight*tableSize), fill='black', width=1)
        draw.line((x0-celWidth, y0+i*celHeight, x0+celWidth*tableSize, y0+i*celHeight), fill='black', width=1)
    draw.line((x0-celWidth, y0-celHeight, x0, y0), fill='black', width=1)
    font = ImageFont.truetype(r'C:\Users\alext\Desktop\arial.ttf', 20)
    for i in range(tableSize):
        draw.text((x0+i*celWidth+5, y0-celHeight/1.5), str(ms+i), font=font, fill=(0, 0, 0, 255))
    for i in range(tableSize):
        draw.text((x0-celWidth+5, y0+(i+1)*celHeight-celHeight/1.5), str(ks+i), font=font, fill=(0, 0, 0, 255))
    draw.text((x0-celWidth+15,y0-celWidth*0.5),'k',font=font)
    draw.text((x0-celWidth*0.4,y0-celWidth*0.8),'m',font=font)
    fontB = ImageFont.truetype(r'C:\Users\alext\Desktop\arial.ttf', 20)
    beg = 0
    p = 1
    colorB = (0,0,0,255)
    colorR =  (255,0,0,255)
    if mod == 1 or mod == 4 or mod == 6 or mod == 8:
        beg = 1
        p = 0
    for k in range(beg+ks-1+p,tableSize+ks):
        for m in range(beg+ms-1+p,tableSize+ms):
            isPaint = True

            if mod == 1:
                x = (10*m+1)*(10*k+1)
                #kEnd = round((-1+2*math.sqrt(10*nEnd - 1))/10), 0)
                if m == 0 or k == 0:
                    isPaint = False
            if mod == 2:
                x = (10*m+3)*(10*k+7)
            if mod == 3:
                x = (10*m+9)*(10*k+9)
            if mod == 4:
                x = (10*m+1)*(10*k+3)
                if m == 0 or k == 0:
                    isPaint = False
            if mod == 5:
                x = (10*m+7)*(10*k+9)
            if mod == 6:
                x = (10*m+1)*(10*k+7)
                if m == 0 or k == 0:
                    isPaint = False
            if mod == 7:
                x = (10*m+3)*(10*k+9)
            if mod == 8:
                x = (10*m+1)*(10*k+9)
                if m == 0 or k == 0:
                    isPaint = False
            if mod == 9:
                x = (10*m+3)*(10*k+3)
            if mod == 10:
                x = (10*m+7)*(10*k+7)
            n = int((x-1)/10)

            if isPaint:
                if n >= nBeg and n <= nEnd:
                    draw.text((y0+(k-ks)*celHeight+15, x0+(m-ms)*celWidth+15),str(n),font = fontB, fill=colorR)
                else:
                    draw.text((y0+(k-ks)*celHeight+15, x0+(m-ms)*celWidth+15),str(n),font = fontB, fill=colorB)

    im.show()

root = Tk()
root.title("Travnikov table generation")
root.geometry("700x500")

header = Label(text="Table number:", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

tables = [("1.1", 1), ("1.2", 2), ("1.3", 3), ("2.1", 4),("2.2", 5),("3.1", 6),("3.2", 7),("4.1", 8),("4.2", 9),("4.3", 10)]


def select():
    l = table.get()

table = IntVar()

col = 1
for txt, val in tables:
    Radiobutton(text=txt, value=val, variable=table, padx=3, pady=5, command=select)\
        .grid(row=col+1, column = 0)
    col += 1


textK = Label(text="k:", padx=15, pady=10)
textM = Label(text="m:", padx=15, pady=10)
intBeg = Label(text="interval_Beg:", padx=15, pady=10)
intEnd = Label(text="interval_End:", padx=15, pady=10)
tablesCount = Label(text="tables_size:", padx=15, pady=10)

txtBegK = Entry(root,width=10)
txtBegM = Entry(root,width=10)
txtintBeg = Entry(root,width=10)
txtintEnd = Entry(root,width=10)
txttablesCount = Entry(root,width=10)

textK.grid(row=2,column=1)
txtBegK.grid(row=2,column=2)

textM.grid(row=2,column=3)
txtBegM.grid(row=2,column=4)

intBeg.grid(row=3,column=1)
txtintBeg.grid(row=3,column=2)

intEnd.grid(row=3,column=3)
txtintEnd.grid(row=3,column=4)

tablesCount.grid(row=4,column=3)
txttablesCount.grid(row=4,column=4)

def ClickedShow():
    m = int(txtBegM.get())
    k = int(txtBegK.get())
    mod = int(table.get())
    iBeg = int(txtintBeg.get())
    iEnd = int(txtintEnd.get())
    nBeg = round(iBeg/10,0)
    nEnd = round(iEnd/10,0)
    tCount = int(txttablesCount.get())
    if(iBeg<=iEnd):
        DrawTable(m,k,mod,nBeg,nEnd,tCount)
    else:
        print("Intevals error!")

btn = Button(root,text="Show",command=ClickedShow)
btn.grid(row=5,column=4)





#DrawTable(0,0,2)

root.mainloop()
