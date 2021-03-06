import unittest
import gamemaker
from Interface.models import HuntUser, Landmark, Game
import team
from django.test import TestCase
from django.utils import timezone
from datetime import datetime, timedelta


class TestMakerAddLandmark(TestCase):
    def setUp(self):
        Landmark.objects.all().delete()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.maker1 = gamemaker.GameMaker()

    def test_add_one_landmark(self):
        self.maker1.add_landmark(["land","clue","question","answer"])
        self.assertEqual(self.maker1.display_landmarks(), "land\n", "Bad landmark")

    def test_add_landmark_same_name(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual("Landmark land already exists!",self.maker1.add_landmark(["land","clue","question","answer"]),
                         "Error: landmark with same name should not have been added to database")

    def test_add_two_landmarks(self):
        self.maker1.add_landmark(["land","clue","question","answer"])
        self.maker1.add_landmark(["land1","clue1","question1","answer1"])
        self.assertEqual(self.maker1.display_landmarks(), "land\nland1\n", "Bad landmarks")

class TestMakerEditLandmarks(TestCase):
    def setUp(self):
        Landmark.objects.all().delete()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.maker1 = gamemaker.GameMaker()

    def test_edit_one_landmark_name(self):
        self.maker1.add_landmark(["land","clue","question","answer"])
        self.assertEqual(self.maker1.edit_landmark(["land","newland","","","","",""]),
                         "Edit to land name successful", "Edit to one landmark name unsuccessful")

    def test_edit_one_landmark_clue(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(self.maker1.edit_landmark(["land", "", "newclue", "", "", "", ""]),
                         "Edit to land clue successful", "Edit to one landmark clue unsuccessful")

    def test_edit_one_landmark_question(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(self.maker1.edit_landmark(["land", "", "", "newquestion", "", "", ""]),
                         "Edit to land question successful", "Edit to one landmark question unsuccessful")

    def test_edit_one_landmark_answer(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(self.maker1.edit_landmark(["land", "", "", "", "newanswer", "", ""]),
                         "Edit to land answer successful", "Edit to one landmark answer unsuccessful")

    def test_edit_one_landmark_order_num(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(self.maker1.edit_landmark(["land", "", "", "", "", "0", ""]),
                         "Edit to land order successful", "Edit to one landmark order unsuccessful")

    def test_edit_one_landmark_penalty(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(self.maker1.edit_landmark(["land", "", "", "", "", "", "11"]),
                         "Edit to land points successful", "Edit to one landmark points unsuccessful")

    def test_edit_one_landmark_all(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(self.maker1.edit_landmark(["land", "newland", "newclue", "newquestion", "newanswer", "0", "11"]),
                         "Edit to land name clue question answer order points successful",
                         "Edit to one landmark name unsuccessful")

    def test_edit_one_landmark_none(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(self.maker1.edit_landmark(["land", "", "", "", "", "", ""]),
            "Edit to land unsuccessful", "No change unsuccessful")

    def test_edit_one_landmark_not_an_int_order_only(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(
            self.maker1.edit_landmark(["land", "", "", "", "", "a", ""]),
            "Edit to land unsuccessful order number must be an integer!", "Edit to one landmark name unsuccessful")

    def test_edit_one_landmark_not_an_int_points_only(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(
            self.maker1.edit_landmark(["land", "", "", "", "", "", "a"]),
            "Edit to land unsuccessful points must be an integer!", "Edit to one landmark ints points unsuccessful")

    def test_edit_one_landmark_not_an_int_points_order_only(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(
            self.maker1.edit_landmark(["land", "", "", "", "", "a", "a"]),
            "Edit to land unsuccessful order number must be an integer! points must be an integer!",
            "Edit to one landmark int points and order unsuccessful")

    def test_edit_one_landmark_not_an_int_points_other(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(
            self.maker1.edit_landmark(["land", "newland", "", "", "", "a", ""]),
            "Edit to land name successful points must be an integer!",
            "Edit to one landmark int points and other unsuccessful")

    def test_edit_one_landmark_not_an_int_points_other(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(
            self.maker1.edit_landmark(["land", "newland", "", "", "", "", "a"]),
            "Edit to land name successful order must be an integer!",
            "Edit to one landmark int order and other unsuccessful")

    def test_edit_one_landmark_not_an_int_points_other(self):
        self.maker1.add_landmark(["land", "clue", "question", "answer"])
        self.assertEqual(
            self.maker1.edit_landmark(["land", "newland", "", "", "", "a", "a"]),
            "Edit to land name successful order number must be an integer! points must be an integer!",
            "Edit to one landmark int order, points and other unsuccessful")


class TestMakerDisplayLandmarks(TestCase):
    def setUp(self):
        Landmark.objects.all().delete()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.maker1 = gamemaker.GameMaker()

    def test_display_one_landmark(self):
        self.maker1.add_landmark(["land","clue","question","answer"])
        self.assertEqual(self.maker1.display_landmarks(), "land\n", "Bad display")

    def test_display_two_landmarks(self):
        self.maker1.add_landmark(["land","clue","question","answer"])
        self.maker1.add_landmark(["land1","clue1","question1","answer1"])
        self.assertEqual(self.maker1.display_landmarks(), "land\nland1\n", "Bad displays")

class TestMakerRemoveLandmarks(TestCase):
    def setUp(self):
        Landmark.objects.all().delete()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.maker1 = gamemaker.GameMaker()

    def test_remove_one_landmark(self):
        self.maker1.add_landmark(["land","clue","question","answer"])
        self.maker1.remove_landmark(["land"])
        self.assertEqual(self.maker1.display_landmarks(), "There are no landmarks", "Did not remove landmark")

    def test_remove_multiple_landmarks_to_none(self):
        self.maker1.add_landmark(["land","clue","question","answer"])
        self.maker1.add_landmark(["land1","clue1","question1","answer1"])
        self.maker1.remove_landmark(["land"])
        self.maker1.remove_landmark(["land1"])
        self.assertEqual(self.maker1.display_landmarks(), "There are no landmarks", "Did not remove landmarks")

    def test_remove_multiple_landmarks_to_one(self):
        self.maker1.add_landmark(["land","clue","question","answer"])
        self.maker1.add_landmark(["land1","clue1","question1","answer1"])
        self.maker1.remove_landmark(["land"])
        self.assertEqual(self.maker1.display_landmarks(), "land1\n", "Did not remove landmarks")


class TestMakerCheckStatus(TestCase):
    def setUp(self):
        HuntUser.objects.all().delete()
        Landmark.objects.all().delete()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        Game.objects.all().delete()
        self.game = Game(name="game",running=False,time_start=timezone.now())
        self.game.save()
        self.game_maker = gamemaker.GameMaker()

    def test_status_single_team(self):
        self.game_maker.make_team(["team1", "password1"])
        self.assertEquals(self.game_maker.display_status(),
                          "Team: team1\nScore: 0\nPenalties: 0\n\nThere is currently no game running",
                          "Bad single team return")

    def test_status_multiple_teams(self):
        self.game_maker.make_team(["team1", "password1"])
        self.game_maker.make_team(["team2", "password2"])
        self.assertEqual(self.game_maker.display_status(),
                         "Team: team1\nScore: 0\nPenalties: 0\n\nTeam: team2\nScore: 0\nPenalties: 0\n\n"
                         "There is currently no game running",
                         "Cannot find entries in two team list")


class TestMakerDisplayMenu(TestCase):
    def setUp(self):
        self.game_maker = gamemaker.GameMaker()

    def test_display_menu(self):
        self.assertEqual(self.game_maker.display_menu(),
                         "Options\n\ndisplaystatus\nmaketeam [team name], [team password]\n"
                         "editteam [team name to edit], [new team name], [new team password]\n"
                         "addlandmark [name], [clue], [question], [answer]\n"
                         "editlandmarks [name], [clue], [question], [answer], [order number], [points]\n"
                         "displaylandmarks\nremovelandmark [name]\n"
                         "setpenaltyscores [time points], [guess points]\n"
                         "setpenalties [new time penalty], [new guess penalty]\n"
                         "creategame [landmark name]...\nstartgame\nendgame\nlogout\n", "Wrong menu")


class TestMakerCreateTeam(TestCase):
    def setUp(self):
        HuntUser.objects.all().delete()
        Landmark.objects.all().delete()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        Game.objects.all().delete()
        self.game = Game(name="game",running=False,time_start=timezone.now())
        self.game.save()
        self.game_maker = gamemaker.GameMaker()

    def test_make_single_team(self):
        self.game_maker.make_team(["team1", "password"])
        self.assertEquals(self.game_maker.display_status(),
                          "Team: team1\nScore: 0\nPenalties: 0\n\nThere is currently no game running",
                          "Bad single team return")

    def test_make_team_same_name(self):
        self.game_maker.make_team(["team1", "password"])
        self.assertEqual("Team team1 already exists!",self.game_maker.make_team(["team1", "password"]),
                         "Error: team1 was added into the database twice")

    def test_make_multiple_teams(self):
        self.game_maker.make_team(["team1", "password"])
        self.game_maker.make_team(["team2", "password"])
        self.assertEqual(self.game_maker.display_status(),
                         "Team: team1\nScore: 0\nPenalties: 0\n\nTeam: team2\nScore: 0\nPenalties: 0\n\n"
                         "There is currently no game running",
                         "Cannot find entries in two team list")


class TestMakerEditTeams(TestCase):
    def setUp(self):
        HuntUser.objects.all().delete()
        Landmark.objects.all().delete()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.game_maker = gamemaker.GameMaker()

    def test_edit_single_team(self):
        self.game_maker.make_team(["team1", "password"])
        self.assertEquals(self.game_maker.edit_team(["team1", "team2", "passnew"]),
                          "Edited team1 to have username team2 and password passnew", "Bad single team edit")

    def test_edit_multiple_teams(self):
        self.game_maker.make_team(["team1", "password"])
        self.game_maker.make_team(["team2", "password"])
        self.assertEquals(self.game_maker.edit_team(["team1", "team", "passnew"]),
                          "Edited team1 to have username team and password passnew",
                          "Bad single team edit")
        self.assertEquals(self.game_maker.edit_team(["team2", "team3", "passnew"]),
                          "Edited team2 to have username team3 and password passnew",
                          "Bad single team edit")


class TestMakerDeleteTeam(TestCase):
    def setUp(self):
        HuntUser.objects.all().delete()
        Landmark.objects.all().delete()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.game_maker = gamemaker.GameMaker()

    def test_delete_single_team(self):
        self.game_maker.make_team(["Team1", "password"])
        self.assertEquals(self.game_maker.delete_team(["Team1"]), "Removed Team1 from teams.", "Bad single team delete")

    def test_delete_multiple_teams(self):
        self.game_maker.make_team(["Team1", "password"])
        self.game_maker.make_team(["team2", "password"])
        self.assertEquals(self.game_maker.delete_team(["Team1"]), "Removed Team1 from teams.", "Bad two team delete")
        self.assertEquals(self.game_maker.delete_team(["team2"]), "Removed team2 from teams.", "Bad 2nd two team delete")


class TestMakerCreateGame(TestCase):
    def setUp(self):
        HuntUser.objects.all().delete()
        Landmark.objects.all().delete()
        Game.objects.all().delete()
        self.game = Game(name="game",running=False,time_start=timezone.now())
        self.game.save()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.maker = gamemaker.GameMaker()
        self.maker.make_team(["team1","password1"])
        self.t = team.Team()
        lm1 = Landmark(name="landmark1", clue="clue1", question="question1", answer="answer1", order_num=-1)
        lm2 = Landmark(name="landmark2", clue="clue2", question="question2", answer="answer2", order_num=-1)
        lm1.save()
        lm2.save()

    def test_create_game_no_landmarks(self):
        self.assertEqual("Need at least one landmark to create a game",self.maker.create_game([]),
                         "Error: can't create a game without any landmarks")

    def test_create_game_one_landmark(self):
        self.assertEqual("Game has been created!",self.maker.create_game(["landmark1"]),
                         "Error: game with one landmark should have been created")
        cur = HuntUser.objects.get(name="team1").current_landmark
        lm1 = Landmark.objects.get(name="landmark1")
        self.assertEqual(0,lm1.order_num,
                         "Error: landmark1 order_num should be 0, instead is " + str(lm1.order_num))

    def test_create_game_invalid_landmark(self):
        self.assertEqual("Landmark inv is not a valid landmark!",self.maker.create_game(["inv"]),
                         "Error: adding a landmark that doesn't exist shouldn't be valid")

    def test_create_game_started(self):
        self.maker.create_game(["landmark1"])
        self.game.running = True
        self.game.save()
        self.assertEqual("Game is already in progress!",self.maker.create_game(["landmark1"]),
                         "Error: game shouldn't have been created while a game is currently running")

    def test_create_game_multiple_landmarks(self):
        self.assertEqual("Game has been created!",self.maker.create_game(["landmark1","landmark2"]),
                         "Error: game with two landmarks should have been created")
        cur = HuntUser.objects.get(name="team1").current_landmark
        lm1 = Landmark.objects.get(name="landmark1")
        lm2 = Landmark.objects.get(name="landmark2")
        self.assertEqual(0,lm1.order_num,
                         "Error: landmark1 order_num should be 0, instead is " + str(lm1.order_num))
        self.assertEqual(1,lm2.order_num,
                         "Error: landmark2 order_num should be 1, instead is " + str(lm2.order_num))


class TestMakerStartAndEndGame(TestCase):
    def setUp(self):
        HuntUser.objects.all().delete()
        Landmark.objects.all().delete()
        Game.objects.all().delete()
        game = Game(name="game",running=False)
        game.save()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.maker = gamemaker.GameMaker()
        self.maker.make_team(["team1","password1"])
        self.t = team.Team()
        lm1 = Landmark(name="landmark1", clue="clue1", question="question1", answer="answer1", order_num=-1)
        lm2 = Landmark(name="landmark2", clue="clue2", question="question2", answer="answer2", order_num=-1)
        lm1.save()
        lm2.save()

    def test_start_game_no_landmarks(self):
        self.assertEqual("No landmarks are part of the game!",self.maker.start_game(),
                         "Error: game can't start if the game wasn't created")
        self.assertFalse(Game.objects.get(name="game").running)

    def test_start_game(self):
        self.maker.create_game(["landmark1"])
        self.assertEqual("Game started!",self.maker.start_game(),
                         "Error: game should have been started")
        self.assertTrue(Game.objects.get(name="game").running)
        cur = HuntUser.objects.get(name="team1").current_landmark
        lm1 = Landmark.objects.get(name="landmark1")
        self.assertEqual(lm1,cur,
                         "Error: team1 current landmark should have updated to landmark1, instead is " + cur.name)

    def test_start_game_already_started(self):
        self.maker.create_game(["landmark1"])
        self.maker.start_game()
        self.assertEqual("Game already started!",self.maker.start_game(),
                         "Error: game cannot be started twice")

    def test_end_game_not_started(self):
        self.maker.create_game(["landmark1"])
        self.assertEqual("There is no game running!",self.maker.end_game(),
                         "Error: a game that hasn't started can't end")

    def test_end_game_started(self):
        self.maker.create_game(["landmark1"])
        self.maker.start_game()
        self.assertEqual("Game over",self.maker.end_game(),
                         "Error: game should have ended when end_game() was called")
        self.assertFalse(Game.objects.get(name="game").running)


class TestPenaltySystem(TestCase):
    def setUp(self):
        HuntUser.objects.all().delete()
        Landmark.objects.all().delete()
        Game.objects.all().delete()
        game = Game(name="game",running=False)
        game.save()
        lm = Landmark(name="dummy", clue="dummy", question="dummy", answer="dummy", order_num=-1)
        lm.save()
        self.maker = gamemaker.GameMaker()

    def test_set_penalty_points(self):
        self.assertEqual("Set time penalty to 2 and guess penalty to 3", self.maker.set_penalty_scores(["2","3"]),
                         "Error: penalties not set correctly")
        game = Game.objects.get(name="game")
        self.assertEqual(2, game.time_penalty, "Error: time penalty not set correctly")
        self.assertEqual(3, game.guess_penalty, "Error: guess_penalty not set correctly")

    def test_set_penalty_values(self):
        self.assertEqual("Time penalty is 2 minutes and guess penalty is 3 guesses", self.maker.set_penalties(["2","3"]),
                         "Error: penalties not set correctly")
        game = Game.objects.get(name="game")
        self.assertEqual(2, game.guess_period, "Error: time penalty not set correctly")
        self.assertEqual(3, game.num_guesses, "Error: guess_penalty not set correctly")


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestMakerAddLandmark))
suite.addTest(unittest.makeSuite(TestMakerEditLandmarks))
suite.addTest(unittest.makeSuite(TestMakerDisplayLandmarks))
suite.addTest(unittest.makeSuite(TestMakerRemoveLandmarks))
suite.addTest(unittest.makeSuite(TestMakerCheckStatus))
suite.addTest(unittest.makeSuite(TestMakerDisplayMenu))
suite.addTest(unittest.makeSuite(TestMakerCreateTeam))
suite.addTest(unittest.makeSuite(TestMakerEditTeams))
suite.addTest(unittest.makeSuite(TestPenaltySystem))
suite.addTest(unittest.makeSuite(TestMakerDeleteTeam))
suite.addTest(unittest.makeSuite(TestMakerCreateGame))
suite.addTest(unittest.makeSuite(TestMakerStartAndEndGame))


runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])
