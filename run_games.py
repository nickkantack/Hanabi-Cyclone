from decision_models.base_agent import BaseAgent
from decision_models.human_complementary_agent import HumanComplementaryAgent
from decision_models.human_like_agent import HumanLikeAgent
import util.observation_bundle_reader as bundle_reader
import util.observation_reader as ob_reader
import util.gym as gym
import util.policy as policy
from decision_models.self_play_agent import SelfPlayAgent
from multiprocessing import Pool
import numpy
import time

def run_many_games():

	number_of_games = 20
	
	#####################################################
	# Using the two lines below, initialize whichever decision model you like
	#####################################################
	decision_model_0 = SelfPlayAgent()
	decision_model_1 = SelfPlayAgent()

	with Pool(processes=4) as pool:
		
		tuple_arguments = [(decision_model_0, decision_model_1) for i in range(number_of_games)]
		results = pool.starmap(run_a_game, tuple_arguments)
		
		scores = []
		worst_score = 26
		
		for result in results:
		
			scores.append(result[0])
			
			# If this score is the worst so far, store the records from the agents
			if result[0] < worst_score:
				worst_score = result[0]
		
		print(f"All {number_of_games} games completed with no errors. Average score: {numpy.mean(scores)}. Std dev: {numpy.std(scores)}, std dev of mean {numpy.std(scores) / number_of_games**0.5}. 95% confidence interval of ({numpy.mean(scores) - 1.96 * numpy.std(scores) / number_of_games**0.5}, {numpy.mean(scores) + 1.96 * numpy.std(scores) / number_of_games**0.5})")
		print(f"The worst game had a score of {worst_score}.")
		
	return True

def run_a_game(decision_model_0, decision_model_1):
	
	# Create a gym object that will manage the observations
	my_gym = gym.Gym()

	agent0 = policy.MyPolicy(decision_model_0)
	agent1 = policy.MyPolicy(decision_model_1)
	
	# Make both of the agents quiet
	agent0.set_verbosity(False)
	agent1.set_verbosity(False)
	
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

	print(f"A game completed at time {time.time()} with score {score}")

	return (score, bundle_reader.get_life_tokens(bundle), bundle_reader.get_information_tokens(bundle), agent0.record, agent1.record)

if __name__ == "__main__":
	run_many_games()