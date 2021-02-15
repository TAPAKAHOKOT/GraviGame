from space_ogj import Space_obj
from pygame.draw import circle

class Star(Space_obj):
	def __init__(self, start_pos, start_speed, settings):
		super(Star, self).__init__(start_pos, start_speed, settings)

		self.m = settings.cur_stars_m
		self.G = 0.1 ** 8

	def draw(self):
		circle(self.settings.surf, (255, 255, 0), self.pos_to_int(self.pos), 8)

		for k, i in zip([90, 155, 205], [6, 4, 2]):
			circle(self.settings.surf, (255, 255 - k * (self.m / self.settings.max_stars_m), 0), self.pos_to_int(self.pos), i)