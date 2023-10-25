import unittest
from turnTracker import TurnTracker

class TestTurnTracker(unittest.TestCase):
    def setUp(self):
        """Sets up a TurnTracker object to be used in further tests"""
        self.tt = TurnTracker()
        self.tt1 = TurnTracker()
        self.tt2 = TurnTracker()
        self.tt3 = TurnTracker()
        self.tt4 = TurnTracker()

    def test_add_player_and_num_players(self):
        """Tests the addPlayer and numberOfPlayers methods"""

        # Test addPlayer and numberOfPlayers on 1 player
        self.tt.addPlayer("Jake")
        self.assertEqual(self.tt.numberOfPlayers(), 1)
        self.assertEqual(self.tt._head.item, "Jake")
        
        # Test addPlayer and numberOfPlayers on 2 players
        self.tt.addPlayer("Lina")
        self.assertEqual(self.tt.numberOfPlayers(), 2)
        self.assertEqual(self.tt._tail.item, "Lina")
        
        # Test addPlayer and numberOfPlayers on 3 players
        self.tt.addPlayer("Tim") 
        self.assertEqual(self.tt.numberOfPlayers(), 3)
        self.assertEqual(self.tt._tail.item, "Tim")

        print("Add Player and Number of Player Tests Complete.")

    def test_next_player(self):
        """Tests the nextPlayer method"""
        self.tt1.addPlayer("Jake")
        self.tt1.addPlayer("Lina")
        self.tt1.addPlayer("Tim")

        # Test nextPlayer
        self.assertEqual(self.tt1.nextPlayer(), "Jake")
        self.assertEqual(self.tt1.nextPlayer(), "Lina")
        self.assertEqual(self.tt1.nextPlayer(), "Tim")
        self.assertEqual(self.tt1.nextPlayer(), "Jake")
        self.assertNotEqual(self.tt1.nextPlayer(), "Tim")

        print("Next Player Tests Complete.")

    def test_skip_next_player(self):
        """Tests the skipPlayer method"""
        self.tt2.addPlayer("Jake")
        self.tt2.addPlayer("Lina")
        self.tt2.addPlayer("Tim")
        
        self.assertEqual(self.tt2.nextPlayer(), "Jake")
        self.assertEqual(self.tt2.nextPlayer(), "Lina")
        self.assertEqual(self.tt2.nextPlayer(), "Tim")

        self.tt2.skipNextPlayer()    # Tim plays Skip card
        self.assertEqual(self.tt2.nextPlayer(), "Lina")

        self.tt2.skipNextPlayer()    # Lina plays Skip card
        self.assertEqual(self.tt2.nextPlayer(), "Jake")
        
        self.assertEqual(self.tt2.nextPlayer(), "Lina")

        print("Skip Next Player Tests Complete.")

    def test_reverse_turn_order(self):
        """Tests the reverseTurnOrder method"""
        self.tt3.addPlayer("Jake")
        self.tt3.addPlayer("Lina")
        self.tt3.addPlayer("Tim")

        self.assertEqual(self.tt3.nextPlayer(), "Jake")
        self.assertEqual(self.tt3.nextPlayer(), "Lina")
        self.tt3.reverseTurnOrder()     # Lina reverses turn order
        self.assertEqual(self.tt3.nextPlayer(), "Jake")
        self.assertEqual(self.tt3.nextPlayer(), "Tim")
        self.assertEqual(self.tt3.nextPlayer(), "Lina")

        print("Reverse Turn Order Tests Complete.")

    def test_reverse_skip(self):
        """Tests a combination of the reverse and skip player methods"""
        self.tt4.addPlayer("Jake")
        self.tt4.addPlayer("Lina")
        self.tt4.addPlayer("Tim")
        
        self.assertEqual(self.tt4.nextPlayer(), "Jake")
        self.assertEqual(self.tt4.nextPlayer(), "Lina")
        self.assertEqual(self.tt4.nextPlayer(), "Tim")

        self.tt4.skipNextPlayer()    # Tim plays Skip card 

        self.assertEqual(self.tt4.nextPlayer(), "Lina")
        self.tt4.reverseTurnOrder()  # Lina plays Reverse card

        self.assertEqual(self.tt4.nextPlayer(), "Jake")
        self.tt4.skipNextPlayer()    # Jake plays Skip card

        self.assertEqual(self.tt4.nextPlayer(), "Lina")
        self.assertEqual(self.tt4.nextPlayer(), "Jake")
        
        print("Reverse Turn Order and Skip Player Tests Complete.")

unittest.main()
