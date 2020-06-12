import numpy as np

# these our the rankings of hands
# straight flush, 4 of a kind, full house, flush, straight, trips, 2 pair, pair, high card
rankings = ['sf', '4p', 'fh', 'flush', 'straight', '3p', '2p', 'p', 'hc']

class pokerDeck():
	def __init__(self):
		self.currentDeck = {}
		self.table = []
		self.cards = np.array(["2_S", "3_S", "4_S", "5_S", "6_S", "7_S", "8_S", "9_S", "10_S", "11_S", "12_S", "13_S", "14_S",
                               "2_H", "3_H", "4_H", "5_H", "6_H", "7_H", "8_H", "9_H", "10_H", "11_H", "12_H", "13_H", "14_H",
                               "2_C", "3_C", "4_C", "5_C", "6_C", "7_C", "8_C", "9_C", "10_C", "11_C", "12_C", "13_C", "14_C",
                               "2_D", "3_D", "4_D", "5_D", "6_D", "7_D", "8_D", "9_D", "10_D", "11_D", "12_D", "13_D", "14_D"])
		# heads up poker game
		self.players = 5

	def shuffleDeck(self):
		self.table = []
		self.currentDeck = list(self.cards)
		np.random.shuffle(self.currentDeck)

	def dealCards(self):
		self.pokerhands = {}

		for i in range(self.players):
			cards = []
			for j in range(2):
				cards.append(self.currentDeck[0])
		# 		tableHands[i, j] = self.currentDeck[0]

				self.currentDeck.pop(0)
			self.pokerhands[i] = hand(cards[0], cards[1])
			self.pokerhands[i].adjust_suitcounts()
			self.pokerhands[i].gethighcard()

	def playhand(self):
		self.board = Board(self.currentDeck)
		print(type(self.currentDeck))
		self.currentDeck = self.board.flop()
		print(self.board.cards)
		self.currentDeck = self.board.turn()
		print(self.board.cards)

		self.currentDeck = self.board.river()
		print(self.board.cards)

class Board():
	def __init__(self, currentdeck):
		self.place = 'preflop'
		self.cards = []
		self.currentdeck = currentdeck
	def flop(self):

		for i in range(3):
			self.cards.append(self.currentdeck[0])
			print(self.currentdeck[0])
			self.currentdeck.pop(0)
		return self.currentdeck
	def turn(self):
		self.cards.append(self.currentdeck[0])
		self.currentdeck.pop(0)
		return self.currentdeck

	def river(self):
		self.cards.append(self.currentdeck[0])
		self.currentdeck.pop(0)
		return self.currentdeck

class hand():
	def __init__(self, card1, card2):
		self.cards = [card1, card2]
		self.best = '2 High'
		self.highcard = 2
		self.all_cards = self.cards
		self.suitcounts = {'H': 0, 'D': 0, 'S': 0, 'C': 0}
		self.numbercounts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
	def gethighcard(self):
		for card in self.cards:
			number = int(card.split("_")[0])
			if number > self.highcard:
				self.highcard = number
		print(self.highcard)

	def adjust_suitcounts(self):
		suits = [self.cards[0].split("_")[1], self.cards[1].split("_")[1]]
		print(self.cards)
		for i in range(2):
			self.suitcounts[suits[i]] = self.suitcounts[suits[i]] + 1
		print(self.suitcounts)
		# print(tableHands[1, 1])
		# return tableHands

	def adjust_numbers(self):
		self.all_cards = self.cards + cards
		for i in range(len(self.all_cards)):
			self.numbercounts[self.all_cards[i]] = self.numbercounts[self.all_cards[i]] + 1

	def analyze_board(self, cards):
		self.all_cards = self.cards + cards

h = pokerDeck()
h.shuffleDeck()
h.dealCards()
h.playhand()