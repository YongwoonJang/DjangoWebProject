class SentenceReader:

	def __init__(self, filepath):
		self.filepath = filepath 

	def __iter__(self):
		for line in open(self.filepath, 'r'):
			yield line.split(' ')
