import models.Input as Input

TYPES: list[Input.Type] = [
    Input.Type(
        type_name="DECIPHERING JUMBLED UP DESCRIPTIONS",
        cases=[
            Input.Case(
                items=[
                    Input.Individual_Question(
                        question='Pointing to a man on the stage, Rita said, "He is the brother of the daughter of the wife of my husband." How is the man on the stage related to Rita ?',
                        number=1,
                    ),
                    Input.Individual_Question(
                        question='Showing the man receiving the prize, Saroj said, "He is the brother of my uncle\'s daughter." Who is the man to Saroj ?',
                        number=2,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a man, a woman said, "His mother is the only daughter of my mother." How is the woman related to the man ?',
                        number=3,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a photograph, a person tells his friend, "She is the grand daughter of the elder brother of my father." How is the girl in the photograph related to the man ?',
                        number=4,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a photograph, Vipul said, "She is the daughter of my grandfather\'s only son." How is Vipul related to the girl in the photograph ?',
                        number=5,
                    ),
                    Input.Individual_Question(
                        question="A woman introduces a man as the son of the brother of her mother. How is the man related to the woman ?",
                        number=6,
                    ),
                    Input.Individual_Question(
                        question='Looking at the portrait of a man, Harsh said, "His mother is the wife of my father\'s son. Brother sna sisters I have none." At whose portrait was Harsh looking ?',
                        number=7,
                    ),
                    Input.Individual_Question(
                        question="A man said to a lady, \"Your mother's husband's sister is my aunt.\" How is the lady related to the man ?",
                        number=8,
                    ),
                    Input.Individual_Question(
                        question='If Neena say, "Anita\'s father Raman is the only son of my father-in-law Mahipal", then how is Bindu, who is the sister of Anita, related to Mahipal ?',
                        number=9,
                    ),
                    Input.Individual_Question(
                        question="Pointing to a girl in the photograph, Amar said, \"Her mother's brother is the only son of my mother's father.\" How is the girl's mother related to Amar ?",
                        number=10,
                    ),
                    Input.Individual_Question(
                        question="A girl introduced a boy as the son of the daughter of the father of her uncle. The boy is girl's",
                        number=11,
                    ),
                    Input.Individual_Question(
                        question="If X is the brother of the son of Y's son, how is X related to Y ?",
                        number=12,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a gentleman, Deepak said, "His only brother is the father of my daughter\'s father." How is the gentleman related to Deepak ?',
                        number=13,
                    ),
                    Input.Individual_Question(
                        question='Introducing a man to her husband, a woman said "his brother\'s father is the only son of my grandfather." How is the woman related to this the man ?',
                        number=14,
                    ),
                    Input.Individual_Question(
                        question='Pointing out to a lady, a girl said, "She is the daughter-in-law of the grandmother of my father\'s only son." How is the lady related to the girl ?',
                        number=15,
                    ),
                    Input.Individual_Question(
                        question="Rita told Mani, \"The girl I met yesterday at the beach was the youngest daughter of the brother-in-law of my friend's mother.\" How is the girl related to Rita's friend ?",
                        number=16,
                    ),
                    Input.Individual_Question(
                        question='If Kamal says, "Ravi\'s mother is the only daughter of my mother", how is Kamal related to Ravi ?',
                        number=17,
                    ),
                    Input.Individual_Question(
                        question="Rahul told Anand, 'Yesterday I defeated the only brother of the daughter of my grandmother.' Who did Rahul defeat ?",
                        number=18,
                    ),
                    Input.Individual_Question(
                        question='When Anuj saw Manish, he recalled, "He is the son of the father of my daughter\'s mother." Who is Manish ?',
                        number=19,
                        modified=True,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a photograph, a lady tells Pramod, "I am the only daughter of this lady and her son is your maternal uncle." How is the speaker related to Pramod\'s father ?',
                        number=20,
                    ),
                    Input.Individual_Question(
                        question='Introducing a man, a woman said, "He is the only son of my mother\'s mother." How is the woman related to the man ?',
                        number=21,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a man in the photograph, Asha said, "His mother\'s only daughter is my mother." How is Asha related to that man ?',
                        number=22,
                    ),
                    Input.Individual_Question(
                        question="Pointing to a photograph, a woman says, \"This man's son's sister is my mother-in-law.\" How is the woman's husband related to the man in the photograph ?",
                        number=23,
                    ),
                    Input.Individual_Question(
                        question='Introducing a man, a woman said, "His wife is the only daughter of my father." How is that man related to the woman ?',
                        number=24,
                    ),
                    Input.Individual_Question(
                        question='Deepak said to Nitin, "That boy playing with the football is the younger of the two brothers of the daughter of my father\'s wife." How is the boy playing football related to Deepak ?',
                        number=25,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a lady on the platform, Manju said, "She is the sister of the father of my mother\'s son." Who is the lady to Manju ?',
                        number=26,
                    ),
                    Input.Individual_Question(
                        question='Arun said, "This girl is the wife of the grandson of my mother." Who is Arun to the girl ?',
                        number=27,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a man in a photograph, a woman said, "His brother\'s father is the only son of my grandfather." How is the woman related to the man in the photograph ?',
                        number=28,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a person, a man said to a woman, "His mother is the daughter of your father." How was the woman related to the person ?',
                        number=29,
                        modified=True,
                    ),
                    Input.Individual_Question(
                        question="A man pointing to a photograph says, \"The lady in the photograph is my nephew's maternal grandmother.\" How is the lady in the photograph related to the man's sister who has no other sister ?",
                        number=30,
                    ),
                    Input.Individual_Question(
                        question='Pointing to a lady, a man said, "The son of her only brother is the brother of my wife." How is the lady related to the man ?',
                        number=31,
                    ),
                    Input.Individual_Question(
                        question='Pointing to an old man, Kailash said, "His son is my son\'s uncle." How is the old man related to Kailash ?',
                        number=32,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="RELATION PUZZLE",
        cases=[
            Input.Case(
                items=[
                    Input.Individual_Question(
                        question="A party consists of grandmother, father, mother, four sons and their wives and one son and two daughters to each of the sons. How many females are there in all ?",
                        number=1,
                    ),
                    Input.Individual_Question(
                        question="Lakshmi and Meena are Rohan's wives. Shalini is Meena's step-daughter. How is Lakshami related to Shalini ?",
                        number=2,
                    ),
                    Input.Individual_Question(
                        question="Daya has a brother Anil. Daya is the son of Chandra. Bimal is Chandra's father. In terms of relationship, what is Anil of Bimal ?",
                        number=3,
                    ),
                    Input.Individual_Question(
                        question="Rahul's mother is the only daughter of Monika's father. How is Monika's husband related to Rahul ?",
                        number=4,
                    ),
                    Input.Individual_Question(
                        question="If (i) M is brother of N; (ii) B is brother of N; and (iii) M is brother of D, then which of the following statements is definitely true ?",
                        number=5,
                    ),
                    Input.Individual_Question(
                        question="Deepak is brother of Ravi. Rekha is sister of Atul. Ravi is son of Rekha. How is Deepak related to Rekha ?",
                        number=6,
                    ),
                    Input.Individual_Question(
                        question="A is B's sister. C is B's mother. D is C's father. E is D's mother. Then, how is A related to D ?",
                        number=7,
                    ),
                    Input.Individual_Question(
                        question="Given that : <ol><li>A is brother of B.</li><li>C is father of A.</li><li>D is brother of E.</li><li>E is daughter of B.</li></ol>The, uncle of D is",
                        number=8,
                    ),
                    Input.Individual_Question(
                        question="Q is the brother of R; P is the sister of Q; T is the brother of S; S is the daughter of R. Who are the cousins of Q ?",
                        number=9,
                        modified=True,
                    ),
                    Input.Individual_Question(
                        question="E is the son of A. D is the son of B. E is married to C. C is B's daughter. How is D related to E ?",
                        number=10,
                    ),
                    Input.Individual_Question(
                        question="A is father of C and D is son of B. E is brother of A. If C is sister of D, how is B related to E ?",
                        number=11,
                        modified=True,
                    ),
                    Input.Individual_Question(
                        question="Q's mother is sister of P and daughter of M. S is daughter of P and sister of T. How is M related to T ?",
                        number=12,
                        modified=True,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information and answer the questions given below :<br><br>A is the son of B. C, B's sister has a son D and a daughter E. F is the maternal uncle of D.",
                        questions=[
                            "How is A related to D ?",
                            "How is E related to F ?",
                            "How many nephews does F have ?",
                        ],
                        from_question=13,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information and answer the questions given below :<br><br>A is the father of C. But C is not his son.<br>E is the daughter of C. F is the spouse of A.<br>B is the brother of C. D is the son of B.<br>G is the spouse of B. H is the father of G.",
                        questions=[
                            "Who is the grandmother of D ?",
                            "Who is the son of F",
                        ],
                        from_question=16,
                    ),
                    Input.Individual_Question(
                        question="C is A's father's nephew. D is A's cousin but not the brother of C. How is D related to C ?",
                        number=18,
                    ),
                    Input.Individual_Question(
                        question="P is the son of Q while Q and R are the sister to one another. T is the mother of R. If S is the son of T, which of the following statements is correct ?",
                        number=19,
                    ),
                    Input.Individual_Question(
                        question="A is the brother of B. B is the brother of C. D is the father of A. Based on these three statements, which of the following statements cannot be definitely true ?",
                        number=20,
                    ),
                    Input.Individual_Question(
                        question="A is father of X; B is mother of Y. The sister of X and Z is Y. Which of the following statements is definitely not true ?",
                        number=21,
                    ),
                    Input.Individual_Question(
                        question="Rajan is the brother of Sachin and Manick is the father of Rajan. Jagat is the brother of Priya and Priya is the daughter of Sachin. Who is the uncle of Jagat ?",
                        number=22,
                    ),
                    Input.Individual_Question(
                        question='Neelam, who is Deepak\'s daughter, says to Deepika, "Your mother Rekha is the younger sister of my father who is the third child of Ramlal." How is Ramlal related to Deepika ?',
                        number=23,
                    ),
                    Input.Individual_Question(
                        question="P is the brother of Q and R. S is R's mother. T is P's father. Which of the following statements cannot be definitely true ?",
                        number=24,
                    ),
                    Input.Individual_Question(
                        question="P is the brother of D. X is the sister of P. A is the brother of F. F is the daughter of D. M is the father of X. Who is the uncle of A ?",
                        number=25,
                    ),
                    Input.Individual_Question(
                        question="K is the brother of N and X. Y is the mother of N and Z is the father of K. Which of the following statements is not definitely true ?",
                        number=26,
                    ),
                    Input.Individual_Question(
                        question='A woman walking with a boy meets another woman and on being asked about her relationship with the boy, she says, "My maternal uncle and his maternal uncle\'s maternal uncle are brother." How is the boy related to the woman ?',
                        number=27,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the information given below and answer the questions that follow :<ol type='i'><li>In a family of six persons A, B, C, D, E and F, there are two married couples.</li><li>D is grandmother of A and mother of B.</li><li>C is wife of B and mother of F.</li><li>F is the grand daughter of E.</li></ol>",
                        questions=[
                            "What is C to A ?",
                            "How many male members are there in the family ?",
                            "Which of the following is true ?",
                            "Who among the following is one of the couples ?",
                        ],
                        from_question=28,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the questions given below it :<br><br>All the six members of a family A, B, C, D, E and F are travelling together. B is the son of C but C is not the mother of B. A and C are a married couple. E is the brother of C. D is the daughter of A. F is the brother of B.",
                        questions=[
                            "How many male members are there in the family ?",
                            "Who is the mother of B ?",
                            "How many children does A have ?",
                            "Who is the wife of E ?",
                            "Which of the following is a pair of females ?",
                            "How is E related to D ?",
                        ],
                        from_question=32,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the information given below and answer the qustions that follow :<ol type='I'><li>A, B, C, D, E and F are six members of a family.</li><li>One couple has parents and their children in the family.</li><li>A is the son of C and E is the daughter of A.</li><li>D is the daughter of F who is the mother of E.</li></ol>",
                        questions=[
                            "Who are the male members in the family ?",
                            "Which of the following pairs is the parents of the children ?",
                            "Which of the following pairs is the parents of the couple ?",
                            "How many female members are there in the family ?",
                            "What relationship do D and E bear to each other ?",
                        ],
                        from_question=38,
                    ),
                    Input.Individual_Question(
                        question="A, B, C, D, E, F and G are members of a family consisting of four adults and three children, two of whom, F and G are girl. A and D are brothers and A is a doctor. E is an engineer married to one of the brothers and has two children. B is married to D and G is their child. Who is C ?",
                        number=43,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the questions given below it :<br><br>In a family, there are six members A, B, C, D, E and F. A and B are a married couple, A being the male member. D is the only son of C, who is the brother of A. E is the sister of D. B is the daughter-in-law of F, whose husband has died.",
                        questions=[
                            "How is F related to A ?",
                            "How is E related to C ?",
                            "Who is C to B ?",
                            "How many male members are there in the family ?",
                            "How is F related to C",
                        ],
                        from_question=44,
                    ),
                    Input.Individual_Question(
                        question="Shobha is the niece of Ashish. Ashish's mother is Priya. Kamla is Priya's mother. Kamla's husband is Hari. Krishna is the mother-in-law of Hari. How is Shobha related to Hari ?",
                        number=49,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the following information carefully and answer the questions given below it :<br><br>There are six person A, B, C, D, E and F. C is the sister of F. B is the brother of E's husband. D is the father of A and grandfather of F. There are two fathers, three brothers and a mother in the group.",
                        questions=[
                            "Who is the mother ?",
                            "Who is E's husband ?",
                            "How many male members are there in the group ?",
                            "How is F related to E ?",
                            "Which of the following is a group of brothers ?",
                        ],
                        from_question=50,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the questions given below it :<br><br>A family consists of six members P, Q, R, X, Y and Z. Q is the son of R but R is not mother of Q. P and R are a married couple. Y is the brother of R. X is the daughter of P. Z is the brother of P.",
                        questions=[
                            "Who is the brother-in-law of R ?",
                            "Who is the father of Q ?",
                            "How many children does P have ?",
                            "How many female members are there in the family ?",
                            "How is Q related to X ?",
                            "Which is a pair of brothers ?",
                        ],
                        from_question=55,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the information given below and answer the questions that follow :<br><br>There is a family of six person A, B, C, D, E and F. They are Lawyer, Doctor, Teacher, Salesman, Engineer and Accountant. There are two married couples in the family. D, the Salesman is married to the Lady Teacher. The Doctor is married to the Lawyer. F, the Accountant is the son of B and brother of E. C, the Lawyer is the daughter-in-law of A. E is the unmarried Engineer. A is the grandmother of F.",
                        questions=[
                            "How is E related to F ?",
                            "What is the profession of B ?",
                            "What is the profession of A ?",
                            "Which of the following is one of the couples ?",
                            "How is D related to F ?",
                        ],
                        from_question=61,
                    ),
                    Input.Group(
                        parent_question="Directions : A family consists of six members P, Q, R, S, T and U . There are two married couples. Q is a doctor and the father of T. U is grandfather of R and is a contractor. S is grandmother of T and is a housewife. There is one doctor, one contractor, one nurse, one housewife and two students in the family.",
                        questions=[
                            "Who is the husband of P ?",
                            "Who is the sister of T ?",
                            "What is the profession of P ?",
                            "Which of the following are two married copules ?",
                            "Which of the following is definitely a group of male members ?",
                        ],
                        from_question=66,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the questions that follow :<br><br>In a village in Bastar district in Madhya Pradesh, only two types of people live who belong to a tribal class. The first type is known as class A, while the other is known as class B. In that village, there is no other type of person except these two. The activities of both types of people are governed by perfectly patterned norms of social behaviour. Each person of the tribe has to obey the norms. They are rigid about this.<br>As far as marriage is concerned, the following norms are to be followed<ol type='A'><li>The people of class A cannot marry any other member of their own class, though they can marry members of class B.</li><li>After being married, each male member ceases to be a member of that class in which he was born but automatically, he becomes the member of the other class to which his wife belongs.</li><li>As far as females are concerned, they remain the members of their own class after being married.</li><li>On his birth, the child automatically becomes the member of this mother's class. When any male member becomes widower or divorcee, then he again belongs to the group in which he was born.</li><li>Nobody can marry more than one person according to social laws.</li></ol>",
                        questions=[
                            "Any class B female can have<br>(P) Grandfather born in class A<br>(Q) Grandmother born in class A",
                            "One boy, who was born in class B (boy and his wife both can have married and unmarried brothers),",
                            "Which of the following is not permissible according to social laws ?",
                        ],
                        from_question=71,
                        skip=True
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="CODED RELATIONS",
        cases=[
            Input.Case(
                items=[
                    Input.Individual_Question(
                        question="P + Q means P is the <em>brother</em> of Q; P - Q means P is the <em>mother</em> of Q and P \\times Q means P is the <em>sister</em> of Q. Which of the following means M is the <em>maternal uncle</em> of R ?",
                        number=1,
                    ),
                    Input.Individual_Question(
                        question="If A + B means A is the <em>brother</em> of B; A \\div B means A is the <em>father</em> of B and A \\times B means A is the <em>sister</em> of B, which of the following means M is the <em>uncle</em> of P ?",
                        number=2,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the questions given below it :<br><br>A \\div B means A is the <em>daughter</em> of B; A \\times B means A is the <em>son</em> of B and A - B means A is the <em>wife</em> of B.",
                        questions=[
                            "If P \times Q - S, which of the following is true ?",
                            "If T - S \\times B - M, which of the following is not true ?",
                            "If Z \\times T - S \\times U + P, what is U to Z.",
                        ],
                        from_question=3,
                    ),
                    Input.Individual_Question(
                        question="P \\times Q means P is the <em>sister</em> of Q; P + Q means P is the <em>father</em> of Q; P - Q means P is the <em>mother</em> of Q. Which of the following means S is the <em>aunt</em> of T ?",
                        number=6,
                    ),
                    Input.Individual_Question(
                        question="If A + B means A is the <em>son</em> of B; A - B means A is the <em>husband</em> of B; A \\times B means A is the <em>sister</em> of B, then which of the following shows the relation Q is the <em>maternal uncle</em> of P ?",
                        number=7,
                    ),
                    Input.Individual_Question(
                        question="If A + B means A is the <em>mother</em> of B; A \\div B means A is the <em>brother</em> of B; A \\times B means A is the <em>son</em> of B and A - B means A is the <em>daughter</em> of B, which of the following means C is the <em>niece</em> of D ?",
                        number=8,
                    ),
                    Input.Individual_Question(
                        question="If X \\circ Y means X is the <em>wife</em> of Y; X * Y means X is the <em>son</em> of Y and X \\sqaure Y means X is the <em>sister</em> of Y, which of the following would means that A is the <em>daughter</em> of B ?",
                        number=9,
                    ),
                    Input.Group(
                        parent_question="Directions : Study the information given below and answer the question that follow :<br><br>A + B means A is the <em>daughter</em> of B; A - B means A is the <em>husband</em> of B; A \\times B means A is the <em>brother</em> of B.",
                        questions=[
                            "If P + Q - R, which of the following is true ?",
                            "If P \\times Q + R, which of the following is true ?",
                            "If P + Q \\times R, which of the following is true ?",
                        ],
                        from_question=10,
                    ),
                    Input.Individual_Question(
                        question="If<ol type='A'><li>P + Q means P is the <em>brother</em> of Q;</li><li>P \\times Q means P is the <em>father</em> of Q;</li><li>P - Q means P is the <em>sister</em> of Q,<li><ol>which of the following represents S is the <em>niece</em> of T ?",
                        number=13,
                    ),
                    Input.Individual_Question(
                        question="To find out the answer to the above question, which of the statements can be dispensed with ?",
                        number=14,
                        skip=True,
                    ),
                    Input.Individual_Question(
                        question="If P + Q means P is the <em>husband</em> of Q; P \\div Q means P is the <em>sister</em> of Q and P \\times Q means P is the <em>son</em> of Q, which of the following shows A is the <em>daughter</em> of B ?",
                        number=15,
                    ),
                    Input.Individual_Question(
                        question="If X - Z means X is the <em>mother</em> of Z; X \\times Z means X is the <em>father</em> of Z and X + Z means X is the <em>daughter</em> of Z. Now, if M - N \\times T + Q, than which of the following is not true ?",
                        number=16,
                    ),
                    Input.Group(
                        parent_question="Directions : Read the following information carefully and answer the questions given below it :<br><br>A + B means A is the <em>father</em> of B; A - B means A is the <em>wife</em> of B; A \\times B means A is the <em>brother</em> of B; A \\div B means A is the <em>daughter</em> of B.",
                        questions=[
                            "If P \\div R + S + Q, which of the following is true ?",
                            "If P - R + Q, which of the following statements is true ?",
                            "If P \\times R \\div Q, which of the following statements is true ?",
                            "If P \\times R - Q, which of the following is true ?",
                            "If P + R \\div Q, which of the following is true ?",
                            "If P \\div R + Q, which of the following is true ?",
                            "If P \\times R + Q, which of the following is true ?",
                            "If P - R \\times Q, which of the following is true ?",
                        ],
                        from_question=17,
                    ),
                ],
            ),
        ],
    ),
]
