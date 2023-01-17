import numpy as np
import pandas as pd
import pygame
from sklearn.svm import SVC

if __name__ == '__main__':
    WIDTH = 500
    HEIGHT = 500
    FPS = 30
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    CLUSTERS = [RED, GREEN]
    POINT_RADIUS = 5

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SVM")
    clock = pygame.time.Clock()
    screen.fill(WHITE)
    pygame.display.flip()

    running = True
    points = pd.DataFrame(columns=['x', 'y', 'color'])
    points['x'] = points['x'].astype('int')
    points['y'] = points['y'].astype('int')
    points['color'] = points['color'].astype('int')

    svc = SVC(kernel='linear')
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                color = -1
                if event.button == 1:
                    color = 0
                elif event.button == 3:
                    color = 1

                pygame.draw.circle(screen, CLUSTERS[color], (x, y), POINT_RADIUS)
                new_point = pd.DataFrame({'x': [x],
                                          'y': [y],
                                          'color': [color]})
                points = pd.concat([points, new_point], ignore_index=True, axis=0)
                pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    svc.fit(points[['x', 'y']], points['color'])

                    w = svc.coef_[0]
                    b = svc.intercept_[0]

                    x_points = np.array([0, WIDTH])
                    y_points = -(w[0] / w[1]) * x_points - b / w[1]

                    pygame.draw.line(screen, BLACK, (x_points[0], y_points[0]), (x_points[1], y_points[1]))
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    x, y = pygame.mouse.get_pos()
                    color = -1

                    new_point = pd.DataFrame({'x': [x],
                                              'y': [y],
                                              })

                    color = svc.predict(new_point)[0]
                    pygame.draw.circle(screen, CLUSTERS[color], (x, y), POINT_RADIUS)
                    pygame.display.flip()
