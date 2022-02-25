TEST_OBSERVATION = {
  "current_player": 0,
  "current_player_offset": 0,
  "life_tokens": 1,
  "information_tokens": 8,
  "num_players": 2,
  "deck_size": 36,
  "fireworks": {"R": 0, "Y": 1, "G": 0, "W": 0, "B": 1},
  "legal_moves": [
    { "action_type": "DISCARD", "card_index": 0 },
    { "action_type": "DISCARD", "card_index": 1 },
    { "action_type": "DISCARD", "card_index": 2 },
    { "action_type": "DISCARD", "card_index": 3 },
    { "action_type": "DISCARD", "card_index": 4 },
    { "action_type": "PLAY", "card_index": 0 },
    { "action_type": "PLAY", "card_index": 1 },
    { "action_type": "PLAY", "card_index": 2 },
    { "action_type": "PLAY", "card_index": 3 },
    { "action_type": "PLAY", "card_index": 4 }
  ],
  "legal_moves_as_int": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  "observed_hands": [
    [
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 }
    ],
    [
      { "color": "G", "rank": 2 },
      { "color": "W", "rank": 0 },
      { "color": "R", "rank": 2 },
      { "color": "W", "rank": 4 },
      { "color": "W", "rank": 0 }
    ]
  ],
  "discard_pile": [
    { "color": "W", "rank": 1 },
    { "color": "R", "rank": 3 }
  ],
  "card_knowledge": [
    [
      { "color": None, "rank": 3 },
      { "color": None, "rank": None },
      { "color": None, "rank": 3 },
      { "color": None, "rank": None },
      { "color": None, "rank": None }
    ],
    [
      { "color": None, "rank": None },
      { "color": None, "rank": None },
      { "color": None, "rank": None },
      { "color": None, "rank": 4 },
      { "color": None, "rank": None }
    ]
  ],
  "vectorized": {},
  "vectorized_sad": {},
  "action_hist": [[], []],
  "prev_move": { "action_type": "PLAY", "card_index": 4 }
}

TEST_OBSERVATION_2 = {
  "current_player": 0,
  "current_player_offset": 0,
  "life_tokens": 1,
  "information_tokens": 1,
  "num_players": 2,
  "deck_size": 36,
  "fireworks": { "R": 0, "Y": 1, "G": 0, "W": 0, "B": 1 },
  "legal_moves": [
    { "action_type": "DISCARD", "card_index": 0 },
    { "action_type": "DISCARD", "card_index": 1 },
    { "action_type": "DISCARD", "card_index": 2 },
    { "action_type": "DISCARD", "card_index": 3 },
    { "action_type": "DISCARD", "card_index": 4 },
    { "action_type": "PLAY", "card_index": 0 },
    { "action_type": "PLAY", "card_index": 1 },
    { "action_type": "PLAY", "card_index": 2 },
    { "action_type": "PLAY", "card_index": 3 },
    { "action_type": "PLAY", "card_index": 4 }
  ],
  "legal_moves_as_int": [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  "observed_hands": [
    [
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 }
    ],
    [
      { "color": "G", "rank": 2 },
      { "color": "W", "rank": 0 },
      { "color": "R", "rank": 2 },
      { "color": "W", "rank": 4 },
      { "color": "W", "rank": 0 }
    ]
  ],
  "discard_pile": [
    { "color": "W", "rank": 1 },
    { "color": "R", "rank": 3 }
  ],
  "card_knowledge": [
    [
      { "color": None, "rank": 3 },
      { "color": None, "rank": None },
      { "color": "W", "rank": 3 },
      { "color": "W", "rank": None },
      { "color": None, "rank": None }
    ],
    [
      { "color": None, "rank": None },
      { "color": None, "rank": None },
      { "color": None, "rank": None },
      { "color": None, "rank": 4 },
      { "color": None, "rank": None }
    ]
  ],
  "vectorized": {},
  "vectorized_sad": {},
  "action_hist": [[], []],
  "prev_move": { "action_type": "PLAY", "card_index": 4 }
}

TEST_OBSERVATION_3 = {
  "current_player": 0,
  "current_player_offset": 0,
  "life_tokens": 3,
  "information_tokens": 2,
  "num_players": 2,
  "deck_size": 36,
  "fireworks": { "R": 0, "Y": 1, "G": 0, "W": 0, "B": 1 },
  "legal_moves": [
    { "action_type": "DISCARD", "card_index": 0 },
    { "action_type": "DISCARD", "card_index": 1 },
    { "action_type": "DISCARD", "card_index": 2 },
    { "action_type": "DISCARD", "card_index": 3 },
    { "action_type": "DISCARD", "card_index": 4 },
    { "action_type": "PLAY", "card_index": 0 },
    { "action_type": "PLAY", "card_index": 1 },
    { "action_type": "PLAY", "card_index": 2 },
    { "action_type": "PLAY", "card_index": 3 },
    { "action_type": "PLAY", "card_index": 4 }
  ],
  "legal_moves_as_int": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  "observed_hands": [
    [
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 },
      { "color": None, "rank": -1 }
    ],
    [
      { "color": "G", "rank": 2 },
      { "color": "W", "rank": 0 },
      { "color": "R", "rank": 2 },
      { "color": "W", "rank": 4 },
      { "color": "W", "rank": 0 }
    ]
  ],
  "discard_pile": [
    { "color": "W", "rank": 1 },
    { "color": "R", "rank": 3 }
  ],
  "card_knowledge": [
    [
      { "color": None, "rank": 3 },
      { "color": None, "rank": 2 },
      { "color": None, "rank": 3 },
      { "color": None, "rank": None },
      { "color": None, "rank": None }
    ],
    [
      { "color": None, "rank": None },
      { "color": None, "rank": None },
      { "color": None, "rank": None },
      { "color": None, "rank": 4 },
      { "color": None, "rank": None }
    ]
  ],
  "vectorized": {},
  "vectorized_sad": {},
  "action_hist": [[], []],
  "prev_move": { "action_type": "PLAY", "card_index": 4 }
}

OBSERVATION_LIST = [TEST_OBSERVATION, TEST_OBSERVATION_2, TEST_OBSERVATION_3]

import util.observation_reader as test
import util.card_utilities as cu
import copy

# The tests
def get_other_player_hand():
	return test.get_other_player_hand(TEST_OBSERVATION) == [
	      { "color": "G", "rank": 2 },
	      { "color": "W", "rank": 0 },
	      { "color": "R", "rank": 2 },
	      { "color": "W", "rank": 4 },
	      { "color": "W", "rank": 0 }
	    ]

def get_discarded_cards():
	return test.get_discarded_cards(TEST_OBSERVATION) == [
	    { "color": "W", "rank": 1 },
	    { "color": "R", "rank": 3 }
	  ]

def get_played_cards():
	correct_played_cards = [cu.make_card("Y", 0), cu.make_card("B", 0)]
	received_played_cards = test.get_played_cards(TEST_OBSERVATION)

	lists_match = lambda x, y : len(x) == len(y) and False not in [card in y for card in x]
			
	if not lists_match(correct_played_cards, received_played_cards):
		return False
	
	# New Case ----------------------------------------------------
	fireworks = { "R": 5, "Y": 4, "G": 3, "W": 2, "B": 1 }
	  
	minimal_observation = {"fireworks": fireworks}
	correct_played_cards = []
	for color, number in fireworks.items():
		for rank in range(number):
			correct_played_cards.append(cu.make_card(color, rank))
	received_played_cards = test.get_played_cards(minimal_observation)
	
	if not lists_match(correct_played_cards, received_played_cards):
		return False
		
	return True

def get_my_clues():
	return test.get_my_clues(TEST_OBSERVATION) == [
	      { "color": None, "rank": 3 },
	      {	"color": None, "rank": None },
	      { "color": None, "rank": 3 },
	      { "color": None, "rank": None },
	      { "color": None, "rank": None }
	    ]

def get_other_player_clues():
	return test.get_other_player_clues(TEST_OBSERVATION) == [
	      { "color": None, "rank": None },
	      { "color": None, "rank": None },
	      { "color": None, "rank": None },
	      { "color": None, "rank": 4 },
	      { "color": None, "rank": None }
	    ]

def get_my_reserved_cards():
	my_reserved_cards = test.get_my_reserved_cards(TEST_OBSERVATION)
	return cu.TOTAL_CARDS - len(my_reserved_cards) == TEST_OBSERVATION["deck_size"] + 5
	
def get_other_player_reserved_cards():
	other_player_reserved_cards = test.get_other_player_reserved_cards(TEST_OBSERVATION)
	tests = []
	for observation in OBSERVATION_LIST:
		correct_observed_cards = test.get_played_cards(observation)
		correct_observed_cards.extend(test.get_discarded_cards(observation))
		tests.append(test.get_other_player_reserved_cards(observation) == correct_observed_cards)
	return False not in tests

def get_fireworks():
	tests = []
	for observation in OBSERVATION_LIST:
		tests.append(observation["fireworks"] == test.get_fireworks(observation))
	return False not in tests
	
def adjust_fireworks_with_playable_card():
	observation = copy.deepcopy(TEST_OBSERVATION)
	tests = []
	test.adjust_fireworks_with_playable_card(observation, cu.make_card("Y", 1))
	tests.append(test.get_fireworks(observation) == { "R": 0, "Y": 2, "G": 0, "W": 0, "B": 1 })
	test.adjust_fireworks_with_playable_card(observation, cu.make_card("Y", 1))
	tests.append(test.get_fireworks(observation) == { "R": 0, "Y": 2, "G": 0, "W": 0, "B": 1 })
	return False not in tests

def get_life_tokens():
	tests = []
	tests.append(test.get_life_tokens(TEST_OBSERVATION) == 1)
	tests.append(test.get_life_tokens(TEST_OBSERVATION_2) == 1)
	tests.append(test.get_life_tokens(TEST_OBSERVATION_3) == 3)
	return False not in tests

def get_deck_size():
	tests = []
	for observation in OBSERVATION_LIST:
		tests.append(observation["deck_size"] == test.get_deck_size(observation))
	return False not in tests

def decrement_deck_size():
	tests = []
	for observation in OBSERVATION_LIST:
		tests.append(observation["deck_size"] == test.get_deck_size(observation))
		old_deck_size = test.get_deck_size(observation)
		test.decrement_deck_size(observation)
		tests.append(test.get_deck_size(observation) == old_deck_size - 1)
	return False not in tests

def get_life_tokens():
	tests = []
	correct_life_token_counts = [1, 1, 3]
	for i in range(len(OBSERVATION_LIST)):
		observation = OBSERVATION_LIST[i]
		tests.append(test.get_life_tokens(observation) == correct_life_token_counts[i])
	return False not in tests
	
def decrement_life_tokens():
	tests = []
	correct_life_token_counts = [0, 0, 2]
	for i in range(len(OBSERVATION_LIST)):
		observation = copy.deepcopy(OBSERVATION_LIST[i])
		test.decrement_life_tokens(observation)
		tests.append(test.get_life_tokens(observation) == correct_life_token_counts[i])
	return False not in tests
	
def get_information_tokens():
	tests = []
	correct_life_token_counts = [8, 1, 2]
	for i in range(len(OBSERVATION_LIST)):
		observation = OBSERVATION_LIST[i]
		tests.append(test.get_information_tokens(observation) == correct_life_token_counts[i])
	return False not in tests
	
def increment_information_tokens():
	tests = []
	correct_life_token_counts = [9, 2, 3]
	for i in range(len(OBSERVATION_LIST)):
		observation = copy.deepcopy(OBSERVATION_LIST[i])
		test.increment_information_tokens(observation)
		tests.append(test.get_information_tokens(observation) == correct_life_token_counts[i])
	return False not in tests
	
def decrement_information_tokens():
	tests = []
	correct_life_token_counts = [7, 0, 1]
	for i in range(len(OBSERVATION_LIST)):
		observation = copy.deepcopy(OBSERVATION_LIST[i])
		test.decrement_information_tokens(observation)
		tests.append(test.get_information_tokens(observation) == correct_life_token_counts[i])
	return False not in tests

def get_number_of_players():
	tests = []
	for observation in OBSERVATION_LIST:
		tests.append(test.get_number_of_players(observation) == 2)
	return False not in tests

def get_current_player():
	tests = []
	for observation in OBSERVATION_LIST:
		tests.append(test.get_current_player(observation) == observation["current_player"])
	return False not in tests

def get_current_player_offset():
	tests = []
	for observation in OBSERVATION_LIST:
		tests.append(test.get_current_player(observation) == observation["current_player_offset"])
	return False not in tests

def get_observed_hand_by_index():
	tests = []
	for observation in OBSERVATION_LIST:
		for player_index in range(2):
			tests.append(test.get_observed_hand_by_index(observation, player_index) == observation["observed_hands"][player_index])
	return False not in tests

def get_previous_move():
	tests = []
	tests.append(test.get_previous_move(TEST_OBSERVATION) == { "action_type": "PLAY", "card_index": 4 })
	return False not in tests

# Add methods to this list if they should be unit tested
methods_to_test = [
	get_other_player_hand,
	get_discarded_cards,
	get_played_cards,
	get_my_clues,
	get_other_player_clues,
	get_my_reserved_cards,
	get_other_player_reserved_cards,
	get_fireworks,
	adjust_fireworks_with_playable_card,
	get_deck_size,
	decrement_deck_size,
	get_life_tokens,
	decrement_life_tokens,
	get_information_tokens,
	increment_information_tokens,
	decrement_information_tokens,
	get_number_of_players,
	get_current_player,
	get_current_player_offset,
	get_observed_hand_by_index,
	get_previous_move
]
