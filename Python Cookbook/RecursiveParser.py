import re
import collections

NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES  = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPARENT = r'(?P<LPARENT>\()'
RPARENT = r'(?P<RPARENT>\))'
WS = r'(?P<WS>\s+)'


master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPARENT, RPARENT, WS]))
Token = collections.namedtuple("Token", ["type", "value"])

def generate_tokens(text):
	scanner = master_pat.scanner(text)
	for m in iter(scanner.match, None):
		tok = Token(m.lastgroup, m.group())
		if tok.type != 'WS':
			yield tok



class ExpressionEvaluator:
	def parse(self, text):
		self.tokens = generate_tokens(text)
		self.tok = None
		self.nexttok = None
		self._advance()
		return self.expr()



	def _advance(self):
		self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

	def _accept(self, toktype):
		if self.nexttok and self.nexttok.type == toktype:
			self._advance()
			return True
		else:
			return False

	def _expect(self, tokentype):
		if not self._accept(tokentype):
			raise SyntaxError("Expected " + tokentype)


	def expr(self):
		exprval = self.term()
		while self._accept('PLUS') or self._accept('MINUS'):
			op = self.tok.type
			right = self.term()
			if op == 'PLUS':
				exprval += right 
			elif op == 'MINUS':
				exprval -= right 
		return exprval


	def term(self):
		termval = self.factor()
		#it's a "while" instead of "if" cause the _accept has _advance so
		#for cause as 2 + 3 * 3 * 3 the "3 * 3 * 3" should be continuous
		while self._accept('TIMES') or self._accept('DIVIDE'):
			op = self.tok.type
			right = self.factor()
			if op == 'TIMES':
				termval *= right
			elif op == 'DIVIDE':
				termval /= right
		return termval


	def factor(self):
		if self._accept('NUM'):
			return int(self.tok.value)
		elif self._accept('LPARENT'):
			exprval = self.expr()
			self._expect("RPARENT")
			return exprval
		else:
			raise SyntaxError("Expected NUMBER OR LPARENT")
parser = ExpressionEvaluator()
print parser.parse("2")
print parser.parse("2 + 3 * 3 / 2")
print parser.parse("23 + 42 * 10 / 2")
print parser.parse("4 * 5 + (2 + 10)")
