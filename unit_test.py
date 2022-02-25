"""
unit_test runs all of the unit tests
"""

import test.card_utilities_test as card_utilities_test
import test.observation_reader_test as observation_reader_test
import test.observation_bundle_reader_test as observation_bundle_reader_test
import test.gym_test as gym_test
import test.action_reader_test as action_reader_test

def test_module(module):
	for method in module.methods_to_test:
		test_pass = method()
		print(f"{method.__name__} ------------------------", "SUCCESS" if test_pass else "FAILURE")
		if not test_pass:
			return False

	return True

def main():
	# Add modules to this list to be tested
	modules_to_test = [
		card_utilities_test,
		observation_reader_test,
		observation_bundle_reader_test,
		gym_test,
		action_reader_test,
	]

	for module in modules_to_test:
		print()
		print(module.__name__)
		print("-------------------------------------------------------")
		if not test_module(module):
			print("Test execution terminated.")
			break

if __name__ == "__main__":
	main()
