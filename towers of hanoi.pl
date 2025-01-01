% Base case: Moving 0 disks requires no moves.
hanoi(0, _, _, _, []).

% Recursive case: Move N disks from Source to Destination using Auxiliary.
hanoi(N, Source, Auxiliary, Destination, Moves) :-
    N > 0, 
    M is N - 1,                           % Calculate the number of disks to move (N-1).
    hanoi(M, Source, Destination, Auxiliary, Moves1), % Move N-1 disks to Auxiliary.
    Moves2 = [move(Source, Destination)], % Move the largest disk to Destination.
    hanoi(M, Auxiliary, Source, Destination, Moves3), % Move N-1 disks from Auxiliary to Destination.
    append(Moves1, Moves2, TempMoves),    % Combine the first set of moves and the current move.
    append(TempMoves, Moves3, Moves).     % Combine with the final set of moves.
