# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
from math import log
import sys

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        if successorGameState.isWin():
            return float("inf")
                    
        for ghostState in newGhostStates:
            if util.manhattanDistance(ghostState.getPosition(), newPos) < 2:
                return float("-inf")
                                
        foodDist = []
        for food in list(newFood.asList()):
            foodDist.append(util.manhattanDistance(food, newPos))
                                        
        foodSuccessor = 0
        if (currentGameState.getNumFood() > successorGameState.getNumFood()):
            foodSuccessor = 300
                                                    
        return successorGameState.getScore() - 5 * min(foodDist) + foodSuccessor

                            

                

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        maxValue = float("-inf")
        maxAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            nextState = gameState.generateSuccessor(0, action)
            nextValue = self.getValue(nextState, 0, 1)
            if nextValue > maxValue:
                maxValue = nextValue
                maxAction = action
        return maxAction

    def getValue(self, gameState, currentDepth, agentIndex):
        if currentDepth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        elif agentIndex == 0:
            return self.maxValue(gameState,currentDepth)
        else:
            return self.minValue(gameState,currentDepth,agentIndex)

    def maxValue(self, gameState, currentDepth):
        maxValue = float("-inf")
        for action in gameState.getLegalActions(0):
            maxValue = max(maxValue, self.getValue(gameState.generateSuccessor(0, action), currentDepth, 1))
        return maxValue

    def minValue(self, gameState, currentDepth, agentIndex):
        minValue = float("inf")
        for action in gameState.getLegalActions(agentIndex):
            if agentIndex == gameState.getNumAgents()-1:
                minValue = min(minValue, self.getValue(gameState.generateSuccessor(agentIndex, action), currentDepth+1, 0))
            else:
                minValue = min(minValue, self.getValue(gameState.generateSuccessor(agentIndex, action), currentDepth, agentIndex+1))
        return minValue

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        max_value, next_action = self.minimax_alpha_beta(gameState, self.index, 0, -sys.maxsize, sys.maxsize)
        return next_action

    def minimax_alpha_beta(self, state, agent, depth, alpha, beta):
        num_agents = state.getNumAgents()
    
        if depth == self.depth and agent % num_agents == 0:
            return self.evaluationFunction(state), None
            
        if agent % num_agents == 0:
            return self.maximize_alpha_beta(state, agent % num_agents, depth, alpha, beta)
        
        return self.minimize_alpha_beta(state, agent % num_agents, depth, alpha, beta)

    def minimize_alpha_beta(self, state, agent, depth, alpha, beta):
        legal_actions = state.getLegalActions(agent)
        
        if len(legal_actions) == 0:
            return self.evaluationFunction(state), None
            
        value = sys.maxsize
        value_action = None
            
        next_agent = agent + 1
        for action in legal_actions:
            successor_state = state.generateSuccessor(agent, action)
            next_value, next_action = self.minimax_alpha_beta(successor_state, next_agent, depth, alpha, beta)
            if next_value < value:
                value = next_value
                value_action = action
            if value < alpha:
                return value, value_action
            beta = min(beta, value)
        
        return value, value_action

    def maximize_alpha_beta(self, state, agent, depth, alpha, beta):
        legal_actions = state.getLegalActions(agent)
        if len(legal_actions) == 0:
            return self.evaluationFunction(state), None
            
        value = -sys.maxsize
        value_action = None
            
        next_agent = agent + 1
        next_depth = depth + 1
        for action in legal_actions:
            successor_state = state.generateSuccessor(agent, action)
            next_value, next_action = self.minimax_alpha_beta(successor_state, next_agent, next_depth, alpha, beta)
            if next_value > value:
                value = next_value
                value_action = action
            if value > beta:
                return value, value_action
            alpha = max(alpha, value)
        
        return value, value_action



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        max_value, next_action = self.expectimax_value(gameState, self.index, 0)
        return next_action
        
    def expectimax_value(self, state, agent, depth):
        num_agents = state.getNumAgents()

        if depth == self.depth and agent % num_agents == 0:
            return self.evaluationFunction(state), None

        if agent % num_agents == 0:
            return self.maximize_value(state, agent % num_agents, depth)
        
        return self.probabilistic_value(state, agent % num_agents, depth)
    
    def probabilistic_value(self, state, agent, depth):
        successor_states = [(state.generateSuccessor(agent, action), action) for action in state.getLegalActions(agent)]
        
        if len(successor_states) == 0:
            return self.evaluationFunction(state), None
        `
        value = 0
        value_action = None
        
        next_agent = agent + 1
        events = 0
        for successor_state, action in successor_states:
            next_value, next_action = self.expectimax_value(successor_state, next_agent, depth)
            value += next_value
            events += 1
        
        return float(value) / events, value_action

    def maximize_value(self, state, agent, depth):
        successor_states = [(state.generateSuccessor(agent, action), action) for action in state.getLegalActions(agent)]
    
        if len(successor_states) == 0:
            return self.evaluationFunction(state), None
        
        value = -sys.maxsize
        value_action = None
        
        next_agent = agent + 1
        next_depth = depth + 1

        for successor_state, action in successor_states:
            next_value, next_action = self.expectimax_value(successor_state, next_agent, next_depth)
            if next_value > value:
                value = next_value
                value_action = action

        return value, value_action


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """

    "*** YOUR CODE HERE ***"
    next_pacman_position = currentGameState.getPacmanPosition()
    next_food = [food for food in currentGameState.getFood().asList() if food]
    next_ghosts_states = currentGameState.getGhostStates()
    next_ghosts_scared_timers = [ghostState.scaredTimer for ghostState in next_ghosts_states]
        
    ghost_distance = min(
        util.manhattanDistance(next_pacman_position, ghost.configuration.pos) for ghost in next_ghosts_states)
    closest_food_distance = min(
        util.manhattanDistance(next_pacman_position, nextFood) for nextFood in next_food) if next_food else 0
    scared_time = min(next_ghosts_scared_timers)
    
    remaining_food_feature = -len(next_food)

    ghost_distance_feature = -2 / (ghost_distance + 1) if scared_time == 0 else 0.5 / (ghost_distance + 1)

    closest_food_feature = 0.4 / (closest_food_distance + 1)
    
    power_pellets_feature = scared_time * 0.5
    game_score = currentGameState.getScore() * 0.6
                                        
    return remaining_food_feature + ghost_distance_feature + closest_food_feature + power_pellets_feature + game_score





# Abbreviation
better = betterEvaluationFunction
