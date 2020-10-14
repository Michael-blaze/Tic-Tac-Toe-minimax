from Game import Game


def main():
	game = Game()
	
	game.init()

	while True:

		while not game.over():
			game.input()
			game.draw()

		game.reset()
		

if __name__ == '__main__':
	main()
