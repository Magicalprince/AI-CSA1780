% Facts: Disease and recommended diets
diet(diabetes, [vegetables, whole_grains, lean_protein, nuts, seeds]).
diet(hypertension, [low_salt, fruits, vegetables, whole_grains, lean_meat]).
diet(anemia, [iron_rich_foods, green_leafy_vegetables, beans, red_meat]).
diet(obesity, [low_calorie_foods, fruits, vegetables, lean_meat, whole_grains]).
diet(gout, [low_purine_foods, low_fat_dairy, fruits, vegetables]).
diet(heart_disease, [low_fat_foods, fruits, vegetables, whole_grains, fish_omega_3]).
diet(kidney_disease, [low_protein_foods, low_potassium_foods, controlled_sodium, fruits]).
diet(allergy, [hypoallergenic_foods, fruits, vegetables, gluten_free, dairy_free]).

% Rule: Suggest diet based on disease
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).

% Sample Queries:
% ?- suggest_diet(diabetes, Diet).
% ?- suggest_diet(anemia, Diet).
