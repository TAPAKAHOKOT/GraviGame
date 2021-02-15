import pygame as pg
import os

from settings import Settings
from astro import Astro
from star import Star

os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (10, 10)

FPS = 30
pg.init()

size_x = 800
size_y = 800
screen = pg.display.set_mode((size_x, size_y), flags=pg.DOUBLEBUF | pg.NOFRAME)

surf = pg.Surface((size_x, size_y))
clock = pg.time.Clock()

settings = Settings(surf, (size_x, size_y))
settings.screen = screen
settings.max_dist = ( (settings.size[0])**2 + (settings.size[1])**2 )**0.5

while True:

	surf.fill((250, 250, 250))

	if (settings.mouse_start_pos):
		pg.draw.line(surf, (255, 0, 0), settings.mouse_start_pos, settings.mouse_pos)
	elif (settings.mouse_star_start_pos):
		pg.draw.line(surf, (0, 0, 255), settings.mouse_star_start_pos, settings.mouse_pos)


	for obj in settings.astros:
		for obj2 in settings.astros:
			obj.calcuate_force(obj2.m, obj2.pos)

		for st_obj in settings.stars:
			if(not obj.calcuate_force(st_obj.m, st_obj.pos)):
				settings.astros.remove(obj)
				break


		obj.update()
		obj.draw()

	for obj in settings.stars:
		for obj2 in settings.stars:
			obj.calcuate_force(obj2.m, obj2.pos)

		obj.update()
		obj.draw()


	clock.tick(FPS)

	screen.blit(surf, (0, 0))
		
	
	for i in pg.event.get():
		if i.type == pg.KEYDOWN:
			if i.key == 113 or i.key == 27:
				exit()
			else:
				print(i.key)
		
		if i.type == pg.MOUSEBUTTONDOWN:
			if i.button == 1:
				settings.mouse_start_pos = i.pos
			elif i.button == 3:
				settings.mouse_star_start_pos = i.pos

		elif i.type == pg.MOUSEBUTTONUP:
			if i.button == 1:
				x0, y0 = settings.mouse_start_pos
				x1, y1 = i.pos 

				r = ( (x1-x0)**2 + (y1-y0)**2 )**0.5

				if (r != 0):

					sp = ( r / settings.max_dist + 0.5)**2
					x_sp = settings.astro_max_speed * sp * ( (x0-x1) / (abs(x0-x1) + abs(y0-y1)) )
					y_sp = settings.astro_max_speed * sp * ( (y0-y1) / (abs(x0-x1) + abs(y0-y1)) )

					settings.astros.append(Astro([x0, y0], [x_sp, y_sp], settings))

				settings.mouse_start_pos = False

			elif i.button == 3:
				x0, y0 = settings.mouse_star_start_pos
				x1, y1 = i.pos 

				r = ( (x1-x0)**2 + (y1-y0)**2 )**0.5

				if (r != 0):

					sp = 0.3 * ( r / settings.max_dist + 0.5)**2
					x_sp = settings.star_max_speed * sp * ( (x0-x1) / (abs(x0-x1) + abs(y0-y1)) )
					y_sp = settings.star_max_speed * sp * ( (y0-y1) / (abs(x0-x1) + abs(y0-y1)) )
				else:
					x_sp = y_sp = 0

				settings.stars.append(Star([x0, y0], [x_sp, y_sp], settings))

				settings.mouse_star_start_pos = False
			elif i.button == 4:
				if (settings.cur_stars_m < settings.max_stars_m):

					if (settings.cur_stars_m >= 1000):
						settings.cur_stars_m += 500
					else:
						settings.cur_stars_m += 100

					print(settings.cur_stars_m)
			elif i.button == 5:
				if (settings.cur_stars_m > settings.min_stars_m):
					if (settings.cur_stars_m > 1000):
						settings.cur_stars_m -= 500
					else:
						settings.cur_stars_m -= 100

					print(settings.cur_stars_m)
			else:
				print(i)

		if i.type == pg.MOUSEMOTION:
			settings.mouse_pos = i.pos

	pg.display.update()
