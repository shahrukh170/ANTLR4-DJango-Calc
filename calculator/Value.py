class Value:
    def __init__(self):
        VOID = object()
        value = Value(object())
        
    
    def Value(self,value):
        self.value = value
        self.VOID = value
	
	
    def asBoolean(self):
       return Boolean.valueOf(self.value);
    

    def asDouble(self):
       return parseFloat(self.value);
    

    def asString(self):
       return String.valueOf(self.value);
    

    def isDouble(self):
       return typeof(self.value)==typeof(Double);
    

    
    def hashCode(self):
        if(self.value == null):
           return 0
        return self.value.hashCode();
    

    
    def equals(self,o):
        if(self.value == o):
            return true;
        

        if(self.value == null or o == null or o.getClass() != self.getClass()):
            return false;
        

        that = o;

        return self.value.equals(that.value);
    

    
    def toString(self):
        return String.valueOf(self.value);
   
