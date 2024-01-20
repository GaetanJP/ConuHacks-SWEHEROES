import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import json
from datetime import datetime


def load_data(json_file):
    with open(json_file, "r") as file:
        return json.load(file)


def parse_data(data):
    return [
        (datetime.fromisoformat(d["TimeStamp"]), d.get("OrderPrice", 0))
        for d in data
        if "OrderPrice" in d
    ]


def scale_data(data, width, height):
    timestamps = [d[0] for d in data]
    prices = [d[1] for d in data]
    min_time = min(timestamps)
    max_time = max(timestamps)
    min_price = min(prices)
    max_price = max(prices)

    norm_data = [
        (
            (timestamp - min_time).total_seconds()
            / (max_time - min_time).total_seconds()
            * width,
            (price - min_price) / (max_price - min_price) * height,
        )
        for timestamp, price in data
    ]
    return norm_data


def draw(data):
    glBegin(GL_LINES)
    for i in range(len(data) - 1):
        glVertex2f(data[i][0], data[i][1])
        glVertex2f(data[i + 1][0], data[i + 1][1])
    glEnd()


def main():
    data = load_data("./dataset/Exchange_3.json")
    parsed_data = parse_data(data)
    scaled_data = scale_data(parsed_data, 800, 600)  # Assuming window size 800x600

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw(scaled_data)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
