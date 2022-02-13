# Make a blackboard that can be used with Jupyter notebooks

Sometime I want to visualise something while I am working in a notebook. This is that.


# TODO:
- Need to have an undo function
    - Think I have to save all objects and redraw...
- Need to have a save function
- Need to stop the bug where if you go off the canvas and then come back on the line starts from the last point
- Auto-scale canvas size
- Adjustable line width

# Usage

`import Blackboard

jb = Blackboard.JupyterBlackboard()

jb.Draw()`