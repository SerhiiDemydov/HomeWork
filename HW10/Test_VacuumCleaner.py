import unittest
from VacuumCleaner import VacuumCleanerRobot



class TestRobot(unittest.TestCase):

    def setUp(self) -> None:
        self.robot1 = VacuumCleanerRobot(100, 0, 100)
        self.robot2 = VacuumCleanerRobot(120, 60, 80)
        self.robot3 = VacuumCleanerRobot(100, -200, 21)
        self.robot4 = VacuumCleanerRobot("0", -200, 21)
        self.robot5 = VacuumCleanerRobot("40", -20, 21.5)
        with self.assertRaises(ValueError):
            self.robot6 = VacuumCleanerRobot("gsa", -200, 21)
        with self.assertRaises(NameError):
            self.robot7 = VacuumCleanerRobot(sdfa, -200, 21)
        with self.assertRaises(TypeError):
            self.robot8 = VacuumCleanerRobot(None, -200, 21)
        # with self.assertRaises(SyntaxError):
        #     self.robot9 = VacuumCleanerRobot( , -200, 21)
        self.robots = [self.robot1, self.robot2, self.robot3, self.robot4, self.robot5]

    def test_init(self):

        for robot in self.robots:
            self.assertIsInstance(robot.currently_battery, (float, int))
            self.assertIsInstance(robot.currently_fullness, (float, int))
            self.assertIsInstance(robot.currently_water, (float, int))

    def test_move1(self):
        i = 0
        for robot in self.robots:
            i += 1
            print(f'\n -----------------Test {i}-----------------\n')
            robot.move(6)

    def test_move2(self):
        robot_cleaner = VacuumCleanerRobot(100, 100, 0)
        print(f'\n -----------------Test 1 (self.robot1.move(3))-----------------\n')
        robot_cleaner.move(3)
        robot_cleaner = VacuumCleanerRobot(100, 100, 0)
        print(f'\n -----------------Test 2 (self.robot2.move("4"))-----------------\n')
        robot_cleaner.move("4")
        robot_cleaner = VacuumCleanerRobot(100, 100, 0)
        print(f'\n -----------------Test 3 (self.robot3.move(-7))-----------------\n')
        robot_cleaner.move(-7)
        robot_cleaner = VacuumCleanerRobot(100, 100, 0)
        print(f'\n -----------------Test 4 (self.robot3.move(4.5))-----------------\n')
        robot_cleaner.move(4.5)

        with self.assertRaises(TypeError):
            robot_cleaner.move()

        with self.assertRaises(NameError):
            robot_cleaner.move(asdfsa)
            
        with self.assertRaises(ValueError):
            robot_cleaner.move("sdafa")





