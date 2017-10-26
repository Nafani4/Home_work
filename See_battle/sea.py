FRESH = '-'
DAMAGED = '!'
DESTROYED = 'X'
MISS = '.'


class Field(object):
	def __init__(self):
		self.field = [['-' for x in range(10)] for y in range(10)]
		self.dots = dict()

	def print_field(self):
		print('\n   А Б В Г Д Е Ж З И К')
		for index, row in enumerate(self.field, 1):
			print('{0: >2}'.format(index), ' '.join(row))
		print()

	def add_ship(self, ship):
		for dot in ship.get_dots():
			self.dots[dot.get_display()] = dot

	def display_dots(self):
		for dot in self.dots():
			row, col = dot.get_idx()
			status = dot.get_status()
			self.field[row][col] = 'K'  #status

	def strike(self, dot):
		row, col = int(dot[0]), int(dot[1])
		if dot not in self.dots.keys():
			self.field[row][col] = MISS
			return 'miss'
		elif self.dots.get(dot).get_status() == FRESH:
			self.field[row][col] = DAMAGED
			return 'damaged'
		return 'error'



class Ship(object):
	def __init__(self, dots):
		self.dots = self.set_dots(dots)
		self.decks = self.decks_left = len(dots)

	def set_dots(self, dots):
		result = []
		for row, col in dots:
			result.append(Dot(row, col, self))
		return result

	def get_dots(self):
		return self.dots

	def strike(self):
		self.decks_left -= 1
		return self.get_status()

	def get_status(self):
		if self.decks_left == self.decks:
			return 'not damaged'
		elif self.decks_left == 0:
			return 'destroyed'
		return 'damaged'


class Dot(object):
	def __init__(self, row, col, ship):
		self.row = row
		self.col = col
		self.display = '{}{}'.format(row, col)
		self.ship = ship
		self.status = FRESH

	def set_status(self, status):
		self.status = status

	def get_ship(self):
		return self.ship

	def get_idx(self):
		return self.row, self.col

	def get_display(self):
		return self.display

	def get_status(self):
		return self.status


def main():
	field = Field()
	field.print_field()
	ship = Ship([(2,2), (2,3), (2,4)])
	field.add_ship(ship)
	field.print_field()
	print(field.strike('23'))
	field.print_field()


if __name__ == '__main__':
	main()
