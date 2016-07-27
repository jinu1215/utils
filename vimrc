colorschem torte                                                               
 
filetype on
 
syntax on
 
map <F7>    :cp<CR>
map <F8>    :cn<CR>
 
set autoindent
set autoread
set cursorcolumn
set cursorline
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=utf-8
set filetype=on
set hlsearch
set ignorecase
set nobackup
set nocompatible
set nocscopeverbose
set nolist
set number
set shiftwidth=4
set showcmd
set showmatch
set smartindent
set tabstop=4
set tags=/mnt/releases/dv/vim/tags
set textwidth=0
set wildmenu
set wrap
 
autocmd filetype python
    \ setlocal expandtab
 
highlight CursorColumn cterm=NONE ctermbg=darkgreen ctermfg=white guibg=darkgreen guifg=white
 
" for cscope search result
highlight ModeMsg ctermfg=green
 
if filereadable("/mnt/releases/dv/vim/cscope.out")
    cs add /mnt/releases/dv/vim/cscope.out
endif
 
" http://svn.python.org/projects/python/trunk/Misc/Vim/vimrc
source ~/.vimrc_python
au BufRead,BufNewFile *py,*pyw,*.c,*.h set tabstop=4
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h set textwidth=0
