class Value(object):
    def __init__(self, *args):
        lead=args[0]
        if type(lead)==type(self):
            # Copy constructor
            self.unit=dict(lead.unit)
            self.value=lead.value
        elif type(lead)==int:
            self.from_constant(lead)
        elif type(lead)==str:
            self.from_symbol(*args)
        elif type(lead)==dict:
            self.from_dictionary(*args)
        else:
            self.from_lists(*args)
    def from_constant(self, constant):
        self.value=constant
        self.unit={}
    def from_symbol(self, symbol, value=1, power=1):
        self.value=value
        self.unit={symbol:power}
    def from_dictionary(self, unit, value=1):
        self.unit=unit
        self.value=value
    def from_lists(self, symbols=[], powers=[], value=1):
        self.value=value
        self.unit={symbol: exponent for symbol,exponent
                in zip(symbols, powers)}
    def add(self, *others):
        return Expression((self,)+others)
    def multiply(self, *others):
        result_unit=dict(self.unit)
        result_coeff=self.value
        # Convert arguments to Values first if they are
        # constants or integers
        others=map(Value,others)
        for another in others:
            for symbol, exponent in another.unit.iteritems():
                if symbol in result_unit:
                    result_unit[symbol]+=another.unit[symbol]
                else:
                    result_unit[symbol]=another.unit[symbol]
            result_coeff*=another.value
        return Value(result_unit,result_coeff)
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