% Facts: Defining family relationships
parent(john, mary).
parent(john, james).
parent(susan, mary).
parent(susan, james).
parent(mary, elizabeth).
parent(mary, charles).
parent(paul, elizabeth).
parent(paul, charles).

% Gender facts
male(john).
male(james).
male(charles).
male(paul).
female(susan).
female(mary).
female(elizabeth).

% Rules: Relationships

% Child relationship: X is a child of Y if Y is a parent of X.
child(X, Y) :- parent(Y, X).

% Sibling relationship: X and Y are siblings if they share the same parent.
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Brother relationship: X is a brother of Y if X is male and they are siblings.
brother(X, Y) :-
    sibling(X, Y),
    male(X).

% Sister relationship: X is a sister of Y if X is female and they are siblings.
sister(X, Y) :-
    sibling(X, Y),
    female(X).

% Grandparent relationship: X is a grandparent of Y if X is a parent of Z, and Z is a parent of Y.
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Grandchild relationship: X is a grandchild of Y if Y is a grandparent of X.
grandchild(X, Y) :- grandparent(Y, X).

% Aunt/Uncle relationship: X is an aunt/uncle of Y if X is a sibling of Y's parent.
aunt_or_uncle(X, Y) :-
    parent(Z, Y),
    sibling(X, Z).

% Cousin relationship: X and Y are cousins if their parents are siblings.
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).
