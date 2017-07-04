import os

from flask_testing import TestCase

# from __init__ import create_app
from overwatchdb.models import db, player, hero, reward, achievement


class ModelsTest(TestCase):

    """ Tests the models """

    # def create_app(self):
    #     return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_players1(self):
        player1 = player(id=1, name='test', server='test',
                     hero_id=1.0, level='1', url='test')
        player2 = player(id=1, name='test', server='test',
                     hero_id=1.0, level='1', url='test')
        db.session.add(player1)
        db.session.add(player2)
        db.session.commit()
        players = player.query.all()
        self.assertTrue(player1 in players)
        self.assertTrue(player2 in players)
        self.assertEqual(len(players), 2)

    def test_players2(self):
        player = player(id=1, name='test', server='test',
                     hero_id=1.0, level='1', url='test')
        db.session.add(player)
        db.session.commit()
        players = player.query.all()
        self.assertTrue(player in players)
        self.assertEqual(players[0].id, 1)
        self.assertEqual(players[0].url, 'test')

    def test_players3(self):
        player = player(id=1, name='test', server='test',
                     hero_id=1.0, level='1', url='test')
        db.session.add(player)
        db.session.commit()
        players = player.query.all()
        self.assertTrue(player in players)
        self.assertEqual(players[0].name, 'test')

    def test_players4(self):
        player1 = player(id=1, name='test', server='test',
                     hero_id=1.0, level='1', url='test')
        player2 = player(id=1, name='test', server='test',
                     hero_id=1.0, level='1', url='test')
        reward = reward(
            id=1, name='test', abbrev='test',
            url='test', cost='50')
        reward.players = [player1, player2]
        db.session.add(player1)
        db.session.add(player2)
        db.session.add(reward)
        db.session.commit()
        rewards = reward.query.all()
        self.assertIn(player1, rewards[0].players)
        self.assertIn(player2, rewards[0].players)

    def test_hero1(self):
        hero1 = hero(
            id=1, name='Tracer', description='test', url=1.0)
        hero2 = hero(
            id=2, name='Reaper', description='test', url=2.0)
        db.session.add(hero1)
        db.session.add(hero2)
        db.session.commit()
        heros = hero.query.all()
        self.assertTrue(hero1 in heros)
        self.assertTrue(hero2 in heros)
        self.assertEqual(len(heros), 2)

    def test_hero2(self):
        hero = hero(
            id=1, name='Tracer', description='test', url=1.0)
        db.session.add(hero)
        db.session.commit()
        db_hero = hero.query.first()
        self.assertEqual(db_hero.url, 1.0)

    def test_hero3(self):
        hero = hero(
            id=1, name='Tracer', description='test', url=1.0)
        db.session.add(hero)
        db.session.commit()
        db_hero = hero.query.first()
        self.assertEqual(db_hero.name, 'Tracer')

    def test_hero4(self):
        hero1 = hero(
            id=1, name='Tracer', server=0.2, url=1.0)
        hero2 = hero(
            id=2, name='Reaper', server=0.4, url=2.0)
        player = player(id=2, name='Aries', server=3.0,
                    hero_id=4.0, level=7000, url=3.0)
        player.heros = [hero1, hero2]
        db.session.add(hero1)
        db.session.add(hero2)
        db.session.add(player)
        db.session.commit()
        db_player = player.query.first()
        self.assertIn(hero1, db_player.heros)
        self.assertIn(hero2, db_player.heros)

    def test_reward1(self):
        reward1 = reward(
            id=1, name='test', quality='test', url='test', cost='50')
        reward2 = reward(
            id=2, name='test', quality='test2', url='test', cost='50')
        db.session.add(reward1)
        db.session.add(reward2)
        db.session.commit()
        rewards = reward.query.all()
        self.assertTrue(reward1 in rewards)
        self.assertTrue(reward2 in rewards)
        self.assertEqual(len(rewards), 2)

    def test_reward2(self):
        reward = reward(
            id=1, name='test', quality='test', url='test', cost='50')
        db.session.add(reward)
        db.session.commit()
        db_reward = reward.query.first()
        self.assertEqual(db_reward.id, 1)

    def test_reward3(self):
        reward = reward(
            id=1, name='test', quality='test', url='test', cost='50')
        db.session.add(reward)
        db.session.commit()
        db_reward = reward.query.first()
        self.assertEqual(db_reward.name, 'test')

    def test_reward4(self):
        reward1 = reward(
            id=1, name='test', quality='test', url='test', cost='50')
        reward2 = reward(
            id=2, name='test', quality='test2', url='test', cost='50')
        achievement = achievement(
            id=1, name='test', description='test', url='test')
        achievement.rewards = [reward1, reward2]
        db.session.add(reward1)
        db.session.add(reward2)
        db.session.add(achievement)
        db_achievement = achievement.query.first()
        self.assertIn(reward1, db_achievement.rewards)
        self.assertIn(reward2, db_achievement.rewards)

    