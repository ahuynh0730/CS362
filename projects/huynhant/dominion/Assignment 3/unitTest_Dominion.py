from unittest import TestCase
import Dominion



class TestAction_card(TestCase):
    def testInitialization(self):
        actionCard = Dominion.Action_card('Test Card', 3, 1, 0, 4, 5)
        self.assertEqual('Test Card', actionCard.name)
        self.assertEqual(3, actionCard.cost)
        self.assertEqual(1, actionCard.actions)
        self.assertEqual(0, actionCard.cards)
        self.assertEqual(4, actionCard.buys)
        self.assertEqual(5, actionCard.coins)

    def test_use(self):
        player = Dominion.Player('Tony')
        self.assertEqual(10, len(player.stack()))
        trash = []

        # makes sure player has no played cards and 5 cards in their hand
        self.assertEqual(5, len(player.hand))
        self.assertEqual(0, len(player.played))

        # adds woodcutter to hand
        player.hand += [Dominion.Woodcutter()]
        self.assertEqual(6, len(player.hand))

        # asserts woodcutter is correct card and uses it
        self.assertEqual('Woodcutter', player.hand[5].name)
        player.hand[5].use(player, trash)

        # makes sure the player has the correct amount of cards played and cards in their hand
        self.assertEqual(1, len(player.played))
        self.assertEqual(5, len(player.hand))

    def test_augment(self):
        player = Dominion.Player('Tony')
        self.assertEqual(10, len(player.stack()))
        trash = []

        player.actions = 1
        player.buys = 1
        player.purse = 0

        # adds market card and calls augment, reducing player actions by 1 after using it
        player.hand += [Dominion.Market()]
        self.assertEqual('Market', player.hand[5].name)
        player.hand[5].augment(player)
        player.hand[5].use(player, trash)
        player.actions -= 1



        # makes sure actions, buys, and purse is accurate
        self.assertEqual(1, player.actions)
        self.assertEqual(2, player.buys)
        self.assertEqual(1, player.purse)
        self.assertEqual(6, len(player.hand))

class TestPlayer(TestCase):

    def test_action_balance(self):
        player = Dominion.Player('Tony')
        self.assertEqual(10, len(player.stack()))

        self.assertEqual(0, player.action_balance())

        # adding some action cards
        player.deck += [Dominion.Smithy()] * 2 + [Dominion.Market()] * 3

        # making sure balance is correct(or close since floats can a little off)
        self.assertAlmostEqual(-9.333, player.action_balance(), 3)

    def test_calcpoints(self):
        player = Dominion.Player('Tony')
        self.assertEqual(10, len(player.stack()))

        # asserts the player has 3 points
        self.assertEqual(3, player.calcpoints())

        #adds an Estate victory card to deck and asserts player has 4 points
        player.deck = player.deck + [Dominion.Estate()]
        self.assertEqual(4, player.calcpoints())

    def test_draw(self):
        player = Dominion.Player('Tony')
        self.assertEqual(10, len(player.stack()))

        # make sure player has 5 cards in hand and 5 cards in deck before drawing
        self.assertEqual(5, len(player.hand))
        self.assertEqual(5, len(player.deck))

        # draw and make sure player has 6 cards in hand and 4 in deck
        player.draw()
        self.assertEqual(6, len(player.hand))
        self.assertEqual(4, len(player.deck))

    def test_cardsummary(self):
        player = Dominion.Player('Tony')
        self.assertEqual(10, len(player.stack()))

        # making sure initial deck is correct
        self.assertEqual(3, player.cardsummary()['Estate'])
        self.assertEqual(7, player.cardsummary()['Copper'])
        self.assertEqual(3, player.cardsummary()['VICTORY POINTS'])

        # adding some cards to deck
        player.deck += [Dominion.Silver()] * 3 + [Dominion.Duchy()] * 2

        # making sure correct amounts in deck
        self.assertEqual(3, player.cardsummary()['Estate'])
        self.assertEqual(2, player.cardsummary()['Duchy'])
        self.assertEqual(7, player.cardsummary()['Copper'])
        self.assertEqual(3, player.cardsummary()['Silver'])
        self.assertEqual(9, player.cardsummary()['VICTORY POINTS'])


class Test_gameOver(TestCase):
    def test_gameover(self):
        supply = {}
        supply['Province'] = [Dominion.Province()] * 10
        supply['Market'] = [Dominion.Market()] * 10
        supply['Gold'] = [Dominion.Gold()] * 10
        supply['Festival'] = [Dominion.Festival()] * 10

        # gameover should return false
        self.assertFalse(Dominion.gameover(supply))

        # gameover should return true
        supply['Province'] = [Dominion.Province()] * 0
        self.assertTrue(Dominion.gameover(supply))

        # gameover should return false
        supply['Province'] = [Dominion.Province()] * 1
        supply['Market'] = [Dominion.Market()] * 0
        supply['Gold'] = [Dominion.Gold()] * 0
        self.assertFalse(Dominion.gameover(supply))

        # gameover should return true
        supply['Festival'] = [Dominion.Festival()] * 0
        self.assertTrue(Dominion.gameover(supply))


