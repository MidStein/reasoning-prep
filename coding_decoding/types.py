import models.Input as Input

TYPES: list[Input.Type] = [
    Input.Type(
        type_name="LETTER CODING",
        cases=[
            Input.Case(
                case_name="To form the code for another word (CODING)",
                items=[
                    Input.Individual_Question(
                        question="If in a certain language, MADRAS is coded as NBESBT, how is BOMBAY coded in that code ?",
                        number=1,
                    ),
                    Input.Individual_Question(
                        question="if in a certain code, TRIPPLE is written as sqhokd. How is DISPOSE written in that code ?",
                        number=2,
                    ),
                    Input.Individual_Question(
                        question="If in a code language, COULD is written as BNTKC and MARGIN is written as LZQFHM, how will MOULDING be written in that code ?",
                        number=3,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, MONKEY is written as XDJMNL. How is TIGER written in that code ?",
                        number=4,
                    ),
                    Input.Individual_Question(
                        question="If FRAGRANCE is written as SBHSBODFG, how can IMPOSING be written ?",
                        number=5,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, COMPUTER is written as RFUVQNPC. How is MEDICINE written in the same code ?",
                        number=6,
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, GAMBLE is coded as FBLCKF, how is FLOWER coded in that code ?",
                        number=7,
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, NATURE is coded as MASUQE, how is FAMINE code in that code ?",
                        number=8,
                    ),
                    Input.Individual_Question(
                        question="If in a certain code, TEACHER is written as VGCEJGT, how would DULLARD be written in the same code ?",
                        number=9,
                    ),
                    Input.Individual_Question(
                        question="If in a certain language FASHION is coded as FOIHSAN, how is PROBLEM coded in that code ?",
                        number=10,
                    ),
                    Input.Individual_Question(
                        question="If in a certain language KINDLE is coded as ELDNIK, how is EXOTIC coded in that code ?",
                        number=11,
                    ),
                    Input.Individual_Question(
                        question="If VICTORY is coded as YLFWRUB, how can SUCCESS be coded ?",
                        number=12,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, TOGETHER is written as RQEGRJCT. In the same code, PAROLE will be written as",
                        number=13,
                    ),
                    Input.Individual_Question(
                        question="If BOMBAY is written as MYMYMY, how will TAMIL NADU be written in that code ?",
                        number=14,
                    ),
                    Input.Individual_Question(
                        question="If FRIEND is coded as HUMJTK, how is CANDLE written in that code ?",
                        number=15,
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, COUNSEL is coded as BITIRAK, how is GUIDANCE written in that code ?",
                        number=16,
                    ),
                    Input.Individual_Question(
                        question="If HEATER is written as KBDQHO, how will you encode COOLER ?",
                        number=17,
                    ),
                    Input.Individual_Question(
                        question="In a code, CORNER is written as GSVRIV. How can CENTRAL be written in that code ?",
                        number=18,
                    ),
                    Input.Individual_Question(
                        question="If MADRAS can be written as ARSARS, how can ARKONAM be written in that code ?",
                        number=19,
                    ),
                    Input.Individual_Question(
                        question="If JOSEPH is coded as FKOALD, then GEORGE will be coded as",
                        number=20,
                    ),
                    Input.Individual_Question(
                        question="If POND is coded as RSTL, how is HEAR written in that code ?",
                        number=21,
                    ),
                    Input.Individual_Question(
                        question="If TABLE is coded as GZYOV, how is JUICE coded ?",
                        number=22,
                    ),
                    Input.Individual_Question(
                        question="If CERTAIN is coded as XVIGZRM, how can MUNDANCE be coded ?",
                        number=23,
                    ),
                    Input.Individual_Question(
                        question="If DELHI is coded as CCIDD, how would you encode BOMBAY ?",
                        number=24,
                    ),
                    Input.Individual_Question(
                        question="According to a military code, SYSTEM is SYSMET and NEARER is AENRER. What is code for FRACTION ?",
                        number=25,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, INSTITUTION is written as NOITUTITSNI. How is PERFECTION written in that code ?",
                        number=26,
                    ),
                    Input.Individual_Question(
                        question="If BELIEF is written as afkkdi, how is SELDOM written in that code ?",
                        number=27,
                    ),
                    Input.Individual_Question(
                        question="In a code language, DISTANCE is written as IDTUBECN and DOCUMENT is written as ODDVNTNE. How is THURSDAY written in that language ?",
                        number=28,
                    ),
                    Input.Individual_Question(
                        question="In a certain language, CHAMPION is coded as HCMAIPNO, how is NEGATIVE coded in that code ?",
                        number=29,
                    ),
                    Input.Individual_Question(
                        question="If PEOPLE is coded as PLPOEE, how is TREND coded ?",
                        number=30,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, MUNICIPALITY is written as INMUAPCIYTLI. How is JUDICIAL written in that code ?",
                        number=31,
                    ),
                    Input.Individual_Question(
                        question="If CIGARETTE is coded as GICERAETT, then DIRECTION will be coded as",
                        number=32,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, PAPER is written as SCTGW. How is MOTHER written in that code ?",
                        number=33,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, SUBSTITUTION is written as ITSBUSNOITUT. How is DISTRIBUTION written in that code ?",
                        number=34,
                    ),
                    Input.Individual_Question(
                        question="In a certain code ADVENTURES is written as TDRESAUVEN. How is SURPRISING wirtten in that code ?",
                        number=35,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, EXPLAINING is written as PXEALNIGNI. How is PRODUCED written in that code ?",
                        number=36,
                    ),
                    Input.Individual_Question(
                        question="In a certain code, GIGANTIC is written as GIGTANCI. How is MIRACLES written in that code ?",
                        number=37,
                    ),
                    Input.Individual_Question(
                        question="If CONTRIBUTE is written as ETBUIRNTOC, which letter will be the sixth place when counted from the left if POPULARISE is written in that code ?",
                        number=38,
                    ),
                    Input.Individual_Question(
                        question="If DIAMOND is coded as VRYMKLV, how is FEMALE coded ?",
                        number=39,
                    ),
                    Input.Individual_Question(
                        question="Which of the following words would correctly decode the word ZHOFRPH if the simple alphabet shifting code is used ?",
                        number=40,
                    ),
                    Input.Group(
                        parent_question="Directions : Below, the word EXPAND has been written four different codes by applying four different rules which are given as four alternatives against it. In each of the questions which follow, a word has been written in one of these codes. Find the alternative applicable to each word and mark your answer.\n\nEXPAND\n\n(a) FYQBOE\n(b) EPDTCR\n(c) GYRBPE\n(d) CWNZLC\n",
                        questions=[
                            "CONSULATE\nFVDPZYUWL",
                            "PERCIEVE\nNDPBCHTD",
                            "MUSHROOM\nKTQGPNML",
                            "MICROWAVE\nFXDATXJQV",
                            "HARMONIOUS\nFZPLMMGNSR",
                            "TRAVELLER\nUSBWFMMFS",
                            "TRANSLATE\nUSBOTMBUF",
                            "HURRICANE\nJVTSKDCOG",
                            "EARTHQUAKE\nFBSUIRVBLF",
                            "CONSULT\nEPPTWMV",
                        ],
                        from_question=41,
                        no_options=True
                    ),
                ],
            ),
            Input.Case(
                case_name="To find the word by analysing the given code (DECODING)",
                items=[
                    Input.Individual_Question(
                        question="If in a certain language, POPULAR is coded as QPQVMBS, which word would be coded as GBNPVT ?",
                        number=1
                    ),
                    Input.Individual_Question(
                        question="If ROBUST is coded as QNATRS in a certain langauge, which word would be coded as ZXCMP ?",
                        number=2
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, UTENSIL is coded as WVGPUKN, which word would be coded as DMSFXG ?",
                        number=3
                    ),
                    Input.Individual_Question(
                        question="If in a certain code, SWITCH is written as TVJSDG, which word would be written as CQFZE ?",
                        number=4
                    ),
                    Input.Individual_Question(
                        question="In a certain code, REFRIGERATOR is coded as ROTAREGIRFER. Which word would be coded as NOITINUMMA ?",
                        number=5
                    ),
                    Input.Individual_Question(
                        question="If in a certain langauge, REMOTE is coded as ROTEME. which word would be coded as PNIICC ?",
                        number=6
                    ),
                    Input.Individual_Question(
                        question="If FULFNHW is the code for CRICKET, then EULGH is the code for which word ?",
                        number=7
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, SHIFT is coded as RFFBO, which word would be coded as LKUMB ?",
                        number=8
                    ),
                    Input.Individual_Question(
                        question="If LBAEHC is the code for BLEACH, then which of the following is coded as NBOLZKMH ?",
                        number=9
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, GRASP is coded as BMVNK, which word would be coded as CRANE ?",
                        number=10
                    ),
                    Input.Individual_Question(
                        question="If in a certain code, COVET is written as FRYHW, whihch word would be written as SHDUO ?",
                        number=11
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, TRIANGLE is coded as SQHZMFKD, which word would be coded as DWZLOKD ?",
                        number=12
                    ),
                    Input.Individual_Question(
                        question="If ELCSUM is the code for MUSCLE, which word has the code LATIPAC ?",
                        number=13
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, ITNIETAM is the code for INTIMATE, which word has the the code TREVNIETARBI ?",
                        number=14
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, DIUGNAL is the code for LANGUID, which word would be coded as ELKCAHS ?",
                        number=15
                    ),
                    Input.Individual_Question(
                        question="If EHFNRQ is the code for BECKON, which word has the code QDFWXULQ ?",
                        number=16
                    ),
                    Input.Individual_Question(
                        question="If QKKQUGQL is the code for OMISSION, which word is coded as RYVIWZB ?",
                        number=17
                    ),
                    Input.Individual_Question(
                        question="If QOSCFLBJO is the code for PORCELAIN, which word is coded as BLMOURPPZ ?",
                        number=18
                    ),
                    Input.Individual_Question(
                        question="If in a certain code, ALMIRAH is written as BNPMWGO, which word would be written as DNRWLUA ?",
                        number=19
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, MACHINE is coded as LBBIHOD, which word would be coded as SLTMFNB ?",
                        number=20
                    ),
                    Input.Individual_Question(
                        question="If NARGRUED is the code for GRANDEUR, which word is coded as SERPEVRE ?",
                        number=21
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, CALCUTTA is coded as GEPGYXXE, which word would be coded as FSQFCE ?",
                        number=22
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="NUMBER CODING",
        cases=[
            Input.Case(
                case_name="When numerical code values are assigned to words",
                items=[
                    Input.Individual_Question(
                        question="If DELHI is coded as 73541 and CALCUTTA as 82589662, how can CALICUT be coded ?",
                        number=1
                    ),
                    Input.Individual_Question(
                        question="In a certain code, RIPPLE is written as 613382 and LIFE is written as 8192. How is PILLER written in that code ?",
                        number=2
                    ),
                    Input.Individual_Question(
                        question="If ROSE is coded as 6821, CHAIR is coded as 73456 and PREACH is coded as 961473, what will be the code for SEARCH ?",
                        number=3
                    ),
                    Input.Individual_Question(
                        question="If in a certain code, TWENTY is written as 863985 and ELEVEN is written as 323039, how is TWELVE written in that code ?",
                        number=4
                    ),
                    Input.Individual_Question(
                        question="If the letters in PRABA are coded as 27595, and THILAK are coded as 368451, how can BHARATHI be coded ?",
                        number=5
                    ),
                    Input.Individual_Question(
                        question="If GIVE is coded as 5137 and BAT is coded as 924, how is GATE coded ?",
                        number=6
                    ),
                    Input.Individual_Question(
                        question="If PALE is coded as 2134, EARTH is coded as 41590, how is PEARL coded in that code ?",
                        number=7
                    ),
                    Input.Group(
                        parent_question="Directions : If in a certain language, ENTRY is coded as 1345 and STEADY is coded as 931785, then state which is the correct code for each of the given words.",
                        questions=[
                            "TENANT",
                            "NEATNESS",
                            "SEDATE",
                            "ARREST",
                            "ENDEAR",
                        ],
                        from_question=8,
                    ),
                    Input.Individual_Question(
                        question="If ENGLAND is written as 1234526 and FRANCE is written as 785291, how is GREECE coded ?",
                        number=13
                    ),
                    Input.Group(
                        parent_question="Directions : If in a certain language CHARCOAL is coded as 45164913 and MORALE is coded as 296137, how are the followsing words coded in that language ?",
                        questions=[
                            "REAL",
                            "ARCHER",
                            "HEARL",
                            "COACH",
                            "ALLOCHIRE",
                            "ROCHEL",
                            "COLLER",
                            "MECHRALE",
                        ],
                        from_question=14
                    ),
                    Input.Individual_Question(
                        question="If SHARP is coded as 58034 and push as 4658, then RUSH is coded as",
                        number=22
                    ),
                    Input.Individual_Question(
                        question="In a certain code GARIMA is written as 725432 and TINA as 6482. How is MARTINA written in that code ?",
                        number=23
                    ),
                    Input.Individual_Question(
                        question="In a certain code, RIPSLE is written as 613082 and WIFE is written as 4192, how is PEWSLE written in that code ?",
                        number=24
                    ),
                    Input.Group(
                        parent_question="Directions : If MISTAKE is coded as 9765412 and NAKED is coded as 84123, how are the followsing words coded ?",
                        questions=[
                            "DISTANT",
                            "NEMISES",
                            "ASSIST",
                            "INTIMATE",
                            "STAIN",
                        ],
                        from_question=25
                    ),
                    Input.Individual_Question(
                        question="In a certain language 24685 is written as 33776. How is 35791 written in that code ?",
                        number=30
                    ),
                    Input.Individual_Question(
                        question="In a certain language 35796 is written as 44887. How is 46823 written in that code ?",
                        number=31
                    ),
                    Input.Individual_Question(
                        question="If MINJUR is coded as 312547 and TADA as 6898, how can MADURAI be coded ?",
                        number=32
                    ),
                    Input.Individual_Question(
                        question="If PALAM could be given the code number 43, what code number can be given to SANTACRUZ ?",
                        number=33
                    ),
                    Input.Individual_Question(
                        question="If Z = 52 and ACT = 48, then BAT will be equal to",
                        number=34
                    ),
                    Input.Individual_Question(
                        question="If REASON is coded as 5 and BELIEVED as 7, what is the code number for GOVERNMENT ?",
                        number=35
                    ),
                    Input.Individual_Question(
                        question="If GO = 32, SHE = 49, then SOME will be equal to",
                        number=36
                    ),
                    Input.Individual_Question(
                        question="If AT = 20, BAT = 40, then CAT will be equal to",
                        number=37
                    ),
                    Input.Individual_Question(
                        question="If MACHINE is coded as 19-7-9-14-15-20-11, how will you code DANGER ?",
                        number=38
                    ),
                    Input.Individual_Question(
                        question="If PRATAP could be given the code number 1618120116, what code number can be given to NAVIN ?",
                        number=39
                    ),
                    Input.Individual_Question(
                        question="If MOBILITY is coded as 46293927, then EXAMINATION is coded as",
                        number=40
                    ),
                    Input.Individual_Question(
                        question="If MASTER is coded as 411259, then POWDER will be coded as",
                        number=41
                    ),
                ],
            ),
            Input.Case(
                case_name="NUMBER TO LETTER CODING",
                items=[
                    Input.Individual_Question(
                        question="In a certain code, 15789 is written as EGKPT and 2346 is written as ALUR. How is 23549 written in that code ?",
                        number=1
                    ),
                    Input.Individual_Question(
                        question="In a certain code, a number 13479 is written as AQFJL and 5268 is written as DMPN. How is 396824 written in that code ?",
                        number=2
                    ),
                    Input.Group(
                        parent_question="Directions : The number in each question below is to be codified in the following code :\n<table><tr><td>Digit</td><td>7</td><td>2</td><td>1</td><td>5</td><td>3</td><td>9</td><td>8</td><td>6</td><td>4</td></tr><tr><td>Letter</td><td>W</td><td>L</td><td>M</td><td>S</td><td>I</td><td>N</td><td>D</td><td>J</td><td>B</td></tr></table>", 
                        questions=[
                            "184632",
                            "879341",
                            "64928",
                        ],
                        from_question=3
                    ),
                    Input.Individual_Question(
                        question="In a certain code, 15789 is written as AXBTC, 2346 is written as MPDU. How is 23549 written in that code ?",
                        number=6
                    ),
                    Input.Individual_Question(
                        question="In a certain code, 15789 is written as XTZAL and 2346 is written as XTZAL and 2346 is written as npsu. how is 23549 written in that code ?",
                        number=7
                    ),
                    Input.Individual_Question(
                        question="In a certain code, 33946 is coded as PPOAL and 1987 is coded as ROSE. How is 94678 coded in that code ?",
                        number=8
                    ),
                    Input.Individual_Question(
                        question="If in a certain language, 943 is coded as BED and 12448 is coded as SWEET, how is 492311 coded in that language ?",
                        number=9
                    ),
                    Input.Group(
                        parent_question="Directions : In a certain language, the numbers are coded as follows :\n<table><tr><td>4</td><td>3</td><td>9</td><td>2</td><td>1</td><td>6</td><td>7</td><td>8</td><td>5</td><td>2</td><td>0</td></tr><tr><td>A</td><td>W</td><td>P</td><td>Q</td><td>R</td><td>B</td><td>E</td><td>S</td><td>G</td><td>J</td><td>M</td></tr></table>", 
                        questions=[
                            "421665",
                            "67825",
                            "5518",
                            "91352",
                            "720435",
                            "6650",
                            "3215",
                            "67852",
                            "439216",
                        ],
                        from_question=10
                    ),
                    Input.Group(
                        parent_question="Directions : In a certain languaage, 36492 is written as SMILE and 058 is written as RUN. How are the following figures coded in that language ?", 
                        questions=[
                            "33980",
                            "6458",
                            "92486",
                            "54324",
                            "90089",
                            "3245",
                            "29463",
                        ],
                        from_question=19
                    ),
                ],
            ),
        ],
    ),
]
