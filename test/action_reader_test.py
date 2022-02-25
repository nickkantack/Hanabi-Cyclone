
import util.action_reader as test

TEST_ACTIONS = [{
		  "action_type": "DISCARD",
		  "card_index": 4
		},
		{
		  "action_type": "PLAY",
		  "card_index": 0
		},
		{
		  "action_type": "REVEAL_COLOR",
		  "target_offset": 1,
		  "color": "W" 
		},
		{
		  "action_type": "REVEAL_RANK",
		  "target_offset": 1,
		  "rank": 4
		}]

def get_action_type():
	
	correct_action_types = ["DISCARD", "PLAY", "REVEAL_COLOR", "REVEAL_RANK"]
	tests = []
	for i in range(len(TEST_ACTIONS)):
		action = TEST_ACTIONS[i]
		tests.append(test.get_action_type(action) == correct_action_types[i])
	return False not in tests
	
def is_action_hint():
	tests = []
	for i in range(len(TEST_ACTIONS)):
		tests.append(test.is_action_hint(TEST_ACTIONS[i]) == (i > 1))
	return False not in tests
	
def get_card_index():
	correct_action_types = [4, 0, None, None]
	tests = []
	for i in range(len(TEST_ACTIONS)):
		action = TEST_ACTIONS[i]
		tests.append(test.get_card_index(action) == correct_action_types[i])
	return False not in tests
	
def get_new_action():
	actions = []
	actions.append(test.get_new_action(test.DISCARD, 4))
	actions.append(test.get_new_action(test.PLAY, 0))
	actions.append(test.get_new_action(test.REVEAL_COLOR, "W"))
	actions.append(test.get_new_action(test.REVEAL_RANK, 4))
	tests = []
	for i in range(len(actions)):
		tests.append(actions[i] == TEST_ACTIONS[i])
	return False not in tests
	
methods_to_test = [
	get_action_type,
	is_action_hint,
	get_card_index,
	get_new_action
]
