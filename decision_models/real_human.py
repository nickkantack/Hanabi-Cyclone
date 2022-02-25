
from decision_models.decision_model import DecisionModel
import util.observation_reader as ob_reader
import copy
from util.decision_basis import DecisionBasis
import jsonpickle

RECORD_HUMAN_ACTIONS = False

class RealHuman(DecisionModel):

	"""
	This is an interactive decision model that allows a human observer to make decisions via the console. This decision model is named after the developer.
	"""

	def get_variant_name(self):
		return f"RealHuman"

	def decide_move(self, observation, my_not_clues, other_player_not_clues, playable_probabilities, safely_discardable_probabilities, unneeded_probabilities,
	hint_nuggets, singled_out_playable_card_index, singled_out_cards, say):
		
		legal_moves = ob_reader.get_legal_moves(observation)
		if len(legal_moves) == 0:
			return None, None, None
	
		observation_to_show = copy.deepcopy(observation)
		observation_to_show["card_knowledge"][1] = []
		observation_to_show["legal_moves"] = []
		observation_to_show["legal_moves_as_int"] = []
		
		# Do a bunch of enters so that the screen is clean
		for i in range(10):
			print()
		
		print("\n\nThe other player made this move:")
		print(observation_to_show["prev_move"])
		
		print("\nHere is the state of the game")
		print(f"Life tokens: {ob_reader.get_life_tokens(observation_to_show)}")
		print(f"Info tokens: {ob_reader.get_information_tokens(observation_to_show)}")
		print(f"Deck size: {ob_reader.get_deck_size(observation_to_show)}")
		print(f"Fireworks: {ob_reader.get_fireworks(observation_to_show)}")
		
		
		print("\nOther player hand:")
		print(ob_reader.get_other_player_hand(observation_to_show))
		print("\nDiscarded cards")
		print(ob_reader.get_discarded_cards(observation_to_show))
		print("\nYour clues")
		print(ob_reader.get_my_clues(observation_to_show))
	
		# Show options
		print("\nHere are you legal moves. Please enter the integer of the move you would like to make.")
		
		for i in range(len(legal_moves)):
			legal_move = legal_moves[i]
			print(i, "-", legal_move)
	
		move_index = None
		while (type(move_index) != int or move_index < 0 or move_index >= len(legal_moves)):
			print("Please enter the integer index of the move you would like to make.")
			move_index = input()
			try:
				move_index = int(move_index)
			except:
				print("Couldn't parse as int")
			
		# Record decision basis and move
		if RECORD_HUMAN_ACTIONS:
			decision_basis = DecisionBasis(observation, my_not_clues, other_player_not_clues, playable_probabilities, safely_discardable_probabilities, unneeded_probabilities,
		hint_nuggets, singled_out_playable_card_index, singled_out_cards, move_index)

			self.record_decision_basis(decision_basis)
			
		print(f"Making this move: {legal_moves[move_index]}")

		return legal_moves[move_index], move_index, None

	def record_decision_basis(self, decision_basis):
		string_to_log = jsonpickle.encode(decision_basis)
		
		output_file = open("logs/human_decision_log.txt", "a")
		output_file.write(string_to_log)
		output_file.write("\n")
		output_file.close()