% Facts
fact(sunny).
fact(warm).
fact(rainy).

% Rules
rule(umbrella, [rainy]).
rule(sunblock, [sunny, warm]).

% Backward Chaining Algorithm
backward_chaining(Goal) :-
    fact(Goal),  % If the goal is a fact, it is true
    write(Goal), write(' is true'), nl.
backward_chaining(Goal) :-
    rule(Goal, Conditions),  % Check if the goal can be derived from a rule
    write('Trying to prove: '), write(Goal), nl,
    prove_conditions(Conditions),  % Try to prove all conditions in the rule
    write(Goal), write(' is true'), nl.

% Prove conditions (recursive)
prove_conditions([]).  % Base case: No more conditions to prove
prove_conditions([Condition|Rest]) :-
    backward_chaining(Condition),  % Try to prove each condition
    prove_conditions(Rest).  % Recursively prove the remaining conditions

