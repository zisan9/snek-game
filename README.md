Introduction:
This project aims to build a Snake Game on python using some pre-existing and new libraries. In this game, a Snake will appear in the middle of the window screen and food will generate randomly every time the snake eats the food. The length of the snake increases every time it eats the food. But at a certain point, the length of the snake will be fixed and it will not increase further.

Libraries Used:
-	OpenGL
-	Glut
-	Random
-	Pymsgbox

In-game Functions:
-	InitGrid() : Initializes the grid coordinates
-	unit() : draws a unit of the grid/ a square
-	drawGrid() : draws the full grid to columns and rows
-	drawSnake() : draws the initial snake with a fixed position and a direction
-	drawFood() : draws the food at a random position everytime

Others:
-	init() : used for changing the background color of the window
-	timer_callback() : called from the main function with glutTimerfunc in order to generate continuous loop which allows displaying new frame every time the function is called.
-	keyboard_Callback() : using glutSpecialKeyFunc() for the input of snake direction
-	display_Callback() : used for displaying the draw functions and then swapped buffers

Methodology: From the main function, glutDisplayFunc() method is called and passed an argument which is display_callback. Then inside the display_callback method, there are the main drawing functions of the game which are drawGrid(), drawSnake(), and drawFood(). 
From drawgrid() method, the program draws a 40x40 grid in the window screen and the lines are drawn by GL_LINES. To cover the whole area two for loops were implemented in which unit() handles the drawing process in every square in every row and column.
After drawing the grid, we move to draw the snake. Here, at first, the length of the snake is 5, and the max length of the snake will not cross 60. So, we declare two arrays(posX, posY) of size 60 and we fill the array with the initial position of the snake. The first 5 indexes of the arrays contain the X and Y positions of the array. Then after eating food, the snake's length increases by one. The keyboard inputs are also defined here which act as control of the snake. If the snake touches any of the borders of the display, the game is over and from pymsgbox, we display “Game Over” and show the score.
For drawing the food, we generate two random X and Y values from the Random library. The X and Y values range between 2 and 38 as we are excluding the border. At first, we set the boolean value of a variable ‘food’ to true and when it is true, the function will generate the coordinates and immediately set the food variable to false so that no new food can be generated while there’s an existing food already. Then using GL_LINES we draw and fill the food.   

Then, after displaying all the functions in the display_callback method, the buffers are swapped and after that, there’s an “if” condition to check if the game is over or not. If it is true then the program exits.   
