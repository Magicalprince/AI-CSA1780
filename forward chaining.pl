% Facts
fact(sunny).
fact(warm).

% Rules
rule(umbrella, [rainy]).
rule(sunblock, [sunny, warm]).

% Forward Chaining Algorithm
forward_chaining([Fact|Rest], [Fact|NewFacts]) :-
    fact(Fact), 
    forward_chaining(Rest, NewFacts).
forward_chaining([Fact|Rest], NewFacts) :-
    \+ fact(Fact),  % Fact does not exist in knowledge base yet
    forward_chaining(Rest, NewFacts).
forward_chaining([], []).

% Deduce rules based on facts
apply_rules([], []).
apply_rules([Fact|Facts], [Conclusion|Conclusions]) :-
    rule(Conclusion, FactsRequired),  % Apply rule if all required facts are present
    all_facts_present(FactsRequired),
    assert(fact(Conclusion)),
    apply_rules(Facts, Conclusions).
apply_rules([Fact|Facts], Conclusions) :-
    apply_rules(Facts, Conclusions).

% Helper predicate to check if all facts in a list are present in the knowledge base
all_facts_present([]).
all_facts_present([Fact|Facts]) :-
    fact(Fact),
    all_facts_present(Facts).

% Main query to run forward chaining and apply all rules
run_forward_chaining :-
    forward_chaining([sunny, warm, rainy], NewFacts),
    apply_rules(NewFacts, Conclusions),
    write('Derived Facts: '), write(Conclusions).
