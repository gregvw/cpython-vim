import collections

def strlistToColumns( strl, maxWidth=80, spacing=4 ):

    longest = max([len(s) for s in strl])
    width = longest+spacing

    # compute numCols s.t. (numCols-1)*(longest+spacing)+longest < maxWidth
    numCols = 1 + (maxWidth-longest)//width
    C = range(numCols)

    # If len(strl) does not have a multiple of numCols, pad it with empty strings
    strl += [""]*(len(strl) % numCols)
    numRows = len(strl)/numCols
    colString = ''

    for r in range(numRows):
        colString += "".join(["{"+str(c)+":"+str(width)+"}" \
            for c in C]+["\n"]).format(*(strl[numCols*r+c] \
            for c in C))
    return str(colString)
    


class VimSyntax(object):

    def __init__(self,param):

        self.hline = "\""+"-"*70

        self.vimfile = param["Vim File Name"]
        sourceFiles = strlistToColumns(param["Source Files"])
 
        output = open(self.vimfile,"w")
        output.write("\" Vim syntax file\n")
        output.close()

        self.comment([                                                        \
        "Language:     {0}".format(param["Language"]),                        \
        "Maintainer:   {0} <{1}>".format(param["Maintainer"],param["Email"]), \
        "Last Change:  {0}".format(param["Last Change"]),                     \
        "Version:      {0}".format(param["Version"]),                         \
        "Changelog:    {0}\n".format(param["Changelog"])])
 
        self.comment("This syntax file was automatically generated from the source files:\n\n")
        self.comment(sourceFiles.split("\n"))
        self.comment(["located in the path:","{0}".format(param["Source Path"])])      
 

        self.write(["\nif version < 600","  syntax clear",           \
        "elseif exists(\"b:current_syntax\")","  finish", "endif\n"])
    
        self.prefix = param["Prefix"]

        base = param["Base Syntax"]

        if base:
            self.comment("Read the syntax in {0} to start with".format(base))
            self.write(["if version < 600",          \
            "  so <sfile>:p:h/{0}.vim".format(base), \
            "else", "  runtime! syntax/cpp.vim",     \
            "  unlet b:current_syntax", "endif\n"])

    def writeln(self, text): 
        output = open(self.vimfile,"a")
        output.write("{0}\n".format(text))
        output.close()

    def write(self,text):
        if isinstance(text,list):
            [self.writeln(t) for t in text]
        else:
            self.writeln(text)

    def syntax(self, category, name):
        self.writeln("syn keyword {0}{1} {2}".format(self.prefix,category,name))

    def comment(self,text,section=False):
        if section:
            self.writeln("")
            self.writeln(self.hline)
        if isinstance(text,list):
            self.write(["\" {0}".format(t) for t in text])
        else:
            self.writeln("\" {0}".format(text))

        if section:
            self.writeln(self.hline)

    def link(self, group, keyword=None):
        if keyword == None:
            keyword = group
        self.writeln("hi def link {0}{1:12} {2:12}".format(self.prefix,group,keyword))


