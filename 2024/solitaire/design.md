first gen: manually type card config  
later: CV card config from screenshot  
maybe ultimately, use python auto mouse movement, solve game

## engine
action = move card/stack from one slot to another
### data structure
how to rep card config?  
dragon, flower?  
use str?  
or use special num? -1?

stack, pop?  
but might want to manipulate whole stack  
need to see previous cards  
especially for some strategies

## strategy
- brute force search
- heuristics
- RL

when many free slots, many possibilities?  
eg break stack into two, move around, then recombine  
but these don't contribute  
brute force search need to ignore these (or maybe we have enough compute to handle that)  
or run program until enough slots freed, the rest of the game is solved manually?  
given how easy to lose in this game (no more slots), a lot of branches should terminate in brute force search

looks like auto collection: not when exceed min by 2? (except: 2 when min is 0)


### heuristics
goal: not just find out how to win, but find a simple strategy that always wins? = solving the game?

start by checking which dragons closest  
or, assemble longest stack

penalty, remove combinations that would have been illegal if not initialized as such

sometimes, do anti pattern  
eg 3 stacks, clear all alternatively, without clearing any dragons first  
but usually, if don't clear any dragon, lose

shuffle substacks between stacks

how many dragons need to be moved (depth) vs benefits

too many dragon types on top of stacks at the same time

9 to top left is poison

few steps look ahead? if worse, stop looking

although sometimes, brain, spots great patterns and do it
