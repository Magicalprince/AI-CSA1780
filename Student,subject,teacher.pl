% Facts: Define the relationships between students, teachers, subjects, and subject codes.
teaches('Mr. Smith', 'Mathematics', 'MATH101').
teaches('Ms. Johnson', 'Physics', 'PHYS201').
teaches('Dr. Brown', 'Chemistry', 'CHEM301').
teaches('Mrs. Taylor', 'Biology', 'BIOL401').

enrolled('Alice', 'MATH101').
enrolled('Bob', 'PHYS201').
enrolled('Charlie', 'CHEM301').
enrolled('Diana', 'BIOL401').
enrolled('Alice', 'PHYS201').
enrolled('Bob', 'MATH101').

% Rule: Find the teacher for a student and subject.
student_teacher(Student, Teacher) :-
    enrolled(Student, SubCode),           % Check which subject code the student is enrolled in.
    teaches(Teacher, _, SubCode).         % Find the teacher associated with that subject code.

% Rule: Find the subject a student is studying.
student_subject(Student, Subject) :-
    enrolled(Student, SubCode),           % Check which subject code the student is enrolled in.
    teaches(_, Subject, SubCode).         % Find the subject associated with that subject code.

% Rule: Find the subject code for a student and subject.
student_subject_code(Student, Subject, SubCode) :-
    enrolled(Student, SubCode),           % Check which subject code the student is enrolled in.
    teaches(_, Subject, SubCode).         % Confirm the subject matches the code.
