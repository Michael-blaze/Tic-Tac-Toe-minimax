import math
import copy

INF = 3000

def minimax(board, depth, minPlayer):
	state = board.game_over() 

	if state == 1:
		return depth + 10
	elif state == 0:
		return depth - 10 
	elif state == 3:
		return 0
	else:
		if minPlayer:
			min_value = INF

			for i in range(board.n):
				for j in range(board.n):
					if board.matrix[i][j] == -1:
						board.matrix[i][j] = 0

						value = minimax(board, depth + 1, not minPlayer)
						min_value = min(min_value, value)

						board.matrix[i][j] = -1
			# print(board.matrix, min_value)
			return min_value
		else:
			max_value = -INF

			for i in range(board.n):
				for j in range(board.n):
					if board.matrix[i][j] == -1:
						board.matrix[i][j] = 1

						value = minimax(board, depth + 1, not minPlayer)
						max_value = max(max_value, value)

						board.matrix[i][j] = -1
			return max_value


def get_best_solution(board):
	board_to_return = None
	best_solution_so_far = INF

	for i in range(board.n):
		for j in range(board.n):
			if board.matrix[i][j] == -1:
				board.matrix[i][j] = 0

				solution_value = minimax(board, 1, False)

				# print(board.matrix, solution_value)

				if solution_value < best_solution_so_far:
					best_solution_so_far = solution_value
					board_to_return = copy.deepcopy(board)

				board.matrix[i][j] = -1

	return board_to_return






