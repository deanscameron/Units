class Unit(object):
    def __init__(self, unit_type, unit_scale):
	    # unit_type (eg. time) to define similar units
		# unit_scale (eg. 60 for minute) to compute in similar units
		# would allow second=Unit("time", 1)
        self.unit_type=unit_type
		self.unit_scale=unit_scale

class Term(object):
    def __init__(self, unit, coeff):
        # just a number times a unit	
        self.unit=unit
        self.coeff=coeff
		
    def add(self, other):
        # adds Terms of the same unit_type
        if other.unit.unit_type = self.unit.unit_type:
            new_coeff=self.coeff+other.coeff*(other.unit.unit_scale/self.unit.unit_scale)
        else:
            raise TypeError("Cannot sum terms with different types of unit")		
        return Term(unit, new_coeff)
		
    def multiply(self, constant):
        # multiplies Terms by a constant
		new_coeff=constant*self.coeff
		return Term(unit, new_coeff)
		
    def equality(self, other):
	    # compares Terms of same unit_type
		
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.multiply(other)
    ### "RightOpValue"
    def __rmul__(self, other):
        return self.__mul__(other)
    def __radd__(self, other):
        return self.__add__(other)
    ### "StringOverload"
    def __str__(self):
        def symbol_string(symbol, power):
            if power==1:
                return symbol
            else:
                return symbol+'^'+str(power)
        symbol_strings=[symbol_string(symbol, power)
                for symbol, power in self.unit.iteritems()]
        prod='*'.join(symbol_strings)
        if not prod:
            return str(self.value)
        if self.value==1:
            return prod
        else:
            return str(self.value)+'*'+prod
    def equality(self, other):
	    unit=dict(self.unit)
        value=self.value
        # Convert arguments to Values first if they are
        # constants or integers
        others=map(Value,others)
        for another in others:
            for symbol, exponent in another.unit.iteritems():
                if symbol in unit:
                    unit[symbol]+=another.unit[symbol]
                else:
                    unit[symbol]=another.unit[symbol]
            value*=another.value
        return Value(unit,value)

### "ExpressionConstruct"

class Expression(object):
    def __init__(self, Values=[]):
        self.Values=list(Values)
    ### "ExpressionFunctions"
    def add(self, *others):
        result=Expression(self.Values)
        for another in others:
            if type(another)==Value:
                result.Values.append(another)
            else:
                result.Values+=another.Values
        return result
    ### "ExpressionOverloads"
    def __add__(self, other):
        return self.add(other)
    ### "RightOp"
    def __radd__(self, other):
        return self.__add__(other)
    ### "ExpressionStringOverload"
    def __str__(self):
        return '+'.join(map(str,self.Values))



### "withfunc"

x=Value('seconds')
y=Value('metres')

first=Value(5).multiply(Value('seconds'),Value('seconds'),Value('metres'))
second=Value(7).multiply(Value('x'))
third=Value(2)
expr=first.add(second,third)

print first
print second
print expr


### "withop"

x_plus_y=Value('x')+'y'
print x_plus_y.Values[0].unit

five_x_ysq=Value('x')*5*'y'*'y'
print five_x_ysq.unit, five_x_ysq.value

### "RightUse"

print 5*Value('x')

### "HardTest"

fivex=5*Value('x')
print fivex.unit, fivex.value

### "UseString"

first=Value(5)*'x'*'x'*'y'
second=Value(7)*'x'
third=Value(2)
expr=first+second+third
print expr
fourth=Value(60)*'seconds'
print fourth.unit
### "Callable"

class MyCallable(object):
    def __call__(self, name):
        print "Hello, ", name

x=MyCallable()

x("James")