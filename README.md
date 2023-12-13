# Minecraft

A fork and modification of https://github.com/fogleman/Minecraft

## Goal

To allow kids to write python code in small files that hide the details to create 3D block structures in a Minecraft-like environment on a Windows environment. You can modify the files in an editor and then reload/render them without starting and stopping the window.

# Requirements

* Python 3
* Pyglet library. `pip install pyglet==1.5.27` if not already loaded.

## Usage

Run `python Minecraft.py MyCode.py` where `MyCode` is the name of a python file that contains the code (written by the student) that `Minecraft.py` will load in and render.

Consider using the `Run.bat` file that prompts for the file name; e.g. `MyCode`.
Or just type `run MyCode` at the command line.

For rapid development, you can open `MyCode.py` (for example) in your editor, make changes, switch to the Minecraft window, then hit `C` and `L` to reload and render your changes.

## Hotkeys

* `W`, `S`, `A`, `D` for standard Minecraft movement.
* `1`, `2`, `3` to change the stone to place. There are only three types of blocks you can place in this demo.
* `LEFT CLICK` remove a stone at the cursor.
* `RIGHT CLICK` add a stone at the cursor.
* Mouse to pan and scroll.
* `TAB` toggle flying. When flying, just point in the air and move. No double-space click needed.
* `SPACE` to jump.
* `ESCAPE` to exit window.
* `C` clear the board and reset.
* `L` to reload the file. Expect a pause while rendering.
* `H` to teleport back home; i.e. the default starting position.
* `M` generate hills. Expect a pause while rendering.
* `Q` quit.