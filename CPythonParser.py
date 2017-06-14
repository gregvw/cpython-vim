import os
import re
import collections

def get_args(string):
    string = string.strip()
    n = string.index('(')
    count = 1
    for k in range(n+1,len(string)):
        if string[k] == '(':
            count += 1
        elif string[k] == ')':
            count -= 1
        if count == 0:       
            break
    return string[n+1:k].split(',')
  

class Parser(object):

    def __init__(self):
        self.functions = {}
        self.constants = []
        self.macros    = {}
        self.objects   = set()
        self.types     = set()

    def parse_header(self,header):

        h = open(header,'r')
        lines = h.readlines()
        h.close()    

        for i,l in enumerate(lines):


            # Find all PyXYZObjects
            if "Py" in l and "Object" in l:

                for el in set(re.findall(r"(Py[a-zA-Z]*?Object)",l)):
                    self.objects.add(el)


            # Find all defines
            elif l[:7] == "#define":
                # Find macro functions s
                if '(' in l or ')' in l and '{' not in l:
                    mc = l.split()[1:] 
                    if mc[-1] == '\\':
                       j = i + 1
                       lnext = lines[j].split()
                       mc += [" "] + lnext
                       while( lnext[-1] == '\\' ):
                           j = j+1
                           lnext = lines[j].split()
                           mc += [" " ] + lnext
                    mline = "".join(mc)
                    margs = get_args(mline)
                    macroName = mline.split('(')[0]
                    if macroName[0] != '_':
                        self.macros[macroName] = len(margs)

                # Find constants
                else:
                    cn = l.split()[1]
                    if cn[0] != '_':
                        self.constants.append(cn)

            # Find all typedefs        
            elif l[:7] == "typedef":
                lsplit = l.split()
                # Find function pointers
                if '(' in l:
                    pass
                # Find enums
                elif 'enum' in l:
                    pass
                # Find structs
                elif 'struct' in l:
                   pass
                # Find types
                else:
                   ptype = lsplit[-1][:-1]
                   if re.search('[a-zA-Z]',ptype):
                       self.types.add(ptype.replace('*',''))

                       # Find all function definitions
            if "PyAPI_FUNC(" in l:
                # Extract the function return type
                rt = re.findall(r"PyAPI_FUNC\((.*?)\)",l)
                returnType = rt[0].replace(' *','*')
    
                # Extract the function name
                fn = re.findall(r"\)(.*?)\(",l)
                if len(fn)>0:
                    functionName = fn[0].replace(' ','')
    
                    # Exclude internal functions which begin with underscore
                    if functionName[0] != '_':
                        #print(functionName)
                        self.functions[functionName] = {"return": returnType}
    
                        # Extract the function arguments
                        fargs = re.findall(r"{0}\((.*?)\);".format(functionName),l)
                        if len(fargs) > 0:  
                            self.functions[functionName].update({"args" : fargs}) 
                            
    def getFunctions(self):
        return collections.OrderedDict(sorted(self.functions.items()))

    def getMacros(self):
        return collections.OrderedDict(sorted(self.macros.items()))

    def getConstants(self):
        self.constants.sort()
        return self.constants

    def getObjects(self):
        return sorted(self.objects)

    def getTypes(self):
        return sorted(self.types)



