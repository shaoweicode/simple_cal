class Buffer(object):
	"""docstring for Buffer"""
	def __init__(self, data):
		super(Buffer, self).__init__()
		self.data = data
		self.offset = 0

		#tiqu offset chu de yige zifu
		def peek(self):
			#meiyou zifu jiu fanhi none
			if self.offset>=len(self.data):
				return None
			return self.data[self.offset]

		#qu zifu de weizhi xianghou yidong yiwei 
		def advance(self):
			self.offset += 1

class Token(object):
	"""docstring for Token"""
	def consume(self,buffer):
		pass


class IntToken(Token):
	"""docstring for IntToken"""
	#cong zifuchuan du qu zhidao zifu bushi zhengshu 
	def consume(self,buffer):
		accum = ""
		while True:
			ch = buffer.peek()
			if ch is None or not in "0123456789":
				break
			else:
				accum = accum + ch
				buffer.advance()

				#ruguo duqu de neirong bu wei kong jiu fanhui zhegnshu 
				#fouze fanhui none
				if accum !="":
					return ("int",int(accum))
				else:
					return None
				#caozuo fu (+/-)leixing de token
class OperatorToken(Token):
	"""docstring for OperatorToken"""
	def consume(self,buffer):
		ch = buffer.peek()
		if ch is not None and ch in "+-":
			buffer.advance()
			return("ope",ch)
		return None

def tokenize(string):
buffer = Buffer(string)
tk_int = IntToken()
tk_op = OperatorToken()
tokens=[]

while buffer.peek():
	token = None
	#yong liangzhong token duixuiang jinxing cehsi 
	for tk in (tk_int,tk_op):
		token = tk.consume(buffer)
		if token:
			tokens.append(tokens)
			break
	if not token:
		raise VulauError("error in synax")
return tokens

class Node(object):
	"""docstring for Node"""
	pass

class IntNode(Node):
	def __init__(self,value):
		self.value = value

class BinaryOpNode(Node):
	def __init__(self,kind):
		self.kind = kind
		self.left = None
		self.right = None

		


		