
TEST_BUNDLE = {'player_observations': [
# Player 0 observation
	{'current_player': 0,
	'current_player_offset': 0,
	'life_tokens': 1,
	'information_tokens': 0,
	'num_players': 2,
	'deck_size': 35,
	'fireworks': {'R': 0, 'Y': 1, 'G': 0, 'W': 0, 'B': 1},
	'legal_moves': [{'action_type': 'DISCARD', 'card_index': 0}, {'action_type': 'DISCARD', 'card_index': 1}, {'action_type': 'DISCARD', 'card_index': 2}, {'action_type': 'DISCARD', 'card_index': 3}, {'action_type': 'DISCARD', 'card_index': 4}, {'action_type': 'PLAY', 'card_index': 0}, {'action_type': 'PLAY', 'card_index': 1}, {'action_type': 'PLAY', 'card_index': 2}, {'action_type': 'PLAY', 'card_index': 3}, {'action_type': 'PLAY', 'card_index': 4}], 
	'legal_moves_as_int': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
	'observed_hands': [
		[{'color': None, 'rank': -1},
		{'color': None, 'rank': -1}, 
		{'color': None, 'rank': -1},
		{'color': None, 'rank': -1},
		{'color': None, 'rank': -1}],

		[{'color': 'G', 'rank': 2},
		{'color': 'W', 'rank': 0},
		{'color': 'R', 'rank': 2},
		{'color': 'W', 'rank': 3},
		{'color': 'W', 'rank': 0}]], 
		
	'discard_pile': [{'color': 'W', 'rank': 1}, {'color': 'R', 'rank': 3}], 
	'card_knowledge': [
		[{'color': None, 'rank': 3},
		{'color': None, 'rank': None},
		{'color': 'W', 'rank': 3},
		{'color': 'W', 'rank': None},
		{'color': None, 'rank': None}],

		[{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': 3},
		{'color': None, 'rank': None}]],

	'vectorized': {},
	'vectorized_sad': {},
	'action_hist': [[], []],
	'prev_move': {'action_type': 'PLAY', 'card_index': 4}}, 
# Player 1 observation
	{'current_player': 0,
	'current_player_offset': 1,
	'life_tokens': 1,
	'information_tokens': 0,
	'num_players': 2,
	'deck_size': 35,
	'fireworks': {'R': 0, 'Y': 1, 'G': 0, 'W': 0, 'B': 1},
	'legal_moves': [], 
	'legal_moves_as_int': [], 
	'observed_hands': [
		[{'color': None, 'rank': -1},
		{'color': None, 'rank': -1},
		{'color': None, 'rank': -1},
		{'color': None, 'rank': -1},
		{'color': None, 'rank': -1}],

		[{'color': 'G', 'rank': 2},
		{'color': 'W', 'rank': 0},
		{'color': 'R', 'rank': 2},
		{'color': 'W', 'rank': 3},
		{'color': 'W', 'rank': 0}]],
	
	'discard_pile': [{'color': 'W', 'rank': 1}, {'color': 'R', 'rank': 3}], 
	'card_knowledge': [
		[{'color': None, 'rank': 3},
		{'color': None, 'rank': None},
		{'color': 'W', 'rank': 3}, 
		{'color': 'W', 'rank': None},
		{'color': None, 'rank': None}],

		[{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': 3},
		{'color': None, 'rank': None}]],
	'vectorized': {}, 
	'vectorized_sad': {},
	'action_hist': [[], []],
	'prev_move': {'action_type': 'PLAY', 'card_index': 4}}]}

TEST_BUNDLE_2 = {'player_observations': 
	# Player 1 observation
	[{'current_player': 0,
	'current_player_offset': 0, 
	'life_tokens': 3,
	'information_tokens': 8,
	'num_players': 2,
	'deck_size': 40,
	'fireworks': {'B': 0, 'G': 0, 'R': 0, 'W': 0, 'Y': 0}, 
	'legal_moves': [{'action_type': 'REVEAL_COLOR', 'target_offset': 1, 'color': 'G'}, {'action_type': 'REVEAL_COLOR', 'target_offset': 1, 'color': 'R'}, {'action_type': 'REVEAL_COLOR', 'target_offset': 1, 'color': 'W'}, {'action_type': 'REVEAL_COLOR', 'target_offset': 1, 'color': 'Y'}, {'action_type': 'REVEAL_RANK', 'target_offset': 1, 'rank': 0}, {'action_type': 'REVEAL_RANK', 'target_offset': 1, 'rank': 1}, {'action_type': 'REVEAL_RANK', 'target_offset': 1, 'rank': 2}, {'action_type': 'REVEAL_RANK', 'target_offset': 1, 'rank': 3}, {'action_type': 'REVEAL_RANK', 'target_offset': 1, 'rank': 4}, {'action_type': 'DISCARD', 'card_index': 0}, {'action_type': 'DISCARD', 'card_index': 1}, {'action_type': 'DISCARD', 'card_index': 2}, {'action_type': 'DISCARD', 'card_index': 3}, {'action_type': 'DISCARD', 'card_index': 4}, {'action_type': 'PLAY', 'card_index': 0}, {'action_type': 'PLAY', 'card_index': 1}, {'action_type': 'PLAY', 'card_index': 2}, {'action_type': 'PLAY', 'card_index': 3}, {'action_type': 'PLAY', 'card_index': 4}], 
	'legal_moves_as_int': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 
	'observed_hands': [
		[{'color': None, 'rank': None}, 
		{'color': None, 'rank': None}, 
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None}],

		[{'color': 'Y', 'rank': 2},
		{'color': 'G', 'rank': 3},
		{'color': 'W', 'rank': 0},
		{'color': 'W', 'rank': 1},
		{'color': 'R', 'rank': 4}]],
	'discard_pile': [], 
	'card_knowledge': [
		[{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': 1}],

		[{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': "R", 'rank': None}]],
	'action_hist': [], 'prev_move': None}, 
	# Player 1 observation
	{'current_player': 0, 
	'current_player_offset': 1,
	'life_tokens': 3,
	'information_tokens': 8,
	'num_players': 2,
	'deck_size': 40,
	'fireworks': {'B': 0, 'G': 0, 'R': 0, 'W': 0, 'Y': 0},
	'legal_moves': [],
	'legal_moves_as_int': [], 
	'observed_hands': [
		[{'color': None, 'rank': None}, 
		{'color': None, 'rank': None}, 
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None}],

		[{'color': 'Y', 'rank': 0},
		{'color': 'W', 'rank': 1},
		{'color': 'B', 'rank': 0},
		{'color': 'Y', 'rank': 1},
		{'color': 'B', 'rank': 1}]],
	'discard_pile': [], 
	'card_knowledge': [
		[{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': "R", 'rank': None}],

		[{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': None},
		{'color': None, 'rank': 1}]],
	'action_hist': [],
	'prev_move': None}]}

import util.gym as gym
import util.observation_reader as ob_reader
import util.observation_bundle_reader as bundle_reader
import util.card_utilities as cu
import copy

def reset():
	my_gym = gym.Gym()
	my_gym.reset()
	tests = []
	tests.append(len(ob_reader.get_other_player_hand(bundle_reader.get_observations(my_gym.get_observation_bundle())[0])) == cu.HAND_SIZE)
	return False not in tests
	
def step():
	return True

def get_observation_bundle():
	my_gym = gym.Gym()
	return my_gym.observation_bundle == my_gym.get_observation_bundle()
	
def get_current_player():
	my_gym = gym.Gym()
	return my_gym.get_current_player() == my_gym.player_index_next_action_is_from

def deal_new_card_to_player():
	my_gym = gym.Gym()

	# Clear out the cards so that we can more clearly test the dealing
	observations = bundle_reader.get_observations(my_gym.get_observation_bundle())
	for observation in observations:
		observation["observed_hands"] = [[], []]

	player_index = 0
	
	my_gym.deal_new_card_to_player(0)
	
	observations = bundle_reader.get_observations(my_gym.get_observation_bundle())
	tests = []
	tests.append(len(ob_reader.get_observed_hand_by_index(observations[player_index], 0)) == 1)
	tests.append(len(ob_reader.get_observed_hand_by_index(observations[player_index], 1)) == 0)
	tests.append(len(ob_reader.get_observed_hand_by_index(observations[not player_index], 0)) == 0)
	tests.append(len(ob_reader.get_observed_hand_by_index(observations[not player_index], 1)) == 1)
	return False not in tests

def get_new_observation_bundle():
	my_gym = gym.Gym()
	bundle = my_gym.get_new_observation_bundle(2)
	tests = []
	tests.append(len(bundle_reader.get_observations(bundle)) == 2)
	observations = bundle_reader.get_observations(bundle)
	for observation in observations:
		tests.append(ob_reader.get_my_clues(observation) == [])
		tests.append(ob_reader.get_other_player_clues(observation) == [])
	return False not in tests

def update_legal_moves():
	true_bundles = [TEST_BUNDLE, TEST_BUNDLE_2]
	bundle_copies = [copy.deepcopy(TEST_BUNDLE), copy.deepcopy(TEST_BUNDLE_2)]
	tests = []
	for i in range(len(bundle_copies)):
		bundle = bundle_copies[i]
		my_gym = gym.Gym()
		my_gym.observation_bundle = bundle
		my_gym.update_legal_moves()

		tests.append(my_gym.get_observation_bundle() == true_bundles[i])
		# Now we'll clear out the legal moves and make sure the gym can rebuild them
		for observation in bundle_reader.get_observations(my_gym.get_observation_bundle()):
			observation["legal_moves"] = []
			
		my_gym.update_legal_moves()
		tests.append(my_gym.get_observation_bundle() == true_bundles[i])
	return False not in tests

def update_player_knowledge_with_hint():
	bundle_copy = copy.deepcopy(TEST_BUNDLE_2)
	hint = {'action_type': 'REVEAL_COLOR', 'target_offset': 1, 'color': 'W'}
	my_gym = gym.Gym()
	my_gym.observation_bundle = bundle_copy
	my_gym.update_player_knowledge_with_hint(hint)
	tests = []
	observations = bundle_reader.get_observations(my_gym.get_observation_bundle())
	tests.append(ob_reader.get_other_player_clues(observations[0]) == [{	'color': None, 'rank': None},
	{'color': None, 'rank': None},
	{'color': "W", 'rank': None},
	{'color': "W", 'rank': None},
	{'color': "R", 'rank': None}])
	tests.append(ob_reader.get_my_clues(observations[0]) == [{	'color': None, 'rank': None},
	{'color': None, 'rank': None},
	{'color': None, 'rank': None},
	{'color': None, 'rank': None},
	{'color': None, 'rank': 1}])
	return False not in tests

def remove_card_from_player_hand_and_deal():
	my_gym = gym.Gym()
	my_gym.observation_bundle = copy.deepcopy(TEST_BUNDLE_2)
	
	my_gym.remove_card_from_player_hand_and_deal(0, 2)
	
	# TEST_BUNDLE_2 is a snapshot before the action.
	current_bundle = my_gym.get_observation_bundle()
	tests = []
	
	# Check that the card was NOT discarded
	old_discarded_cards = bundle_reader.get_discarded_cards(TEST_BUNDLE_2)
	new_discarded_cards = bundle_reader.get_discarded_cards(current_bundle)
	tests.append(old_discarded_cards == new_discarded_cards)
	
	# Check that the deck has decreased in size
	old_deck_size = bundle_reader.get_deck_size(TEST_BUNDLE_2)
	new_deck_size = bundle_reader.get_deck_size(current_bundle)
	tests.append(new_deck_size == old_deck_size - 1)
	
	# Check player 0's hand is now what is expected
	old_player_0_hand = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 0)
	new_player_0_hand = bundle_reader.get_player_hand_by_index(current_bundle, 0)
	for i in range(2):
		tests.append(old_player_0_hand[i] == new_player_0_hand[i])
	for i in range(2, 4):
		tests.append(old_player_0_hand[i + 1] == new_player_0_hand[i])
	# It's hard to put a constraint on the 5th card because it could be identical to another in the old hand, so only require that a card was placed here
	tests.append(len(new_player_0_hand) == cu.HAND_SIZE)
	
	# Check that player 0's card knowledge is what is expected
	old_player_0_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 0)
	new_player_0_clues = bundle_reader.get_player_clues_by_index(current_bundle, 0)
	for i in range(2):
		tests.append(old_player_0_hand[i] == new_player_0_hand[i])
	for i in range(2, 4):
		tests.append(old_player_0_hand[i + 1] == new_player_0_hand[i])
	tests.append(len(new_player_0_clues) == cu.HAND_SIZE)

	# Check that player 1's hand has not changed
	old_player_1_hand = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 1)
	new_player_1_hand = bundle_reader.get_player_hand_by_index(current_bundle, 1)
	tests.append(len(old_player_1_hand) == len(new_player_1_hand))
	for i in range(len(old_player_1_hand)):
		tests.append(old_player_1_hand[i] == new_player_1_hand[i])
	
	# Check that player 1's card knowledge has not changed
	old_player_1_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 1)
	new_player_1_clues = bundle_reader.get_player_clues_by_index(current_bundle, 1)
	tests.append(len(old_player_1_clues) == len(new_player_1_clues))
	for i in range(len(old_player_1_clues)):
		tests.append(old_player_1_clues[i] == new_player_1_clues[i])

	return False not in tests
	
def discard_card_from_player_hand_and_deal():
	my_gym = gym.Gym()
	my_gym.observation_bundle = copy.deepcopy(TEST_BUNDLE_2)
	
	# Grab a copy of the card that will be removed
	card_to_remove = bundle_reader.get_player_hand_by_index(my_gym.get_observation_bundle(), 0)[2]
	my_gym.discard_card_from_player_hand_and_deal({ "action_type": "DISCARD", "card_index": 2})
	
	# TEST_BUNDLE_2 is a snapshot before the action.
	current_bundle = my_gym.get_observation_bundle()
	tests = []
	
	# Check that the card was NOT discarded
	old_discarded_cards = copy.deepcopy(bundle_reader.get_discarded_cards(TEST_BUNDLE_2))
	new_discarded_cards = bundle_reader.get_discarded_cards(current_bundle)
	what_new_discarded_cards_should_be = old_discarded_cards
	what_new_discarded_cards_should_be.append(card_to_remove)
	tests.append(what_new_discarded_cards_should_be == new_discarded_cards)
	
	# Check that the deck has decreased in size
	old_deck_size = bundle_reader.get_deck_size(TEST_BUNDLE_2)
	new_deck_size = bundle_reader.get_deck_size(current_bundle)
	tests.append(new_deck_size == old_deck_size - 1)
	
	# Check player 0's hand is now what is expected
	old_player_0_hand = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 0)
	new_player_0_hand = bundle_reader.get_player_hand_by_index(current_bundle, 0)
	for i in range(2):
		tests.append(old_player_0_hand[i] == new_player_0_hand[i])
	for i in range(2, 4):
		tests.append(old_player_0_hand[i + 1] == new_player_0_hand[i])
	# It's hard to put a constraint on the 5th card because it could be identical to another in the old hand, so only require that a card was placed here
	tests.append(len(new_player_0_hand) == cu.HAND_SIZE)
	
	# Check that player 0's card knowledge is what is expected
	old_player_0_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 0)
	new_player_0_clues = bundle_reader.get_player_clues_by_index(current_bundle, 0)
	for i in range(2):
		tests.append(old_player_0_hand[i] == new_player_0_hand[i])
	for i in range(2, 4):
		tests.append(old_player_0_hand[i + 1] == new_player_0_hand[i])
	tests.append(len(new_player_0_clues) == cu.HAND_SIZE)

	# Check that player 1's hand has not changed
	old_player_1_hand = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 1)
	new_player_1_hand = bundle_reader.get_player_hand_by_index(current_bundle, 1)
	tests.append(len(old_player_1_hand) == len(new_player_1_hand))
	for i in range(len(old_player_1_hand)):
		tests.append(old_player_1_hand[i] == new_player_1_hand[i])
	
	# Check that player 1's card knowledge has not changed
	old_player_1_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 1)
	new_player_1_clues = bundle_reader.get_player_clues_by_index(current_bundle, 1)
	tests.append(len(old_player_1_clues) == len(new_player_1_clues))
	for i in range(len(old_player_1_clues)):
		tests.append(old_player_1_clues[i] == new_player_1_clues[i])
	
	# Make sure no list of observed cards has grown behond the hand limit
	tests.append(len(new_player_1_clues) <= cu.HAND_SIZE)
	tests.append(len(new_player_0_clues) <= cu.HAND_SIZE)
	
	return False not in tests

def attempt_play():
	my_gym = gym.Gym()
	my_gym.observation_bundle = copy.deepcopy(TEST_BUNDLE_2)
	tests = []
	
	# Player 0 attempts a play that is not valid.
	card_being_played = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 0)[4]
	my_gym.attempt_play({ "action_type": "PLAY", "card_index": 4 })
	current_bundle = my_gym.get_observation_bundle()
	
	# Life tokens should decrement
	tests.append(bundle_reader.get_life_tokens(TEST_BUNDLE_2) - 1 == bundle_reader.get_life_tokens(current_bundle))
	
	# Fireworks should be unchanged
	tests.append(bundle_reader.get_fireworks(TEST_BUNDLE_2) == bundle_reader.get_fireworks(current_bundle))
	
	# the card should be added to the discard pile
	tests.append(card_being_played in bundle_reader.get_discarded_cards(current_bundle))
	tests.append(len(bundle_reader.get_discarded_cards(TEST_BUNDLE_2)) + 1 == len(bundle_reader.get_discarded_cards(current_bundle)))

	# a new card should be dealt to player 0
	old_player_0_hand = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 0)
	new_player_0_hand = bundle_reader.get_player_hand_by_index(current_bundle, 0)
	for i in range(4):
		tests.append(old_player_0_hand[i] == new_player_0_hand[i])
	
	# Player 0 should have changed card knowledge
	old_player_0_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 0)
	new_player_0_clues = bundle_reader.get_player_clues_by_index(current_bundle, 0)
	for i in range(4):
		tests.append(old_player_0_clues[i] == new_player_0_clues[i])
	tests.append(old_player_0_clues[4] != new_player_0_clues[4])
	
	# Player 1 should have the same hand
	old_player_1_hand = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 1)
	new_player_1_hand = bundle_reader.get_player_hand_by_index(current_bundle, 1)
	tests.append(old_player_1_hand == new_player_1_hand)
	
	# Player 1 should have the same card knowledge
	old_player_1_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 1)
	new_player_1_clues = bundle_reader.get_player_clues_by_index(current_bundle, 1)
	tests.append(old_player_1_clues == new_player_1_clues)
	
	my_gym.observation_bundle = copy.deepcopy(TEST_BUNDLE_2)
	my_gym.player_index_next_action_is_from = 1
	# By virtuie of the earlier part of this test, the current player index is 1
	
	# Player 1 makes a valid play
	play_action = { "action_type": "PLAY", "card_index": 2 }
	card_being_played = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 1)[2]
	
	# Make sure it is player 1's turn
	tests.append(my_gym.get_current_player() == 1)
	
	my_gym.attempt_play(play_action)
	current_bundle = my_gym.get_observation_bundle()
	
	# Life tokens should not change
	tests.append(bundle_reader.get_life_tokens(TEST_BUNDLE_2) == bundle_reader.get_life_tokens(current_bundle))
	
	# Fireworks should be changed
	old_fireworks = bundle_reader.get_fireworks(TEST_BUNDLE_2)
	new_fireworks = bundle_reader.get_fireworks(current_bundle)
	for color in old_fireworks.keys():
		if color == cu.get_color(card_being_played):
			tests.append(old_fireworks[color] + 1 == new_fireworks[color])
		else:
			tests.append(old_fireworks[color] == new_fireworks[color])
	
	# The discard pile size should be unchanged
	tests.append(bundle_reader.get_discarded_cards(TEST_BUNDLE_2) == bundle_reader.get_discarded_cards(current_bundle))
	
	# A new card should be dealt to player 1
	old_player_1_hand = bundle_reader.get_player_hand_by_index(TEST_BUNDLE_2, 1)
	new_player_1_hand = bundle_reader.get_player_hand_by_index(current_bundle, 1)
	for i in range(2):
		tests.append(old_player_1_hand[i] == new_player_1_hand[i])
	for i in range(2, 4):
		tests.append(old_player_1_hand[i + 1] == new_player_1_hand[i])
	# It's possible to be dealt the same type of card that was played, so we can't insist on the card having changed.
	
	# Player 1 should have changed card knowledge
	old_player_1_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 1)
	new_player_1_clues = bundle_reader.get_player_clues_by_index(current_bundle, 1)
	for i in range(2):
		tests.append(old_player_1_clues[i] == new_player_1_clues[i])
	for i in range(2, 4):
		tests.append(old_player_1_clues[i + 1] == new_player_1_clues[i])
	tests.append(old_player_1_clues[4] != new_player_1_clues[4])
	tests.append(cu.get_empty_clue() == new_player_1_clues[4])

	# Player 0 should have the same hand
	old_player_0_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 0)
	new_player_0_clues = bundle_reader.get_player_clues_by_index(current_bundle, 0)
	tests.append(old_player_0_clues == new_player_0_clues)
	
	# Player 0 should have the same card knowledge
	old_player_0_clues = bundle_reader.get_player_clues_by_index(TEST_BUNDLE_2, 0)
	new_player_0_clues = bundle_reader.get_player_clues_by_index(current_bundle, 0)
	tests.append(old_player_0_clues == new_player_0_clues)
	
	return False not in tests

def add_card_to_discard_pile():
	tests = []
	bundle = copy.deepcopy(TEST_BUNDLE_2)
	card = cu.make_card("G", 3)
	my_gym = gym.Gym()
	my_gym.observation_bundle = bundle
	my_gym.add_card_to_discard_pile(card)
	observations = bundle_reader.get_observations(my_gym.get_observation_bundle())
	discard_pile_player_0 = observations[0]["discard_pile"]
	discard_pile_player_1 = observations[1]["discard_pile"]
	correct_discard_pile = bundle_reader.get_discarded_cards(TEST_BUNDLE_2)
	correct_discard_pile.append(card)
	tests.append(discard_pile_player_0 == correct_discard_pile)
	tests.append(discard_pile_player_1 == correct_discard_pile)
	return False not in tests

methods_to_test = [
	reset,
	step,
	get_observation_bundle,
	get_current_player,
	deal_new_card_to_player,
	get_observation_bundle,
	update_legal_moves,
	update_player_knowledge_with_hint,
	remove_card_from_player_hand_and_deal,
	discard_card_from_player_hand_and_deal,
	attempt_play,
	add_card_to_discard_pile,
	get_new_observation_bundle
]
