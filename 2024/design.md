first gen: manually type card config  
later: CV card config from screenshot

how to rep card config?  
dragon, flower?  
use str?  
or use special num? -1?

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
