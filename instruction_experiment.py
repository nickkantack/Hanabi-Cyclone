"""
human_play allows a human to play Hanabi via the console with an AI teammate built from one of the available decision models.
"""

from decision_models.base_agent import FIXED_ACTIONS
import util.observation_bundle_reader as bundle_reader
import util.observation_reader as ob_reader
import util.gym as gym
from decision_models.real_human import RealHuman
from decision_models.human_like_agent import HumanLikeAgent
from decision_models.self_play_agent import SelfPlayAgent
import util.policy as policy
import numpy
import pickle
import os
import matplotlib.pyplot as plt

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

def run_experiment():

    # Create a gym object that will manage the observations
    my_gym = gym.Gym()

    agent0 = policy.MyPolicy(RealHuman())
    agent1 = policy.MyPolicy(SelfPlayAgent())

    print(f"You are playing with {agent1.decision_model.get_variant_name()}")

    # Make both of the agents quiet. If you skip this step, the agent will remain verbose and
    # print a lot of information about its decision before each decision is made.
    agent0.set_verbosity(False)
    agent1.set_verbosity(False)

    number_of_games = 1
    lines_for_log = ""
    scores = []

    if number_of_games != 1:
        print("You cannot queue up more than one game to be played with a human. Please fix the human_play.py script.")
        return True

    (success, score) = run_a_game(my_gym, agent0, agent1)
    if not success:
        print(f"Error encountered in game")
        return False
    else:
        final_player_0_observation = bundle_reader.get_observations(my_gym.get_observation_bundle())[0]

        print(f"Completed game with no error. Fireworks: {ob_reader.get_fireworks(final_player_0_observation)}")
        scores.append(score)


    human_decision_log_path = agent0.decision_model.filename

    # Generate instructions
    number_of_instruction_sets = 40
    instructor_decision_model = HumanLikeAgent()
    initial_weights = instructor_decision_model.w.copy()
    best_matching_weights = instructor_decision_model.w.copy()
    best_match_fraction = 0
    all_matching_fractions = []
    _, initial_match_fraction = build_H_and_Y_matrices_from_log(instructor_decision_model, human_decision_log_path, True)
    all_matching_fractions.append(initial_match_fraction)
    log_text = ""
    for i in range(number_of_instruction_sets):
        instructor_decision_model, local_corrects = build_H_and_Y_matrices_from_log(instructor_decision_model, human_decision_log_path, False)
        log_text = print_and_log(f"Finished analysis step {i}/{number_of_instruction_sets} with a matching fraction of {local_corrects}", log_text)
        all_matching_fractions.append(local_corrects)
        if local_corrects > best_match_fraction:
            best_matching_weights = instructor_decision_model.w.copy()
            best_match_fraction = local_corrects

    # Give the instructions
    delta_w = initial_weights - best_matching_weights
    log_text = print_and_log(f"I was able to improve matching from {initial_match_fraction} to {best_match_fraction}. Therefore, I estimate you could play more like me with the following changes:", log_text)
    log_text = print_and_log(f"Change in misplay cost for less than 2 strikes: {format_instruction(delta_w[0])}", log_text)
    log_text = print_and_log(f"Change in misplay cost for 2 strikes: {format_instruction(delta_w[1])}", log_text)
    log_text = print_and_log(f"Playing singled out cards: {format_instruction(delta_w[2])}", log_text)
    log_text = print_and_log(f"Singling out playable cards: {format_instruction(delta_w[3])}", log_text)
    log_text = print_and_log(f"Singling out non-playable card penalty: {format_instruction(delta_w[4])}", log_text)
    log_text = print_and_log(f"Penalty for discarding a single out card: {format_instruction(delta_w[5])}", log_text)
    log_text = print_and_log(f"Cost to other player misplays: {format_instruction(delta_w[6])}", log_text)
    log_text = print_and_log(f"Value other player plays: {format_instruction(delta_w[7])}", log_text)
    log_text = print_and_log(f"Value playing a card: {format_instruction(delta_w[8])}", log_text)
    log_text = print_and_log(f"Clue bonus per info token: {format_instruction(delta_w[9])}", log_text)
    log_text = print_and_log(f"Value of a good discard: {format_instruction(delta_w[10])}", log_text)
    log_text = print_and_log(f"Force safe discard factor: {format_instruction(delta_w[11])}", log_text)

    log_text = print_and_log("The experiment is now complete.", log_text)

    # Save log_text
    output_log = open(os.path.join(os.getcwd(), "logs", f"instructions_{agent0.decision_model.log_index}.txt"), "w")
    output_log.write(log_text)
    output_log.close()

    # Plot and save the progression
    plt.plot([i for i in range(len(all_matching_fractions))], all_matching_fractions)
    plt.title(f"Quality of match after applying inverse instructions for experiment {agent0.decision_model.log_index}")
    plt.ylabel("Fraction of human moves predicted")
    plt.xlabel("Number of instruction steps taken")
    plt.savefig(os.path.join(os.getcwd(), "logs", f"training_progression_{agent0.decision_model.log_index}"))

def print_and_log(message, log_string):
    print(message)
    log_string += message + "\n"
    return log_string

def build_H_and_Y_matrices_from_log(decision_model, log_path, preserve_instructee = False):

    human_decisions_by_fixed_index = []

    file = open(log_path, "rb")
    decision_bases = pickle.load(file)

    number_of_decisions = len(decision_bases)
    stacked_H = numpy.zeros((len(FIXED_ACTIONS) * number_of_decisions, len(decision_model.w)))
    stacked_ideal_outputs = numpy.zeros((len(FIXED_ACTIONS) * number_of_decisions,))
    stacked_norm_minimal_output_difference_ideal_v_current = numpy.zeros((len(FIXED_ACTIONS) * number_of_decisions,))

    for line_index, decoded_decision_basis in enumerate(decision_bases):
        move, _, _, h_matrix, y_vector = decision_model.decide_move(decoded_decision_basis.observation, decoded_decision_basis.my_not_clues, decoded_decision_basis.other_player_not_clues, decoded_decision_basis.playable_probabilities,
        decoded_decision_basis.safely_discardable_probabilities, decoded_decision_basis.unneeded_probabilities,
        decoded_decision_basis.hint_nuggets, decoded_decision_basis.singled_out_playable_card_index, decoded_decision_basis.singled_out_cards, lambda x : x)
        legal_moves = ob_reader.get_legal_moves(decoded_decision_basis.observation)
        move_index = -1
        for i in range(len(legal_moves)):
            if legal_moves[i] == move:
                move_index = i
                break

        human_move_index = decoded_decision_basis.human_legal_move_index

        # Calculate norm minimal Y diff
        instructee_choice_fixed_index = FIXED_ACTIONS.index(legal_moves[move_index])
        human_choice_fixed_index = FIXED_ACTIONS.index(legal_moves[human_move_index])
        human_decisions_by_fixed_index.append(human_choice_fixed_index)
        if instructee_choice_fixed_index != human_choice_fixed_index:
            max_element_allowed = (y_vector[instructee_choice_fixed_index] + y_vector[human_choice_fixed_index]) / 2
            norm_min_z = y_vector.copy()
            for i in range(len(norm_min_z)):
                if norm_min_z[i] > max_element_allowed:
                    norm_min_z[i] = max_element_allowed
                if i == human_choice_fixed_index:
                    norm_min_z[i] = max_element_allowed + 1
            stacked_ideal_outputs[line_index * len(FIXED_ACTIONS):(line_index + 1) * len(FIXED_ACTIONS)] = y_vector
            stacked_norm_minimal_output_difference_ideal_v_current[line_index * len(FIXED_ACTIONS):(line_index + 1) * len(FIXED_ACTIONS)] = norm_min_z - y_vector

        # Store the vectors and matrices
        stacked_H[line_index * len(FIXED_ACTIONS):(line_index + 1) * len(FIXED_ACTIONS),:] = h_matrix


    # Calculate instruction
    delta_w = numpy.linalg.lstsq(stacked_H, stacked_norm_minimal_output_difference_ideal_v_current, rcond=None)
    delta_w = delta_w[0]

    # See how human like ultron is with the corrections applied. stacked_H * (ultron.w + delta_w) should be used
    times_agreed_uncorrected = 0
    times_agreed_corrected = 0
    for i in range(number_of_decisions):
        human_index = human_decisions_by_fixed_index[i]
        h_matrix = stacked_H[i * len(FIXED_ACTIONS):(i + 1) * len(FIXED_ACTIONS),:]
        ultron_output = numpy.matmul(h_matrix, decision_model.w)
        ultron_corrected_output = numpy.matmul(h_matrix, decision_model.w + delta_w)
        if ultron_corrected_output[human_index] == max(ultron_corrected_output):
            times_agreed_corrected += 1
        if ultron_output[human_index] == max(ultron_output):
            times_agreed_uncorrected += 1

    # Change and return the decision model
    if not preserve_instructee:
        decision_model.load_new_weights(decision_model.w + delta_w)

    return decision_model, times_agreed_corrected / number_of_decisions
	
def format_instruction(value):
    result = ""
    if abs(value) < 0.1:
        result += "No change"
    else:
        result += "Value "
        if 0.1 < abs(value) < 0.3:
            result += "slightly "
        if 0.3 <= abs(value) < 1:
            result += ""
        if 1 <= abs(value):
            result += "much "
        if value > 0:
            result += "more"
        else:
            result += "less"
    result += "..........({:.2f})".format(value)
    return result


if __name__ == "__main__":
	run_experiment()
	