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