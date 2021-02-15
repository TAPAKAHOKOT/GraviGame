
class Space_obj:
	def __init__(self, start_pos, start_speed, settings):
		self.pos = start_pos
		self.speed = start_speed
		self.settings = settings

		self.m = 0
		self.G = 0

		self.pos_to_int = lambda k: [int(i) for i in k]

	def draw(self):
		circle(self.settings.surf, (255, 255, 255), self.pos_to_int(self.pos), 3)

	def update(self):
		self.pos[0] += self.speed[0]
		self.pos[1] += self.speed[1]

	def calcuate_force(self, m, pos):
		r = ( (self.pos[0] - pos[0])**2 + (self.pos[1] - pos[1])**2 )**0.5

		if ( r < 11):
			return False
		
		force = (self.G * (self.m * m) / (r**2)) * (1 -  (self.m / (m + self.m)) )

		self.speed[0] -= (self.pos[0] - pos[0]) * force
		self.speed[1] -= (self.pos[1] - pos[1]) * force

		return True