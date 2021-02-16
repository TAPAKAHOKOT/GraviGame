from space_ogj import Space_obj
from pygame.draw import circle

class Astro(Space_obj):
	def __init__(self, start_pos, start_speed, settings):
		super(Astro, self).__init__(start_pos, start_speed, settings)

		self.m = 0.01
		self.G = 2.3
		self.rad = 3

		self.tail_size = 10
		self.tail = [[0, 0] for k in range(self.tail_size)]

	def draw(self):
		sp_k = (abs(self.speed[0]) + abs(self.speed[1])) / 80
		sp_k = 1 if sp_k > 1 else sp_k
		circle(self.settings.surf, (255, 255 - 255 * sp_k, 255 - 255 * sp_k), self.pos_to_int(self.pos), 4)
		
		for dot in self.tail:
			circle(self.settings.surf, (255, 0, 0), self.pos_to_int(dot), 0)

		circle(self.settings.surf, (0, 0, 0), self.pos_to_int(self.pos), self.rad)

	def update(self):
		for k in range(1, self.tail_size):
			self.tail[-k] = self.tail[-k-1]
		self.tail[0] = [*self.pos]

		self.pos[0] += self.speed[0]
		self.pos[1] += self.speed[1]


