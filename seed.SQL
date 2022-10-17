DROP DATABASE IF EXISTS thyme2eat;
CREATE DATABASE thyme2eat;

\c thyme2eat

DROP TABLE IF EXISTS jokes;
CREATE TABLE jokes 
(
  id SERIAL PRIMARY KEY, 
  "[text]" VARCHAR(255) NOT NULL
);

INSERT INTO jokes ("[text]")
VALUES 
  ('Just burned 2,000 calories. Thats the last time I leave brownies in the oven while I nap'),
  ('Smoking will kill you. Bacon will kill. But, smoking bacon  will cure it'),
  ('I eat my tacos over a Tortilla. That way when stuff falls out, BOOM, another taco'),
  ('Why do the French eat snails? They dont like fast food'),
  ('One day youre the best thing since sliced brea. The next, youre toast'),
  ('Ive just written a song about tortillas...actually, its more of a wrap'),
  ('Justice is a dish best served cold because if it were served warm, it would be justwater'),
  ('For Halloween we dressed up as almonds. Everyone could tell we were nuts'),
  ('What happens if you eat yeast and shoe polish? Every morning you will rise and shine'),
  ('Why do seagulls fly over the sea? Because if they flew over the bay theyd be bagels'),
  ('Ive started telling everyone about the benefits of eating dried grapes. Its all about raisin awareness'),
  ('I always knock on the fridge before I open it. Just in case theres a salad dressing'),
  ('What do you call an academically successful slice of bread? An honor roll'),
  ('Ive become such a bad cook that Im able to use the smoke alarm as a timer'),
  ('I had a joke to tell about pizza, but everyone says its too cheezy');
