
# The Cyclone Hanabi Agent

## Overview

This repo provides the source code for the Cyclone Hanabi agent detailed in [this paper](https://arxiv.org/abs/2111.01726). This agent was designed and trained to excel at playing two-player Hanabi well with human teammates (although this repo also includes variant agents that were trained towards different objectives). The mean score achieved in human play experiments is 16 as mentioned in the paper.

## Compatibility

This repo contains a gym environment that follows the same game state management as the [Hanabi Learning Environment](https://github.com/deepmind/hanabi-learning-environment/). The parsers in this repo (`observation_reader.py` and `observation_bundle_reader.py`) are compatible with this game state format. This project has no major dependencies other than standard python libraries (`math`, `multiprocessing`, `copy`, `numpy`, `random`, and `time`).

## Functionality

There are three scripts provided in the project root.

1. `unit_test.py` runs through a series of unit tests for the repo. These tests primarily monitor the integrity of utility, parsing, and math functions. This script can be useful for anyone making changes to the repo who wants to check that important functionality remains intact.

1. `run_games.py` allows the developer to hard code two agents to play a series of games and to view basic score statistics at the end. The games are configured to run in multiple processes.

1. `human_play.py` launches a command line interface through which one can play Hanabi with a hard coded agent from the repo.

## Agents

There are three AI agents in this repo that have the same general structure with parameters trained for three different objectives.

1. `human_like_agent.py` was trained to emulate the play style of the author of this repo (with ~70% accuracy).

1. `self_play_agent.py` was trained to achieve a high score when paired with a copy of itself.

1. `human_complimentary_agent.py` was trained to achieve a high score with the `human_like_agent.py`. The `human_complimentary_agent.py` is the agent that has the best performance with human teammates out of the three agents in this repo.

There is also a `random_model.py` that can be used to create a teammate who makes random moves. The utility of this agent is understandably low.

## Under the Hood

### Basic Gameplay

Games are played by

1. Calling `gym.get_observation()` and passing the result to _both_ agents via `policy.get_actions(observation_bundle)` on each of the two policies
1. Passing the result (`move`) of `policy.get_actions(observation_bundle)` to the gym via `gym.step(move)`.

It is important, but not obvious, that an observation bundle from the gym be passed to both players on each ply (even though it is either one player's turn or the other's). The reason is that `policy.get_actions` is responsible for tracking state information from turn to turn (for instance, what a player knows about their hand). Furthermore, each player policy is capable of detecting whether the current ply belongs to the policy's player, and if it does not, the policy will return a move of `None`. Therefore, the appropriate procedure for running a game is captured in the minimal code snippet below

```python

# Decision models are chosen from those in the repo (e.g. SelfPlayAgent()) or custom agents.
agent0 = policy.MyPolicy(decision_model_0)
agent1 = policy.MyPolicy(decision_model_1)

# Here agents learn which player they are (agent0 learns it will play first) and if these agents existed in prior games, they are reset.
agent0.game_reset(0)
agent1.game_reset(1)

my_gym = gym.Gym()

while not my_gym.is_game_over():

    # One of the two statements below returns a valid move (depending on whose turn it is) and the other will return None.
    agent0_action = agent0.get_actions(my_gym.get_observation_bundle())
    agent1_action = agent1.get_actions(my_gym.get_observation_bundle())

    if agent0_action is not None:
        my_gym.step(agent0_action)
    else
        my_gym.step(agent1_action)
```

### The AI

While the `policy` object keeps track of information that _might_ be used by an agent, the decision model passed to the policy at instantiation is responsible for dictating how the agent uses this information to make a decision. The `decision_model` base class has one method, `decide_move`, and it takes a set of arguments that, for the agents of this repo, contain all the information needed to decide an appropriate move. Specifically, the `base_agent` class is fairly liberally commented and illustrates how most of the agents in the repo make a decision.

The `base_agent` contains most of the logic for how a move is decided, but it is missing twelve weights that dictate the final play style. These weights are supplied by the derived classes of `base_agent`. These weights correspond to expected values for various outcomes (e.g. successfully discarding a card that wasn't desperately needed). Changing these weights can profoundly change the play style of an agent. For instance, the three principal agents of this repo (`SelfPlayAgent`, `HumanComplementaryAgent`, and `HumanLikeAgent`) differ from one another only in the values of the weights, yet their play styles are markedly different.

The `policy` object contains a `verbose` flag. If the `verbose` flag is set to `True`, then the agent will print a large amount of information to the console explaining its decision. If this is not desired, set the flag as `False` to suppress this console output.

## Saving Decisions for Analysis

It can be of interest to save game scenarios and corresponding decisions so as to create a labeled (or unlabeled) dataset of game states. For instance, to train the `HumanLikeAgent`, the author of this repo first played a number of games via `human_play.py` where each decision of the author's was saved. Later, a copy of the `SelfPlayAgent` was trained (through changes on the weights) to better predict the decisions the author made. To facilitate research like this, a class (`decision_basis`) is included which represents an object that stores all of the information needed for a decision model to make a decision (along with an extra field for storing a decision index label, such as the index of the decision that a human made).

If you find it useful to store decisions for later analysis, one option is to initialize a `decision_basis` during a game and to append it to an array. The array can be saved (for instance, using the Python `pickle` library) for later analysis. When analyzing, one can read a `decision_basis` from a file and extract its fields to give to a decision model. In this way, AI decisions can be obtained using saved `decision_basis` objects, and no policy is needed (since each `decision_basis` includes information that would normally be curated by a `policy` object).

## Support

If you need help with this repo or spot any problems, send correspondence to nick.kantack@jhuapl.edu.