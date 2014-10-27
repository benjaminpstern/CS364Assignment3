/* CS364 AI */
/* Ask and verify for use with deduction systems */

:- dynamic know/1.

list_codes([], "").

list_codes([Atom], Codes) :- atom_codes(Atom, Codes).

list_codes([Atom|ListTail], Codes) :-
        atom_codes(Atom, AtomCodes),
	append(AtomCodes, ListTailCodes, Codes),
	list_codes(ListTail, ListTailCodes).

list_string(List, String) :-
	ground(List),
	list_codes(List, Codes),
	atom_codes(String, Codes), !.

ask(P,X,Y) :- ground(X), know(P), !.
ask(P,X,Y) :- atom(X), !, write(X), read(Y), asserta(know(P)).
ask(P,X,Y) :- list_string(X,Z), ask(P,Z,Y).

verify(P, X) :- ask([P,Y], X, Y), (Y==yes; Y==y).

clean :- retractall(know(_)).

check(P) :- know(P).
check(P,X) :- know([P, Z]), ((Z==y ; Z==yes) -> X=yes ; X=no).
