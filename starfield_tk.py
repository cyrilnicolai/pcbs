import math
from tkinter import Tk, Canvas, mainloop
from random import randrange


class Star:
    __slots__ = ['x', 'y', 'z', 'id', 'radius', 'fill']

    def __init__(self, x, y, z) -> None:
        super().__init__()
        
        ## Star properties
        self.id = None #ID of the star's oval shape on the canvas
        self.x = x
        self.y = y
        self.z = z
        self.radius = 1
        self.fill = 0


class StarField:

    def __init__(self, width, height, depth=32, num_stars=500):     # Create the main Tkinter window
        self.master = Tk()
        self.master.title("StarField")
        self.master.resizable(False, False)
        self.master.maxsize(width, height)
        
        # Conversion factor from degrees to radians for field of view
        self.fov = 180 * math.pi / 180
        
        # Distance from the viewer to the screen (initialized as 0)
        self.view_distance = 0
        
        # List to store the Star objects representing the stars
        self.stars = []
        
        # Dimensions of the window and the depth of the star field
        self.width = width
        self.height = height
        self.max_depth = depth
        
        # Create a canvas to draw the stars
        self.canvas = Canvas(self.master, width=width, height=height, bg="#000000")
        self.canvas.pack()


	 # Create the specified number of stars with random positions and depths
        for x in range(num_stars):
            star = Star(x=randrange(-self.width, self.width),
                        y=randrange(-self.height, self.height),
                        z=randrange(1, self.max_depth))
                        
            # Create an oval shape representing the star and store its ID
            star.id = self.canvas.create_oval(star.x - star.radius, star.y - star.radius, star.x + star.radius, star.y + star.radius,
                                              fill='#FFFFFF')
            self.stars.append(star)
            
        # Start the animation loop
        self.draw()
        mainloop()

    def draw(self):
        for star in self.stars:
            # Move the star towards the viewer (decrease its depth)
            star.z -= 0.8

            # Calculate the radius and fill color of the star based on its depth
            star.radius = (1 - float(star.z) / self.max_depth) * 1.7
            star.fill = int((1 - float(star.z) / self.max_depth) * 255)

            # Reset the star's position if it goes behind the viewer
            if star.z <= 0:
                star.x = randrange(-self.width, self.width)
                star.y = randrange(-self.height, self.height)
                star.z = self.max_depth
                star.radius = 1
                star.fill = 0

            # Convert 3D coordinates to 2D using perspective projection
            factor = self.fov / (self.view_distance + star.z)
            x = star.x * factor + self.width / 2
            y = -star.y * factor + self.height / 2

            # Update the position and color of the star in the canvas
            self.canvas.coords(star.id, x - star.radius, y - star.radius, x + star.radius, y + star.radius)
            self.canvas.itemconfig(star.id, fill='#%02x%02x%02x' % (star.fill, star.fill, star.fill))

        self.canvas.after(30, self.draw)


if __name__ == '__main__':
    s = StarField(800, 600)
