class Buffer(object):
	"""docstring for Buffer"""
	def __init__(self, data):

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

	pass


class IntToken(Token):
	"""docstring for IntToken"""
	#cong zifuchuan du qu zhidao zifu bushi zhengshu 		
	def consume(self,buffer):
		accum = ""
		while True:
			ch = buffer.peek()
			if ch is None or ch not in "0123456789":
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
				tokens.append(token)
				break
		if not token:
			raise ValueError("error in synax")
	return tokens

class Node(object):
	"""docstring for Node"""
	pass
		


class IntNode(Node):
	"""docstring for IntNode"""
	def __init__(self, value):
		super(IntNode, self).__init__()
		self.value = value
		
		

		

#caozuo fu jiedian(=/-)
class BinaryOpNode(Node):
	def __init__(self,kind):
		self.kind = kind
		self.left = None #zuo jie jiedian
		self.right = None#you jiedian

#cong token liebiao shengch biaodashi erchashu

def parse(tokens):
	if tokens[0][0]  != "int":
		raise ValueError("must start with an int")
	#quchu token[0],gai token wei zhengshu
	node  = IntNode(tokens[0][1])
	nbo  = None
	last = tokens[0][0]

	#cong di er ge token kaishi xunhuan quchu 
	for token in tokens[1:]:
		#xianling liangge token de leixing yixiang zewei cuowu 
		if token[0]==last:
			raise ValueError('error in syntax')
		last = token[0]
		#ruguo token wei caozuofu .ze baocun caozuofu jiedian,baqian yige zhengshu 
		#token zuowei zuo jiedian
		if token[0]=='ope':
			nbo = BinaryOpNode(token[1])
			nbo.left = node

		#ruguo token wei zhengshu ,ze baocun gai token wei youjiedian 
		if token[0]=='int':
			nbo.right = IntNode(token[1])
			node = nbo
	return node


#caiyong digui fangfa jisuan erchashu de zhi

def calculate(nbo):
	#ruguo zuojiedian shi ercha shu ,xian jisuan zuo jiedian de zhi 
	if isinstance(nbo.left,BinaryOpNode):
		leftval = calculate(nbo.left)
	else:
		leftval = nbo.left.value
	#genju caozuofu +/-
	if nbo.kind =='-':
		return leftval-nbo.right.value
	elif nbo.kind =='+':
		return leftval+nbo.right.value
	else:
		raise ValueError("wrong operator")

def evaluate(node):
	if isinstance(node,IntNode):
		return node.value
	else:
		return calculate(node)


if __name__ == '__main__':
	input = input("Input:")

	tokens=tokenize(input)

	node = parse(tokens)

	print(str(evaluate(node)))
				