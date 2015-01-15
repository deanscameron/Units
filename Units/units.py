class Unit(object):
    def __init__(self, unit_type, unit_scale):
        # unit_type (eg. time) to define similar units
        # unit_scale (eg. 60 for minute) to compute in similar units
        # would allow second=Unit("time", 1)
        self.unit_type=unit_type
        self.unit_scale=unit_scale
		 
    def multiply(self, constant):
        # multiplies Units by a constant
        if type(constant) == int and type(self)==Unit:		
            return Term(self, constant)
        elif type(constant) == float and type(self)==Unit:
            return Term(self, constant)
        else:
            raise TypeError("Units can only be multiplied by int or float")

class Term(object):
    def __init__(self, unit, coeff):
        # just a number times a unit	
        self.unit=unit
        self.coeff=coeff
		
    def add(self, other):
        # adds Terms of the same unit_type
        if other.unit.unit_type == self.unit.unit_type:
            new_coeff=self.coeff+other.coeff*float(other.unit.unit_scale/self.unit.unit_scale)
        else:
            raise TypeError("Cannot sum terms with different types of unit")		
        return Term(unit, new_coeff)
		
    def multiply(self, constant):
        # multiplies Terms by a constant
        if type(constant) == int and type(self)==Unit:
            new_coeff=constant*self.coeff		
            return Term(unit, new_coeff)
        elif type(constant) == float and type(self)==Unit:
            new_coeff=constant*self.coeff
            return Term(unit, new_coeff)
        else:
            raise TypeError("Terms can only be multiplied by int or float")
		
    def equality(self, other):
        # compares Terms of same unit_type
        if other.unit.unit_type != self.unit.unit_type:
            raise TypeError("Terms with different unit types cannot be equal")
        elif other.coeff*other.unit.unit_scale == self.coeff*self.unit.unit_scale:
            return True
        else:
            return False	
			
    def to_unit(self, unit):
        if self.unit.unit_type != unit.unit_type:
            raise TypeError("Terms cannot be converted to units of different type")
        else:
            new_coeff=self.coeff*float(self.unit.unit_scale/unit.unit_scale)
        return Term(unit, new_coeff)