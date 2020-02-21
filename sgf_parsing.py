class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other

#returns the properties key, identified by uppercase characters before the [values]
def propkey(input_string):

    prop_key=""
    flag_prop_key=0
    n=0

    while flag_prop_key==0:
        if input_string[n].isalpha() and input_string[n].isupper():
            prop_key=prop_key+input_string[n]
            n=n+1
        else:
            if input_string[n]=="[":
                flag_prop_key=1
            else:
                raise ValueError("Error in Key")

    return prop_key,n

#returns the properties values, identified by characters between []
def propvalue(input_string):

    flag_prop_value=0
    prop_value=[]
    n=0

    while flag_prop_value==0:
        
        if input_string[n]=="[":
            n=n+1
            str_value=""

            while input_string[n]!="]":
                if input_string[n]=="\\": #treatment for special caracthers
                    str_value=str_value+input_string[n+1]
                    n=n+2
                    
                else:
                    if input_string[n]=="\n": #treatment for special caracthers
                        str_value=str_value+"\n"
                        n=n+1
                    else:
                        if input_string[n]=="\t": #treatment for special caracthers
                            str_value=str_value+" "
                            n=n+1
                        else:
                            str_value=str_value+input_string[n]
                            n=n+1
                      
            prop_value.append(str_value)
            n=n+1
        
        else:
            flag_prop_value=1
                
    return prop_value,n

#function to parse itself
def parse(input_string):

    if len(input_string)<3:
        raise ValueError("Input not valid")
    if input_string[0:2]!="(;":
        raise ValueError("Input not valid")
       
    n=2

        
    prop_key_list=[]
    prop_value_list=[]

    #getting the properties Keys and Values
    while input_string[n] != ";" and input_string[n] !=")" and input_string[n] != "(":
        
        prop_key,k=propkey(input_string[n:])
        n=n+k
        prop_key_list.append(prop_key)

        prop_value,k=propvalue(input_string[n:])
        n=n+k
        prop_value_list.append(prop_value)

    child_key_list=[]
    child_value_list=[]

    #getting the children properties and values
    while len(input_string[n:])>1:
        if input_string[n]=="(" or input_string[n]==")" or input_string[n]==";":
            n=n+1    
        else:
            child_key,k=propkey(input_string[n:])
            n=n+k
            child_key_list.append(child_key)
            print(child_key_list)

            child_value,k=propvalue(input_string[n:])
            n=n+k
            child_value_list.append(child_value)
            print(child_value_list)

    prop_dict=dict(zip(prop_key_list, prop_value_list))
    children_dict=dict(zip(child_key_list, child_value_list))

    ch_parse=[]

    print(prop_dict, children_dict)

    for x,y in children_dict.items():
        ch_parse.append(SgfTree({x:y}))
 
    return SgfTree(properties=prop_dict, children=ch_parse)
                
