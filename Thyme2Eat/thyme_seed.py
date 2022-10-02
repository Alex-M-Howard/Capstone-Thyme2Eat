from .db import db

from .models.joke_model import Joke

def seed():
  j1 = Joke(text="Just burned 2,000 calories. That's the last time I leave brownies in the oven while I nap")
  j2 = Joke(text="Smoking will kill you. Bacon will kill. But, smoking bacon  will cure it")
  j3 = Joke(text="I eat my tacos over a Tortilla. That way when stuff falls out, BOOM, another taco")
  j4 = Joke(text="Why do the French eat snails? They don't like fast food")
  j5 = Joke(text="One day you're the best thing since sliced bread. The next, you're toast")
  j6 = Joke(text="I've just written a song about tortillas...actually, it's more of a wrap")
  j7 = Joke(text="Justice is a dish best served cold because if it were served warm, it would be justwater")
  j8 = Joke(text="For Halloween we dressed up as almonds. Everyone could tell we were nuts")
  j9 = Joke(text="What happens if you eat yeast and shoe polish? Every morning you will rise and shine")
  j10 = Joke(text="Why do seagulls fly over the sea? Because if they flew over the bay they'd be bagels")
  j11 = Joke(text="I've started telling everyone about the benefits of eating dried grapes. It's all about raisin awareness")
  j12 = Joke(text="I always knock on the fridge before I open it. Just in case there's a salad dressing")
  j13 = Joke(text="What do you call an academically successful slice of bread? An honor roll")
  j14 = Joke(text="I've become such a bad cook that I'm able to use the smoke alarm as a timer")
  j15 = Joke(text="I had a joke to tell about pizza, but everyone says it's too cheezy")


  db.session.add_all([j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15])
  db.session.commit()