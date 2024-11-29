make a js script for drawing circles on a 1000x1000 pixel grid, functions implemented as below with parameters:
circle( obj_id(int), radius (pixels), fill (True or False), fill_color (RGB Tuple), outline (True or False), outline_color (RGB TUple))   -    draws a cicle, always spawns in the middle of the drawing board, assigns obj id to it, next circle will always be below the first circle in layers
up(number_of_pixels (int))     -    moves the circle up by specified number of pixel values, simply calling the function will result in movement by 1 pixel
down(number_of_pixels (int))     -    moves the circle down by specified number of pixel values, simply calling the function will result in movement by 1 pixel
left(number_of_pixels (int))     -    moves the circle left by specified number of pixel values, simply calling the function will result in movement by 1 pixel
right(number_of_pixels (int))     -    moves the circle right by specified number of pixel values, simply calling the function will result in movement by 1 pixel
move_to_top(obj_id(int))    -   on valid obj id, moves the specified obj up one layer
move_to_bottom(obj_id(int))    -   on valid obj id, moves the specified obj down one layer
resize(obj_id(int), new_size(int))    -  on valid obj id, resizes the obj to sepcified size
kill ( obj_id (int))     -      on valid obj id, removes the object
highlight (obj_id (int), highlight_color(RGB Tuple))         -     on valid obj, highlights the object in the specified color
recolor (obj_id (int), color(RGB Tuple))     -     on valid obj id, recolors the object to specified colors
remove_fill
remove_outline



#to improve typeshit
add a game with four levels of difficulty, easy is simple image in greyscale, medium is simple image but with color, hard is a bit complex with colors, impossible is fucking impossible




#lets add an autofill and showing of parameters like we have in vscode
