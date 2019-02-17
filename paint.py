from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0;
    DEFAULT_COLOR = 'red';

    def __init__(self):
        self.root = Tk();
        self.root.title("Doodle Maker.");
        
        self.pen_button = Button(self.root, text='PEN', command=self.use_pen,width=20,fg="red");
        self.pen_button.grid(row=0, column=0);
        
        self.color_button = Button(self.root, text='COLOR', command=self.choose_color,width=20,fg="green");
        self.color_button.grid(row=0, column=1);

        self.eraser_button = Button(self.root, text='ERASER', command=self.use_eraser,width=20,fg="blue");
        self.eraser_button.grid(row=0, column=2);
        
        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL,fg="DeepPink");
        self.choose_size_button.grid(row=0, column=3);

        self.c = Canvas(self.root, bg='white', width=1600, height=900);
        self.c.grid(row=1, columnspan=4);

        self.setup();
        self.root.mainloop();

    def setup(self):
        self.old_x = None;
        self.old_y = None;
        self.line_width = self.choose_size_button.get();
        self.color = self.DEFAULT_COLOR;
        self.eraser_on = False;
        self.active_button = self.pen_button;
        self.c.bind('<B1-Motion>', self.paint);
        self.c.bind('<ButtonRelease-1>', self.reset);

    def use_pen(self):
        self.activate_button(self.pen_button);

    def choose_color(self):
        self.eraser_on = False;
        self.color = askcolor(color=self.color)[1];

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True);
   
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED);
        some_button.config(relief=SUNKEN);
        self.active_button = some_button;
        self.eraser_on = eraser_mode;

    def paint(self, event):
        self.line_width = self.choose_size_button.get();
        paint_color = 'white' if self.eraser_on else self.color;
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36);
        self.old_x = event.x;
        self.old_y = event.y;

    def reset(self, event):
        self.old_x, self.old_y = None, None;

Paint();
