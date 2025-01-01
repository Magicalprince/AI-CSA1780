% Facts: Define the database of planets.
planet('Mercury', small, 57.9, no).
planet('Venus', medium, 108.2, no).
planet('Earth', medium, 149.6, no).
planet('Mars', small, 227.9, no).
planet('Jupiter', large, 778.3, yes).
planet('Saturn', large, 1427, yes).
planet('Uranus', large, 2871, yes).
planet('Neptune', large, 4495, yes).

% Rule: Find planets based on size.
find_by_size(Size, Name) :-
    planet(Name, Size, _, _).

% Rule: Find planets with rings.
planets_with_rings(Name) :-
    planet(Name, _, _, yes).

% Rule: Find planets within a certain distance from the Sun.
planets_within_distance(Distance, Name) :-
    planet(Name, _, Dist, _),
    Dist =< Distance.

% Rule: Find details of a planet.
planet_details(Name, Size, Distance, HasRings) :-
    planet(Name, Size, Distance, HasRings).
