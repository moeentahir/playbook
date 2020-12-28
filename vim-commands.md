zz - move line at the cursor to the middle of the screen
zt - move line at the cursor to the top of the screen

ZZ - save and quite
ZQ - quit without saving

## Movements
$ - move to the end of line
^,0 - move to the start of line
{ - move a paragraph
w - move word
3w - move 3 words
G - move to the end of file
gg - move to the firest line
25G - move to 25th line



## Insert mode
i - Go to insert mode at where cursor is
I - Insert at the beginning of the line
a - Insert after the cursor
A - Insert at the end of line
o - Insert from next line
O - insert from previous line

## Screen movements
Ctrl F - Forward full screen 
Ctrl B - Backward full screen

zz - move line at the cursor to the middle of the screen
zt - move line at the cursor to the top of the screen

Ctrl D - half screen down
Ctrl U - half screen up

zz - move line at the cursor to the middle of the screen
zt - move line at the cursor to the top of the screen
zb - move line at the cursor to the bottom  of the screen
T - move cursor to the top of the screen
M - move cursor to the middle of the screen
B - move cursor to the bottom of the screen

## Delete commands
dw - delete w word
d$ | D - delete to the end of line
d0 - delete to the start of line
de - delete to the end of word
d{ - delete the whole paragraph
daw - delete around word (including white spaces)
diw - delete inner word (do not delete spaces around the word)
dap - delete aroud paragraph (including whitespace)
dip - delete inner paragraph (don't delete spaces around paragraph)
5dap - delete 5 paragraphs
di( - delete iniside parantheses (excluding the parantheses)
da( - delete around parantheses (including the parantheses)
di" - delete inside the quotes ( MAGIC: You dont' even have to be inside the
quotes)
## Command mode
:earlier 5m - restore to how file was 5 minutes ago
:later 15m - come back in time

## Undo / redo
u - undo
U - undo all changes in on a line
Ctrl r - redo

## Search
/ - search for the pattern forwards
? - search backwords
n - move to the next occurance
N - move to the previous occurance
% - find the matching parentheses (if you put cursor on either starting or ending of parentheses)
:s/old/new/g - replace old with new in the current line
:%s/old/new/g - replace old with new in the whole file
:%s/old/new/gc - replace old with new and prompt before replacing

## Visual mode something here
v - enter in visual mode
V - select entire line
vap - select entire paragraph
Ctrl v - block selection
:norm . - run previous command in visual mode

## Spell check
:setlocal spell! spelllang=en_us
:set nospell - disable spell check for some of the files
z= - get list of suggestions
[s - move to next spell error
zw - add to dictionary

## Copy and paste
yy - copy line
yip - copy from inside paragraph
yap - copy around paragraph
