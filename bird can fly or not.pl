% Facts defining types of birds.
bird(sparrow).
bird(penguin).
bird(ostrich).
bird(eagle).
bird(parrot).

% Facts defining flight ability of birds.
cannot_fly(penguin).
cannot_fly(ostrich).

% Rule to determine if a bird can fly.
can_fly(Bird) :-
    bird(Bird),          % Ensure it is a bird.
    \+ cannot_fly(Bird). % Check that it is not in the list of non-flying birds.

% Query examples to check if a bird can fly.
% ?- can_fly(sparrow).  % Output: true.
% ?- can_fly(penguin).  % Output: false.
% ?- can_fly(eagle).    % Output: true.
% ?- can_fly(ostrich).  % Output: false.
% ?- can_fly(parrot).   % Output: true.
