'''
Before starting the notebook I had to use this may be an issue when importing...

- jupyter nbextension enable --py widgetsnbextension

- modified from -https://hub.mybinder.turing.ac.uk/user/martinrenou-ipycanvas-jm1q0gth/lab/tree/examples/hand_drawing.ipynb

'''

from ipywidgets import Image, ColorPicker, IntSlider, link, AppLayout, HBox, VBox, widgets

from ipycanvas import RoughCanvas, hold_canvas, Canvas


class JupyterBlackboard:
    
    def __init__(self):
        self.width = 1000
        self.height = 500
        
        self.canvas = Canvas(width=self.width, height=self.height, sync_image_data=True)

        self.drawing = False
        self.position = None
        self.shape = []
        self.canvas.fill_style = "black"
        self.canvas.fill_rect(0, 0, 1000, 500)

    def on_mouse_down(self, x, y):
        '''
        When left click mouse
        '''
        self.drawing = True
        self.position = (x, y)
        self.shape = [self.position]


    def on_mouse_move(self, x, y):
        '''
        When moving the mouse
        '''
        
        if not self.drawing:
            return

        with hold_canvas(self.canvas):
            self.canvas.stroke_line(self.position[0], self.position[1], x, y)

            self.position = (x, y)

        self.shape.append(self.position)


    def on_mouse_up(self, x, y):
        '''
        I think this is when you let go of left click
        '''
        self.drawing = False

        with hold_canvas(self.canvas):
            self.canvas.stroke_line(self.position[0], self.position[1], x, y)
        
        self.shape = []
       
    def undo_last(self, *args):
        print(self.canvas.restore())
        #del self.shape[-1]
        
    def redraw(self, *args):
        '''
        Reset Canvas
        '''
        
        self.canvas.clear()
        self.canvas.fill_style = "black"
        self.canvas.fill_rect(0, 0, 1000, 500)
        self.canvas.stroke_style = '#FFFFFF'
        
    def save_to_file(self, *args, **kwargs):
        self.canvas.to_file('blackboard.png')
        
        # Listen to changes on the ``image_data`` trait and call ``save_to_file`` when it
        # changes
        self.canvas.observe(self.save_to_file, 'image_data')
        


    def Draw(self):
        
        self.canvas.on_mouse_down(self.on_mouse_down)
        self.canvas.on_mouse_move(self.on_mouse_move)
        self.canvas.on_mouse_up(self.on_mouse_up)

        self.canvas.stroke_style = '#FFFFFF'

        self.picker = ColorPicker(description='Color:', value='#FFFFFF')

        link((self.picker, 'value'), (self.canvas, 'stroke_style'))
        link((self.picker, 'value'), (self.canvas, 'fill_style'))
        
        self.reset_button = widgets.Button(description='Reset')
        self.reset_button.on_click(self.redraw)
        
        self.save_button = widgets.Button(description='Save')
        self.save_button.on_click(self.save_to_file)
        
        return VBox((self.canvas, self.picker, self.reset_button, self.save_button))
    
if __name__ == "__main__":
    JupyterBlackboard()
