import random
import string

class shortner:
	token_size = 5
	def __init__(self, token_size = None):
		self.token_size=token_size if token_size is not None else 5

	def issue_token(self):
		str_token = string.ascii_letters
		return ''.join(random.choice(str_token) for i in range(self.token_size))
	
	  