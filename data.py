# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
import requests as rq

class Post:
   def __init__(self):
      # Add your own JSON if you want to
      blogs_data = rq.get("https://api.npoint.io/538e38d88701bdb3fee0", timeout=20).json()
      self.data = blogs_data

