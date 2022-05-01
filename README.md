
# The Cyclone Hanabi Agent

## Overview

This branch is an experimental research branch tailored exclusively towards a demonstration of generating AI instructions via the norm minimal correction algorithm in [this paper](https://arxiv.org/abs/2111.01726). If you are here for the Cyclone Hanabi agent but not interested in this specific AI instruction demonstration, see the `main` branch of this repo.

## How to run the experiment

To run the experiment, from the root of this project execute the command
```
python instruction_experiment.py
```
The script will
1. Launch a game of Hanabi in the command line for you to play with the Cyclone agent (your actions will form the basis of the AI instructions).
1. At the games completion, the AI instructions will be automatically calculated and you will be presented with AI instructions that describe an estimate for the norm minimal modification to your decision policy needed in order for you to execute the Cyclone agent's decision policy. These instructions therefore represent instructions of how you could better emulate the Cyclone agent.
1. Results from the experiment will be saved in the `logs` folder for later review.

## Support

If you need help with this repo or spot any problems, send correspondence to nick.kantack@jhuapl.edu.
