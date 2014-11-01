/* CS364 AI
   Oberlin Building Identification Game.  
   start with ?- go.

   all verify predicates elicit answers from the user.
*/

:- [ask].

go :- hypothesize(Building),
      write('I guess that the building is: '),
      write(Building),
      nl,
      clean.

/* hypotheses to be tested */
hypothesize(north)          :- north, !.
hypothesize(east)           :- east, !.
hypothesize(burton)         :- burton, !.
hypothesize(asia_house)     :- asia_house, !.
hypothesize(spanish_house)  :- spanish_house, !.
hypothesize(french_house)   :- french_house, !.
hypothesize(king)           :- king, !.
hypothesize(science_center) :- science_center, !.
hypothesize(conservatory)   :- conservatory, !.
hypothesize(peters)         :- peters, !.
hypothesize(stevie)         :- stevie, !.
hypothesize(dascomb)        :- dascomb, !.
hypothesize(mudd)           :- mudd, !.
hypothesize(wilder)         :- wilder, !.
hypothesize(unknown).             /* no diagnosis */

/* animal identification rules */
north   :- dorm, 
           not(themed), 
           verify(has_large_lounge, 'Is there a large lounge with a high ceiling in this building? ').
east    :- dorm,  
           not(themed),
           verify(pot_smell, 'Do you smell pot? '),
           verify(e_shaped, 'Is the building E shaped? ').
burton  :- dorm,  
           not(themed),
           not(cafeteria),
           not(verify(pot_smell, 'Do you smell pot? ')),
           not(verify(has_large_lounge, 'Is there a large lounge with a high ceiling in this building? ')).
asia_house :- dorm,  
              themed,
              verify(has_large_lounge, 'Is there a large lounge with a high ceiling in this building? ').
spanish_house :- dorm,  
                 themed,
                 verify(spanish, 'Are there a lot of people speaking Spanish? ').
french_house  :- dorm,  
                 themed,
                 verify(french, 'Are there a lot of people speaking French? ').
king          :- not(dorm),  
                 classroom,
                 not(con),
                 not(cafeteria),
                 verify(has_three_floors, 'Are there three floors in this building? ').
science_center   :- not(dorm),  
                    classroom,
                    not(con),
                    cafeteria,
                    verify(has_big_atrium, 'Is there a large windowed atrium in this building? ').
conservatory     :- classroom,
                    con.
peters        :- not(dorm),  
                 classroom,
                 not(con),
                 not(cafeteria),
                 verify(has_spire, 'Is there a large spire on this building? ').
stevie        :- not(dorm),  
                 not(classroom),
                 cafeteria,
                 verify(has_glass_ceiling, 'Does this building have glass ceilings in places? ').
dascomb       :- dorm,  
                 not(classroom),
                 not(con),
                 cafeteria,
                 verify(freshman, 'Do exclusively freshmen live here? ').
mudd          :- not(dorm),  
                 not(classroom),
                 cafeteria,
                 verify(has_womb_chairs, 'Are there womb chairs in this building? ').
wilder        :- not(dorm),  
                 classroom,
                 not(con),
                 cafeteria,
                 verify(has_theater, 'Is there a theater in this building? ').


/* classification rules */

dorm      :- verify(is_dorm, 'Do people live here? ').
classroom :- verify(has_classes, 'Do classes happen here? ').
cafeteria :- verify(has_food, 'Can you get food here? ').
themed    :- verify(theme_house, 'Are you in a theme house? ').
con       :- verify(in_con, 'Is music being played everywhere? ').
