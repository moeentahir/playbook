
ZZ - save and quite 
ZQ - quit without saving 

## Movements 
$ - move to the end of line 
^,0 - move to the start of line 
{ - move a paragraph 
w - move word 
3w - move 3 words 
G - move to the end of file 
gg - move to the first line 
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
Ctrl D - half screen down 
Ctrl U - half screen up 
Ctrl E - scroll down line by line 
Ctrl Y - scroll up line by line 
zt - move line at the cursor to the top of the screen 
zz - move line at the cursor to the middle of the screen 
zb - move line at the cursor to the bottom  of the screen 
H - move cursor to the top of the screen 
M - move cursor to the middle of the screen 
L - move cursor to the bottom of the screen 
 
## Delete commands 
dw - delete w word 
d$ | D - delete to the end of line 
d0 - delete to the start of line 
de - delete to the end of word 
d{ - delete the whole paragraph 
daw - delete around word (including white spaces) 
diw - delete inner word (do not delete spaces around the word) 
dap - delete around paragraph (including white space) 
dip - delete inner paragraph (don't delete spaces around paragraph) 
5dap - delete 5 paragraphs 
di( - delete inside parentheses (excluding the parentheses) 
da( - delete around parentheses (including the parentheses) 
di" - delete inside the quotes ( MAGIC: You don't' even have to be inside the 
d/find-something - delete until you find something 
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
? - search backwards 
n - move to the next occurrence 
N - move to the previous occurrence 
% - find the matching parentheses (if you put cursor on either starting or ending of parentheses) 
:s/old/new/g - replace old with new in the current line 
:%s/old/new/g - replace old with new in the whole file 
:%s/old/new/gc - replace old with new and prompt before replacing 
 
## Visual mode something here 
v - enter in visual mode 
V - enter in visual mode and select entire line;q 
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
ap - copy around paragraph 
 
## Casing 
 ~    : changes the case of current character  
 guu  : Change current line from upper to lower.  
 gUU  : Change current LINE from lower to upper.  
 guw  : Change to end of current WORD from upper to lower.  
 guaw : Change all of current WORD to lower.  
 gUw  : Change to end of current WORD from lower to upper.  
 gUaw : Change all of current WORD to upper.  
 g~~  : Invert case to entire line  
 g~w  : Invert case to current WORD  
 guG : Change to lower-case until the end of document. 
 
## Buffer 
:bd > buffer delete 
 
## File manipulation 
:wq ~/dev/newfile.txt  

## G Command
:g/^$/d > delete all white lines

## Widnow and buffer management
:qa   - Clos all windows
