# Decision_Making_Ad_fontes
This code provide the optimal solution of the problem of uncertanity, while choosing different values. 
Problem setting and possible strategies

We have known number N of items is to be presented to an observer one by one in random order, all possible orderings being equally likely. The observer is able at any time to rank without ties the items that have so far been presented in order of desirability. As each item is presented he must accept it, in which case the process stops,  or reject, in that case the next item in the sequence is presented and the observer faces the same dilemma as before. If the last item is reached it must be accepted. The observer aim is to find the best of the N items available by employing a strategy with as high a probability of success as possible. This problem is very familiar to the Secretary Problem. This problem demonstrates a scenario involving optimal stopping strategy. 

The observer must either accept or reject current item that is presented, he can’t go back and choose an already-presented item that turns out to be the best. The problem is to find the best item among N presented. An observer has to balance the risk of stopping too soon and accepting an apparently desirable item, when even better item than a current one is to be presented in future. So all possible strategies range between two equally likely extremes that continue the worst choices an observer can make. An observer is able to pick the first item, or, eventually, pick the last one. The probability of picking an item with maximum value is 1 / N which is very small as N is large. But there is some chances for an observer to increase the probability of selecting the best item.

Derivation of the formula for success probability of Sn

Let us define the following N - 2 non trivial Sn strategies:
The observer lets n items pass, , ranks them in order of desirability, and then among the next items selects the first one found with a higher rank. 
Among all possible strategies Sn, the observer wants to select and employ one with the maximum probability of success. 
We can apply brute-force method of finding the optimal strategy, but for large N we have too many different permutation (when N = 10, we have over 1 million orderings!). 
The    is a winning strategy if:
the best item is a candidate for selection, and
the ranks of the items, if any, preceding the best, do not exceed those of the first n items
	
This two conditions give us a general expression for the probability of success of Sn which is Pn(Sn)
Ek - the event that the best item is at some position k. Since all ordering are equally likely, then by condition a 

Fk - event describing the condition b. which means that the highest rank of first k - 1 terms appears  in the first n terms, so


Then Sn is a winning strategy of both conditions are satisfied.
