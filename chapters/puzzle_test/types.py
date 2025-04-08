import models.Input as Input

TYPES: list[Input.Type] = [
    Input.Type(
        type_name="Classification Type Questions",
        cases=[
            Input.Case(
                items=[
                    Input.Group(
                        parent_question="Directions : Read the following information and answer the question given based on it :<br><br>In a school, there were five teachers. A and B were teaching Hindi and English. C and B were teaching English and Geography. D and A were teaching Mathematics and Hindi. E and B were teaching History and French.",
                        questions=[
                            "Who among the teachers was teaching maximum number of subjects ?",
                            "Which of the following pairs was teaching both Geography and Hindi ?",
                            "More than two teachers were teaching which subject ?",
                            "D, B and A were teaching which of the following subjects ?",
                            "Who among the teachers was teaching less than two subjects ?",
                        ],
                        from_question=1,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question that follow :<br><br>Madhu and Shobha are good in Dramatics and Computer Science.<br>Anjali and Madhu are good in Computer Science and Physics.<br>Anjali, Poonam and Nisha are good in Physics and History.<br>Nisha and Anjali are good in Physics and Mathematics.<br>Poonam and Shobha are good in History and Dramatics.",
                        questions=[
                            "Who is good in Computer Science, History and Dramatics ?",
                            "Who is good in Physics, Dramatics and Computer Science ?",
                            "Who is good in Physics, History and Dramatics ?",
                            "Who is good in History, Physics, Computer Science and Mathematics ?",
                            "Who is good in Physics, History and Mathematics but not Computer Science ?",
                        ],
                        from_question=6,
                    ),
                    Input.IndividualQuestion(
                        question="Ravi is not wearing white and Ajay is not wearing blue. Ravi and Sohan wear different colours. Sachin alone wears red.<br>What is Sohan's colour, if all four of them are wearing different colours ?",
                        number=11,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information ans answer the question given below it :<ol type='i'><li>Kailash, Govind and Harinder are intelligent.</li><li>Kailash, Rajesh and Jitendra are hard-working.</li><li>Rajesh, Harinder and Jitendra are honest.</li><li>Kailash, Govind and Jitendra are ambitious.</li></ol>",
                        questions=[
                            "Which of the following persons is neither hard-working nor ambitious ?",
                            "Which of the following persons is neither honest nor hard-working but is ambitious ?",
                        ],
                        from_question=12,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information and answer the question that follow :<br><br>Four youngmen Raj, Prem, Ved and Ashok are friendly with four girls Sushma, Kusum, Vimla and Poonam. Sushma and Vimla are friends. Ved's girl friend does not like Sushma and Vimla. Kusum does not care for Ved. Prem's girl friend is friendly with Sushma. Sushma does not like Raj.",
                        questions=[
                            "Who is Raj's girl friend ?",
                            "With whom is Sushma friendly ?",
                            "Who is Poonam's boy friend ?",
                            "Who does not like Sushma and Vimla ?",
                        ],
                        from_question=14,
                    ),
                    Input.IndividualQuestion(
                        question="In a cricket season, India defeated Australia twice, West Indies defeated India twice, Australia defeated West Indies twice, India defeated New Zealand twice and West Indies defeated New Zealand twice. Which country has lost most number of times ?",
                        number=18,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information and answer the question given below it :<br><br>Six students A, B, C, D, E and F are sitting in the field. A and B are from Nehru House while the rest belong to Gandhi House. D and F are tall while the others are short. A, C and D are wearing glasses while the others are not.",
                        questions=[
                            "Which two students, who are not wearing glasses are short ?",
                            "Which short student of Gandhi House is not wearing glasses ?",
                            "Which tall student of Gandhi House is not wearing glasses ?",
                        ],
                        from_question=19,
                    ),
                    Input.IndividualQuestion(
                        question="Six students A, B, C, D, E and F are sitting in the field. A and B are from Delhi while the rest are from Bangalore. D and F are tall while others are short. A, C and D are girls while others are boys. Which is the tall girl from Bangalore ?",
                        number=22,
                    ),
                    Input.IndividualQuestion(
                        question="On a shelf are placed six volume side-by-side labelled A, B, C, D, E and F. B, C, E, F have green covers while others have yellow covers. A, D, B are new volumes while the rest are old volumes. A, C, B are law reports while the rest are medical extracts. Which two volumes are old medical extracts and have green covers ?",
                        number=23,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>There are six persons A, B, C, D, E and F in a school. Each of the teachers teaches two subjects, one compulsory subject and the other optional subject. D's optional subject was History while three others have it as compulsory subject. E and F have Physics as one of their subjects. F's compulsory subject is Mathematics which is an optional subject of both C and E. History and English are A's subjects but in terms of compulsory and optional subjects, they are just reverse to those of D's. Chemistry is an optional subject of only one of them. The only female teacher in the school has English as her compulsory subject.",
                        questions=[
                            "What is C's compulsory subject ?",
                            "Who is a female member in the group ?",
                            "Which of the following has same compulsory and optional subjects as those of F's ?'",
                            "Disregarding which if the compulsory and which is the optional subject, who has the same two subject combination as F ?",
                            "Which of the following groups has History as the compulsory subject ?",
                        ],
                        from_question=24,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question that follow :<ol type='i'><li>Jayant, Kamal, Namita, Asha and Tanmay are five members of a family.</li><li>They have their birth dates from January to May, each member in one of these months.</li><li>Each one likes one particular item for his/her birthday out of Bengali Sweets, Chocolates, Pastries, Ice Cream and Dry Fruits.</li><li>The one who likes Pastries is born in the month which is exactly middle in the months given.</li><li>Asha does not like Ice cream but brings Chocolates for Jayant in February.</li><li>Tanmay who is fond of Bengali sweets is born in the next month immediately after Namita.</li><li>Namita does not like Dry fruits or Ice cream.</li></ol>",
                        questions=[
                            "What is the choice of Asha ?",
                            "Which combination of month and item is true for Jayant?",
                            "What is the choice of Kamal ?",
                            "In which month was Kamal born ?",
                        ],
                        from_question=29,
                        modified=True,
                        # correct_option for 29 should be b not d
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question that follow :<ol type='i'><li>P, Q, R, S, T and U are six students procuring their Master's degree in six different subjects - English, History, Philosophy, Physics, Statistics and Mathematics.</li><li>Two of them stay in hostel, two stay as paying guest (PG) and the remaining two stay at their home.</li><li>R does not stay as PG and studies Philosophy.</li><li>The students studying Statistics and History do not stay as PG.</li><li>T studies Mathematics and S studies Physics.</li><li>U and S stay in hostel. T stays as PG and Q stays at home.</li></ol>",
                        questions=[
                            "Who studies English ?",
                            "Which of the following combinations of subject and place of stay is not correct ?",
                            "Which of the following pairs of students stay one each at hostel and at home ?",
                            "Which subject does Q study ?",
                            "Which of the following pairs of students stay at home ?",
                        ],
                        from_question=33,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information and answer the question given below it :<br><br>Rohit, Kunal, Ashish and John are students of a school. Three of them stay far from the school and one near it. Two study in class IV, one in class V and one in class VI. They study Hindi, Mathematics, Social Science and Science. One is good at all the four subjects while another is weak in all of these. Rohit stays far from the school and is good at Mathematics only while Kunal is weak in Mathematics only and stay close to the school. Neither of these two nor Ashish studies in class VI. One who is good at all the subjects studies in class V.",
                        questions=[
                            "Name the boy who is good at all the subjects.",
                            "Name the boy who is weak in all the subjects.",
                            "Which two boys are good at Hindi ?",
                            "Which two boys are good at Mathematics ?",
                            "Other than Rohit and the boy good at all the subjects, who else stays far from the school ?",
                        ],
                        from_question=38,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the given information carefully and answer the question that follow :<ol type='i'><li>There are six friends A, B, C, D, E and F.</li><li>Each one is proficient in on the of the games, namely Badminton, Volleyball, Cricket, Hockey, Tennis and Polo.</li><li>Each owns a different coloured car, namely yellow, green, black, white, blue and red.</li><li>D plays Polo and owns a yellow coloured car.</li><li>C does not play either Tennis or Hockey and owns neither blue nor yellow coloured car.</li><li>E owns a white car and plays Badminton.</li><li>B does not play Tennis, he owns a red coloured car.</li><li>A plays Cricket and owns a black car.</li></ol>",
                        questions=[
                            "Who plays Volleyball ?",
                            "Which coloured car F owns ?",
                            "Which of the following combinations of colour of car and game played is not correct ?",
                        ],
                        from_question=43,
                    ),
                    Input.IndividualQuestion(
                        question="In a group of six women, there are four dancers, four vocal musicians, one actress and three violinists. Girija and Vanaja are among the violinists while Jalaja and Shailaja do not know how to play on the violin. Shailaja and Tanuja are among the dancers. Jalaja, Vanaja, Shailja and Tanuja are all vocal musicians and two of them are also violinists. If Pooja is an actress, who among the following is both a dancer and a violonist ?",
                        number=46,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Seating/Placing Arrangements",
        cases=[
            Input.Case(
                items=[
                    Input.IndividualQuestion(
                        question="Four girls are sitting on a bench to be photographed. Shikha is to the left of Reena. Manju is to the right of Reena. Rita is between Reena and Manju. Who would be second from the left in the photograph ?",
                        number=1,
                        # correct_option should be a not d
                        modified=True,
                    ),
                    Input.IndividualQuestion(
                        question="There are five different houses, A to E, in a row. A is to the right of B and E is to the left of C and right of A. B is to the right of D. Which of the houses is in the middle ?",
                        number=2,
                    ),
                    Input.IndividualQuestion(
                        question="In a March Past, seven persons are standing in a row. Q is standing left to R but right to P. O is standing right to N and left to P. O is standing right to N and left to P. Similarly, S is standing right to R and left to T. Find out who is standing in the middle.",
                        number=3,
                    ),
                    Input.IndividualQuestion(
                        question="Five children are sitting in a row. S is sitting next to P but not T. K is sitting next to R who is sitting on the extreme left and T is not sitting next to K. Who are sitting adjacent to S ?",
                        number=4,
                    ),
                    Input.IndividualQuestion(
                        question="Five girls are sitting in a row. Rashi is not adjacent to Sulekha or Abha. Anuradha is not adjacent to Sulekha. Rashi is adjacent to Monika. Monika is at the middle in the row. The, Anuradha is adjacent to whom out of the following ?",
                        number=5,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<ol type='A'><li>There are five friends.</li><li>They are standing in a row facing South.</li><li>Jayesh is to the immediate right of Alok.</li><li>Pramod is between Bhagat and Subodh.</li><li>Subodh is between Jayesh and Pramod.</li></ol>",
                        questions=[
                            "Who is at the extreme left end ?",
                            "Who is in the middle ?",
                            "To find answers to the above two questions, which of the given staatements can be dispensed with ?",
                        ],
                        from_question=6,
                    ),
                    Input.IndividualQuestion(
                        question="Five persons A, B, C, D and E are sitting in a row facing you such that D is on the left of C and B is on the right of E. A is on the right of C and B is on the left of D. If E occupies a corner position, then who is sitting in the centre ?",
                        number=9,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the given information carefully and answer the question that follow :<ol type='i'><li>A, B, C, D, E, F and G are sitting on a wall and all of them are facing east.</li><li>C is on the immediate right of D.</li><li>B is at an extreme end and has E as his neighbour.</li><li>G is between E and F.</li><li>D is sitting third from the south end.</li></ol>",
                        questions=[
                            "Who is sitting to the right of E ?",
                            "Which of the following pairs of people are sitting at the extreme ends ?",
                            "Name the person who should change placed with C such that he gets the third place from the north end.",
                            "Immediately between which of the following pairs of people is D sitting ?",
                            "Which of the conditions (i) to (v) given above is not required to find out the place in which A is sitting ?",
                        ],
                        from_question=10,
                    ),
                    Input.IndividualQuestion(
                        question="In the Olympic Games, the flags of six nations were flown on the masts in the following way :<br>The flag of America was to the left of Indian tricolour and to the right of the flag of France. The flag of Australia was on the right of the Indian flag but was to the left of the flag of Japan, which was to the left of the flag of China. Find the two flags which are in the centre.",
                        number=15,
                    ),
                    Input.IndividualQuestion(
                        question="Mr. A, Miss B, Mr. C and Miss D are sitting around a table and discussing their trades.<ol><li>Mr. A sits opposite to cook.</li><li>Miss B sits right to the barber.</li><li>The washerman is on the left of the tailor.</li><li>Miss D sits opposite Mr. C.</li></ol>What are the trades of A and B ?",
                        number=16,
                    ),
                    Input.IndividualQuestion(
                        question="Sitting in a row in front of a camera, Mr. X is on the left of the person sitting in the centre but is on the right of Mr. Y. Mr. P. is on the right of Mr. Z and Mr. R is on the right of Mr. P. Mr. R is the second person from the person sitting in the centre. Who is the person sitting in the centre ?",
                        number=17,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the given information carefully and answer the question that follow :<ol type='i'><li>Eleven students, A, B, C, D, E, F, G, H, I, J and K are sitting in the first row of the class facing the teacher.</li><li>D who is the immediate left of F is second to the right of C.</li><li>A is second to the right of E, who is at one of the ends.</li><li>J is the immediate neighbour of A and B and third to the left of G.</li><li>H is to the immediate left of D and third to the right of I.</li></ol>",
                        questions=[
                            "Who is sitting in the middle of the row ?",
                            "Which of the following groups of friends is sitting to the right of G ?",
                            "Which of the following statements is true in context of the above sitting arrangements ?",
                            "In the above sitting arrangement, which of the following statements is superfluous ?",
                            "If E and D, C and B, A and H and K and F interchange their positions, which of the following pairs of students is sitting at the ends ?",
                        ],
                        from_question=18,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<ol type='i'><li>Eight persons, E, F, G, H, I, J, K and L are seated around a square table - two on each side.</li><li>There are three lady members and they are not seated next to each other.</li><li>J is between L and F.</li><li>G is between I and F.</li><li>H, a lady member, is second to the left of J.</li><li>F, a male member is seated opposite E, a lady member.</li><li>There is a lady member between F and I.</li></ol>",
                        questions=[
                            "Who among the following is seated to the left of J.",
                            "How many persons are seated between K and F ?",
                            "Who among the following are the three lady members ?",
                            "Who amon the following is to the immediate left of F ?",
                            "Which of the following is true about J ?",
                        ],
                        from_question=23,
                    ),
                    Input.Group(
                        parent_question="Directions : On the basis of the following information given below, answer the question.<ol type='i'><li>P, Q, R, S and T are sitting in a circle facing the centre.</li><li>R is immediate left of T.</li><li>P is between S and T.</li></ol>",
                        questions=[
                            "Who is to the immediate left of R ?",
                            "To find the answer to the above question, which of the following statements can be dispensed with ?",
                        ],
                        from_question=28,
                    ),
                    Input.IndividualQuestion(
                        question="Six friends A, B, C, D, E and F are sitting in a closed circle facing the centre. A is facing D. C is between A and B. F is between E and A. Who is to the immediate left of B ?",
                        number=30,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question that follow :<br><br>A, B, C, D, E and F are seated in a circle facing the centre. D is between F and B. A is second to the left of D and second to the right of E.",
                        questions=[
                            "Who is facing A ?",
                            "Who among the following is facing D ?",
                        ],
                        from_question=31,
                        # correct_option for 31 should be d not a
                        modified=True,
                    ),
                    Input.Group(
                        parent_question="Directions : On the basis of the information given below, answer question.<br><br>Eight friends A, B, C, D, E, F, G and H are sitting in a circle facing the centre. B is sitting between G and D. H is third to the left of B and second to the right of A. C is sitting between A and G and B and E are not sitting opposite to each other.",
                        questions=[
                            "Who is third to the left of D ?",
                            "Which of the following statements is not correct ?",
                        ],
                        from_question=33,
                    ),
                    Input.IndividualQuestion(
                        question="A group of eight members sit in a circle. D is between A and F and is opposite to G. E is to the right of A but on the left of C, whose right hand neighbour is G. B enjoys having H to his left and F to his right. Find the member who is diagonally opposite to A.",
                        number=35,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the given information carefully and answer the question that follow :<ol type='i'><li>There are seven books one each on Psychology, Hindi, English, Sociology, Economics, Education and Accountancy, lying on a table one above the other.</li><li>Sociology is on the top of all the books.</li><li>Accountancy is immediately below Education which is immediately below Sociology.</li><li>Economics is immediately above Psychology but not in the middle.</li><li>Hindi is immediately below Psychology.</li></ol>",
                        questions=[
                            "Economics is between which of the following books ?",
                            "Which three books are between Accountancy and Hindi ?",
                            "If Sociology and English, Accountancy and Hindi and Education and Psychology interchange their positions, which book will be between Psychology and Sociology ?",
                        ],
                        from_question=36,
                    ),
                    Input.IndividualQuestion(
                        question="In a shop, the items were arranged in a shelf consistin of six rows. Biscuits are arranged above the tins of chocolates but below the rows of packets of chips, cakes are at the bottom and the bottle of peppermints are below the chocolates. The topmost row had the display of jam bottles. Where exactly are the bottle of peppermints ? Mention the place from the top.",
                        number=39,
                    ),
                    Input.IndividualQuestion(
                        question="In a pile of reading material, there are novels, story-books, dramas and comics. Every novel has a drama next to it, every story-book has a comic next to it and there is no story-book next to a novel. If there be a novel at the top and the number of books be 40, the order of the books in the pile is :",
                        number=40,
                    ),
                    Input.Group(
                        parent_question="Directions : The following question is based on the information given below :<ol type='i'><li>Seven books are placed one above the other in a particular way.</li><li>History book is placed exactly above Civics book.</li><li>Geography book is fourth from the bottom and English book is fifth from the top.</li><li>There are two books in between Civics and Economics books.</li></ol>",
                        questions=[
                            "How many books are there between Civics and Science books ? To answer this question, which other extra information is required, if any, from the following ?",
                            "Out of the following, which three books are kept above English book ? To answer this question, which of the other information, if any, is required ?",
                        ],
                        from_question=41,
                    ),
                    Input.IndividualQuestion(
                        question="In a pile of 10 books, there are 3 of History, 3 of Hindi, 2 of Mathematics and 2 of English. Taking from the above, there is an English book between History and Mathematics book, a History book between Mathematics and an English book, a Hindi book between an English and a Mathematics book, a Mathematics book between two Hindi books and two Hindi books between a Mathematics and a History book. Book of which subject is at the sixth position from the top ?",
                        number=43,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>In a car exhibition seven cars of seven different companies viz. Cardilac, Ambassador, Fiat, Maruti, Mercedes, Bedford and Fargo were displayed in a row, facing east such that :<ol><li>Cardilac car was to the immediate right of Fargo.</li><li>Fargo was fourth to the right of Fiat.</li><li>Maruti car was between Ambassador and Bedford.</li><li>Fiat, which was third to the left of Ambassador car, was at one of the ends.</li></ol>",
                        questions=[
                            "Which of the following was the correct positions of the Mercedes ?",
                            "Which of the following is definitely true ?",
                            "Which cars are on the immediate either sides of the Cardilac car ?",
                            "Which of the following is definitely true ?",
                            "Which of the following groups of cars is to the right of the Ambassador car ?",
                        ],
                        from_question=44,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question given below it :<br><br>All the roads of a city are either perpendicular or parallel to one another. The roads are all straight. Roads A, B, C, D and E are parallel to one another. Roads G, H, I, J, K, L and M are parallel to one another.<ol type='i'><li>Road A is 1 km east of road B.</li><li>Road B is \\(\\frac{1}{2}\\) km west of road C.</li><li>Road D is 1 km west of road E.</li><li>Road G is \\(\\frac{1}{2}\\) km south of road H.</li><li>Road I is 1 km north of road J.</li><li>Road K is \\(\\frac{1}{2}\\) km north of road L.</li><li>Road K is 1 km south of road M.</li></ol>",
                        questions=[
                            "Which is necessarily true ?",
                            "If E is between B and C, which of the following is false ?",
                            "If road E is between B and C, then distance between A and D is :",
                            "Which of the following possibilities would make two road coincide ?",
                            "If K is parallel to I and K is \\(\\frac{1}{2}\\) km south of J and 1 km north of G, which two roads would be \\(\\frac{1}{2}\\) km apart ?",
                        ],
                        from_question=49,
                        # correct_option for 50 should be a not b
                        modified=True,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>Seven friends Kamla, Manish, Rohit, Amit, Gaurav, Pritam and Priya are sitting in a circle. Kamla, Manish, Rohit, Amit, Pritam and Priya are sitting at equal distances from each other.<br>Rohit is sitting two places right of Pritam, who is sitting one place right of Amit. Kamla forms an angle of 90 degrees from Gaurav and an angle of 120 degrees from Manish. Manish is just opposite Priya and is sitting on the left of Gaurav.",
                        questions=[
                            "Who is the only person sitting between Rohit and Manish ?",
                            "Gaurav is not sitting at equal distance from",
                            "Gaurav is sitting ................. of Priya.",
                            "The angle between Gaurav and Manish in the clockwise directions is",
                            "Which of the following statements is not correct ?",
                        ],
                        from_question=54,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Comparison Type Questions",
        cases=[
            Input.Case(
                items=[
                    Input.IndividualQuestion(
                        question="Compare the knowledge of persons X, Y, Z, A, B and C in relation to each other :<ol><li>X knows more than A.</li><li>Y knows as much as B.</li><li>Z knows less than C.</li><li>Z knows less than B</li><li>A knows more than Y.</li></ol>The best knowledgeable person amongst all is :",
                        number=1,
                        modified=True
                        # added point for Z < B from the explanation
                    ),
                    Input.IndividualQuestion(
                        question="Five children were administered psychological tests to know their intellectual levels. In the report, psychologists pointed out that the child A is less intelligent than child B. The child C is less intelligent than child D. The child B is less intelligent than the child C and child A is more intelligent than the child E. Which child is the most intelligent ?",
                        number=2,
                    ),
                    Input.IndividualQuestion(
                        question="Among the five boys, Vineet is taller than Manick, but not as tall as Ravi. Jacob is taller than Dilip but shorter than Manick. Who is the tallest in their group ?",
                        number=3,
                    ),
                    Input.IndividualQuestion(
                        question="If (i) P is taller than Q; (ii) R is shorter than P; (iii) S is taller than T but shorter than Q, then who among them is the tallest ?",
                        number=4,
                    ),
                    Input.IndividualQuestion(
                        question="Five boys participated in a competition. Rohit was ranked lower than Sanjay. Vikas was ranked higher than Dinesh. Kamal's rank was between Rohit and Vikas. Who was ranked highest.",
                        number=5,
                    ),
                    Input.IndividualQuestion(
                        question="In an examination, Raj got more marks than Mukesh but not as many as Priya. Priya got more marks than Gaurav and Kavita. Gaurav got less marks than Mukesh but his marks are not the lowest in the group. Who is second in the order of descending order of marks ?",
                        number=6,
                    ),
                    Input.IndividualQuestion(
                        question="Ashish is heavier than Govind. Mohit is lighter than Jack. Pawan is heavier than Jack but lighter than Govind. Who among them is the heaviest ?",
                        number=7,
                    ),
                    Input.IndividualQuestion(
                        question="Pune is bigger than Jhansi, Sitapur is bigger than Chittor. Raigarh is not as big as Jhansi, but is bigger than Sitapur. Which is the smallest ?",
                        number=8,
                    ),
                    Input.IndividualQuestion(
                        question="Rohan is taller than Anand but shorter than Seema. Krishna is taller than Pushpa but shorter than Anand. Dhiraj is taller than Krishna but shorter than Seema. Who among them is the tallest ?",
                        number=9,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<ol type='A'><li>Gopal is shorter than Ashok but taller than Kunal;</li><li>Navin is shorter than Kunal;</li><li>Jayesh is taller than Navin;</li><li>Ashok is taller than Jayesh.</li></ol>",
                        questions=[
                            "Who among them is the tallest",
                            "Which of the given information is not necessary to answer the above question ?",
                        ],
                        from_question=10,
                    ),
                    Input.IndividualQuestion(
                        question="B is twice as old as A but twice younger than F.<br>C is half the age of A but twice the age of D.<br>Which two person form the pair of oldest and youngest ?",
                        number=12,
                    ),
                    Input.IndividualQuestion(
                        question="Sudhanshu is as much older than Kokila as he is younger than Praveen. Nitin is as old as Kokila. Which of the following statements is wrong ?",
                        number=13,
                    ),
                    Input.IndividualQuestion(
                        question="A is elder to B while C and D are elder to E who lies between A and C. If C be elder to B, which one of the following statements is necessarily true ?",
                        number=14,
                    ),
                    Input.IndividualQuestion(
                        question="Hitesh is richer than Jaya whereas Mohan is richer than Pritam. Lalit is as rich as Jaya. Amit is richer than Hitesh. What conclusion can be definitely drawn from the above statements ?",
                        number=15,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information and answer the question given below it :<br><br>A black smith has five iron articles A, B, C, D and E, each having a different weight.<ol type='i'><li>A weighs twice as much as B.</li><li>B weighs four and a half times as much as C.</li><li>C weights half as much as D.</li><li>D weighs half as much as E.</li><li>E weighs less than A but more than C.</li></ol>",
                        questions=[
                            "Which of the following is the lightest in weight ?",
                            "E is lighter in weight that which of the other two articles ?",
                            "E is heavier than which of the following two articles ?",
                            "Which of the following articles is the heaviest in weight ?",
                            "Which of the following represents the descending order of weights of the articles ?",
                            "Which of the above given statements is not necessary to determine the correct order of articles according to their weights ?",
                        ],
                        from_question=16,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information and answer the question given below it :<ol type='i'><li>Seven students P, Q, R, S, T, U and V take a series of tests.</li><li>No two students get similar marks.</li><li>V always scores more than P.</li><li>P always scores more than Q.</li><li>Each time either R scores the highest and T gets the least, or alternatively S scores the highest and U or Q scores the least.</li></ol>",
                        questions=[
                            "If S is ranked sixth and Q is ranked fifth, which of the following can be true ?",
                            "If R gets most, V should be ranked not lower than :",
                            "If R is ranked second and Q is ranked fifth, which of the following must be true ?",
                            "If S is ranked second, which of the following can be true ?",
                            "If V is ranked fifth, which of the following must be true ?",
                        ],
                        from_question=22,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the information given below and answer the quetsion that follows :<ol type='i'><li>A, B, C, D, E and F are six students in a class.</li><li>B and C are shorter than F but heavier than A.</li><li>D is heavier than B and taller than C.</li><li>E is shorter than D but taller than F.</li><li>F is heavier than D.</li><li>A is shorter than E but taller than F.</li></ol>",
                        questions=[
                            "Who among them is the tallest ?",
                            "Who is the third from the top when they are arranged in descending order of height ?",
                            "Which of the following groups of friends is shorter than A ?",
                            "Who among them is the lightest ?",
                            "Which of the following statements is true for F as regards height and weight ?",
                        ],
                        from_question=27,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<ol type='i'><li>A, B, C, D and E are five friends.</li><li>B is elder to E, but not as tall as C.</li><li>C is younger to A, and is taller to D and E.</li><li>A is taller to D, but younger to E.</li><li>D is elder to A but is shortest in the group.</li></ol>",
                        questions=[
                            "Who among the following is the eldest ?",
                            "Which of the following pairs of students is elder to D ?",
                            "Which of the following statements is correct about B ?",
                            "If F, another friend, is taller than C, how many of them will be between F and E according to their height ?",
                            "If a selection is to be made among them who would be relatively older and also taller, who among them should be chosen ?",
                        ],
                        from_question=32,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the given information carefully and answer the question that follows :<ol type='i'><li>Six friends P, Q, R, S, T and U are members of a club and play a different game of Football, Cricket, Tennis, Basketball, Badminton and Volleyball.</li><li>T who is taller than P and S plays Tennis.</li><li>The tallest among them plays Basketball.</li><li>The shortest among them plays Volleyball.</li><li>Q and S neither play Volleyball nor Basketball.</li><li>R plays Volleyball.</li><li>T is between Q who plays Football and P in order of height.</li></ol>",
                        questions=[
                            "Who among them is taller than R but shorter than P ?",
                            "Who will be at the third place if they are arranged in the descending order of their height ?",
                            "Which of the following statements is not true ?",
                            "Who among them plays Basketball ?",
                            "What does S play ?",
                        ],
                        from_question=37,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>At the end of a cricket series, when five players were arranged in the ascending order of runs scored by them, O was fourth while N was first. When they were arranged in descending order for wickets taken by them, K replaces O while O replaces L. M's position remains unchanged. K has scored more runs than M. L is having first rank in one ranking and fifth in another.",
                        questions=[
                            "Who has scored the highest runs in the series ?",
                            "Who has taken the lowest number of wickets ?",
                        ],
                        from_question=42,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the information given below and answer the question that follows :<br><br>A * B means A and B are of the same age;<br>A - B means B is younger than A;<br>A + B means A is younger than B.",
                        questions=[
                            "Sachin * Madan - Reena means",
                            "X + Y + Z is same as",
                            "For an expression Farha - Farida - Arif, which of the following cannot be correct under any circumstances ?",
                            "Deven - Shashi * Hemant is opposite to",
                        ],
                        from_question=44,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Sequential Order of Things",
        cases=[
            Input.Case(
                items=[
                    Input.IndividualQuestion(
                        question="Five boys took part in a race. Raj finished before Mohit but behind Gaurav. Ashish finished before Sanchit but behind Mohit. Who won the race ?",
                        number=1,
                    ),
                    Input.Group(
                        parent_question="Five men A, B, C, D and E read a newspaper. The one who reads first gives it to C. The one who reads last had taken from A. E was not the first or last to read. There were two readers between B and A.",
                        questions=[
                            "B passed the newspaper to whom ?",
                            "Who read the newspaper last ?",
                        ],
                        from_question=2,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question based on it.<br><br>Seven executives P, Q, R, S, T, U and W reach office in a particular sequence. U reaches immediately before P but does not immediately follow S. R is the last to reach office. T follows immediately after P and is subsequently followed by W.",
                        questions=[
                            "Among the executives, who reaches the office first ?",
                            "Who ranks fourth in the sequence of reaching office ?",
                        ],
                        from_question=4,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question that follows :<br><br>Six lectures A, B, C, D, E and F are to be organised in a span of seven days - from Sunday to Saturday, only one lecture on each day in accordance with the following :<ol type='i'><li>A should not be organised on Thursday.</li><li>C should be organised immediately after F.</li><li>There should be a gap of two days between E and D.</li><li>One day there will be no lecture (Friday is not that day), just before that day D will be organised.</li><li>B should be organised on Tuesday and should not be followed by D.</li></ol>",
                        questions=[
                            "On which day there is no lecture ?",
                            "How many lectures are organised between C and D ?",
                            "Which day will the lecture F be organised ?",
                            "Which of the following is the last lecture in the series ?",
                            "Which of the following information is not required in finding the complete sequence of organisation of lectures ?",
                        ],
                        from_question=6,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information to answer the given question :<br><br>The Director of the Institute has announced that six guest lectures on different areas like Leadership, Decision Making, Quality Circles, Motivation, Assessment Centre and Group Discussion are to be organised only one on each day from Monday to Sunday.<ol type='i'><li>Motivation should be organised immediately after Assessment Centre.</li><li>Quality Circle should be organised on Wednesday and should not be followed by Group Discussion.</li><li>Decision Making should be organised on Friday and there should be a gap of two days between Leadership and Group Discussion.</li><li>One day there will be no lecture (Saturday is not that day), just before that day Group Discussion will be organised.</li></ol>",
                        questions=[
                            "Which of the pairs of lectures were organised on first and last day ?",
                            "How many lectures are organised between Motivation and Quality Circle ?",
                            "Which day will the lecture on Leadership be organised ?",
                            "On which day there is no lecture ?",
                            "Which of the following information is not required for the above lecture arrangements ?",
                        ],
                        from_question=11,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information and answer the question given below it :<br><br>A training college has to conduct a refresher course for teachers of seven different subjects - Mechanics, Psychology, Philosophy, Sociology, Economics, Science and Engineering from 22nd July to 29th July.<ol type='i'><li>Course should start with Psychology.</li><li>23rd July, being Sunday, should be a holiday.</li><li>Science subject should be on the previous day of the Engineering subject.</li><li>Course should end with Mechanics subject.</li><li>Philosophy should be immediately after the holiday.</li><li>There should be a gap of one day between Economics and Engineering.</li></ol>",
                        questions=[
                            "The refresher course will start with which one of the following subjects ?",
                            "Which subject will be on Tuesday ?",
                            "Which subjects precedes Mechanics ?",
                            "How many days' gap is there between Science and Philosophy ?",
                            "Which subject is followed by Science ?",
                        ],
                        from_question=16,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question that follows :<br><br>Five plays A, B, C, D and E are to be staged from Monday to Friday of a week. On each day, only one play will be staged. D or E should not be either the first or last to be staged. E should be immediately followed by C. B should be staged immediately after D. One play is staged between A and B.",
                        questions=[
                            "Which is the first play to be staged ?",
                            "Which of the following is the correct sequence of staging all the plays ?",
                            "Which play was staged on Wednesday ?",
                        ],
                        from_question=21,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question given below it :<br></br>A sales representative plans to visit each of six companies M, N, P, Q, R and S exactly once during the course of one day. She is setting up her schedule for the day according to the following conditions :<ol type='i'><li>She must visit M before N and R.</li><li>She must visit N before Q.</li><li>The third company she visits must by P.</li></ol>",
                        questions=[
                            "Which of the following must be true of the sales representative's schedule ?",
                            "If the sales representative visits S first, which company must she visit second ?",
                            "The sales representative could visit any of the following companies immediately after P except :",
                            "If the sales representative visits Q immediately before R and immediately after S, she must visit Q :",
                            "Which of the following could be the order in which the sales representative visits the six companies ?",
                        ],
                        from_question=24,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Selection Based on Given Conditions",
        cases=[
            Input.Case(
                items=[
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question that follows :<br><br>A team of five is to be selected from amongst five boys A, B, C, D and E and four girls P, Q, R and S. Some criteria for selection are :<br>A and S have to be together.<br>P cannot be put with R.<br>D and Q cannot go together.<br>C and E have to be together.<br>R cannot be put with B.<br>Unless otherwise stated, these criteria are applicable to all the question below :",
                        questions=[
                            "If two of the members have to be boys, the team will consist of :",
                            "If R be one of the members, the other members of the team are :",
                            "If two of the members are girls and D is one of the members, the members of the team other than D are :",
                            "If A and C are members, the other members of the team cannot be :",
                            "If including P at least three members are girls, the members of the team other than P are :",
                        ],
                        from_question=1,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>There are five men A, B, C, D and E and six women P, Q, R, S, T and U. A, B and R are advocates; C, D, P, Q and S are doctors and rest are teachers. Some teams are to be selected from amongst these eleven persons subject to the following conditions :<br>A, P and U have to be together.<br>B cannot go with D or R.<br>E and Q have to be together.<br>C and T have to be together.<br>D and P cannot go together.<br>C cannot go with Q.",
                        questions=[
                            "If the team is to consist of two male advocates, two lady doctors and one teacher, the members of the team are :",
                            "If the team is to consist of one advocate, two doctors, three teachers and C may not go with T, the members of the team are :",
                            "If the team is to consist of one male advocate, one male doctor, one lady doctor and two teachers, the members of the team are :",
                            "If the team is to consist of one advocate, three doctors and one male teacher, the members of the team are :",
                            "If the team is to consist of two advocates, two doctors, two teachers and not more than three ladies, the members of the team are :",
                        ],
                        from_question=6,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question that follows :<br><br>From amongst five doctors A, B, C, D and E, four engineers G, H, K and L and six teachers M, N, O, P, Q and R, some teams are to be selected. Of these, A, B, G, H, O, P and Q are females and rest are males.<br>The formation of teams is subject to the following conditions :<br>Wherever there is a male doctor, there will be not female teacher.<br>Wherever there is a male engineer, there will be no female doctor.<br>There shall not be more than two male teachers in any team.",
                        questions=[
                            "If the team consists of two doctors, three female teachers and two engineers, the members of the team are :",
                            "If the team consists of two doctors, one engineer and four teachers, all the following teams are possible except :",
                            "If the team consists of two doctors, two female teachers and two engineers, all the following teams are possible except :",
                            "If the team consists of three doctors, two male engineers and two teachers, the members of the team could be :",
                            "If the team consists of two doctors, two engineers and two teachers, all the following teams are possible except :",
                        ],
                        from_question=11,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>Eight students A, B, C, D, E, F, G and H are planning to enjoy car racing. There are only two cars and following are the conditions :<ol type='i'><li>One car can accommodate maximum five and minimum four students.</li><li>A will sit in the same car in which D is sitting but H is not in the same car.</li><li>B and C can't sit in the same car in which D is sitting.</li><li>F will sit in the car of four people only alongwith A and E but certainly not with G.</li></ol>",
                        questions=[
                            "If H and G are sitting in the same car, who are the other two students sitting in the same car ?",
                            "If E and A are sitting in the same car, which of the following statements is true ?",
                            "Which of the following statements is superfluous for the above sitting arrangements ?",
                        ],
                        from_question=16,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question that follows :<br><br>At an Electronic Data Processing Unit, five out of the eight program sets P, Q, R, S, T, U, V and W are to be operated daily. On any one day, except for the first day of a month, only three of the program sets must be the ones that were operated on the previous day. The program operating must also satisfy the following conditions :<ol type='i'><li>If program P is to be operated on a day, V cannot be operated on that day.</li><li>If Q is to be operated on a day, T must be one of the programs to be operated after Q.</li><li>If R is to be operated on a day, V must be one of the programs to be operated after R.</li><li>The last program to be operated on any day must be either S or U.</li></ol>",
                        questions=[
                            "Which of the following could be the set of programs to be operated on the first day of a month ?",
                            "Which of the following is true of any day's valid program set operator ?",
                            "If R is operated at third place in a sequence, which of theh following cannot be the second program in that sequence ?",
                            "If the programs set R and W are to be operated on the first day, which of the following could be the other programs on that day ?",
                            "If the programs sets operated on a day is P, Q, W, T, U, each of the following could be the next day's program set except :",
                        ],
                        from_question=19,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Family-based Problems",
        cases=[
            Input.Case(
                items=[
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question given below it :<br><br>Prashant Arora has three children - Sangeeta, Vimal and Ashish. Ashish married Monika, the eldest daughter of Mr. and Mrs. Roy. The Roys married their youngest daughter to the eldest son of Mr. and Mrs. Sharma, and they had two children named Amit and Shashi. The Roys have two more children, Roshan and Vandana, both elder to Veena. Sameer and Ajay are sons of Ashish and Monika. Rashmi is the daughter of Amit.",
                        questions=[
                            "What is the surname of Rashmi ?",
                            "How is Sameer related to the father of Monika ?",
                            "What is the surname of Sameer ?",
                            "How is Mrs. Roy related to Ashish ?",
                        ],
                        from_question=1,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question that follows :<ol type='i'><li>P, Q, R, S, T and U are travelling in a bus</li><li>There are two reporters, two technicians, one photographer and one writer in the group.</li><li>The photographer P is married to S who is a reporter.</li><li>P, R, Q, S are two married couples and nobody in the group has same profession.</li><li>U is brother of R.</li></ol>",
                        questions=[
                            "Which of the following is a pair of technicians ?",
                            "Which of the following is a pair of reporters ?",
                            "How is R related to U ?",
                            "Which of the following pairs is a couple",
                            "Which of the following is a pair of husbands ?",
                        ],
                        from_question=5,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question given below it :<ol type='i'><li>P, Q, R, S, T and U are six members in a family in which there are two married couples.</li><li>T, a teacher is married to the doctor who is mother of R and U.</li><li>Q, the lawyer is married to P.</li><li>P has one son and one grandson.</li><li>Of the two married ladies one is a housewife.</li><li>There is also one student and one male engineer in the family.</li></ol>",
                        questions=[
                            "How is P related to R ?",
                            "Who among the following is the housewife ?",
                            "How is R related to U ?",
                            "Which of the following represents the group of females in the family ?",
                            "Which of the following is true about the grand-daughter in the family ?",
                        ],
                        from_question=10,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information given below and answer the question that follows :<br><br>There are five persons P, Q, R, S and T. One is football player, one is chess player and one is hockey player. P and S are unmarried ladies and do not participate in any game. None of the ladies play chess or football. There is a married couple in which T is the husband. Q is the brother of R and is neither a chess player nor a hockey player.",
                        questions=[
                            "Who is the football player",
                            "Who is the hockey player",
                            "Who is the chess player",
                            "Who is the wife of T ?",
                            "The three ladies are :",
                        ],
                        from_question=15,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<ol type='i'><li>There is a family of six members A, B, C, D, E and F.</li><li>There are two married couples in the family and the family members represent three generations.</li><li>Each member has a distinct choice of a colour amongst green, yellow, black, red, white and pink.</li><li>No lady member likes either green or white.</li><li>C, who likes black colour is the daughter-in-law of E.</li><li>B is brother of F and son of D and likes pink.</li><li>A is grandmother of F and F does not like red.</li><li>The husband has a choice of green colour, his wife likes yellow.</li></ol>",
                        questions=[
                            "Which of the following is the colour preference of A ?",
                            "How many male members are there in the family ?",
                            "Which of the following is true about F ?",
                            "Which of the following is the colour combination of one of the couples ?",
                            "Which of the following is one of the married couples ?",
                        ],
                        from_question=20,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question that follows :<ol type='i'><li>A, B, C, D, E and F are six members in a family in which there are two married couples.</li><li>D is brother of F. Both D and F are lighter than B.</li><li>B is mother of D and lighter than E.</li><li>C, a lady, is neither heaviest nor the lightest in the family.</li><li>E is lighter than C.</li><li>The grandfather in the family is the heaviest.</li></ol>",
                        questions=[
                            "How is E related to F ?",
                            "Which of the following is a pair of married couples ?",
                            "How many male members are there in the family ?",
                            "Who among the following will be in the second place if all the members in the family are arranged in the descending order of their weights ?",
                            "How is C related to D ?",
                        ],
                        from_question=25,
                    ),
                    Input.Group(
                        parent_question="Directions : On the basis of the following information given below, answer the question.<ol type='i'><li>P, Q, R, S, T and U are six members of a group of which three are males and three are females.</li><li>There are two engineer, two lawyers, one teacher and one doctor in the group.</li><li>Q, T, P and R are two married copules and no person in this group has the same profession.</li><li>T, a teacher with blue dress, married a male lawyer with brown dress.</li><li>Colour of the dresses of both the husbands and that of both the wives is the same.</li><li>Two persons have blue dress, two have brown and the remaining one each has black and green</li><li>P is a male engineer whose sister S is also an engineer.</li><li>Q is a doctor.</li></ol>",
                        questions=[
                            "Who is the wife of P ?",
                            "Which of the following is a group of female members ?",
                            "Which of the following is a pair of married ladies ?",
                            "What is the colour of U's dress ?",
                        ],
                        from_question=30,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information to answer the question given below it :<ol type='i'><li>In a family of six persons, there are people from three generations. Each person has separate profession and also they like different colours. There are two couples in the family.</li><li>Rohan is a CA and his wife neither is a doctor nor likes green colour.</li><li>Engineer likes red colour and his wife is a teacher.</li><li>Mohini is mother-in-law of Sunita and she likes orange colour.</li><li>Vinod is grandfather of Tanmay and Tanmay, who is a principal, likes black colour.</li><li>Nanu is grand-daughter of Mohini and she likes blue colour. Nanu's mother likes white colour.</li></ol>",
                        questions=[
                            "Who is an Engineer ?",
                            "What is the profession of Sunita ?",
                            "Which of the following is the correct pair of two couples ?",
                            "How many ladies are there in the family ?",
                            "Which colour is liked by CA ?",
                        ],
                        from_question=34,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Jumbled Problems",
        cases=[
            Input.Case(
                items=[
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question that follows :<ol type='i'><li>There is a group of five persons - A, B, C, D and E.</li><li>One of them is a horticulturist, one is a physicist, one is a journalist, one is an industrialist and one is an advocate.</li><li>Three of them - A, C and advocate prefer tea to coffee and two of them - B and the journalist prefer coffee to tea.</li><li>The industrialist and D and A are friends to one another but two of these prefer coffee to tea.</li><li>The horticulturist is C's brother.</li></ol>",
                        questions=[
                            "Who is a horticulturist ?",
                            "Who is an industrialist ?",
                            "Which of the following groups includes a person who likes tea but is not an advocate ?",
                            "Who is a physicist ?",
                            "Which of the statements above is superfluous ?",
                        ],
                        from_question=1,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question given below it :<br><br>There are five friends A, B, C, D and E. Two of them are businessmen while the other three belong to different occupations viz. medical, engineer and legal. One businessman and the lawyer stay in the same locality S, while the other three stay in three different localities P, Q and R. Two of these five person are Hindus while the remaining three come from three different communities viz. Muslim, Christian and Sikh. The lawyer is the oldest in age while one of the businessmen who runs a factory is the youngest. The other businessman is a cloth merchant and agewise lies between the doctor and the lawyer. D is a cloth merchant and stays in locality S while E is a Muslim and stays in locality R. The doctor is a Christian and stays in locality P, B is a Sikh while A is a Hindu and runs a factory.",
                        questions=[
                            "Who stays in locality Q ?",
                            "What is E's occupation ?",
                            "Agewise who among the following lies between A and C ?",
                            "What is B's occupation ?",
                            "What is C's occupation ?",
                        ],
                        from_question=6,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question that follows :<br><br>A, B, C, D and E are five towns out of which two are hill stations and the rest are in plain. Two towns, which are in plain, are harbours. Four towns out of five are capitals and two are industrial towns. Population of two towns is less than 5 lacs. It is 20 lacs of one town and more than 50 lacs of two towns. Two towns are on the same latitudes and other two are on the same longitudes. Latitudes and longitudes of both harbours are different and out of these one is an industrial town. The population of both industrial towns is more than 50 lacs. The longitudes of one hill station and one of the industrial towns are same. The latitudes and longitudes of the other hill station and other harbour are different. One industrial town is neither a hill station nor a harbour. None of the hill stations is an industrial town. The hill station of which longitudes are same as that of a harbour, is a capital. B is a hill station while the longitudes of A and E are same. E is a harbour. The latitudes of D and C are same and the population of D is 20 lacs. Both the harbours are capitals and one of them is an industrial town.",
                        questions=[
                            "Which of the following two towns are those whose population is less than 5 lacs ?",
                            "Which of the following towns is not a capital ?",
                            "Which of the following is a harbour, capital and industrial town ?",
                            "Which of the following towns have population more than 50 lacs ?",
                            "Which one of the following towns is hill station as well as capital ?",
                        ],
                        from_question=11,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the given information carefully and choose the correct alternative in the question.<ol type='i'><li>There are eight faculty members A, B, C, D, E, F, G and H in the institute, each teaching a different subject.</li><li>There are three lady members and of the eight, four are holding Ph.D. Degree.</li><li>E teaches Psychology and is Ph.D. A teaches Chemistry.</li><li>The one who teaches Economics is not Ph.D. No lady member teaches either Commerce or Law. Law faculty does not award Ph.D.</li><li>D and G do not teach either Commerce or Physics.</li><li>H and C are lady members and are not Ph.D. F who is Ph.D. teaches Zoology.</li><li>B and G are Ph.Ds and G is a lady member.</li></ol>",
                        questions=[
                            "Who teaches Physics ?",
                            "Which of the following lady members is/are Ph.D. ?",
                            "Which of the following statements is true ?",
                            "Which of the following combinations is not correct ?",
                            "What is the subject taught by G ?",
                        ],
                        from_question=16,
                        modified=True
                        # answers not provided in book, provided by self
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the question given below it :<br><br>Of the five boys A, B, C, D and E two are good, one is poor and two are average in studies. Two of them study in post-graduate classes and three in under-graduate classes. One comes from a rich family, two from middle-class families and two from poor families. One of them is interested in music, two in acting and one in sports. Of those studying in under-graduate classes, two are average and one is poor in studies. Of the two boys interested in acting, one is a post-graduate student. The one interested in music comes from a middle-class family. Both the boys interested in acting are not industrious. The two boys coming from middle-class families are average in studies and one of them is interested in acting. The boy interested in sports comes from a poor family, while the one interested in music is industrious. E is industrious, good in studies, comes from a poor family and is not interested in acting, music or sports. C is poor in studies in spite of being industrious. A comes from a rich family and is not industrious but good in studies. B is industrious and comes from a middle-class family.",
                        questions=[
                            "Name the boy interested in sports.",
                            "Name the boy interest in music.",
                            "Name the middle-class family boy interested in acting.",
                            "Name the boys studying in post-graduate classes.",
                            "Name the boy who is not industrious and is average in studies.",
                        ],
                        from_question=21,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Some Miscellaneous Puzzles",
        cases=[
            Input.Case(
                items=[
                    Input.Group(
                        parent_question="Directions : Study the following information and answer the question given below it :<br><br>A, B, C and D are four friends who do not mind exchanging items. A had two chessboards each costing Rs 500 and a record player. C originally had a cycle and a walkman. Each cricket bat costs Rs 700. Both D and C got a cricket bat from B. A gave his record player costing Rs 2000 to B. C got a camera costing Rs 1500 from D. The cycle C had costs Rs 1000 and the walkman costs Rs 700. B had three cricket bats at the beginning and D had two cameras total cost of which is Rs 5000. A gave one of his chessboards to C and took C's cycle. C gave his walkman to D.",
                        questions=[
                            "Who did not have a cricket bat at the end of exchange of items ?",
                            "Total cost of materials C had at the beginning was",
                            "After completion of exchange of items, A had with him an item which no one else had. What is the item ?",
                            "At the beginning who had the costliest item ?",
                            "In the process of exchange of items, B received an item from",
                            "After exchange of items, B had",
                            "After exchange of items, who had the items total cost of which is Rs 1500 ?",
                            "Who incurred maximum loss after the exchange of items ?",
                            "Who made profit after the exchange of items ?",
                            "At the exchange of items, D had in his possession",
                        ],
                        from_question=1,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>The sum of income of A and B is more than that of C and D taken together. The sum of the income of A and C is the same as that of B and D taken together. Moreover, A earns half as much as the sum of the income of B and D.",
                        questions=[
                            "Whose income is the highest ?",
                            "Which of the following statements is not correct ?",
                            "If A's income be Rs 80,000 per annum and the difference between the income of B and D be the same as A's income, B's income is",
                        ],
                        from_question=11,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information given below and answer the question that follows :<br><br>A, B, C, D, E and F are cousins. No two cousins are of the same age, but all have birthdays on the same date. The youngest is 17 years old and the oldest E is 22. F is somewhere between B and D in age. A is older than B. C is older than D.",
                        questions=[
                            "Which of the following is not possible ?",
                            "Which of the following could be the ages of D and C respectively, if B is 17 years old ?",
                            "Which of the following must be true if exactly two of the cousins are between C and F in age ?",
                            "If A is one year older than C, the number of logically possible orderings of all six cousins by increasing age is",
                            "Which of the following must be true if C is 19 years old ?",
                        ],
                        from_question=14,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>There are five identical looking boxes having different objects in it and every box has a label indicating their contents. The following is a description of the contents and the label of each box :<table><thead><tr><th>Contents</th><th>Label</th></tr></thead><tr><td>Two Pins</td><td>PP</td></tr><tr><td>Two Balls</td><td>BB</td></tr><tr><td>Two Clips</td><td>CC</td></tr><tr><td>One Pin and One Clip</td><td>PC</td></tr><tr><td>One Ball and One Clip</td><td>BC</td></tr></table>Somebody has mischieviously interchanged these labels in such a way that no box contains the label correctly explaining its contents.",
                        questions=[
                            "If the first box opened contained label PP and the second box opened contained label PC and out of the combined four items, one item was a Ball, which of the following is definitely true ?",
                            "If the first box, containing the label BC was opened and it was found that one item is a Ball, which of the following would be definitely true ?",
                            "If the information is available that box PC does not contain either any Pin or any Clip and box PP does not contain any Pin and box CC contains one Clip and one Ball, which of the following will be definitely true if only one of the remaining boxes is opened ?",
                            "If the box PP contained two Clips, the box CC contained two Pins and the box BB contained atleast one Ball, which of the following will definitely not be true ?",
                        ],
                        from_question=19,
                    ),
                    # the following two are in reverse order in the book
                    Input.Group(
                        parent_question="Read the following passage carefully and answer the question that follow :<br><br>Score Card of the final match of Sharjah Singer Cup 1996 is given below :<br>SCORE BOARD<br>Paskistan : Saeed Anwar c Fleming b Vaughan 1; Aamir Sohail st Germon b Patel 16; Shahid Afridi c Greatbatch b Larsen 21; Ijaz Ahmed c Fleming b Astle 10; Salim Malik lbw Cairns 40; Azam Khan c Greatbatch b Harris 22; Moin Khan lbw Cairns 32; Wasim Akram c Vaughan b Patel 0; Saqlain Mushtaq lbw Harris 0; Waqar Younis run out 0; Mushtaq Ahmed not out 4.<br>Extras : (lb-12, w-2); 14<br>Total : (all out in 48.5 overs); 160<br>Fall of wickets : 1-4, 2-32, 3-51, 4-63, 5-116, 6-120, 7-120, 8-138, 9-145.<br>Bowling : Vaughan 8-0-33-1; Larsen 9-1-22-1; Cairns 9.5-0-24-2; Astle 3-0-7-1; Harris 9-2-32-2; Patel 10-2-30-2.<br>New Zealand : Bryan Young b Akram 5; Mark Greatbatch c Ijaz b Mustaq 52; Adam Parore lbw Sqlain 22; Nathan Astle c Mushtaq b Saqlain 8; Stephen Fleming lbw Younis 4; Chris Carins lbw Akram 8; Chris Harris c Afridi b Mushtaq 2; Lee Germon lbw Akram 5; Dipak Patel lbw Afridi 1; Justin Vaughan not out 1; Gavin Larsen b Afridi 0.<br>Extras : (w-5, nb-6); 11<br>Total : (all out in 36.5 overs); 119<br>Fall of wickets : 1-7, 2-66, 3-81, 4-98, 5-102, 6-111, 7-114, 8-117, 9-119.<br>Bowling : Akram 8-1-20-3; Younis 8-0-22-1; Saqlain 8-0-32-2; Afridi 2.5-0-14-2; Mushtaq 10-0-31-2.",
                        questions=[
                            "How many Pakistani batsmen were bowled by bowlers of New Zealand ?",
                            "Highest runs were scored in the match by the partnership of",
                            "If runs per wicket is the criterion for evaluation bowling performance, then which bowler had the best bowling performance in the match ?",
                            "If number of balls per wicket is considered to evaluate bowling performance, then who was the best bowler of the match ?",
                            "Performance of which bowlers were the same, where criterion for evaluation is number of runs per wicket ?",
                            "Which bowler of Pakistan had the worst bowling performance considering number of balls per wicket as the criterion ?",
                            "How many leg before wickets were given in the match ?",
                            "Who was run out in the match ?",
                            "Who took maximum number of catches in the match ?",
                            "Which of the following statements is false ?",
                        ],
                        from_question=23,
                    ),
                    Input.Group(
                        parent_question="Priya and Promila are best friends. Priya's father, Prem, is a police officer while Promila's father, Somesh, is an engineer. Prem and Somesh have a common friend in Rohan who has two children, Kunal and Renu. Priya and Kunal are college fellows while Promila and Renu are in the same class and study in another college. Promila and Kunal are good debaters and represent their colleges in inter-college debates. Renu writes poems while Priya is a good singer. Somesh is very proud of his daughter and often talks to his friends about her special talent in painting. Renu's father is a businessman and stays in the same locality where Prem stays while Somesh, who stays in another locality, is more intimate with Prem than with Rohan. Families of all the three persons stay with them.<br><br>In the following question, two statements P and Q are given.<br>Mark your answer as (a) if both P and Q are true; (b) if one of the two is true and the other is wrong; (c) if both the statements are wrong; and (d) if it is not possible to draw any conclusion about the correctness or otherwise of either or both P and Q on the basis of information available in the above statement.",
                        questions=[
                            "P : Priya and Promia read in different colleges.<br>Q : Promila is a good debater as also a good painter.",
                            "P : Rohan is an electronics engineer.<br>Q : Priya and Kunal are class-fellows.",
                            "P : Somesh is civil engineer.<br>Q : Priya and Renu are good debaters and represent their colleges in inter-college debates.",
                            "P : Priya and Renu are college-fellows.<br>Q : Promila's father is more intimate with Renu's father than with Priya's father",
                            "P : Rohan is a businessman.<br>Q : Renu and Priya stay in the same locality.",
                            "P : Promila's special talent has impressed her father very much.<br>Rohan and Somesh stay in the same locality.",
                            "P : Rohan and Prem stay in the same locality.<br>Renu and Kunal stay in the same locality.",
                        ],
                        from_question=33,
                        no_options=True,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Try Yourself",
        cases=[
            Input.Case(
                items=[
                    Input.IndividualQuestion(
                        question="Six roads lead to a country. They may be indicated by letters X, Y, Z and digits 1, 2, 3. When there is storm, Y is blocked. Where there are floods, X, 1 and 2 will be affected. When road 1 is blocked, Z also is blocked. At a time when there are floods and a storm also blows, which road(s) can be used ?",
                        number=1,
                    ),
                    Input.IndividualQuestion(
                        question="Six persons A, B, C, D, E and F are standing in a circle. B is between F and C; A is between E and D; F is to the left of D. Who is between A and F ?",
                        number=2,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<ol type='i'><li>Mohan and Sumit are good in Chemistry and Biology.</li><li>Ashish and Mohan are good in Biology and Physics.</li><li>Ashish, Pratap and Neeraj are good in Physics and History.</li><li>Neeraj and Ashish are good in Physics and Mathematics.</li><li>Pratap and Sumit are good in History and Chemistry.</li></ol>",
                        questions=[
                            "Who is good in Physics, History and Mathematics, but not in Biology ?",
                            "Who is good in History, Physics, Biology and Mathematics ?",
                        ],
                        from_question=3,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the information given below and answer the question that follows :<br><br>There are four friends A, B, C, D. One of them is a cricketer and studies Chemistry and Biology. A and B play football. Both football players study Maths. D is a boxer. One football player also studies Physics. The boxer studies Maths and Accounts. All the friends study two subjects each and play one game each.",
                        questions=[
                            "Who is the cricketer.",
                            "Who studies Accounts and plays football ?",
                            "Who studies Physics ?",
                            "How many games are played and subjects studies by the four friends ?",
                        ],
                        from_question=5,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information and answer the question given below it :<ol type='i'><li>Sanchit, Kamal, Rahul, Madan and Tarun are five friends who stay in one building.</li><li>Each one owns a separate garage A, B, C, D and E and a different coloured car viz., Red, Yellow, White, Black and Blue.</li><li>Kamal does not own either garage D or E. His car is of red colour.</li><li>Madan owns yellow coloured car and garage C.</li><li>Tarun who owns garage A does not own black or white coloured car.</li></ol>",
                        questions=[
                            "Who owns garage D ?",
                            "Who is the owner of blue coloured car ?",
                            "Which of the following combinations of colour of car and garage is correct ?",
                        ],
                        from_question=9,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<ol type='i'><li>P, Q, R, S, T and U are six members of a family, each of them engaged in a different profession - Doctor, Lawyer, Teacher, Engineer, Nurse, Manager.</li><li>Each of them remains at home on a different day of the week from Monday to Saturday.</li><li>The lawyer in the family remains at home on Thursday.</li><li>R remains at home on Tuesday.</li><li>P, the Doctor does not remain at home either on Saturday or on Wednesday.</li><li>S is neither the Doctor nor the Teacher and remains at home on Friday.</li><li>Q is the Engineer and T is the Manager.</li></ol>",
                        questions=[
                            "Who remains at home on Saturday",
                            "Which of the following combinations is not correct ?",
                            "Who among them remains at home on the following day of the Nurse ?",
                            "Which of the following combinations is correct ?",
                        ],
                        from_question=12,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the information given below and answer the question that follows :<ol type='i'><li>Six friends A, B, C, D, E and F are seated in a circle facing each other.</li><li>A is between D and B and F is between C and E.</li><li>C is third to the left of B.</li></ol>",
                        questions=[
                            "Who is between B and F ?",
                            "Who is between F and D ?",
                            "Which of the following is the position of A in relation to F ?",
                        ],
                        from_question=16,
                    ),
                    Input.IndividualQuestion(
                        question="Seven students A, B, C, D, E, F and G are sitting in a row. C is sitting between A and D. E is between F and G and B is between D and F. A and G are at two ends. D is sitting between",
                        number=19,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>From a group of six boys M, N, O, P, Q, R and five girls G, H, I, J, K, a team of six is te be selected. Some of the criteria of selection are as follows :<br>M and J go together.<br>O cannot be placed with N.<br>I cannot go with J.<br>N goes with H.<br>P and Q have to be together.<br>K and R go together.<br>Unless otherwise stated, these criteria are applicable to all the following questions :",
                        questions=[
                            "If the team consists of two girls and I is one of them, the other members are",
                            "If the team has four boys including O and R, the members of the team other than O and R are",
                            "If four members are boys, which of the following cannot consistute the team ?",
                            "If both K and P are members of the team and three boys in all are included in the team, the members of the team other than K and P are",
                            "If the team has three girls including J and K, the members of the team other than J and K are",
                        ],
                        from_question=20,
                    ),
                    Input.IndividualQuestion(
                        question="Shekhar is taller than Kunal. Atul is taller than Pawan but not as tall as Kunal. Prashant is taller than Shekhar. Who among them is the shortest.",
                        number=25,
                    ),
                    Input.IndividualQuestion(
                        question="Seven persons P, Q, R, S, T, U and V participate in and finish all the events of a series of swimming races. There are no ties at the finish of any of the events. V always finishes somewhere ahead of P. P always finished somewhere ahead of Q. Either R finishes first and T finished last or S finishes first and U or Q finishes last. If in a particular race V finished fifth, then which one of the following would be true ?",
                        number=26,
                    ),
                    Input.IndividualQuestion(
                        question="There are five bus stops A, B, C, D and E at equal intervals. C is not the middle stop. A and E are not terminal stops. C comes twice as many stops before D in upward journey as B comes after A. D is the first stop in downward journey. Which of the following gives the correct sequene of the stops in downward journey ?",
                        number=27,
                    ),
                    Input.IndividualQuestion(
                        question="A, B, C, D, E and F, not necessarily in that order, are sitting on six chairs regularly placed around a round table. It is observed that :<br>A is between D and F.<br>C is opposite D.<br>D and E are not on neighbouring chairs.<br>Which of the following pairs must be sitting on neighbouring chairs ?",
                        number=28,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the question given below it :<br><br>There is a group of five persons A, B, C, D and E. In the group, there is a Professor of Philosophy, a Professor of Psychology and a Professor of Economics. A and D are ladies who have no specialisation in any subject and are unmarried. No lady is a philosopher or an economist. There is a married couple in the group of which E is the husband. B is the brother of C and is neither a psychologist nor an economist.",
                        questions=[
                            "Who is the Professor of Psychology ?",
                            "Which of the following groups includes all the men ?",
                            "Who is the Professor of Philosophy ?",
                            "Who is the wife of E ?",
                            "Who is the Professor of Economics ?",
                        ],
                        from_question=20,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the information given below and answer the question that follows :<ol type='i'><li>Six plays A, B, C, D, E and F are to be organised from Monday to Saturday i.e. 5th to 10th - one play each day.</li><li>There are two plays between C and D and one play between A and C.</li><li>There is one play between F and E and E is to be organised before F.</li><li>Which day is play B organised ?</li><li>Which of the following is the correct sequence of organising plays ?</li></ol>",
                        questions=[
                            "The organisation would start from which play ?",
                            "On which date is play E to be organised ?",
                            "The organisation would end with which play ?",
                            "Which day is play B organised ?",
                            "Which of the following is the correct sequence of organising plays ?",
                        ],
                        from_question=34,
                    ),
                ],
            ),
        ],
    ),
]
