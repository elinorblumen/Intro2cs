REC_ILLNESS = 0
REC_SYMPTS = 1

class Node:
	def __init__(self, data = "", pos = None, neg = None):
		self.data = data
		self.positive_child = pos
		self.negative_child = neg
	
	def get_data(self):
		return self.data
	
class Record:
	def __init__(self, illness, symptoms):
		self.illness = illness
		self.symptoms = symptoms
	
			
def parse_data(filepath):
	with open(filepath) as data_file:
		records = []
		for line in data_file:
			words = line.split()
			records.append(Record(words[REC_ILLNESS], words[REC_SYMPTS:]))
		return records
		
		
class Diagnoser:
	def __init__(self, root):
		self.__root = root
		
	def diagnose(self, symptoms):

	    if str(self.__root) in symptoms:

        	return 





	def calculate_error_rate(self, records):
		pass
		
	def all_illnesses(self):
		pass
		
	def most_common_illness(self, records):
		pass
		
	def paths_to_illness(self, illness):
		pass
		

def build_tree(records, symptoms):
	pass
	
def optimal_tree(records, symptoms, depth):
	pass
	
if __name__ == "__main__":
	
	# Manually build a simple tree.
	#                cough
	#          Yes /       \ No
	#        fever           healthy
	#   Yes /     \ No
	# influenza   cold
	
	
	flu_leaf = Node("influenza", None, None)
	cold_leaf = Node("cold", None, None)
	inner_vertex = Node("fever", flu_leaf, cold_leaf)
	healthy_leaf = Node("healthy", None, None)
	root = Node("cough", inner_vertex, healthy_leaf)
	
	diagnoser = Diagnoser(root)
	
	# Simple test
	diagnosis = diagnoser.diagnose(["cough"])
	if diagnosis == "cold":
		print("Test passed")
	else:
		print("Test failed. Should have printed cold, printed: ", diagnosis)
		
	# Add more tests for sections 2-7 here.
