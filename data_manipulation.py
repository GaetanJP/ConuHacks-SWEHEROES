import parser_script
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from datetime import datetime
import json


def parse_data(data, symbol, exchange):
    # Filter data based on the symbol and exchange
    return [
        (datetime.fromisoformat(d['TimeStamp']), d['OrderPrice'])
        for d in data if d['Symbol'] == symbol and d['Exchange'] == exchange and 'OrderPrice' in d
    ]

def draw(data):
    # This function is responsible for drawing the data
    glBegin(GL_LINES)
    for i, (timestamp, price) in enumerate(data):
        x = i * 0.1  # This is a placeholder for actual x-coordinate logic
        y = price    # This is a placeholder for actual y-coordinate logic
        glVertex2f(x, y)
    glEnd()

def main():
    all_datas = parser_script.parse(
        "./dataset/Exchange_1.json",
        "./dataset/Exchange_2.json",
        "./dataset/Exchange_3.json",
    )
    
    for data in all_datas:
        parsed_data = parse_data(data, '5AV4I', 'Exchange_3')
    
    # Initialize Pygame and the OpenGL context
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    # Set up your OpenGL context here
    # ...

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen, and set up the view
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # Call the draw function with your parsed data
        draw(parsed_data)
        
        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
