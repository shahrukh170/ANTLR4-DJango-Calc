from antlr4 import *
import math
#import HashMap
#import Map
conditions = []
##var Stack = require('stack');
from calculator.CalculatorXLexer import CalculatorXLexer
from calculator.CalculatorXParser import CalculatorXParser
from calculator.CalculatorXVisitor import CalculatorXVisitor
from calculator.Value import Value
class HashTable:

	# Create empty bucket list of given size
	def __init__(self, size):
		self.size = size
		self.hash_table = self.create_buckets()

	def create_buckets(self):
		return [[] for _ in range(self.size)]

	# Insert values into hash map
	def set_val(self, key, val):
		
		# Get the index from the key
		# using hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be inserted
			if record_key == key:
				found_key = True
				break

		# If the bucket has same key as the key to be inserted,
		# Update the key value
		# Otherwise append the new key-value pair to the bucket
		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))

	# Return searched value with specific key
	def get_val(self, key):
		
		# Get the index from the key using
		# hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key being searched
			if record_key == key:
				found_key = True
				break

		# If the bucket has same key as the key being searched,
		# Return the value found
		# Otherwise indicate there was no record found
		if found_key:
			return record_val
		else:
			return "No record found"

	# Remove a value with specific key
	def delete_val(self, key):
		
		# Get the index from the key using
		# hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be deleted
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return

	# To print the items of hash map
	def __str__(self):
		return "".join(str(item) for item in self.hash_table)

	
class CalculatorXBaseVisitorImpl(CalculatorXVisitor):
    variables = HashTable(50)
    Map = HashTable(50)        

    
    def visitPlus(self,ctx:CalculatorXParser.PlusContext):
        return self.visit(ctx.plusOrMinus()) + self.visit(ctx.multOrDiv())
    
    
     
    def visitMinus(self,ctx:CalculatorXParser.MinusContext):
        return self.visit(ctx.plusOrMinus()) - self.visit(ctx.multOrDiv())
    

     
    def visitMultiplication(self, ctx:CalculatorXParser.MultiplicationContext):
        return self.visit(ctx.multOrDiv()) * self.visit(ctx.pows())
    

     
    def visitDivision(self,ctx:CalculatorXParser.DivisionContext):
        return self.visit(ctx.multOrDiv()) / self.visit(ctx.pows())
    

     
    def visitSetVariable(self,ctx:CalculatorXParser.SetVariableContext):
        value = self.visit(ctx.plusOrMinus())
        self.variables.set_val(ctx.ID().getText(), value)
        return value;
    

     
    def visitPower(self,ctx:CalculatorXParser.PowerContext):
        if (ctx.pows() != None):
            return math.pow(self.visit(ctx.unaryMinus()), self.visit(ctx.pows()))
        return self.visit(ctx.unaryMinus())
    

     
    def visitChangeSign(self,ctx:CalculatorXParser.ChangeSignContext):
        return -1*self.visit(ctx.unaryMinus())
    

     
    def visitBraces(self,ctx:CalculatorXParser.BracesContext):
        return self.visit(ctx.plusOrMinus())
    

     
    def visitConstantPI(self,ctx:CalculatorXParser.ConstantPIContext):
        return math.PI
    

     
    def visitConstantE(self,ctx:CalculatorXParser.ConstantEContext):
        return math.E
    

     
    def visitInt(self,ctx:CalculatorXParser.IntContext):
        return float(ctx.INT().getText())
    

     
    def visitVariable(self,ctx:CalculatorXParser.VariableContext):
        return self.variables.get_val(ctx.ID().getText())
    

     
    def visitDouble(self,ctx:CalculatorXParser.DoubleContext):
        return float(ctx.DOUBLE().getText())
    

     
    def visitCalculate(self,ctx:CalculatorXParser.CalculateContext):
        return self.visit(ctx.plusOrMinus())
    

