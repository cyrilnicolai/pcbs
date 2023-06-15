import math
from tkinter import Tk, Canvas, Button, Toplevel, Label, Entry, mainloop
from random import randrange, choice

class Star:
    __slots__ = ['x', 'y', 'z', 'id', 'radius', 'color']

    ## Star properties
    def __init__(self, x, y, z, color):
        self.id = None #ID of the star's oval shape on the canvas
        self.x = x
        self.y = y
        self.z = z
        self.radius = 1
        self.color = color

class StarField:

    def __init__(self, width, height, depth=32, num_stars=500): 
        # Initialize the main window
        self.master = Tk()
        self.master.attributes('-fullscreen', True)  # Set the main window to fullscreen
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

        # Create a canvas within the main window
        self.canvas = Canvas(self.master, width=width, height=height, bg="#000000")
        self.canvas.pack()

        # Generate stars with random positions, depths, and colors
        for _ in range(num_stars):
            color = choice(["pink", "pink", "pink", "pink", "pink", "yellow"])  # Randomly choose the color for each star
            star = Star(x=randrange(-self.width, self.width),
                        y=randrange(-self.height, self.height),
                        z=randrange(1, self.max_depth),
                        color=color)
            star.id = self.canvas.create_oval(star.x - star.radius, star.y - star.radius, star.x + star.radius, star.y + star.radius)
            self.stars.append(star)

        self.animation_id = None
        self.draw()
        self.master.after(4000, self.change_color)  # Schedule color change after 1 second
        self.master.after(20000, self.display_question)
        mainloop()

    def draw(self):
        # Update the positions, sizes, and colors of the stars
        for star in self.stars:
            # Move the star towards the viewer (decrease its depth)
            star.z -= 0.8

            # Calculate the radius and fill color of the star based on its depth
            star.radius = (1 - float(star.z) / self.max_depth) * 3.3

            # Reset the star's position if it goes behind the viewer
            if star.z <= 0:
                # Regenerate the star at a random position and depth
                star.x = randrange(-self.width, self.width)
                star.y = randrange(-self.height, self.height)
                star.z = self.max_depth
                star.radius = 1

            # Convert 3D coordinates to 2D using perspective projection
            factor = self.fov / (self.view_distance + star.z)
            x = star.x * factor + self.width / 2
            y = -star.y * factor + self.height / 2

            # Update the position and color of the star on the canvas
            self.canvas.coords(star.id, x - star.radius, y - star.radius, x + star.radius, y + star.radius)
            self.canvas.itemconfig(star.id, fill=star.color)

        # Schedule the next frame update
        self.animation_id = self.canvas.after(30, self.draw)

    def change_color(self):
        # Randomly change the color of the stars between yellow and pink
        for star in self.stars:
            if star.color == "yellow":
                star.color = choice(["yellow", "pink", "pink", "pink", "pink", "pink", "pink","pink","pink","pink",])  # Randomly choose the next color between yellow and pink
            else:
                star.color = choice(["yellow", "yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","pink"])  # Randomly choose the next color between red and blue

            self.canvas.itemconfig(star.id, fill=star.color)  # Update the color of each star on the canvas

        # Schedule the next color change
        self.master.after(4000, self.change_color)

    def display_question(self):
        # Stop the animation and create a new window for asking questions
        self.stop_animation()
        question_window = Toplevel(self.master)
        question_window.title("Question")
        question_window.attributes('-fullscreen', True)  # Set the question window to fullscreen

        questions = [
            "Which color did dominate last? Pink or yellow?",
            "How long (in seconds) was the waiting time?",
            "How fast did the time pass? (Very Slow, Slow, Neutral, Fast, Very Fast)"
        ]

        question_label = Label(question_window, text=questions[0])
        question_label.pack()

        response_entry = Entry(question_window)
        response_entry.pack()

        current_question_index = [0]  # Use a list to store the current question index

        def next_question():
            # Move to the next question or submit the responses
            current_question_index[0] += 1
            if current_question_index[0] < len(questions):
                question_label.config(text=questions[current_question_index[0]])
                response_entry.delete(0, END)
            else:
                submit_response()

        submit_button = Button(question_window, text="Submit", command=next_question)
        submit_button.pack()

        def submit_response():
            # Handle the submitted responses and close the question window
            response = response_entry.get()
            print("Response:", response)
            question_window.destroy()

        question_window.protocol("WM_DELETE_WINDOW", submit_response)  # Handle window close event

    def stop_animation(self):
        # Cancel the animation callback if it's active
        if self.animation_id is not None:
            self.canvas.after_cancel(self.animation_id)

if __name__ == '__main__':
    # Create an instance of the StarField class with specified dimensions
    s = StarField(1920, 1080)



#(1)The script imports necessary modules: math, tkinter, and random.
#(2)The Star class represents a star in the starfield. It has attributes for the position (x, y, z), unique identifier (id), radius, and color.
#(3)The StarField class is responsible for creating the starfield animation. It initializes the main window, sets the fullscreen mode, and creates a canvas.
#(4)Stars are created randomly and added to a list. Each star is represented by an instance of the Star class. The stars are initially positioned randomly within the window and given a random depth and color.
#(5)The draw method updates the position and size of the stars based on their depth and distance from the viewer. It also handles star regeneration when a star reaches the viewer.
#(6)The change_color method randomly changes the color of the stars between yellow and pink.
#(7)The display_question method stops the animation, creates a new fullscreen window (Toplevel) for asking questions, and handles user input.
#(8)The stop_animation method cancels the animation by canceling the scheduled after callback.
#(9)In the __main__ block, an instance of the StarField class is created, specifying the dimensions of the window.
