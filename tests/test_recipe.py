import unittest
from app.models import Recipe

class test_recipe(unittest.TestCase):
  def setUp(self):
    self.new_recipe = Recipe('name',5,'5 cups of water', 'Leave to boil','12.06.2021','Kenyan')