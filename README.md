# cpython-vim
Vim syntax highlighting for writing Python extensions with the C API

The script cpython-vim.py will parse all of the Python header files
in the directory that contains Python.h and assign Vim highlighting 
keywords to various CPython elements and write the syntax information

~/.vim/after/syntax/cpython.vim 

Sample usage:

$ python cpython-vim.py /path-to-Python.h

In Linux/Darwin, you can get the path with 

$ locate Python.h

Since the syntax keyword list is automatically generated, this script
should work with any version of Python. 

This is still very much a work in progress. While most CPython specific
keywords are correctly collected and identified, there are still a 
few things (e.g. enums, certain structs, function pointers, etc)
which need to be implemented. 

Also included is a dark themed syntax color scheme that I have been 
playing with to test this out. To do so, copy cpython-darkcolors.vim to
~/.vim/colors and add the following to your .vimrc:

if has("gui\_running")
  autocmd BufNewFile,BufRead cpython colorscheme cpython-darkcolors
endif

Note that this will apply the colorscheme to C/C++ as well 



