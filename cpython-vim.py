import os
import sys

from VimSyntax import VimSyntax
from CPythonParser import Parser


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("\nPlease specify the path in which the Python.h\n" + \
              "file you wish to use is located. For example:\n\n" + \
              "$ python cpython-vim.py /usr/local/include/python2.7/\n")

        sys.exit()

    vimpath = os.path.join(os.path.expanduser("~"),".vim")

    ftdetect = open(os.path.join(vimpath,"ftdetect","cpython.vim"),"w")
    ftdetect.write("au BufRead,BufNewFile *.h,*.c,*.hpp,*.cpp set filetype=cpython\n")
    ftdetect.close()

    output = os.path.join(vimpath,"after","syntax","cpython.vim")

    header_path = sys.argv[1]
    header_files = [h for h in os.listdir(header_path) if os.path.splitext(h)[1]=='.h']

    headers = [os.path.join(header_path,hf) for hf in header_files]

    parameters = { "Language"      : "CPython",               \
                   "Maintainer"    : "Greg von Winckel",      \
                   "Email"         : "gregvw@gmail.com",      \
                   "Last Change"   : "11 Jun 2017",           \
                   "Version"       : "0.1",                   \
                   "Changelog"     : "0.1 - initial version", \
                   "Vim File Name" : output       ,           \
                   "Source Path"   : header_path,             \
                   "Source Files"  : header_files,            \
                   "Base Syntax"   : "cpp",                   \
                   "Prefix"        : "cpy",                   \
                   "Docstring"     :                          \
                   "Syntax highlighting for Python extensions in the C API"}   
   
    parser = Parser()

    for h in headers:
        parser.parse_header(h)

    functions = parser.getFunctions()
    macros    = parser.getMacros()
    constants = parser.getConstants()
    objects   = parser.getObjects()  
    types     = parser.getTypes() 

    vim = VimSyntax( parameters )

    vim.syntax("PyAPI_FUNC","PyAPI_FUNC")

    vim.comment('Objects',True)
    for o in objects:
        vim.syntax("Object",o)

    vim.comment('Types',True)
    for t in types:
        vim.syntax("Type",t)

    vim.comment('Functions',True)
    for f in functions:
        vim.syntax("Function",f)

    vim.comment('Constants',True)
    for c in constants:
        vim.syntax('Constant',c)           
  
    vim.comment('Macros',True);
    for m in macros:
        vim.syntax('Macro',m) 
    
    
    vim.write([""]*2)


    vim.link("PyAPI_FUNC","API_FUNC")
    vim.link("Object")
    vim.link("Type")
    vim.link("Macro","Function")
    vim.link("Constant")
    vim.link("Function")
   


    

   
