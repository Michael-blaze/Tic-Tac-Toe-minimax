from Board import Board
import pygame
from AI import *
import sys
import time

class Game:
	def __init__(self):
		# -1 means the spot is empty
		#  0 means O
		#  1 means X

		self.Board = Board([
			[-1, -1, -1],
			[-1, -1, -1],
			[-1, -1, -1]
			])
 		
		self.game_over = False
		self.screen = 0 # dummy value

		self.font = 0 
		self.text = 0
		self.win_pos = 0

		self.turn = -1 # X turn
		self.x_score = 0
		self.o_score = 0

		self.scoreboard = f'Player - {self.x_score}                         Bot - {self.o_score}'

	def init(self):
		pygame.init()

		self.screen = pygame.display.set_mode((600, 640))
		self.screen.fill((255, 255, 255))

		for i in range(self.Board.n):
			for j in range(self.Board.n):
				pygame.draw.rect(self.screen, (0, 0, 0), (j * 200, 40 + i * 200, 200, 200), 5)

		pygame.display.update()

		self.font = pygame.font.SysFont("freesans", 20)
		self.text = self.font.render(self.scoreboard, True, (0, 255, 0))


		pygame.display.set_caption('Tic Tac Toe')
		
		self.screen.blit(self.text, (160, 10))

		self.Board.draw(self.screen)

		

		pygame.display.update()

	def input(self):
		# print(self.turn)
		if self.turn == -1:
			not_pressed = True
			while not_pressed:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					elif pygame.mouse.get_pressed()[0] == 1:
						x, y = pygame.mouse.get_pos()
						
						# for i in range(self.Board.n):
						# 	for j in range(self.Board.n):
						# 		if j * 200 <= x <= j * 200 + 200 and i * 200 <= y <= i * 200 + 200:
						# 			if self.Board.matrix[i][j] == -1:
						# 				self.Board.matrix[i][j] = 1
						# 				not_pressed = False
						# 				self.turn *= -1

						x = x // 200
						y = y // 200

						if x == 3:
							x -= 1
						if y == 3:
							y -= 1

						if self.Board.matrix[y][x] == -1:
							self.Board.matrix[y][x] = 1
							not_pressed = False
							self.turn *= -1
									
		else:
			self.Board = get_best_solution(self.Board)
			self.turn *= -1
		
	def draw(self):
		self.Board.draw(self.screen)

	def reset(self):
		self.game_over = False
		self.turn = -1

		self.Board = Board([
			[-1, -1, -1],
			[-1, -1, -1],
			[-1, -1, -1]
			])

		

		time.sleep(2)

		self.screen.fill((255, 255, 255))

		self.scoreboard = f'Player - {self.x_score}                         Bot - {self.o_score}'
		self.text = self.font.render(self.scoreboard, True, (0, 255, 0))

		self.screen.blit(self.text, (160, 10))

		for i in range(self.Board.n):
			for j in range(self.Board.n):
				pygame.draw.rect(self.screen, (0, 0, 0), (j * 200, 40 + i * 200, 200, 200), 5)

		pygame.display.update()

	def over(self):
		temp = self.Board.game_over()
		# print(temp)

		if temp == 2:
			return False

		if temp == 1:
			self.x_score += 1
		elif temp == 0:
			self.o_score += 1
			
		return True

		
		
				

