# Source code
The entire code, programmed following an OOP paradigm, is based on the class <code>Robot</code>, extended here by <code>AVG_polimi_lab</code> class, which implements, further than normal <code>Robot</code> functionalities, also a nipper function, through a <code>Nipper</code> class attribute object.

A simple demonstration can be run following the assembly instructions in the <code>docs</code> directory and running the <code>robot</code> module as a script: <br>
<code>$ python3 robot.py</code>


# Class Robot

This class contains all the function for the robot movement and the position to pick up the product. The operating principle consists in using two suitably separated sensors which serve to keep the robot as close to the line as possible. If one of the sensors detects the black color then it automatically corrects the trajectory by bending on the opposite side. 

##Costants
S





# Class Nipper
In this class you have all the function for controll the pull and the push of a product on your production line.
We decided to separate the <code>nipper</code> class from the <code>robot</code> class because in this way it is possible to use the properties separately in case you want to use the two parts of the robot in other projects.

The gripper uses two motors initialized within <code> __init__ </code>: the first is <code>motorMove</code> and it is used to move the carriage back and forth, the second, <code>motorRotate</code>, is necessary to raise the arm.

## Costants

Time costants:

- <code>ROTATION_TIME</code> rappresent the time to move the arm from the highest to the lowest position
- <code>PULL_FORWARD_TIME</code> is the time required to bring the carriege into contact with the production line
- <code>PULL_BACKWARD_TIME</code> is the time to bring the trolley to the starting position

Speed costants:

- <code>ROTATION_SPEED </code> is the rotation speed of the arm
- <code>PULL_SPEED</code> rappresent the carriege speed

There is also <code>POSITION_1</code> that we use in function <code>push</code> and it represents the time required to raise the arm more during the re-entry phase.

All this costants have been found with field tests and depend on how the arm is built, if you want to insert a sensor or change some components it is necessary to carry out the tests again.

## Functions

The function <code>pull</code> takes care of upload the product from the production line while the <code>push</code> function is used to unload the product. It possible to use the function <code>stop</code> for arrest both motors.
