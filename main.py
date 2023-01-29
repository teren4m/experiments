import numpy as np
import pygame

img = np.full((3,2,3), fill_value=1,dtype=np.uint8)
surf = pygame.surfarray.make_surface(img)
print(img.shape)
print(surf.get_bitsize())

# pygame.init()
# display = pygame.display.set_mode((350, 350))
# x = np.arange(0, 300)
# y = np.arange(0, 300)
# X, Y = np.meshgrid(x, y)
# print(X)
# Z = X + Y
# Z = 255*Z/Z.max()
# surf = pygame.surfarray.make_surface(Z)
# print(display.get_bitsize())

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     display.blit(surf, (0, 0))
#     pygame.display.update()
# pygame.quit()