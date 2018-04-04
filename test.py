import unittest

from app import db
from flask import Flask

class BasicTests(unittest.TestCase):
     # set up and teardown

     def setUp(self):
        self.app = Flask(__name__)
