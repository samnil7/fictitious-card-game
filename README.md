#  Fictitious Card Game

[![Build Status](https://travis-ci.org/suhasgaddam/deck-of-cards-python.svg?branch=master)](https://travis-ci.org/suhasgaddam/deck-of-cards-python)
[![Documentation Status](https://readthedocs.org/projects/deck-of-cards-python/badge/?version=latest)](http://deck-of-cards-python.readthedocs.org/en/latest/)

![deck-of-cards](banner.png)

## Purpose
 - Development of Fictitious Card System for branching out the music event for DICE FM

## About
This project is about python implementation for Deck of Cards Game.
Running this application creates deck of card (52 cards) and then cards are shuffled.
It returns any two random cards. e.g output looks like - Two of Hearts, Jack of Diamonds.

It consists of below modules:
- `deck_card/`: consist of python code for for deck of card game -  [card.py](https://github.com/samnil7/fictitious-card-game/blob/main/deck_cards/card.py)
- `test/`: consist of test use case - [test_cases_card.py](https://github.com/samnil7/fictitious-card-game/blob/main/test/test_card.py)
- `[1]`:  Solution of stage 1 - [Github Action/workflow to create docker image](https://github.com/samnil7/fictitious-card-game/tree/main/.github/workflows)
- `[2]`:  Solution of stage 2 - [docker image in Github Package Storage](https://github.com/samnil7?tab=packages&repo_name=fictitious-card-game)


## Installation

The project requirements necessitate Docker for Desktop, Python IDE, Ubuntu 18.04 LTS and Github Personal Access Token

#### Install Requirements

-   Install the dependencies using the following command: 
     ```
    pip freeze > requirements.txt 
    ```
#### Preparations for Github Package Storage :

Rather than allowing Docker to retrieve the image from the Docker Hub
or Github container Repositories, users may also build the docker
image locally by cloning the image repo from Github.

- Create a new personal access token (PAT)

- Save your PAT. We recommend saving your PAT as an environment variable.
     ```
    $ export CR_PAT=YOUR_TOKEN
    ```
- Clone the repo:
     ```
    git clone https://github.com/samnil7/fictitious-card-game.git
    ```
- After cloning, navigate to the location:
     ```
    cd fictitious-card-game
    ```
  
- Alter the Dockerfile as desired, then build the image locally: (don't
miss the dot at the end)
     ```
    docker build -t ghcr.io/samnil7/fictitious-card-game-package:latest .
    -> Login Succeeded
    ```

- Pushing container images

     ```
    docker push ghcr.io/samnil7/fictitious-card-game-package:latest
    ```
    
## How to use

-   For application run- Run the following command in the parent directory:
    ```
    python main.py
    ```

-   For running test use case - Run the following command in the parent directory:

    ```
    python py.test
    ```
    
## Further information

- logging is added to monitor, track and troubleshoot issues if any while running in production system
- Python 3.9 version is used

