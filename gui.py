import transmitter as tm
import tkinter as tk

def main():
    ser = tm.openSerial()


    root =  tk.Tk()
    root.title("LibreT6")

    c_width = 500
    c_height = 400
    c = tk.Canvas(root, width=c_width, height=c_height, bg= 'white')
    c.pack()
    drawChannelsOutline(c)
    exit = 0
    while exit == 0:
        channels = tm.getChannelPositions(ser)
        c.delete("ch")
        drawnChannel = drawChannels(c, channels)
        c.update()

    root.mainloop()

def drawChannels(c, channels):
    # gap between canvas edge and y axis
    xgap = 30
    # gap between canvas edge and x axis
    ygap = 20
    # spacing between graphs
    yspacing = 15
    ywidth = 25
    xlength = 300
    for i in range(6):
        x0 = xgap 
        y0 = ygap + i*ywidth + i*yspacing
        y1 = ygap + (i+1)*ywidth + i*yspacing
        chlength = xgap + ((channels[i+1] - 1000)*xlength / 1024)
        c.create_rectangle(x0, y0 , chlength, y1, fill = "blue", tags=("ch"))

def drawChannelsOutline(c):
    # gap between canvas edge and y axis
    xgap = 30
    # gap between canvas edge and x axis
    ygap = 20
    # spacing between graphs
    yspacing = 15
    ywidth = 25
    xlength = 300
    for i in range(6):
        x0 = xgap
        y0 = ygap + i*ywidth + i*yspacing
        x1 = xgap + xlength
        y1 = ygap + (i+1)*ywidth + i*yspacing
        c.create_rectangle(x0, y0 , x1, y1, fill = "white")
        c.create_text(x0, y0+6, anchor=tk.NE, text="ch" + str(i+1))

if __name__ == "__main__":
    main()
