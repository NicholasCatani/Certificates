########################################################################################
## PROBLEM 1 ##


# You will need to design two classes to keep track of which parts of the room have been cleaned as well as the position and direction of each robot.
#
# In ps2.py, we've provided skeletons for the following two classes, which you will fill in in Problem 1:
#
# RectangularRoom: Represents the space to be cleaned and keeps track of which tiles have been cleaned.
# Position: We've also provided a complete implementation of this class. It stores the x- and y-coordinates of a robot in a room.
# Read ps2.py carefully before starting, so that you understand the provided code and its capabilities.
#
# Problem 1
# In this problem you will implement the RectangularRoom class. For this class, decide what fields you will use and decide how the following operations are to be performed:
#
# Initializing the object
# Marking an appropriate tile as cleaned when a robot moves to a given position (casting floats to ints - and/or the function math.floor - may be useful to you here)
# Determining if a given tile has been cleaned
# Determining how many tiles there are in the room
# Determining how many cleaned tiles there are in the room
# Getting a random position in the room
# Determining if a given position is in the room
# Complete the RectangularRoom class by implementing its methods in ps2.py.
#
# Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only a couple of lines of code.
#
# Hint: During debugging, you might want to use random.seed(0) so that your results are reproducible.
#
# Enter your code for RectangularRoom below.


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.
    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        width: an integer > 0
        height: an integer > 0
        """
        # raise NotImplementedError
        self.width = width
        self.height = height
        self.cleaned_tiles = []

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        pos: a Position
        """
        # raise NotImplementedError
        point = (int(pos.getX()), int(pos.getY()))
        if point not in self.cleaned_tiles:
            self.cleaned_tiles.append(point)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        Assumes that (m, n) represents a valid tile inside the room.
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # raise NotImplementedError
        self.m = m
        self.n = n
        tile = (self.m, self.n)
        if tile in self.cleaned_tiles:
            return True
        else:
            return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        returns: an integer
        """
        # raise NotImplementedError
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        returns: an integer
        """
        # raise NotImplementedError
        return len(self.cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        """
        # raise NotImplementedError
        randx = random.uniform(0, self.width)
        randy = random.uniform(0, self.height)
        return Position(randx, randy)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # raise NotImplementedError
        if pos.x >= 0 and pos.x < self.width and pos.y >= 0 and pos.y < self.height:
            return True
        else:
            return False


## Correct




########################################################################################
## PROBLEM 2 ##


# In ps2.py we provided you with the Robot class, which stores the position and direction of a robot. For this class, decide what fields you will use and decide how the following operations are to be performed:

# Initializing the object
# Accessing the robot's position
# Accessing the robot's direction
# Setting the robot's position
# Setting the robot's direction
# Complete the Robot class by implementing its methods in ps2.py.
#
# Note: When a Robot is initialized, it should clean the first tile it is initialized on. Generally the model these Robots will follow is that after a robot lands on a given tile, we will mark the entire tile as clean. This might not make sense if you're thinking about really large tiles, but as we make the size of the tiles smaller and smaller, this does actually become a pretty good approximation.
#
# Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only a couple of lines of code.
#
# Note: The Robot class is an abstract class, which means that we will never make an instance of it. Read up on the Python docs on abstract classes at this link and if you want more examples on abstract classes, follow this link.
#
# In the final implementation of Robot, not all methods will be implemented. Not to worry -- its subclass(es) will implement the method updatePositionAndClean()
#
# Enter your code for classes RectangularRoom (from the previous problem) and Robot below.


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.
    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        width: an integer > 0
        height: an integer > 0
        """
        # raise NotImplementedError
        self.width = width
        self.height = height
        self.cleaned_tiles = []

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        pos: a Position
        """
        # raise NotImplementedError
        point = (int(pos.getX()), int(pos.getY()))
        if point not in self.cleaned_tiles:
            self.cleaned_tiles.append(point)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        Assumes that (m, n) represents a valid tile inside the room.
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # raise NotImplementedError
        self.m = m
        self.n = n
        tile = (self.m, self.n)
        if tile in self.cleaned_tiles:
            return True
        else:
            return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        returns: an integer
        """
        # raise NotImplementedError
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        returns: an integer
        """
        # raise NotImplementedError
        return len(self.cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        """
        # raise NotImplementedError
        randx = random.uniform(0, self.width)
        randy = random.uniform(0, self.height)
        return Position(randx, randy)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # raise NotImplementedError
        if pos.x >= 0 and pos.x < self.width and pos.y >= 0 and pos.y < self.height:
            return True
        else:
            return False


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.
    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.
    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # raise NotImplementedError
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 359)

    def getRobotPosition(self):
        """
        Return the position of the robot.
        returns: a Position object giving the robot's position.
        """
        # raise NotImplementedError
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.
        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # raise NotImplementedError
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
        position: a Position object.
        """
        # raise NotImplementedError
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.
        direction: integer representing an angle in degrees
        """
        # raise NotImplementedError
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!


## Correct



########################################################################################
## PROBLEM 3 ##


# Each robot must also have some code that tells it how to move about a room, which will go in a method called updatePositionAndClean.
#
# Ordinarily we would consider putting all the robot's methods in a single class. However, later in this problem set we'll consider robots with alternate movement strategies, to be implemented as different classes with the same interface. These classes will have a different implementation of updatePositionAndClean but are for the most part the same as the original robots. Therefore, we'd like to use inheritance to reduce the amount of duplicated code.
#
# We have already refactored the robot code for you into two classes: the Robot class you completed in Problem 2 (which contains general robot code), and a StandardRobot class that inherits from it (which contains its own movement strategy).
#
# Complete the updatePositionAndClean method of StandardRobot to simulate the motion of the robot after a single time-step (as described on the Simulation Overview page).
#
# class StandardRobot(Robot):
#     """
#     A StandardRobot is a Robot with the standard movement strategy.
#
#     At each time-step, a StandardRobot attempts to move in its current direction; when
#     it hits a wall, it chooses a new direction randomly.
#     """
#     def updatePositionAndClean(self):
#         """
#         Simulate the passage of a single time-step.
#
#         Move the robot to a new position and mark the tile it is on as having
#         been cleaned.
#         """
# We have provided the getNewPosition method of Position, which you may find helpful:
#
# class Position(object):
#
#     def getNewPosition(self, angle, speed):
#         """
#         Computes and returns the new Position after a single clock-tick has
#         passed, with this object as the current position, and with the
#         specified angle and speed.
#
#         Does NOT test whether the returned position fits inside the room.
#
#         angle: number representing angle in degrees, 0 <= angle < 360
#         speed: positive float representing speed
#
#         Returns: a Position object representing the new position.
#         """
# Note: You can pass in an integer or a float for the angle parameter.
#
# Before moving on to Problem 4, check that your implementation of StandardRobot works by uncommenting the following line under your implementation of StandardRobot. Make sure that as your robot moves around the room, the tiles it traverses switch colors from gray to white. It should take about a minute for it to clean all the tiles.
#
# testRobotMovement(StandardRobot, RectangularRoom)
#
# Enter your code for classes Robot (from the previous problem) and StandardRobot below.


class Robot(object):
    """
    Represents a robot cleaning a particular room.
    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.
    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # raise NotImplementedError
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 359)
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.
        returns: a Position object giving the robot's position.
        """
        # raise NotImplementedError
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.
        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # raise NotImplementedError
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
        position: a Position object.
        """
        # raise NotImplementedError
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.
        direction: integer representing an angle in degrees
        """
        # raise NotImplementedError
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.
    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # raise NotImplementedError
        next_position = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.speed)
        if self.room.isPositionInRoom(next_position) == False:
            self.setRobotDirection(random.randint(0, 359))
        else:
            self.setRobotPosition(next_position)
            self.room.cleanTileAtPosition(next_position)


## Correct




########################################################################################
## PROBLEM 4 ##


# In this problem you will write code that runs a complete robot simulation.
#
# Recall that in each trial, the objective is to determine how many time-steps are on average needed before a specified fraction of the room has been cleaned. Implement the following function:
#
# def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
#                   robot_type):
#     """
#     Runs NUM_TRIALS trials of the simulation and returns the mean number of
#     time-steps needed to clean the fraction MIN_COVERAGE of the room.
#
#     The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
#     speed SPEED, in a room of dimensions WIDTH x HEIGHT.
#     """
# The first six parameters should be self-explanatory. For the time being, you should pass in StandardRobot for the robot_type parameter, like so:
#
# avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot)
# Then, in runSimulation you should use robot_type(...) instead of StandardRobot(...) whenever you wish to instantiate a robot. (This will allow us to easily adapt the simulation to run with different robot implementations, which you'll encounter in Problem 6.)
#
# Feel free to write whatever helper functions you wish.
#
# We have provided the getNewPosition method of Position, which you may find helpful:
#
# class Position(object):
#
#     def getNewPosition(self, angle, speed):
#         """
#         Computes and returns the new Position after a single clock-tick has
#         passed, with this object as the current position, and with the
#         specified angle and speed.
#
#         Does NOT test whether the returned position fits inside the room.
#
#         angle: integer representing angle in degrees, 0 <= angle < 360
#         speed: positive float representing speed
#
#         Returns: a Position object representing the new position.
#         """
# For your reference, here are some approximate room cleaning times. These times are with a robot speed of 1.0.
#
# One robot takes around 150 clock ticks to completely clean a 5x5 room.
#
# One robot takes around 190 clock ticks to clean 75% of a 10x10 room.
#
# One robot takes around 310 clock ticks to clean 90% of a 10x10 room.
#
# One robot takes around 3322 clock ticks to completely clean a 20x20 room.
#
# Three robots take around 1105 clock ticks to completely clean a 20x20 room.
#
# (These are only intended as guidelines. Depending on the exact details of your implementation, you may get times slightly different from ours.)
#
# You should also check your simulation's output for speeds other than 1.0. One way to do this is to take the above test cases, change the speeds, and make sure the results are sensible.
#
# For further testing, see the next page in this problem set about the optional way to use visualization methods. Visualization will help you see what's going on in the simulation and may assist you in debugging your code.
#
# Enter your code for the definition of runSimulation below.


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.
    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.
    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    #raise NotImplementedError
    # do this in a while loop, but has to be in for loop of num_trials:
    # and instantiate a container to store the results
    results = []
    for i in range(num_trials):
        #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        num_steps = 0
        # Instantiate a new room
        room = RectangularRoom(width, height)
        # Instantiate the robots
        robots = [robot_type(room, speed) for j in range(num_robots)]
        while (room.getNumCleanedTiles()/room.getNumTiles()) < min_coverage:
            num_steps += 1
            #anim.update(room, robots)
            for k in robots:
                k.updatePositionAndClean()
            if (room.getNumCleanedTiles()/room.getNumTiles()) >= min_coverage:
                results.append(num_steps)
                #anim.done()
            else:
                continue
    # return mean
    return sum(results)/len(results)


## Correct



########################################################################################
## PROBLEM 5 ##


# iRobot is testing out a new robot design. The proposed new robots differ in that they change direction randomly after every time step, rather than just when they run into walls. You have been asked to design a simulation to determine what effect, if any, this change has on room cleaning times.
#
# Write a new class RandomWalkRobot that inherits from Robot (like StandardRobot) but implements the new movement strategy. RandomWalkRobot should have the same interface as StandardRobot.
#
# Test out your new class. Perform a single trial with the StandardRobot implementation and watch the visualization to make sure it is doing the right thing. Once you are satisfied, you can call runSimulation again, passing RandomWalkRobot instead of StandardRobot.
#
# Enter your code for classes Robot and RandomWalkRobot below.


class Robot(object):
    """
    Represents a robot cleaning a particular room.
    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.
    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # raise NotImplementedError
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 359)
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.
        returns: a Position object giving the robot's position.
        """
        # raise NotImplementedError
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.
        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # raise NotImplementedError
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
        position: a Position object.
        """
        # raise NotImplementedError
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.
        direction: integer representing an angle in degrees
        """
        # raise NotImplementedError
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!


class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # raise NotImplementedError
        next_position = self.getRobotPosition().getNewPosition(random.randint(0, 359), self.speed)
        if self.room.isPositionInRoom(next_position) == False:
            self.setRobotDirection(random.randint(0, 359))
        else:
            self.setRobotPosition(next_position)
            self.setRobotDirection(random.randint(0, 359))
            self.room.cleanTileAtPosition(next_position)

## Correct


