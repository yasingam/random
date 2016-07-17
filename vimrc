"RUST SYNTAX HIGHLIGHTING
"follow instructions on: http://blog.awk.ninja/2015/08/rust-syntax-highlighting-in-vim.html
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'rust-lang/rust.vim'
call vundle#end()
filetype plugin indent on

"USER INTERFACE
"line numbers
set nu

"TRAILING WHITESPACE
"highlight trailing whitespace in red
match ErrorMsg '\s\+$'

"TABS AND SPACES
"set shiftwidth to 4 spaces for indent
set shiftwidth=4
"set tabstop to 4 spaces
set tabstop=4
"Tab is 4 spaces
set expandtab

"INDENTS
"automaticly indent to upper indent space
set autoindent
