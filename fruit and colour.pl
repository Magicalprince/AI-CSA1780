% Facts: Fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, green).
fruit_color(orange, orange).
fruit_color(cherry, red).
fruit_color(blueberry, blue).
fruit_color(lemon, yellow).

% Rule: Find fruits of a given color
find_fruits_by_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
