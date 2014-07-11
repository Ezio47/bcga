from .op_split import split

from .op_comp import comp
from .op_comp import f, e, v
from .op_comp import front, side, top

from .op_extrude import extrude

from .op_color import color

from .base import attr, random
from .base import context
from .base import Rule

x = "x"
y = "y"
z = "z"

def rule(operator):
	def inner(*args, **kwargs):
		state = context.getExecutionState()
		if not state['valid']:
			print(operator.__name__, "invalid state")
		if context.immediateExecution:
			operator(*args, **kwargs)
		else:
			return Rule(operator, args, kwargs)
	return inner

def repeat(*args):
	return args

def flt(value):
	return {'flt':value}

def rel(value):
	return {'rel':value}

def size(sizeX, sizeY, sizeZ):
	pass

def translate(tx, ty, tz):
	pass

def insert(assetId):
	pass
