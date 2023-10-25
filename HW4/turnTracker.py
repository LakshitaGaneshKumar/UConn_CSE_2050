class TurnTrackerNode:
# Hint: This class should look just like the LinkNode class (the doubly linked list version)
    def __init__(self, item, prev=None, link=None):
        self.item = item
        self.prev = prev
        self.link = link

class TurnTracker:
# Hint: This class shares a lot of functionality/logic with the DoublyLinkedList class from the textbook.
# A good place to start is by looking at that DoublyLinkedList class and examining which methods are going
# to be similar to those needed by the TurnTracker. Then start adjusting those methods to suit your needs here.
    def __init__(self):
        """Initializes a TurnTracker object"""
        self._head = None
        self._tail = None
        self._len = 0
        self._nextPlayer = None
        self._reversed = False
        self._skipping = False

    def addPlayer(self, player):
        """At the beginning of the game, each player is added to the turn tracker this method"""
        # Edge Case: this is the first player added
        if self._len == 0:
            new_node = TurnTrackerNode(player, self._tail, self._head)
            self._head = new_node
            self._tail = new_node
            self._nextPlayer = new_node

        # Else, add a new node to the DLL
        else:
            new_node = TurnTrackerNode(player, self._tail, self._head)
            self._head.prev = new_node
            self._tail.link = new_node
            self._tail = new_node

        # Increment length of the list by 1
        self._len += 1
        

    def nextPlayer(self):
        """Returns the player that should play the next card"""
        # Raise RuntimeError if there are no players
        if self._len == 0: 
            raise RuntimeError
        # Else, return the next player and update the next player
        else:
            # Checks if the turn order is reversed
            if self._reversed:
                # Checks if the next player is skipped
                if self._skipping:
                    nextPlayer = self._nextPlayer.prev
                    self._skipping = False
                else:
                    nextPlayer = self._nextPlayer
                self._nextPlayer = nextPlayer.prev

            else:
                # Checks if a player is being skipped
                if self._skipping:
                    nextPlayer = self._nextPlayer.link
                    self._skipping = False
                else:
                    nextPlayer = self._nextPlayer
                self._nextPlayer = nextPlayer.link
            
        return nextPlayer.item
        
    def numberOfPlayers(self):
        """Returns number of players in the time tracker"""
        return self._len

    def skipNextPlayer(self):
        """Skips the next player when a "Skip" card is played"""
        self._skipping = True

    def reverseTurnOrder(self):
        """Reverses the turn order when the "Reverse" card is played"""
        self._reversed = not self._reversed
        if self._reversed:
            self._nextPlayer = self._nextPlayer.prev.prev
        else:
            self._nextPlayer = self._nextPlayer.link.link