CREATE DATABASE IF NOT EXISTS wwbm;
use wwbm;

insert into mainapp_questions(content) values 
	('Who was the first president of the united states?'),
    ('What does the acronym REM stand for?'),
    ('What disease is characterized by a body\'s inability to properly metabolize glucose?'),
    ('From what language does the term RSVP originate'),
    ('What animal is considered sacred in India'),
    ('Henry James famously remarked that \'the two most beautiful words in the English language\' are what?'),
    ('The inscription \'Pass and Stow,\' appears on which of these US landmarks?'),
    ('The \'Pua alohalo\' is Hawaii\'s official state what?'),
    ('What song\'s famous melody was written in 1893 by sisters Patty and Mildred Hill?'),
    ('Under President Ford, 34 year old Dick Cheney became the youngest man to hold what position?'),
    ('What extremely tall author once used the pen name John Lange, a German surnamed meaning \'long?\''),
    ('Born with the less cool-sounding name Walter, which of these actors prefers to go by his middle name?'),
    ('In Egyptian mythology, a criosphinx is a figure that has the body of a lion and the head of a what?'),
    ('The first X-ray photograph taken of the human body was an image of the hand of what scientist\'s wife?'),
    ('Aristotle wrote that what animal, though immune from other illnesses, is occasionally subject to \'flatulency\'?'),
    ('According to the Population Reference Bureau, about how many people have ever lived on earth?'),
    ('Which of these words meaning \'disaster\' is also the name of a straw-colored wine often used for chianti?'),
    ('Played at Wimbledon in 2010, the longest match in tennis history lasted how long?')
;


insert into mainapp_possibleanswers(content, questions_possible_answers_id) values
	('Abraham Lincoln,Benjamin Franklin,John Adams', 1),
    ('random energy module,red entertainment machine,really energetic music', 2),
    ('Influenza,Septicemia,Arthritis', 3),
    ('Russian,Italian,Portuguese', 4),
    ('Sheep,Chicken,Dog', 5),
    ('Complete silence,Outdoor cafe,Babbling brook', 6),
    ('Plymouth Rock,Lincoln Memorial,Statue of Liberty', 7),
    ('Bird,Fish,Gem', 8),
    ('Row Row Row Your Boat,Don\'t Stop Till You Get Enough,Jingle Bells', 9),
    ('Attorney General,National Security Advisor,Secretary of State', 10),
    ('Robert Ludlum,Stephen King,John Irving', 11),
    ('Harrison Ford,Matt Damon,Nicholas Cage', 12),
    ('Hawk,Horse,Dog', 13),
    ('Hans Geiger,Enrico Fermi,Niehls Bohr', 14),
    ('Dog,Lion,Goat', 15),
    ('5 trillion,1 trillion,50 billion', 16),
    ('Scourge,Calamity,Debacle', 17),
    ('6 hrs 11 min,8 hrs 24 min,3 hours 42 min', 18)
;

insert into mainapp_answers(content, which_questions_answer_id) values 
	('George Washington', 1),
	('rapid eye movement', 2),
	('Diabetes', 3),
	('French', 4),
	('Cow', 5),
    ('Summer Afternoon', 6),
    ('Liberty Bell', 7),
    ('Flower', 8),
    ('Happy Birthday to You', 9),
    ('White House Chief of Staff', 10),
    ('Michael Crichton', 11),
    ('Bruce Willis', 12),
    ('Ram', 13),
    ('Wilhem Roentgen', 14),
    ('Elephant', 15),
    ('100 Billion', 16),
    ('Fiasco', 17),
    ('11 hrs 5 min', 18)
;

