# python-oop
python object oriented programming practice

## src files :
---
## 01 Coder Class
---
a Coder Class, this class have the following properties:
-   `name`
-   `location`
-   `course`
-   `graduation_date`

it also have the following methods:

-   `greet`

```py
alex.greet('Joe') # Should return 'Hello Joe, my name is Alex'
```

-   `alumni`

```py
alex.alumni() # Should return True as Alex's graduation date has passed.
```

---

## 02 High Scores Container Class
---
high scores board

-   takes one argument to control a `limit` property.

-   holds a `scores` property that returns a list. All scores in the list returned in descending order.

```py
high_scores = HighScoreTable(3)
high_scores.scores == [] # Should return True
high_scores.limit # Should return 3
```
-   it has an `update` method to update the scores list with a **dictionary** containing the name of the player and their score.
-   The `update` method does not allow more scores to be added if the `limit` has been reached. If the `limit` has been reached, and the score passed to the `update` method is larger than any of the stored scores, the new high scores are stored.


```py
high_scores.update({'player':'Cat', 'score':95})
high_scores.update({'player':'Verity', 'score':150})
high_scores.scores # Should return [{'player':'Verity', 'score':150},{'player':'Cat', 'score':95}] as the scores are in descending order
```
-  also it has  `average_score`, `highest_scorer` and `lowest_scorer` methods 
- `reset` methods to remove all high scores

```py
high_scores.scores # Would return [{'player':'Verity', 'score':150},{'player':'Cat', 'score':95}]
high_scores.reset()
high_scores.scores # After reset method should return []
```

---

## 03 Chost Class
---
a base class of a Ghost that can be extended to create the Ghost Gang.

-   a class of Ghost has the following properties :`name`, `speed` and `colour`

```py
ghost = Ghost('Ducky', 3, 'yellow')
ghost.name # Would return 'Ducky'
ghost.colour # Would return 'yellow'
```

-   Each Ghost has `is_scared` property which has default value to False. 

```py
ghost.is_scared # Would return False
```
-   it has a `can_be_eaten` method which returns True if Ghost `is_sacred` is `True` , or `False` otherwise.

```py
mack = Ghost('Mack', 9, 'grey')
mack.colour # Should return 'grey'
mack.is_scared # Should return False
mack.can_be_eaten() # Should return False
```

-  If the Ghosts are scared, their `colour` will change to blue. If a Ghost is blue, they can also be eaten. The Ghost class has a `frighten` method to create this change.

```py
mack.is_scared # Should return False
mack.can_be_eaten() # Should return False

mack.frighten()
mack.is_scared # Should return True
mack.can_be_eaten() # Should return True
mack.colour # Should return 'blue'
```

-   As Pac Man's lives reduce, each ghost's `speed` is increased by 10%. The Ghost Class has a `speed_up` method that updates the ghost's speed with each invocation.

```py
jersey = Ghost('Jersey', 3, 'white')
jersey.speed_up()
jersey.speed # Should return 3.3
jersey.speed_up()
jersey.speed # Should return 3.63
jersey.speed_up()
jersey.speed # Should return 3.993
```
### - It has the follwing extended subclasses
-   Blinky is red and has a speed of 3,
-   Pinky is pink and has a speed of 2,
-   Inky is cyan and has a speed of 4,
-   Clyde is yellow and has a speed of 1.

```py
blinky = Blinky('Blinky', 3,'red')
blinky.colour # Should return 'red'

blinky.frighten()
blinky.colour # Should return 'blue'
blinky.is_scared # Should return True
blinky.can_be_eaten # Should return True
```

All of your class extensions still have access to the original methods in the Ghost Class and show the expected behaviour. Extensions are tested thoroughly.

---
## 4. 🏴‍☠️ Piracy 🏴‍☠️
### Captain Calss

Each Captain class has the following properties:

- `name`
- `nickname`
- `crew_size`
- `catchphrase`

```py
david = Captain('David', 'General Bartlett', 10, 'I will not say arr')
david.name # Would return 'David'
david.nickname # Would return 'General Bartlett'
david.crew_size # Would return 10
david.catchphrase # Would return 'I will not say arr'
```
### Ship Calss

Each Ship class has the following attributes:

-   `draft` - an estimate of the ship's weight based on how low it is in the water.
-   `captain`- Should be an instance of a Captain class.

```py
hms_boaty = Ship(20, david)
hms_boaty.draft # Should return 20
hms_boaty.crew # Should return the crew_size present on the Captain class
```
Also, each Ship class has the following method:

-   `worth_it` method. This method should remove the weight of the crew from the draft. If the draft is more than 20 the method should return True, else return False. Each shipmate adds 1.5 units to the ship draft.

```py
hms_boaty.worth_it() # Should return False
```

---

## 5. 📊 Vectors 📊
Create a Vector Class that takes a list of integers.

```py
list_one = Vector([1,2,3])
list_two = Vector([2,3,4])
```

Your class should have the following methods:

-   `add` Should return a **new Vector**

```py
list_one = Vector([1,2,3])
list_two = Vector([2,3,4])
list_one.add(list_two) # Should return Vector([3,5,7])
```

-   `subtract` Should return a **new Vector**

```py
list_one = Vector([1,2,3])
list_two = Vector([2,3,4])
list_one.subtract(list_two) # Should return Vector([-1,-1,-1])
```

-   `dot` https://en.wikipedia.org/wiki/Dot_product

```py
list_one = Vector([1,2,3])
list_two = Vector([2,3,4])
list_one.dot(list_two) # Should return (1*2 + 2*3 + 3*4) = 20
```

-   `is_equal` should check whether or not the two vector lengths are equal.

```py
list_one = Vector([1,2,3])
list_two = Vector([2,3,4])
list_one.is_equal(list_two) # Should return True

list_one = Vector([1,2,3,5])
list_two = Vector([2,3,4])
list_one.is_equal(list_two) # Should return False
```

If you try to `add`, `subtract` or `dot` two vectors with different lengths your Class should throw an exception.

---
## 6. 🏦 Banking App 🏦

You are building a mobile banking app for a new tech startup! The CTO of the company wants you to design a `User` class that will have various features enabling a user to interact with their new account.

The CTO's specification for the `User` class is detailed below.

It must have a `current_balance` property, which will be a **float** representing amount of pounds, starting at `0.00`:

```py
joes_account = User();
joes_account.current_balance # Should return 0.00
```

It must have a `pots` property, which will be an **empty dictionary** that will store pots for saving money for specific things.

```py
joes_account = User();
joes_account.pots # Should return {};
```

It must have a `deposit_money` method which will update the the `current_balance` in pounds:

```py
joes_account = User();
joes_account.deposit_money(10.56)
joes_account.current_balance # Should return 10.56
joes_account.deposit_money(2.3)
joes_account.current_balance # Should return 12.86
```

It must have a `create_new_pot` method which will add a new property to the `pots` property with a key for the type of the pot being created and an object containing the `pot_balance`:

```py
joes_account = User();
joes_account.pots # Should return {}

joes_account.createNewPot('holiday')
joes_account.pots['holiday'] # Should return {'pot_balance': 0}

joes_account.createNewPot('mortgage_deposit')
joes_account.pots['mortgage_deposit'] # Should return {pot_balance: 0}

joes_account.pots # Should return {'holiday' : {'pot_balance':0},'mortgage_deposit':{'pot_balance':0}}
```

It must have an `add_to_pot` method which will add money to the `pot_balance` of a given pot:

```py
joes_account = User();
joes_account.pots # Would return an empty dictionary

joes_account.create_new_pot('holiday');
joes_account.add_to_pot('holiday', 10);
joes_account.pots['holiday'] # Should return { pot_balance: 10 }

joes_account.add_to_pot('holiday', 30);
joes_account.pots['holiday'] # Should return { potBalance: 40 }

```

It must have a `transfer_to_pot` method which will transfer money from the `current_balance` to the `pot_balance`. If there is **insufficient money** in the `current_balance` then the function should have no effect on the current User.

```py
joes_account = new User();
joes_account.deposit_money(10.56)
joes_account.current_balance # Should return 10.56

joes_account.create_new_pot('holiday')
joes_account.add_to_pot('holiday', 10)
joes_account.transfer_to_pot('holiday', 5.03)

joes_account.currentBalance # Should return 5.53
joes_account.pots['holiday'] # Should return { potBalance: 15.03 }

joes_account.transfer_to_pot('holiday', 6.50) /* insufficient funds */
joes_account.currentBalance # Should return 5.53
joes_account.pots['holiday'] # Should return { potBalance: 15.03 }

```

---
## 7. 🛗 Lift me up 🛗

You are designing a lift for a swanky new apartment in Manchester. You decide to go for an object-oriented approach, with a `Lift` class that can generate lift instances with certain useful properties and methods to model the behaviour of the lift.

The site manager's specification for the `Lift` class is detailed below. Be **sure to write tests** for each aspect of behaviour you want from the class.

Your lift should have a `max_capacity` property, which will be a **number** representing the total weight (in kg) that the lift can hold, which will be passed to the `class` when it it invoked.

```py
testLift = Lift(100)
testLift.maxCapacity # Should return 100
```

Your lift should have a `passengers` property, which will **initially be an empty list**, holding each passenger in the lift.

```py
testLift = Lift(100)
testLift.passengers # Should return []
```

Your lift should have a `floors_count` property, which will be passed to the `class` when it it invoked.

```py
testLift = Lift(100, 3)
testLift.floorsCount # Should return 3
```

Your lift should have a `current_floor` property which will be intialised at `0`

```py
testLift = Lift(100, 3)
testLift.currentFloor # Should return 0
```

Create a Passenger class with the following properties `name`, `weight`

```py
bob = Passenger('Bob',12)
```

Your lift should have an `add_passenger` method can update the `passengers` property with a Passenger class. If the `max_weight` is exceeded, no more Passengers can be added to the lift.

```py
bob = Passenger('Bob',12)
testLift = Lift(100, 3)

testLift.passengers # Should return []
testLift.add_passenger(bob)
testLift.passengers # Should return [bob]
```

Your lift should have a `find_total_weight` method that can find the total weight of the passengers in the lift's passengers property

```py
testLift = Lift(100, 3)
bob = Passenger('Bob',12)
testLift.add_passenger(bob)
testLift.find_total_weight() # Should return 12
```

```py
testLift = Lift(100, 3)
alex = Passenger('Alex', 12)
cat = Passenger('Cat',9)
mitch = Passenger('Mitch',11)
testLift.add_passenger(Cat)
testLift.add_passenger(alex)
testLift.find_total_weight() # Should return 21
testLift.add_passenger(mitch)
testLift.find_total_weight() # Should return 32
```

Your lift should have a `remove_passenger` method that updates the `passengers` property and return value from `find_total_weight`

```py
testLift = Lift(100, 3)
alex = Passenger('Alex', 12)
cat = Passenger('Cat',9)

testLift.add_passenger(Cat)
testLift.add_passenger(alex)
testLift.find_total_weight() # Should return 21
testLift.remove_passenger(cat)
testLift.find_total_weight() # Should return 12
```

Your lift should have a `move` method that will either move the lift up or down a floor. However, the method should return a warning message if you try to go up from the top floor or if you try to go below the ground floor (floor `0`). See below:

```py
testLift = Lift(100, 3)
testLift.move('up')
testLift.current_floor # Should return 1
```

```py
testLift = Lift(100, 3)
testLift.move('up') # Now at floor 1
testLift.currentFloor # Should return 1
```

```py
testLift = Lift(100, 3)
testLift.move('up') # Now at floor 1
testLift.move('up') # Now at floor 2
testLift.move('up') # Now at floor 3
testLift.move('up') # Should return 'You are already on the top floor!'
```

```py
testLift = Lift(100, 3)
testLift.move('up') # Now at floor 1
testLift.move('up') # Now at floor 2
testLift.move('up') # Now at floor 3
testLift.move("down") # Now at floor 2
testLift.currentFloor # Should return 2
```

---
## 8. 🤖My new robot 🤖

Write a Robot class that will return robot instances.

It must have a `name` property, which will be a string representing the name of the robot.

```py
testRobot = Robot('R2D2')
testRobot.name # Should return 'R2D2'
```

It must have a `direction` property, which will be a string representing the current direction the robot instance is facing: it can be either 'N' for facing north, 'E' for East, 'S' for South and 'W' for west. The direction will be intialised at'N' - i.e. the robot starts facing north

```py
testRobot = Robot('R2D2')
testRobot.direction # Should return 'N' <-- initially the robot is facing North
```

It must have a `word_list` property, containing a unique list of all the words the Robot can understand. It will be initialised as an empty list in the beginning when the instance is first created

```py
testRobot = Robot('R2D2')
testRobot.wordList # Should return []
```

It must have a `position` property, which is an list of 2 numbers representing the position of the robot. The first number in the position list represents "how far to the right" the robot is. The second number in the position list represents "how far up the robot is"

```py
testRobot = Robot('R2D2')
testRobot.position # Should return [0, 0] <-- robot's initial starting position
```

It must have an `add_words` method - this function will add words on to the `word_list` property. This method can take any number of string arguments.

```py
testRobot = Robot('R2D2')
testRobot.add_words('ball', 'code', 'apple')
testRobot.word_list # Should return ['ball','code','apple']

testRobot.addWords('sky')
testRobot.wordList # Should return ['ball','code','apple','sky']
```

The `word_list` must contain unique words so if someone attempts to add the same word twice it won't get added to the wordList.

```py
testRobot = Robot('R2D2')
testRobot.add_words('apple', 'banana', 'kiwi')
testRobot.add_words('banana', 'kiwi')

testRobot.wordList # Should return ['apple','banana', 'kiwi'] <-- 'banana' only stored once
```

It must have a `move_horizontally` method and a `move_vertically` method which will update the first number in the position list and the second number in the position list, respectively.

Note: the robot's current position doesn't affect the `move_horizontally` and `move_vertically` functionality i.e. the robot can move up vertically even if it is facing south.

```py
testRobot = Robot('R2D2')
testRobot.position # Should return [0, 0]

testRobot.move_horizontally(10) // moves right 10 units
testRobot.position # Should return [10, 0]

testRobot.move_vertically(60) // moves up 60 units
testRobot.position # Should return [10, 60]
```

It must have a `rotate` method which takes a number indicating the number of 90 degree turns clockwise the robot should make so to end up facing a new direction. The effect of `rotate` should be up to update the `direction` property with the correct value of either 'N', 'E', 'S' or 'W'.

```py
testRobot = Robot('R2D2')
testRobot.direction // initially 'N' (facing north)

testRobot.rotate(1)
testRobot.direction # Should return 'E' now facing East

testRobot.rotate(2)
testRobot.direction # Should return 'w' now facing West (equivalent to moving 180 degrees clockwise starting at East)
```

---

