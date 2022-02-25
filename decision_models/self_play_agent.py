
from decision_models.base_agent import BaseAgent
import numpy

class SelfPlayAgent(BaseAgent):

    def __init__(self):
        super().__init__()
        self.cost_misplay_by_strikes = [1, 1.5, 3]
        self.singled_out_playable_value_bump = 6
        self.decision_to_single_out_playable_card_bonus = 3
        self.decision_to_single_out_non_playable_card_penalty = 1
        self.singled_out_playable_discard_penalty = 0.5
        self.info_token_end_discard_penalty_factor = 4
        self.cost_misplay_other_player = 1
        self.play_multiplier = 2
        self.self_certain_play_bonus = 11
        self.clue_bonus_per_info_token = 0
        self.value_good_discard = 0.8
        self.force_safe_discard_factor = 0

    def get_variant_name(self):
        return f"SelfPlayAgent"