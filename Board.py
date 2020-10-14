import numpy as np
import pygame

class Board:
	def __init__(self, matrix=np.array([])):
		self.matrix = matrix
		self.value = -1
		self.n = 3

	def game_over(self):
		# check principal diagonal

		if self.matrix[0][0] != -1 and self.matrix[0][0] == self.matrix[1][1]\
			and self.matrix[0][0] == self.matrix[2][2]:
			return self.matrix[0][0]
		

		# check secondary diagonal

		if self.matrix[0][self.n - 1] != -1 and self.matrix[0][self.n - 1] == self.matrix[1][self.n - 2]\
			and self.matrix[0][self.n - 1] == self.matrix[self.n - 1][0]:
			return self.matrix[0][self.n - 1]

		# check rows

		ok = False
		row = 0

		for i in range(0, self.n):
			val = self.matrix[i][0]
			
			if val != -1 and val == self.matrix[i][1] and val == self.matrix[i][2]:
				row = i
				ok = True
				break

		if ok:
			return self.matrix[row][0] 

		# check columns

		ok = False
		col = 0

		for j in range(0, self.n):
			val = self.matrix[0][j]
			
			if val != -1 and val == self.matrix[1][j] and val == self.matrix[2][j]:
				ok = True
				col = j
				break

		if ok:
			return self.matrix[0][col]

		#check if the game can go on
		for i in range(0, self.n):
			for j in range(0, self.n):
				if self.matrix[i][j] == -1:
					return 2

		# otherwise tie
		return 3

	def draw(self, screen):
		for i in range(self.n):
			for j in range(self.n):
				if self.matrix[i][j] == 1:
					pygame.draw.line(screen, (255, 0, 0), (j * 200 + 10, i * 200 + 10 + 40), (j * 200 + 190, i * 200 + 190 + 40), 5)
					pygame.draw.line(screen, (255, 0, 0), (j * 200 + 10, i * 200 + 190 + 40), (j * 200 + 190, i * 200 + 10 + 40), 5)
					
				elif self.matrix[i][j] == 0:
					center = ((j * 200 + j * 200 + 200) // 2, (i * 200 + i * 200 + 200 + 80) // 2) 
					radius = 80

					pygame.draw.circle(screen, (0, 0, 255) , center, radius, 5)

		pygame.display.update()
		
	def draw_winning_r_c_d(self, screen, temp):
		if 'p' in temp:
			pygame.draw.line(screen, (102, 252, 255), (10, 50), (590, 630), 5)
		elif 's' in temp:
			pygame.draw.line(screen, (102, 252, 255), (10, 630), (590, 50), 5)
		elif 'c' in temp:
			pygame.draw.line(screen, (102, 252, 255), (temp['c'] * 200 + 100, 50), (temp['c'] * 200 + 100, 630), 5)	
		elif 'r' in temp:
			pygame.draw.line(screen, (102, 252, 255), (10, 40 + temp['r'] * 200 + 100), (590, 40 + temp['r'] * 200 + 100), 5)
		pygame.display.update()