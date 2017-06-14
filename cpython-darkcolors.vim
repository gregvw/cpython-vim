" Vim color file - cpython_darkcolors_vim
" Name: cpython-darkcolors
" Description: A dark color scheme for writing Python extensions with the C API
" Maintainer: Greg von Winckel <gregvw@gmail.com>
" Version: 0.1

" Mark as a dark theme
set background=dark

if version > 580
	hi clear
	if exists("syntax_on")
		syntax reset
	endif
endif

set t_Co=256

" Declare name of this colorscheme
let g:colors_name = "cpython_darkcolors"

"hi clear -- no settings --
"hi CTagsClass -- no settings --
"hi CTagsGlobalConstant -- no settings --
"hi CTagsGlobalVariable -- no settings --
"hi CTagsImport -- no settings --
"hi CTagsMember -- no settings --
"hi Ignore -- no settings --
"hi EnumerationName -- no settings --
"hi EnumerationValue -- no settings --
"hi LocalVariable -- no settings --
"hi Question -- no settings --
"hi Union -- no settings --

hi Normal            guifg=aquamarine1       guibg=grey32   
" hi IncSearch       guifg=#192224           guibg=#BD9800  
" hi WildMenu        guifg=NONE              guibg=#A1A6A8 
" hi SignColumn      guifg=#192224           guibg=#536991 
" hi SpecialComment  guifg=#BD9800           guibg=NONE 
" hi Typedef         guifg=#536991           guibg=NONE 
" hi Title           guifg=#F9F9FF           guibg=#192224 
" hi Folded          guifg=#192224           guibg=#A1A6A8 
" hi PreCondit       guifg=#BD9800           guibg=NONE    
" hi Include         guifg=#BD9800           guibg=NONE    
" hi TabLineSel      guifg=#192224           guibg=#BD9800 
" hi StatusLineNC    guifg=#192224           guibg=#5E6C70 
" hi NonText         guifg=#5E6C70           guibg=NONE    
" hi DiffText        guifg=NONE              guibg=#492224 
" hi ErrorMsg        guifg=#A1A6A8           guibg=#912C00 
" hi Debug           guifg=#BD9800           guibg=NONE    
" hi PMenuSbar       guifg=NONE              guibg=#848688
" hi Identifier      guifg=#BD9800           guibg=NONE    
" hi SpecialChar     guifg=#BD9800           guibg=NONE    
" hi Conditional     guifg=#BD9800           guibg=NONE    
" hi StorageClass    guifg=#536991           guibg=NONE    
" hi Todo            guifg=#F9F9FF           guibg=#BD9800 
" hi Special         guifg=#ffdf0d           guibg=NONE    
" hi LineNr          guifg=#68bdb2           guibg=#423b42 
" hi StatusLine      guifg=#192224           guibg=#BD9800 
" hi Label           guifg=#BD9800           guibg=NONE    
" hi PMenuSel        guifg=#192224           guibg=#BD9800 
" hi Search          guifg=#192224           guibg=#BD9800 
" hi Delimiter       guifg=#BD9800           guibg=NONE    
" hi Statement       guifg=#ffc619           guibg=NONE    
" hi SpellRare       guifg=#F9F9FF           guibg=#192224
" hi Comment         guifg=#538c9c           guibg=NONE    
" hi Character       guifg=#A1A6A8           guibg=NONE    
" hi Float           guifg=#A1A6A8           guibg=NONE    
" hi Number          guifg=#ffffff           guibg=NONE    
" hi Boolean         guifg=#A1A6A8           guibg=NONE    
" hi Operator        guifg=#BD9800           guibg=NONE    
" hi CursorLine      guifg=NONE              guibg=#222E30
" hi TabLineFill     guifg=#192224           guibg=#5E6C70 
" hi WarningMsg      guifg=#A1A6A8           guibg=#912C00 
" hi VisualNOS       guifg=#192224           guibg=#F9F9FF
" hi DiffDelete      guifg=NONE              guibg=#192224
" hi ModeMsg         guifg=#F9F9F9           guibg=#192224 
" hi CursorColumn    guifg=NONE              guibg=#222E30
" hi Define          guifg=#BD9800           guibg=NONE    
" hi Function        guifg=#f3f7a3           guibg=NONE    
" hi FoldColumn      guifg=#192224           guibg=#A1A6A8 
" hi PreProc         guifg=#eeff00           guibg=NONE    
" hi Visual          guifg=#192224           guibg=#F9F9FF 
" hi MoreMsg         guifg=#BD9800           guibg=NONE    
" hi SpellCap        guifg=#F9F9FF           guibg=#192224
" hi VertSplit       guifg=#192224           guibg=#5E6C70 
" hi Exception       guifg=#BD9800           guibg=NONE    
" hi Keyword         guifg=#BD9800           guibg=NONE    
" hi Type            guifg=#ff87f3           guibg=#30434d 
" hi DiffChange      guifg=NONE              guibg=#492224 
" hi Cursor          guifg=#192224           guibg=#F9F9F9 
" hi SpellLocal      guifg=#F9F9FF           guibg=#192224 
" hi Error           guifg=#A1A6A8           guibg=#912C00 
" hi PMenu           guifg=#192224           guibg=#5E6C70 
" hi SpecialKey      guifg=#5E6C70           guibg=NONE    
" hi Constant        guifg=#A1A6A8           guibg=NONE    
" hi Tag             guifg=#BD9800           guibg=NONE    
" hi String          guifg=#9ce3ff           guibg=NONE    
" hi PMenuThumb      guifg=NONE              guibg=#a4a6a8 
" hi MatchParen      guifg=#BD9800           guibg=NONE    
" hi Repeat          guifg=#BD9800           guibg=NONE    
" hi SpellBad        guifg=#F9F9FF           guibg=#192224
" hi Directory       guifg=#536991           guibg=NONE    
" hi Structure       guifg=#536991           guibg=NONE    
" hi Macro           guifg=#BD9800           guibg=NONE    
" hi Underlined      guifg=#F9F9FF           guibg=#192224
" hi DiffAdd         guifg=NONE              guibg=#193224 E
" hi TabLine         guifg=#192224           guibg=#5E6C70 
" hi cursorim        guifg=#192224           guibg=#536991 
