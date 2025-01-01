% Define edges in the graph and their respective costs (heuristic values)
edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 8).
edge(c, e, 10).
edge(d, f, 6).
edge(e, f, 3).

% Define the heuristic function for nodes
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 5).
heuristic(d, 3).
heuristic(e, 7).
heuristic(f, 0).

% Best First Search algorithm
best_first_search(Start, Goal, Path, Cost) :-
    bfs([[Start, 0]], Goal, [], Path, Cost).

% Base case: If the current node is the goal, return the path and cost
bfs([[Goal, Cost]|_], Goal, Visited, Path, Cost) :-
    reverse([Goal|Visited], Path).

% Recursive case: Expand the current node
bfs([[Current, CurrentCost]|Rest], Goal, Visited, Path, Cost) :-
    findall([Next, NewCost],
            (edge(Current, Next, StepCost),
             \+ member(Next, Visited),  % Avoid revisiting nodes
             heuristic(Next, HCost),
             NewCost is CurrentCost + StepCost + HCost),
            Neighbors),
    append(Rest, Neighbors, UpdatedQueue),
    sort(2, @=<, UpdatedQueue, SortedQueue),  % Sort by cost
    bfs(SortedQueue, Goal, [Current|Visited], Path, Cost).
