% Define the initial state
initial_state(state(at_door, on_floor, has_no_banana)).

% Define the goal state
goal_state(state(_, _, has_banana)).

% Actions and their resulting states
move(state(at_door, on_floor, has_no_banana), walk_to_banana, state(under_banana, on_floor, has_no_banana)).
move(state(under_banana, on_floor, has_no_banana), climb_box, state(under_banana, on_box, has_no_banana)).
move(state(under_banana, on_box, has_no_banana), grab_banana, state(under_banana, on_box, has_banana)).

% Define the path from initial state to goal state
solve(State, []) :- goal_state(State).  % Base case: Goal state reached
solve(State, [Action|Actions]) :-
    move(State, Action, NextState),  % Perform an action
    solve(NextState, Actions).       % Recursively solve from the next state



