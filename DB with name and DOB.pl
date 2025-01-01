% Facts: Define the database with names and DOBs.
person('John Doe', '1990-01-15').
person('Jane Smith', '1985-07-23').
person('Alice Johnson', '2000-11-05').
person('Robert Brown', '1995-03-30').

% Rule: Find the DOB of a person by their name.
find_dob(Name, DOB) :-
    person(Name, DOB).

