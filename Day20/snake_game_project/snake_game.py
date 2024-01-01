from turtle import Turtle 



STARTING_POSITION = [(0,0),(-20,0),(-40,0)] # Square box of the snake.
MOVE_DISTANCE = 20 # How much should the snake move forward.
UP = 90 # Direction of the Sanke north.
DOWN =270 # Direction of the snake using arrow key south.
RIGHT =0 # Direction of the snake using arrow key west.
LEFT =180 # Direction of the snake using arrow key east. 

# Making class Snake in which all the method will be store to use in main.py
class Snake:
    
    # The python __init__ method is declared within a class and is used 
    # to initialize the attributes of an object as soon as the object is formed

    def __init__(self) -> None:
        self.segment =[] # which store and the most imp part of the game it store the box which we created white box of snake
        self.create_snake() 
        self.head = self.segment[0]
    # Take ittrate in starting position and make 3 square box.
    def create_snake(self):
        for position in STARTING_POSITION:
             self.add_segment(position)
    # When ever snake eat the random circle one segmet will increse 
    def add_segment(self, position ): 
        new_segment = Turtle("square") # Make new_segment a turtle object so that we can acces fuction of the turtle module 
        new_segment.penup() # Now using new segment we use turtlr pen up method
        new_segment.color("orange")
        new_segment.goto(position)
        self.segment.append(new_segment)



       
    def extend(self):
         self.add_segment(self.segment[-1].pos())
         
   
    def move(self):
            for seg in range(len(self.segment) -1 ,0,-1):
                new_x =self.segment[seg - 1].xcor()
                new_y =self.segment[seg - 1].ycor()
                self.segment[seg].goto(new_x , new_y)
            
            self.head.forward(MOVE_DISTANCE)
    def up(self):
            if self.head.heading() != DOWN:
        
                self.head.setheading(UP)
    def right(self):
                        
        if self.head.heading() != LEFT:

        
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
        
            self.head.setheading(DOWN)