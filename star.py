from space_ogj import Space_obj
from pygame.draw import circle

class Star(Space_obj):
	def __init__(self, start_pos, start_speed, settings):
		super(Star, self).__init__(start_pos, start_speed, settings)

		self.m = settings.cur_stars_m
		self.G = 0.1 ** 8
		self.rad = 8

	def draw(self):
		if self.m >= 8000:
			self.m = 600000
			circle(self.settings.surf, (255, 165, 0), self.pos_to_int(self.pos), self.rad + 1)
			circle(self.settings.surf, (255, 255, 255), self.pos_to_int(self.pos), self.rad - 1)

			for k in range(4):
				n = 255 - 255 * (k / 4)
				circle(self.settings.surf, (n, n, n), self.pos_to_int(self.pos), 8 - k)
		else:
			circle(self.settings.surf, (255, 255, 0), self.pos_to_int(self.pos), self.rad)

			for k, i in zip([90, 155, 205], [6, 4, 2]):
				n = (self.m / self.settings.max_stars_m)
				n = 1 if n > 1 else n

				circle(self.settings.surf, (255, 255 - k * n, 0), self.pos_to_int(self.pos), i)