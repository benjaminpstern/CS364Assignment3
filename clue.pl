/* CS364 AI
   Simple Clue-based deduction system
*/

:- [ask].

/* top level:  invoke with ?- solve(X,Y,Z). */

solve(Who, Where, How) :- killed_in(Where), in_room(Who, Where), has(Who, How), clean, !.

/* facts */

person(mr_green).
person(miss_scarlett).
person(col_mustard).
person(mrs_white).
person(prof_plum).
person(mrs_peacock).

weapon(knife).
weapon(candlestick).
weapon(rope).
weapon(lead_pipe).
weapon(wrench).
weapon(revolver).

room(hall).
room(study).
room(lounge).
room(library).
room(billiard_room).
room(dining_room).
room(conservatory).
room(ballroom).
room(kitchen).

/* rules */

has(X, Z) :- in_room(X, Y), contains(Y, Z).
killed_in(X) :- body_found_in(X).
body_found_in(X) :- ask(body_found_in(X), 'Where was the body found? ', X).

/* "facts" that require answers from the user */

contains(X, Y) :- check(contains(X, Y), Z), !, Z == yes.
contains(X, Y) :- room(X), weapon(Y), verify(contains(X,Y), ['Does ', X, ' contain a ', Y, '? ']), !.

in_room(X, Y) :- check(in_room(X, Y), Z), !, Z == yes.
in_room(X, Y) :- person(X), room(Y), verify(in_room(X, Y), ['Is ', X, ' in ', Y, '? ']), !.
	 
