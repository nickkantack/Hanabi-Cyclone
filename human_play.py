"""
human_play allows a human to play Hanabi via the console with an AI teammate built from one of the available decision models.
"""

import util.observation_bundle_reader as bundle_reader
import util.observation_reader as ob_reader
import util.gym as gym
from decision_models.real_human import RealHuman
from decision_models.human_complementary_agent import HumanComplementaryAgent
import util.policy as policy

# Change the line below to initialize whichever decision model you want to play with.
DECISION_MODEL_OF_AGENT_TO_PLAY_WITH = HumanComplementaryAgent()

def run_a_game(my_gym, agent0, agent1):
	
	my_gym.reset()
	
	bundle = my_gym.get_observation_bundle()
	
	agent0.game_reset(0)
	agent1.game_reset(1)
	done = False

	while not done:
		agent0_action = agent0.get_actions(bundle)
		agent1_action = agent1.get_actions(bundle)

		action = None
		if my_gym.get_current_player() == 0:
			action = agent0_action
		else:
			action = agent1_action

		bundle = my_gym.step(action)
		
		if my_gym.is_game_over():
			done = True
			score = 0
			fireworks = bundle_reader.get_fireworks(bundle)
			for color in fireworks:
				score += fireworks[color]

	return (len(agent0.get_errors()) == 0 and len(agent1.get_errors()) == 0, score)

def run_many_games():

	# Create a gym object that will manage the observations
	my_gym = gym.Gym()

	agent0 = policy.MyPolicy(RealHuman())
	agent1 = policy.MyPolicy(DECISION_MODEL_OF_AGENT_TO_PLAY_WITH)

	print(f"You are playing with {agent1.decision_model.get_variant_name()}")
	
	# Make both of the agents quiet. If you skip this step, the agent will remain verbose and
	# print a lot of information about its decision before each decision is made.
	agent0.set_verbosity(False)
	agent1.set_verbosity(False)

	scores = []

	(success, score) = run_a_game(my_gym, agent0, agent1)
	if not success:
		print(f"Error encountered in game")
		return False
	else:
		final_player_0_observation = bundle_reader.get_observations(my_gym.get_observation_bundle())[0]

		print(f"Completed game with no error. Fireworks: {ob_reader.get_fireworks(final_player_0_observation)}")
		scores.append(score)

	return True
	
if __name__ == "__main__":
	run_many_games()
	
methods_to_test = [
	run_many_games
]
