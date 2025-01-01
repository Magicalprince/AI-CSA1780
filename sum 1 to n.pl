% Base case: The sum of integers from 1 to 0 is 0.
sum_to_n(0, 0).

% Recursive case: The sum of integers from 1 to N is N + sum of integers from 1 to (N-1).
sum_to_n(N, Sum) :-
    N > 0,                        % Ensure N is positive.
    N1 is N - 1,                  % Calculate N-1.
    sum_to_n(N1, Sum1),           % Recursive call for N-1.
    Sum is N + Sum1.              % Add N to the sum of integers from 1 to N-1.
