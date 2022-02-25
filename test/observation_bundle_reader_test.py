
import util.observation_bundle_reader as test
import util.observation_reader as ob_reader
import test.observation_reader_test as ob_reader_test
import util.card_utilities as cu
import copy

BUNDLE_1 = {"player_observations": [ob_reader_test.TEST_OBSERVATION, ob_reader_test.TEST_OBSERVATION_2]}

def get_observations():
	observations = test.get_observations(BUNDLE_1)
	return observations == [ob_reader_test.TEST_OBSERVATION, ob_reader_test.TEST_OBSERVATION_2]
	
def get_number_of_players():
	return test.get_number_of_players(BUNDLE_1) == 2
	
def get_player_hand_by_index():
	hand_1 = test.get_player_hand_by_index(BUNDLE_1, 0)
	hand_2 = test.get_player_hand_by_index(BUNDLE_1, 1)
	tests = []
	tests.append(hand_1 == ob_reader.get_other_player_hand(ob_reader_test.TEST_OBSERVATION_2))
	tests.append(hand_2 == ob_reader.get_other_player_hand(ob_reader_test.TEST_OBSERVATION))
	return False not in tests
	
def get_player_clues_by_index():
	clues = []
	for i in range(2):
		clues.append(test.get_player_clues_by_index(BUNDLE_1, i))
	tests = []
	correct_clues = [[
		{ "color": None, "rank": 3 },
		{ "color": None, "rank": None },
		{ "color": None, "rank": 3 },
		{ "color": None, "rank": None },
		{ "color": None, "rank": None }
	],
	[
		{ "color": None, "rank": 3 },
		{ "color": None, "rank": None },
		{ "color": "W", "rank": 3 },
		{ "color": "W", "rank": None },
		{ "color": None, "rank": None }
    ]]

	for i in range(len(clues)):
		clue = clues[i]
		correct_clue = correct_clues[i]
		tests.append(clue == correct_clue)
	return False not in tests
	
def get_fireworks():
	return test.get_fireworks(BUNDLE_1) == ob_reader.get_fireworks(ob_reader_test.TEST_OBSERVATION)
	
def decrement_deck_size():
	tests = []
	bundle_copy = copy.deepcopy(BUNDLE_1)
	test.decrement_deck_size(bundle_copy)
	for i in range(len(ob_reader.get_observations(bundle_copy))):
		observation = test.get_observations(bundle_copy)[i]
		old_observation = test.get_observations(BUNDLE_1)[i]
		tests.append(ob_reader.get_deck_size(observation) == ob_reader.get_deck_size(old_observation) - 1)
	return False not in tests
	
def adjust_fireworks_with_playable_card():
	bundle_copy = copy.deepcopy(BUNDLE_1)
	test.adjust_fireworks_with_playable_card(bundle_copy, cu.make_card("G", 0))
	fireworks = test.get_fireworks(bundle_copy)
	tests = []
	tests.append(fireworks == {
    "R": 0,
    "Y": 1,
    "G": 1,
    "W": 0,
    "B": 1
	})
	# Test a card that is actually not playable, and make sure it is not played
	test.adjust_fireworks_with_playable_card(bundle_copy, cu.make_card("G", 0))
	fireworks = test.get_fireworks(bundle_copy)
	tests.append(fireworks == {
    "R": 0,
    "Y": 1,
    "G": 1,
    "W": 0,
    "B": 1
	})
	
	test.adjust_fireworks_with_playable_card(bundle_copy, cu.make_card("Y", 1))
	fireworks = test.get_fireworks(bundle_copy)
	tests.append(fireworks == {
    "R": 0,
    "Y": 2,
    "G": 1,
    "W": 0,
    "B": 1
	})
	return False not in tests

def get_deck_size():
	return test.get_deck_size(BUNDLE_1) == BUNDLE_1["player_observations"][0]["deck_size"]

def decrement_deck_size():
	bundle_copy = copy.deepcopy(BUNDLE_1)
	initial_deck_size = ob_reader.get_deck_size(test.get_observations(bundle_copy)[0])
	test.decrement_deck_size(bundle_copy)
	later_deck_size = ob_reader.get_deck_size(test.get_observations(bundle_copy)[0])
	tests = []
	tests.append(later_deck_size == initial_deck_size - 1)
	return False not in tests

def get_life_tokens():
	tests = []
	tests.append(test.get_life_tokens(BUNDLE_1) == BUNDLE_1["player_observations"][0]["life_tokens"])
	return False not in tests

def decrement_life_tokens():
	bundle_copy = copy.deepcopy(BUNDLE_1)
	initial_deck_size = ob_reader.get_life_tokens(test.get_observations(bundle_copy)[0])
	test.decrement_life_tokens(bundle_copy)
	later_deck_size = ob_reader.get_life_tokens(test.get_observations(bundle_copy)[0])
	tests = []
	tests.append(later_deck_size == initial_deck_size - 1)
	return False not in tests
	
def get_information_tokens():
	tests = []
	tests.append(test.get_information_tokens(BUNDLE_1) == 8)
	return False not in tests
	
def increment_information_tokens():
	tests = []
	bundle_copy = copy.deepcopy(BUNDLE_1)
	test.increment_information_tokens(bundle_copy)
	tests.append(test.get_information_tokens(bundle_copy) == 9)
	return False not in tests
	
def decrement_information_tokens():
	tests = []
	bundle_copy = copy.deepcopy(BUNDLE_1)
	test.decrement_information_tokens(bundle_copy)
	tests.append(test.get_information_tokens(bundle_copy) == 7)
	return False not in tests
	
def get_discarded_cards():
	tests = []
	tests.append(ob_reader.get_discarded_cards(ob_reader_test.TEST_OBSERVATION) == test.get_discarded_cards(BUNDLE_1))
	return False not in tests
	
def is_game_over():
	tests = []
	tests.append(not test.is_game_over(BUNDLE_1))
	bundle_copy = copy.deepcopy(BUNDLE_1)
	player_0_hand = test.get_player_hand_by_index(bundle_copy, 0)
	player_1_hand = test.get_player_hand_by_index(bundle_copy, 1)
	player_0_hand.clear()
	player_1_hand.clear()
	tests.append(test.is_game_over(bundle_copy))
	bundle_copy = copy.deepcopy(BUNDLE_1)
	for observation in test.get_observations(bundle_copy):
		observation["life_tokens"] = 0
	tests.append(test.is_game_over(bundle_copy))

	return False not in tests

methods_to_test = [
	get_observations,
	get_number_of_players,
	get_player_hand_by_index,
	get_player_clues_by_index,
	get_fireworks,
	adjust_fireworks_with_playable_card,
	get_deck_size,
	decrement_deck_size,
	get_life_tokens,
	decrement_life_tokens,
	get_information_tokens,
	increment_information_tokens,
	decrement_information_tokens,
	get_discarded_cards,
	is_game_over
]
