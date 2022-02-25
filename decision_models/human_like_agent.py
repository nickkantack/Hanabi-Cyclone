
from decision_models.decision_model import DecisionModel
import numpy

# Constants that do not need to be varied
INSURMOUNTABLE_COST = 1000000

class HumanLikeAgent(DecisionModel):

	"""
	HumanLikeAgent is trained to predict and make the decision that Nick (a human) would have made.
	"""

	def __init__(self):
		self.cost_misplay_by_strikes = [1, 1.5, 3]
		self.singled_out_playable_value_bump = 3
		self.decision_to_single_out_playable_card_bonus = 3
		self.decision_to_single_out_non_playable_card_penalty = 0
		self.singled_out_playable_discard_penalty = 0.5
		self.info_token_end_discard_penalty_factor = 2
		self.cost_misplay_other_player = 0
		self.play_multiplier = 1.5
		self.self_certain_play_bonus = 1
		self.clue_bonus_per_info_token = 0.5
		self.value_good_discard = 0.1
		self.force_safe_discard_factor = 0.25

	def get_variant_name(self):
		return "HumanLikeAgent"