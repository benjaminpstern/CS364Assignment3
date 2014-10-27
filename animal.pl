/* CS364 AI
   Animal identification game.  
   start with ?- go.

   all verify predicates elicit answers from the user.
*/

:- [ask].

go :- hypothesize(Animal),
      write('I guess that the animal is: '),
      write(Animal),
      nl,
      clean.

/* hypotheses to be tested */
hypothesize(cheetah)   :- cheetah, !.
hypothesize(tiger)     :- tiger, !.
hypothesize(giraffe)   :- giraffe, !.
hypothesize(zebra)     :- zebra, !.
hypothesize(ostrich)   :- ostrich, !.
hypothesize(penguin)   :- penguin, !.
hypothesize(albatross) :- albatross, !.
hypothesize(unknown).             /* no diagnosis */

/* animal identification rules */
cheetah :- mammal, 
           carnivore, 
           verify(has_tawny_color, 'Does the animal have tawny color? '),
           verify(has_dark_spots, 'Does the animal have dark spots? ').
tiger :- mammal,  
         carnivore,
         verify(has_tawny_color, 'Does the animal have tawny color? '),
         verify(has_black_stripes, 'Does the animal have black stripes? ').
giraffe :- ungulate, 
	verify(has_long_neck, 'Does the animal have long neck? '),
	verify(has_long_legs, 'Does the animal have long legs? ').
zebra :- ungulate,  
	verify(has_black_stripes, 'Does the animal have black stripes? ').
ostrich :- bird,
           verify(does_not_fly, 'Is the animal unable to fly? '), 
           verify(has_long_neck, 'Does the animal have long neck? ').
penguin :- bird,
           verify(does_not_fly, 'Is the animal unable to fly? '), 	
           verify(swims, 'Does the animal swim? '),
           verify(is_black_and_white, 'Is the animal black and white? ').
albatross :- bird,
             verify(appears_in_story_Ancient_Mariner, 'Does the animal appear in the Rime of the Ancient Mariner? '),
             verify(flies_well, 'Can the animal fly well? ').

/* classification rules */

mammal    :- verify(has_hair, 'Does the animal have hair? '), !.
mammal    :- verify(gives_milk, 'Does the animal give milk? ').
bird      :- verify(has_feathers, 'Does the animal have feathers? '), !.
bird      :- verify(flies, 'Does the animal fly? '),
             verify(lays_eggs, 'Does the animal lay eggs? ').
carnivore :- verify(eats_meat, 'Does the animal eat meat? '), !.
carnivore :- verify(has_pointed_teeth, 'Does the animal have pointed teeth? '), 
             verify(has_claws, 'Does the animal have claws? '),
             verify(has_forward_eyes, 'Does the animal have forward eyes? ').
ungulate :- mammal, 
            verify(has_hooves, 'Does the animal have hooves? '), !.
ungulate :- mammal, 
            verify(chews_cud, 'Does the animal chew its cud? ').
