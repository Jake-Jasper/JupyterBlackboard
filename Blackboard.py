'''
Before starting the notebook I had to use this may be an issue when importing...

- jupyter nbextension enable --py widgetsnbextension

- modified from -https://hub.mybinder.turing.ac.uk/user/martinrenou-ipycanvas-jm1q0gth/lab/tree/examples/hand_drawing.ipynb

'''
from ipywidgets import Image

from ipywidgets import ColorPicker, IntSlider, link, AppLayout, HBox

from ipycanvas import RoughCanvas, hold_canvas, Canvas


class JupyterBlackboard:
    
    def __init__(self):
        self.width = 500
        self.height = 500
        
        self.canvas = Canvas(width=self.width, height=self.height)

        self.drawing = False
        self.position = None
        self.shape = []
        self.canvas.fill_style = "black"
        self.canvas.fill_rect(0, 0, 500, 500)


    def on_mouse_down(self, x, y):

        self.drawing = True
        self.position = (x, y)
        self.shape = [self.position]


    def on_mouse_move(self, x, y):
        
        if not self.drawing:
            return

        with hold_canvas(self.canvas):
            self.canvas.stroke_line(self.position[0], self.position[1], x, y)

            self.position = (x, y)

        self.shape.append(self.position)


    def on_mouse_up(self, x, y):

        self.drawing = False

        with hold_canvas(self.canvas):
            self.canvas.stroke_line(self.position[0], self.position[1], x, y)
            #self.canvas.fill_polygon(self.shape)

        self.shape = []

    def Draw(self):
        
        self.canvas.on_mouse_down(self.on_mouse_down)
        self.canvas.on_mouse_move(self.on_mouse_move)
        self.canvas.on_mouse_up(self.on_mouse_up)

        self.canvas.stroke_style = '#FFFFFF'

        self.picker = ColorPicker(description='Color:', value='#FFFFFF')

        link((self.picker, 'value'), (self.canvas, 'stroke_style'))
        link((self.picker, 'value'), (self.canvas, 'fill_style'))

        return HBox((self.canvas, self.picker))
    
