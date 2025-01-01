% Facts: Symptoms associated with diseases
symptom(cough, flu).
symptom(fever, flu).
symptom(sore_throat, flu).
symptom(fatigue, flu).

symptom(cough, cold).
symptom(runny_nose, cold).
symptom(sneezing, cold).
symptom(fatigue, cold).

symptom(cough, pneumonia).
symptom(difficulty_breathing, pneumonia).
symptom(fever, pneumonia).
symptom(chest_pain, pneumonia).

symptom(headache, migraine).
symptom(sensitivity_to_light, migraine).
symptom(nausea, migraine).

% Rules to diagnose diseases based on symptoms
diagnose(Disease) :-
    symptom(cough, Disease),
    symptom(fever, Disease),
    symptom(sore_throat, Disease),
    symptom(fatigue, Disease),
    !.  % Cut to prevent further unnecessary backtracking

diagnose(Disease) :-
    symptom(cough, Disease),
    symptom(runny_nose, Disease),
    symptom(sneezing, Disease),
    symptom(fatigue, Disease),
    !.

diagnose(Disease) :-
    symptom(cough, Disease),
    symptom(difficulty_breathing, Disease),
    symptom(fever, Disease),
    symptom(chest_pain, Disease),
    !.

diagnose(Disease) :-
    symptom(headache, Disease),
    symptom(sensitivity_to_light, Disease),
    symptom(nausea, Disease),
    !.

% If no disease matches, we return no diagnosis
diagnose(no_diagnosis).
