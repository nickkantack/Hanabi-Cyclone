
import util.card_utilities as test
import test.observation_reader_test as observation_reader_test

def all_cards_correct_number():
	return len(test.ALL_CARDS) == test.TOTAL_CARDS

def get_empty_clue():
	return test.get_empty_clue() == test.EMPTY_CLUE
	
def get_empty_not_clue():
	return test.get_empty_not_clue() == test.EMPTY_NOT_CLUE

def get_color():
	for card in test.ALL_CARDS:
		if card["color"] != test.get_color(card):
			return False
	return True

def get_rank():
	tests = []
	for card in test.ALL_CARDS:
		tests.append(card["rank"] == test.get_rank(card))
	action = {
		  "action_type": "REVEAL_RANK",
		  "card_rank": 4
		}
	tests.append(action["card_rank"] == test.get_rank(action))
	return False not in tests
	
def rank_invalid():
	for card in test.ALL_CARDS:
		if (test.rank_invalid(test.get_rank(card))):
			return False
	tests = []
	tests.append(test.rank_invalid(test.get_rank(test.make_card("G"))))
	tests.append(test.rank_invalid(test.get_rank(test.make_card("R", -1))))
	return False not in tests
	
def get_multiplicity_by_rank():
	correct_multiplicities = [3, 2, 2, 2, 1]
	received_multiplicities = [test.get_multiplicity_by_rank(i) for i in range(5)]
	return correct_multiplicities == received_multiplicities

def does_card_match_clue():
	tests = []
	tests.append(test.does_card_match_clue(test.make_card("G", 2), test.make_card(color="G")))
	tests.append(test.does_card_match_clue(test.make_card("W", 0), test.make_card(rank=0)))
	tests.append(test.does_card_match_clue(test.make_card("W", 2), test.make_card("W", 2)))
	tests.append(not test.does_card_match_clue(test.make_card("Y", 2), test.make_card(color="G")))
	tests.append(not test.does_card_match_clue(test.make_card("B", 4), test.make_card(rank=2)))
	tests.append(not test.does_card_match_clue(test.make_card("R", 1), test.make_card("B", 3)))
	return False not in tests
	
def get_cards_matching_clue():
	correct_cards = test.ALL_CARDS
	matching_cards = test.get_cards_matching_clue(test.EMPTY_CLUE, test.EMPTY_NOT_CLUE)
	for card in correct_cards:
		if card not in matching_cards:
			return False
	if len(correct_cards) != len(matching_cards):
		return False

	correct_cards = []
	for card in test.ALL_CARDS:
		if test.get_color(card) == "W":
			correct_cards.append(card)
	matching_cards = test.get_cards_matching_clue(test.make_card("W"), test.EMPTY_NOT_CLUE)
	for card in correct_cards:
		if card not in matching_cards:
			return False
	if len(correct_cards) != len(matching_cards):
		return False
		
	correct_cards = []
	for card in test.ALL_CARDS:
		if test.get_rank(card) == 3:
			correct_cards.append(card)
	matching_cards = test.get_cards_matching_clue(test.make_card(rank=3), test.EMPTY_NOT_CLUE)
	for card in correct_cards:
		if card not in matching_cards:
			return False
	if len(correct_cards) != len(matching_cards):
		return False
		
	not_clue = {"colors": ["W", "Y"], "ranks": [2, 3]}
	correct_cards = []
	for card in test.ALL_CARDS:
		if test.get_color(card) == "G" and test.get_rank(card) not in not_clue["ranks"]:
			correct_cards.append(card)
	matching_cards = test.get_cards_matching_clue(test.make_card("G"), not_clue)
	for card in correct_cards:
		if card not in matching_cards:
			return False
	if len(correct_cards) != len(matching_cards):
		return False
		
	return True

def get_indexed_wild_card():
	tests = []
	for i in range(5):
		tests.append(test.get_indexed_wild_card(i) == test.make_card(test.WILD, i))
	return False not in tests

def is_card_wild():
	tests = []
	for color in test.COLORS:
		for rank in test.ALL_UNIQUE_RANKS:
			tests.append(test.is_card_wild(test.make_card(test.WILD, rank)))
			tests.append(not test.is_card_wild(test.make_card(color, rank)))
	return False not in tests
	
def make_card():
	tests = []
	tests.append(test.make_card("B", 2) == {"color": "B", "rank": 2})
	tests.append(test.make_card("W", 1) == {"color": "W", "rank": 1})
	tests.append(test.make_card("Y", 3) == {"color": "Y", "rank": 3})
	tests.append(test.make_card("G", 0) == {"color": "G", "rank": 0})
	tests.append(test.make_card("R", 4) == {"color": "R", "rank": 4})
	tests.append(test.make_card("B", 2) == {"color": "B", "rank": 2})
	return False not in tests
	
def merge_clue():
	old_clues = [test.get_empty_clue() for i in range(test.HAND_SIZE)]
	old_clues[0]["rank"] = 3
	new_clue = [test.get_empty_clue() for i in range(test.HAND_SIZE)]
	new_clue[0]["color"] = "W"
	test.merge_clue(old_clues, new_clue)
	tests = []
	tests.append(old_clues[0] == test.make_card("W", 3))
	for i in range(test.HAND_SIZE - 1):
		tests.append(old_clues[i + 1] == test.get_empty_clue())
		
	return False not in tests
	
def merge_not_clue():
	old_not_clues = [test.get_empty_not_clue() for i in range(test.HAND_SIZE)]
	old_not_clues[0]["ranks"] = [3]
	new_not_clue = [test.get_empty_not_clue() for i in range(test.HAND_SIZE)]
	new_not_clue[0]["colors"] = ["W"]
	test.merge_not_clue(old_not_clues, new_not_clue)
	tests = []
	tests.append(old_not_clues[0] == {"colors": ["W"], "ranks": [3]})
	for i in range(test.HAND_SIZE - 1):
		tests.append(old_not_clues[i + 1] == test.get_empty_not_clue())
		
	return False not in tests
	
def delete_slot():
	some_clue = [test.get_empty_clue() for i in range(test.HAND_SIZE)]
	some_clue[1] = test.make_card("G")
	test.delete_slot(some_clue, 0, test.get_empty_clue())
	tests = []
	tests.append(some_clue[0] == test.make_card("G"))
	for i in range(test.HAND_SIZE - 1):
		tests.append(some_clue[i + 1] == test.get_empty_clue())

	some_not_clue = [test.get_empty_not_clue() for i in range(test.HAND_SIZE)]
	some_not_clue[1]["ranks"] = [1, 2]
	test.delete_slot(some_not_clue, 0, test.get_empty_not_clue())	

	tests.append(some_not_clue[0] == {"colors": [], "ranks": [1, 2]})
	for i in range(test.HAND_SIZE - 1):
		tests.append(some_not_clue[i + 1] == test.get_empty_not_clue())
		
	removed_not_clue = test.delete_slot(some_not_clue, 0)
	tests.append(removed_not_clue["ranks"] == [1, 2])
	tests.append(len(some_not_clue) == 4)
	for i in range(len(some_not_clue) - 1):
		tests.append(some_not_clue[i] == test.get_empty_not_clue())
		
	test.delete_slot(some_not_clue, 0, {"colors": ["W"], "ranks": [3, 4]})
	tests.append(some_not_clue[3] == {"colors": ["W"], "ranks": [3, 4]})
		
	return False not in tests

def get_not_clue_from_clue():
	clue = [test.get_empty_clue() for i in range(test.HAND_SIZE)]
	clue[0] = test.make_card("G")
	not_clue = test.get_not_clue_from_clue(clue)
	tests = []
	tests.append(not_clue[0] == test.get_empty_not_clue())
	for i in range(test.HAND_SIZE - 1):
		tests.append(not_clue[i + 1]["colors"] == ["G"])
	for i in range(test.HAND_SIZE):
		tests.append(not_clue[i]["ranks"] == [])
	return False not in tests

def has_overrepresented_card():
	tests = []
	tests.append(not test.has_overrepresented_card([test.make_card("G", i) for i in range(5)]))
	tests.append(test.has_overrepresented_card([test.make_card("G", 0) for i in range(5)]))
	tests.append(not test.has_overrepresented_card([test.make_card("G", i % 2) for i in range(5)]))
	tests.append(not test.has_overrepresented_card([test.make_card("G", int(i / 3)) for i in range(5)]))
	tests.append(test.has_overrepresented_card([test.make_card("G", int(i / 4)) for i in range(5)]))
	return False not in tests

def get_hand_entropy():

	correct_entropies = [10**5, 3 * 2 * 2 * 2 * 1, 1, 46 * 47 * 48 * 49 * 50, 3 * 2 * 2 * 2 * 6, 5 * 9 * 8 * 7 * 6, 5 * 4 * 3 * 2 * 1]
	received_entropies = []

	# Case 1 ---------------------------------------------------------
	clues = [test.make_card(test.COLORS[i]) for i in range(test.HAND_SIZE)]
	
	not_clues = [test.get_empty_not_clue() for i in range(test.HAND_SIZE)]
	reserved_cards = []
	
	hand_entropy = test.get_hand_entropy(clues, not_clues, reserved_cards)
	received_entropies.append(hand_entropy[0])
	
	# Case 2 ---------------------------------------------------------
	clues = [test.make_card("G", i) for i in range(5)]
	hand_entropy = test.get_hand_entropy(clues, not_clues, reserved_cards)
	received_entropies.append(hand_entropy[0])

	# Case 3 ---------------------------------------------------------
	clues = [test.make_card(color, 4) for color in test.COLORS]
	hand_entropy = test.get_hand_entropy(clues, not_clues, reserved_cards)
	received_entropies.append(hand_entropy[0])

	# Case 4 ---------------------------------------------------------
	# First just initialize at list of all non-clues
	clues = [test.get_empty_clue() for i in range(test.HAND_SIZE)]
	hand_entropy = test.get_hand_entropy(clues, not_clues, reserved_cards)
	received_entropies.append(hand_entropy[0])
	
	# Case 5 ---------------------------------------------------------
	clues = [test.make_card("G") for i in range(5)]
	for i in range(4): # Intentionally iterating over less than the entire hand
		clues[i]["rank"] = i

	hand_entropy = test.get_hand_entropy(clues, not_clues, reserved_cards)
	received_entropies.append(hand_entropy[0])

	# Case 6 ---------------------------------------------------------
	clues = [test.make_card("G") for i in range(5)]
	not_clues[2]["ranks"] = [0, 1]
	hand_entropy = test.get_hand_entropy(clues, not_clues, reserved_cards)
	received_entropies.append(hand_entropy[0])
	
	# Case 7 ---------------------------------------------------------
	clues = [test.make_card("G") for i in range(5)]
	for i in range(5):
		not_clues[i]["ranks"] = [0, 1]
	hand_entropy = test.get_hand_entropy(clues, not_clues, reserved_cards)
	received_entropies.append(hand_entropy[0])
	
	return correct_entropies == received_entropies
	
def get_clues_from_hint():
	hint = {
            "action_type": "REVEAL_RANK",
            "target_offset": 1,
            "rank": 2
        }
		
	other_player_hand = [
      { "color": "G", "rank": 2 },
      { "color": "W", "rank": 0 },
      { "color": "R", "rank": 2 },
      { "color": "W", "rank": 4 },
      { "color": "W", "rank": 0 }
    ]
	
	received_clue, received_not_clue = test.get_clues_from_hint(hint, other_player_hand)
	tests = []
	tests.append(False not in [(test.get_rank(received_clue[i]) == test.get_rank(other_player_hand[i]) or received_not_clue[i]["ranks"] == [2]) for i in range(test.HAND_SIZE)])
	
	# Case 2 --------------------------------------------------------
	hint = {
            "action_type": "REVEAL_COLOR",
            "target_offset": 1,
            "color": "W"
        }
		
	other_player_hand = [
      { "color": "G", "rank": 2 },
      { "color": "W", "rank": 0 },
      { "color": "R", "rank": 2 },
      { "color": "W", "rank": 4 },
      { "color": "W", "rank": 0 }
    ]
	
	received_clues, received_not_clues = test.get_clues_from_hint(hint, other_player_hand)
	tests = []
	tests.append(False not in [(test.get_color(received_clues[i]) == test.get_color(other_player_hand[i]) or received_not_clues[i]["colors"] == ["W"]) for i in range(test.HAND_SIZE)])
	return False not in tests

def get_clues_from_observation_change():

	tests = []

	received_clues, received_not_clues = test.get_clues_from_observation_change(observation_reader_test.TEST_OBSERVATION, observation_reader_test.TEST_OBSERVATION_2)
	
	tests.append(received_clues == [{'color': None, 'rank': None}, {'color': None, 'rank': None}, {'color': 'W', 'rank': None}, {'color': 'W', 'rank': None}, {'color': None, 'rank': None}])
	tests.append(received_not_clues == [{'colors': ['W'], 'ranks': []}, {'colors': ['W'], 'ranks': []}, {'colors': [], 'ranks': []}, {'colors': [], 'ranks': []}, {'colors': ['W'], 'ranks': []}])
	
	received_clues, received_not_clues = test.get_clues_from_observation_change(observation_reader_test.TEST_OBSERVATION, observation_reader_test.TEST_OBSERVATION_3)
	
	tests.append(received_clues == [{'color': None, 'rank': None}, {'color': None, 'rank': 2}, {'color': None, 'rank': None}, {'color': None, 'rank': None}, {'color': None, 'rank': None}])
	tests.append(received_not_clues == [{'colors': [], 'ranks': [2]}, {'colors': [], 'ranks': []}, {'colors': [], 'ranks': [2]}, {'colors': [], 'ranks': [2]}, {'colors': [], 'ranks': [2]}])
	
	return False not in tests
	
def get_entropy_change_factor_for_clue():

	correct_entropy_change_factors = [(3 * 7 * 6 * 5 * 4) / (10 * 9 * 8 * 7 * 6)]
	received_entropy_change_factors = []

	clues = [test.make_card("G") for i in range(test.HAND_SIZE)]
	not_clues = [test.get_empty_not_clue() for i in range(test.HAND_SIZE)]
	reserved_cards = []

	new_clue = [test.get_empty_clue() for i in range(test.HAND_SIZE)]
	new_clue[0]["rank"] = 0
	new_not_clue = [test.get_empty_not_clue() for i in range(test.HAND_SIZE)]
	for i in range(test.HAND_SIZE - 1):
		new_not_clue[i + 1]["ranks"].append(0)
	
	entropy_factor, _, _, _, _ = test.get_entropy_change_factor_for_clue(clues, not_clues, reserved_cards, new_clue, new_not_clue)
	received_entropy_change_factors.append(entropy_factor)
	
	return correct_entropy_change_factors == received_entropy_change_factors
	
def is_card_playable():
	fireworks = {test.COLORS[i]: i for i in range(len(test.COLORS))}
	tests = []
	for i in range(len(test.COLORS)):
		color = test.COLORS[i]
		for rank in test.ALL_UNIQUE_RANKS:
			card = test.make_card(color, rank)
			tests.append(test.is_card_playable(card, fireworks) == (i == rank))
	
	return False not in tests
	
def get_unique_playable_cards():
	fireworks = [
		{"B": 0, "G": 0, "R": 0, "W": 0, "Y": 0},
		{"B": 3, "G": 0, "R": 0, "W": 0, "Y": 0},
		{"B": 0, "G": 4, "R": 5, "W": 1, "Y": 0},
		{"B": 1, "G": 0, "R": 2, "W": 6, "Y": 1}
	]
	correct_cards = [
		[test.make_card("B", 0), test.make_card("G", 0), test.make_card("R", 0), test.make_card("W", 0), test.make_card("Y", 0)],
		[test.make_card("B", 3), test.make_card("G", 0), test.make_card("R", 0), test.make_card("W", 0), test.make_card("Y", 0)],
		[test.make_card("B", 0), test.make_card("G", 4), test.make_card("W", 1), test.make_card("Y", 0)],
		[test.make_card("B", 1), test.make_card("G", 0), test.make_card("R", 2), test.make_card("Y", 1)]
	]
	
	tests = []
	for i in range(len(fireworks)):
		current_fireworks = fireworks[i]
		tests.append(correct_cards[i] == test.get_unique_playable_cards(current_fireworks))
	return False not in tests
	
def is_already_played():
	fireworks = {"B": 0, "G": 4, "R": 5, "W": 1, "Y": 0}
	tests = []
	tests.append(not test.is_already_played(test.make_card("B", 0), fireworks))
	tests.append(test.is_already_played(test.make_card("G", 0), fireworks))
	tests.append(test.is_already_played(test.make_card("G", 2), fireworks))
	tests.append(not test.is_already_played(test.make_card("G", 4), fireworks))
	for i in range(5):
		tests.append(test.is_already_played(test.make_card("R", i), fireworks))
		tests.append(not test.is_already_played(test.make_card("Y", i), fireworks))
	fireworks = {'B': 3, 'G': 1, 'R': 5, 'W': 2, 'Y': 3}
	tests.append(test.is_already_played(test.make_card("W", 1), fireworks))
	return False not in tests
	
def is_safely_discardable():
	fireworks = {"B": 0, "G": 4, "R": 5, "W": 1, "Y": 0}
	deck_size = 40
	discarded_cards = []
	tests = []
	for i in range(5):
		tests.append(test.is_safely_discardable(test.make_card("R", i), fireworks, test.ALL_CARDS, discarded_cards, deck_size))
	tests.append(test.is_safely_discardable(test.make_card("W", 0), fireworks, test.ALL_CARDS, discarded_cards, deck_size))
	non_reserved_cards = [test.make_card("Y", i) for i in range(5)]
	for i in range(5):
		tests.append(not test.is_safely_discardable(test.make_card("Y", i), fireworks, non_reserved_cards, discarded_cards, deck_size))
	non_reserved_cards = [test.make_card("R", i) for i in range(5)]
	for i in range(5):
		tests.append(test.is_safely_discardable(test.make_card("R", i), fireworks, non_reserved_cards, discarded_cards, deck_size))
	# Test that an unplayed card is safe to discard if you are locked out of every playing it
	for i in range(3):
		discarded_cards.append(test.make_card("Y", 0))
	non_reserved_cards = [test.make_card("Y", 3)]
	tests.append(test.is_safely_discardable(test.make_card("Y", 3), fireworks, non_reserved_cards, discarded_cards, deck_size))
	return False not in tests

def get_playable_probabilities():
	tests = []
	return False not in tests

def get_safely_discardable_probabilities():
	tests = []
	return False not in tests

def get_unneeded_probabilities():
	tests = []
	fireworks = {"B": 0, "G": 4, "R": 5, "W": 1, "Y": 0}
	discarded_cards = []
	clues = [test.get_empty_clue() for i in range(5)]
	clues[0]["color"] = "R"
	not_clues = [test.get_empty_not_clue() for i in range(5)]
	not_clues[-1]["ranks"].append(0)
	tests.append(test.get_unneeded_probabilities(clues, not_clues, discarded_cards, fireworks) == [1, 12/40, 12/40, 12/40, 6/28])
	return False not in tests

def get_unseen_cards():
	tests = []
	fireworks = {"B": 0, "G": 0, "R": 0, "W": 0, "Y": 0}
	discarded_cards = []
	other_player_hand = None
	tests.append(len(test.get_unseen_cards(discarded_cards, fireworks, other_player_hand)) == len(test.ALL_CARDS))
	fireworks = {"B": 0, "G": 4, "R": 5, "W": 1, "Y": 0}
	tests.append(len(test.get_unseen_cards(discarded_cards, fireworks, other_player_hand)) == len(test.ALL_CARDS) - 10)
	discarded_cards.append(test.make_card("B", 0))
	discarded_cards.append(test.make_card("B", 0))
	discarded_cards.append(test.make_card("B", 0))
	tests.append(len(test.get_unseen_cards(discarded_cards, fireworks, other_player_hand)) == len(test.ALL_CARDS) - 13)
	tests.append(test.make_card("B", 0) not in test.get_unseen_cards(discarded_cards, fireworks, other_player_hand))
	other_player_hand = [test.make_card("B", 1)]
	tests.append(len(test.get_unseen_cards(discarded_cards, fireworks, other_player_hand)) == len(test.ALL_CARDS) - 14)
	return False not in tests
	
def fast_binom():
	tests = []
	tests.append(test.fast_binom(5, 4) == 5)
	tests.append(test.fast_binom(5, 1) == 5 * 4 * 3 * 2)
	return False not in tests

# Add methods to this list if they should be unit tested
methods_to_test = [
	all_cards_correct_number,
	get_empty_clue,
	get_empty_not_clue,
	get_color,
	get_rank,
	rank_invalid,
	get_multiplicity_by_rank,
	does_card_match_clue,
	get_cards_matching_clue,
	get_indexed_wild_card,
	is_card_wild,
	make_card,
	merge_clue,
	merge_not_clue,
	delete_slot,
	get_not_clue_from_clue,
	has_overrepresented_card,
	get_hand_entropy,
	get_clues_from_hint,
	get_clues_from_observation_change,
	get_entropy_change_factor_for_clue,
	is_card_playable,
	get_unique_playable_cards,
	is_already_played,
	is_safely_discardable,
	get_unneeded_probabilities,
	fast_binom
]
