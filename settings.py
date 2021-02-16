
class Settings:
	def __init__(self, surf, size):
		self.surf = surf
		self.size = size
		self.max_dist = 0

		self.astro_max_speed = 30
		self.star_max_speed = 5

		self.mouse_start_pos = False
		self.mouse_star_start_pos = False
		self.mouse_pos = False

		self.cur_stars_m = 1000
		self.max_stars_m = 2000
		self.min_stars_m = 200

		self.max_speed = 30

		self.astros = []
		self.stars = []