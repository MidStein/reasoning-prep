import models.Input as Input

TYPES: list[Input.Type] = [
    Input.Type(
        type_name="Letter Coding",
        cases=[
            Input.Case(
                case_name="To form the code for another word (Coding)",
                items=[
                    Input.IndividualQuestion(
                        question="If in a certain language, MADRAS is coded as NBESBT, how is BOMBAY coded in that code ?",
                        number=1,
                    ),
                    Input.IndividualQuestion(
                        question="if in a certain code, TRIPLE is written as sqhokd. How is DISPOSE written in that code ?",
                        number=2,
                    ),
                    Input.IndividualQuestion(
                        question="If in a code language, COULD is written as BNTKC and MARGIN is written as LZQFHM, how will MOULDING be written in that code ?",
                        number=3,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, MONKEY is written as XDJMNL. How is TIGER written in that code ?",
                        number=4,
                    ),
                    Input.IndividualQuestion(
                        question="If FRAGRANCE is written as SBHSBODFG, how can IMPOSING be written ?",
                        number=5,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, COMPUTER is written as RFUVQNPC. How is MEDICINE written in the same code ?",
                        number=6,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, GAMBLE is coded as FBLCKF, how is FLOWER coded in that code ?",
                        number=7,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, NATURE is coded as MASUQE, how is FAMINE code in that code ?",
                        number=8,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain code, TEACHER is written as VGCEJGT, how would DULLARD be written in the same code ?",
                        number=9,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language FASHION is coded as FOIHSAN, how is PROBLEM coded in that code ?",
                        number=10,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language KINDLE is coded as ELDNIK, how is EXOTIC coded in that code ?",
                        number=11,
                    ),
                    Input.IndividualQuestion(
                        question="If VICTORY is coded as YLFWRUB, how can SUCCESS be coded ?",
                        number=12,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, TOGETHER is written as RQEGRJCT. In the same code, PAROLE will be written as",
                        number=13,
                    ),
                    Input.IndividualQuestion(
                        question="If BOMBAY is written as MYMYMY, how will TAMIL NADU be written in that code ?",
                        number=14,
                    ),
                    Input.IndividualQuestion(
                        question="If FRIEND is coded as HUMJTK, how is CANDLE written in that code ?",
                        number=15,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, COUNSEL is coded as BITIRAK, how is GUIDANCE written in that code ?",
                        number=16,
                    ),
                    Input.IndividualQuestion(
                        question="If HEATER is written as KBDQHO, how will you encode COOLER ?",
                        number=17,
                    ),
                    Input.IndividualQuestion(
                        question="In a code, CORNER is written as GSVRIV. How can CENTRAL be written in that code ?",
                        number=18,
                    ),
                    Input.IndividualQuestion(
                        question="If MADRAS can be written as ARSARS, how can ARKONAM be written in that code ?",
                        number=19,
                    ),
                    Input.IndividualQuestion(
                        question="If JOSEPH is coded as FKOALD, then GEORGE will be coded as",
                        number=20,
                    ),
                    Input.IndividualQuestion(
                        question="If POND is coded as RSTL, how is HEAR written in that code ?",
                        number=21,
                    ),
                    Input.IndividualQuestion(
                        question="If TABLE is coded as GZYOV, how is JUICE coded ?",
                        number=22,
                    ),
                    Input.IndividualQuestion(
                        question="If CERTAIN is coded as XVIGZRM, how can MUNDANE be coded ?",
                        number=23,
                    ),
                    Input.IndividualQuestion(
                        question="If DELHI is coded as CCIDD, how would you encode BOMBAY ?",
                        number=24,
                    ),
                    Input.IndividualQuestion(
                        question="According to a military code, SYSTEM is SYSMET and NEARER is AENRER. What is code for FRACTION ?",
                        number=25,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, INSTITUTION is written as NOITUTITSNI. How is PERFECTION written in that code ?",
                        number=26,
                    ),
                    Input.IndividualQuestion(
                        question="If BELIEF is written as afkkdi, how is SELDOM written in that code ?",
                        number=27,
                    ),
                    Input.IndividualQuestion(
                        question="In a code language, DISTANCE is written as IDTUBECN and DOCUMENT is written as ODDVNTNE. How is THURSDAY written in that language ?",
                        number=28,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain language, CHAMPION is coded as HCMAIPNO, how is NEGATIVE coded in that code ?",
                        number=29,
                    ),
                    Input.IndividualQuestion(
                        question="If PEOPLE is coded as PLPOEE, how is TREND coded ?",
                        number=30,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, MUNICIPALITY is written as INMUAPCIYTLI. How is JUDICIAL written in that code ?",
                        number=31,
                    ),
                    Input.IndividualQuestion(
                        question="If CIGARETTE is coded as GICERAETT, then DIRECTION will be coded as",
                        number=32,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, PAPER is written as SCTGW. How is MOTHER written in that code ?",
                        number=33,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, SUBSTITUTION is written as ITSBUSNOITUT. How is DISTRIBUTION written in that code ?",
                        number=34,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code ADVENTURES is written as TDRESAUVEN. How is SURPRISING wirtten in that code ?",
                        number=35,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, EXPLAINING is written as PXEALNIGNI. How is PRODUCED written in that code ?",
                        number=36,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, GIGANTIC is written as GIGTANCI. How is MIRACLES written in that code ?",
                        number=37,
                    ),
                    Input.IndividualQuestion(
                        question="If CONTRIBUTE is written as ETBUIRNTOC, which letter will be the sixth place when counted from the left if POPULARISE is written in that code ?",
                        number=38,
                    ),
                    Input.IndividualQuestion(
                        question="If DIAMOND is coded as VRYMKLV, how is FEMALE coded ?",
                        number=39,
                    ),
                    Input.IndividualQuestion(
                        question="Which of the following words would correctly decode the word ZHOFRPH if the simple alphabet shifting code is used ?",
                        number=40,
                    ),
                    Input.Group(
                        parent_question="Directions : Below, the word EXPAND has been written four different codes by applying four different rules which are given as four alternatives against it. In the question which follow, a word has been written in one of these codes. Find the alternative applicable to each word and mark your answer.<br><br>EXPAND<br><br>(a) FYQBOE<br>(b) EPDTCR<br>(c) GYRBPE<br>(d) CWNZLC<br>",
                        questions=[
                            "CONSULATE<br>FVDPZYUWL",
                            "PERCIEVE<br>NDPBCHTD",
                            "MUSHROOM<br>KTQGPNML",
                            "MICROWAVE<br>FXDATXJQV",
                            "HARMONIOUS<br>FZPLMMGNSR",
                            "TRAVELLER<br>USBWFMMFS",
                            "TRANSLATE<br>USBOTMBUF",
                            "HURRICANE<br>JVTSKDCOG",
                            "EARTHQUAKE<br>FBSUIRVBLF",
                            "CONSULT<br>EPPTWMV",
                        ],
                        from_question=41,
                        no_options=True,
                    ),
                ],
            ),
            Input.Case(
                case_name="To find the word by analysing the given code (Decoding)",
                items=[
                    Input.IndividualQuestion(
                        question="If in a certain language, POPULAR is coded as QPQVMBS, which word would be coded as GBNPVT ?",
                        number=1,
                    ),
                    Input.IndividualQuestion(
                        question="If ROBUST is coded as QNATRS in a certain langauge, which word would be coded as ZXCMP ?",
                        number=2,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, UTENSIL is coded as WVGPUKN, which word would be coded as DMSFXG ?",
                        number=3,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain code, SWITCH is written as TVJSDG, which word would be written as CQFZE ?",
                        number=4,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, REFRIGERATOR is coded as ROTAREGIRFER. Which word would be coded as NOITINUMMA ?",
                        number=5,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain langauge, REMOTE is coded as ROTEME. which word would be coded as PNIICC ?",
                        number=6,
                    ),
                    Input.IndividualQuestion(
                        question="If FULFNHW is the code for CRICKET, then EULGH is the code for which word ?",
                        number=7,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, SHIFT is coded as RFFBO, which word would be coded as LKUMB ?",
                        number=8,
                    ),
                    Input.IndividualQuestion(
                        question="If LBAEHC is the code for BLEACH, then which of the following is coded as NBOLZKMH ?",
                        number=9,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, GRASP is coded as BMVNK, which word would be coded as CRANE ?",
                        number=10,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain code, COVET is written as FRYHW, whihch word would be written as SHDUO ?",
                        number=11,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, TRIANGLE is coded as SQHZMFKD, which word would be coded as DWZLOKD ?",
                        number=12,
                    ),
                    Input.IndividualQuestion(
                        question="If ELCSUM is the code for MUSCLE, which word has the code LATIPAC ?",
                        number=13,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, ITNIETAM is the code for INTIMATE, which word has the the code TREVNIETARBI ?",
                        number=14,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, DIUGNAL is the code for LANGUID, which word would be coded as ELKCAHS ?",
                        number=15,
                    ),
                    Input.IndividualQuestion(
                        question="If EHFNRQ is the code for BECKON, which word has the code QDFWXULQ ?",
                        number=16,
                    ),
                    Input.IndividualQuestion(
                        question="If QKKQUGQL is the code for OMISSION, which word is coded as RYVIWZB ?",
                        number=17,
                    ),
                    Input.IndividualQuestion(
                        question="If QOSCFLBJO is the code for PORCELAIN, which word is coded as BLMOURPPZ ?",
                        number=18,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain code, ALMIRAH is written as BNPMWGO, which word would be written as DNRWLUA ?",
                        number=19,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, MACHINE is coded as LBBIHOD, which word would be coded as SLTMFNB ?",
                        number=20,
                    ),
                    Input.IndividualQuestion(
                        question="If NARGRUED is the code for GRANDEUR, which word is coded as SERPEVRE ?",
                        number=21,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, CALCUTTA is coded as GEPGYXXE, which word would be coded as FSQFCE ?",
                        number=22,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Number Coding",
        cases=[
            Input.Case(
                case_name="When numerical code values are assigned to words",
                items=[
                    Input.IndividualQuestion(
                        question="If DELHI is coded as 73541 and CALCUTTA as 82589662, how can CALICUT be coded ?",
                        number=1,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, RIPPLE is written as 613382 and LIFE is written as 8192. How is PILLER written in that code ?",
                        number=2,
                    ),
                    Input.IndividualQuestion(
                        question="If ROSE is coded as 6821, CHAIR is coded as 73456 and PREACH is coded as 961473, what will be the code for SEARCH ?",
                        number=3,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain code, TWENTY is written as 863985 and ELEVEN is written as 323039, how is TWELVE written in that code ?",
                        number=4,
                    ),
                    Input.IndividualQuestion(
                        question="If the letters in PRABA are coded as 27595, and THILAK are coded as 368451, how can BHARATHI be coded ?",
                        number=5,
                    ),
                    Input.IndividualQuestion(
                        question="If GIVE is coded as 5137 and BAT is coded as 924, how is GATE coded ?",
                        number=6,
                    ),
                    Input.IndividualQuestion(
                        question="If PALE is coded as 2134, EARTH is coded as 41590, how is PEARL coded in that code ?",
                        number=7,
                    ),
                    Input.Group(
                        parent_question="Directions : If in a certain language, ENTRY is coded as 12345 and STEADY is coded as 931785, then state which is the correct code for the given word.",
                        questions=[
                            "TENANT",
                            "NEATNESS",
                            "SEDATE",
                            "ARREST",
                            "ENDEAR",
                        ],
                        from_question=8,
                    ),
                    Input.IndividualQuestion(
                        question="If ENGLAND is written as 1234526 and FRANCE is written as 785291, how is GREECE coded ?",
                        number=13,
                    ),
                    Input.Group(
                        parent_question="Directions : If in a certain language CHARCOAL is coded as 45164913 and MORALE is coded as 296137, how is the following word coded in that language ?",
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
                        from_question=14,
                    ),
                    Input.IndividualQuestion(
                        question="If SHARP is coded as 58034 and PUSH as 4658, then RUSH is coded as",
                        number=22,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code GARIMA is written as 725432 and TINA as 6482. How is MARTINA written in that code ?",
                        number=23,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, RIPSLE is written as 613082 and WIFE is written as 4192, how is PEWSLE written in that code ?",
                        number=24,
                    ),
                    Input.Group(
                        parent_question="Directions : If MISTAKE is coded as 9765412 and NAKED is coded as 84123, how is the following word coded ?",
                        questions=[
                            "DISTANT",
                            "NEMISES",
                            "ASSIST",
                            "INTIMATE",
                            "STAIN",
                        ],
                        from_question=25,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain language 24685 is written as 33776. How is 35791 written in that code ?",
                        number=30,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain language 35796 is written as 44887. How is 46823 written in that code ?",
                        number=31,
                    ),
                    Input.IndividualQuestion(
                        question="If MINJUR is coded as 312547 and TADA as 6898, how can MADURAI be coded ?",
                        number=32,
                    ),
                    Input.IndividualQuestion(
                        question="If PALAM could be given the code number 43, what code number can be given to SANTACRUZ ?",
                        number=33,
                    ),
                    Input.IndividualQuestion(
                        question="If Z = 52 and ACT = 48, then BAT will be equal to",
                        number=34,
                    ),
                    Input.IndividualQuestion(
                        question="If REASON is coded as 5 and BELIEVED as 7, what is the code number for GOVERNMENT ?",
                        number=35,
                    ),
                    Input.IndividualQuestion(
                        question="If GO = 32, SHE = 49, then SOME will be equal to",
                        number=36,
                    ),
                    Input.IndividualQuestion(
                        question="If AT = 20, BAT = 40, then CAT will be equal to",
                        number=37,
                    ),
                    Input.IndividualQuestion(
                        question="If MACHINE is coded as 19-7-9-14-15-20-11, how will you code DANGER ?",
                        number=38,
                    ),
                    Input.IndividualQuestion(
                        question="If PRATAP could be given the code number 1618120116, what code number can be given to NAVIN ?",
                        number=39,
                    ),
                    Input.IndividualQuestion(
                        question="If MOBILITY is coded as 46293927, then EXAMINATION is coded as",
                        number=40,
                    ),
                    Input.IndividualQuestion(
                        question="If MASTER is coded as 411259, then POWDER will be coded as",
                        number=41,
                    ),
                ],
            ),
            Input.Case(
                case_name="NUMBER to Letter Coding",
                items=[
                    Input.IndividualQuestion(
                        question="In a certain code, 15789 is written as EGKPT and 2346 is written as ALUR. How is 23549 written in that code ?",
                        number=1,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, a number 13479 is written as AQFJL and 5268 is written as DMPN. How is 396824 written in that code ?",
                        number=2,
                    ),
                    Input.Group(
                        parent_question="Directions : The number in the question below is to be codified in the following code :<br><table><tr><td>Digit</td><td>7</td><td>2</td><td>1</td><td>5</td><td>3</td><td>9</td><td>8</td><td>6</td><td>4</td></tr><tr><td>Letter</td><td>W</td><td>L</td><td>M</td><td>S</td><td>I</td><td>N</td><td>D</td><td>J</td><td>B</td></tr></table>",
                        questions=[
                            "184632",
                            "879341",
                            "64928",
                        ],
                        from_question=3,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, 15789 is written as AXBTC, 2346 is written as MPDU. How is 23549 written in that code ?",
                        number=6,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, 15789 is written as XTZAL and 2346 is written as NPSU. how is 23549 written in that code ?",
                        number=7,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, 33946 is coded as PPOAL and 1987 is coded as ROSE. How is 94678 coded in that code ?",
                        number=8,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, 943 is coded as BED and 12448 is coded as SWEET, how is 492311 coded in that language ?",
                        number=9,
                    ),
                    Input.Group(
                        parent_question="Directions : In a certain language, the numbers are coded as follows :<br><table><tr><td>4</td><td>3</td><td>9</td><td>2</td><td>1</td><td>6</td><td>7</td><td>8</td><td>5</td><td>2</td><td>0</td></tr><tr><td>A</td><td>W</td><td>P</td><td>Q</td><td>R</td><td>B</td><td>E</td><td>S</td><td>G</td><td>J</td><td>M</td></tr></table><br>How is the following figure coded in that code ?",
                        questions=[
                            "421665",
                            "67825",
                            "55218",
                            "91352",
                            "720435",
                            "6650",
                            "3215",
                            "67852",
                            "439216",
                        ],
                        from_question=10,
                    ),
                    Input.Group(
                        parent_question="Directions : In a certain languaage, 36492 is written as SMILE and 058 is written as RUN. How is the following figure coded in that language ?",
                        questions=[
                            "33980",
                            "6458",
                            "92486",
                            "54324",
                            "90089",
                            "3245",
                            "29463",
                        ],
                        from_question=19,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Matrix Coding",
        cases=[
            Input.Case(
                items=[
                    Input.Group(
                        parent_question="Directions : In the following questions, a word is represented by only one set of numbers as given in any of the alternatives. The sets of numbers given in the alternatives are represented by two classes of alphabets as in the two given matrices. The columns and rows of matrix I are numbered from 0 to 4 and that of matrix II from 5 to 9. A letter from these matrices can bre represented first by its row and next by column number e.g., in the matrices for question 1, A can be represented by 13, 23 etc. T can be represented by 58, 65 etc. Similary, you have to identify the set for the word given in the question",
                        questions=[
                            "<table><caption>Matrix I</caption><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>D</td><td>K</td><td>A</td><td>E</td><td>C</td></tr><tr><td>1</td><td>C</td><td>D</td><td>K</td><td>A</td><td>E</td></tr><tr><td>2</td><td>K</td><td>C</td><td>E</td><td>A</td><td>D</td></tr><tr><td>3</td><td>K</td><td>C</td><td>D</td><td>E</td><td>A</td></tr><tr><td>4</td><td>E</td><td>D</td><td>A</td><td>K</td><td>C</td></tr></table><br><table><caption>Matrix II</caption><tr><td></td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>5</td><td>P</td><td>L</td><td>O</td><td>T</td><td>N</td></tr><tr><td>6</td><td>T</td><td>P</td><td>N</td><td>L</td><td>O</td></tr><tr><td>7</td><td>P</td><td>N</td><td>T</td><td>O</td><td>L</td></tr><tr><td>8</td><td>O</td><td>N</td><td>T</td><td>P</td><td>L</td></tr><tr><td>9</td><td>L</td><td>O</td><td>P</td><td>N</td><td>T</td></tr></table><br>COLD",
                            "<table><caption>Matrix I</caption><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>A</td><td>C</td><td>E</td><td>D</td><td>K</td></tr><tr><td>1</td><td>D</td><td>K</td><td>A</td><td>C</td><td>E</td></tr><tr><td>2</td><td>C</td><td>E</td><td>D</td><td>K</td><td>A</td></tr><tr><td>3</td><td>K</td><td>A</td><td>C</td><td>E</td><td>D</td></tr><tr><td>4</td><td>E</td><td>D</td><td>K</td><td>A</td><td>C</td></tr></table><br><table><caption>Matrix II</caption><tr><td></td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>5</td><td>T</td><td>O</td><td>P</td><td>N</td><td>L</td></tr><tr><td>6</td><td>N</td><td>L</td><td>T</td><td>O</td><td>P</td></tr><tr><td>7</td><td>O</td><td>P</td><td>N</td><td>L</td><td>T</td></tr><tr><td>8</td><td>L</td><td>T</td><td>O</td><td>P</td><td>N</td></tr><tr><td>9</td><td>P</td><td>N</td><td>L</td><td>T</td><td>O</td></tr></table>POND",
                            "<table><caption>Matrix I</caption><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>E</td><td>A</td><td>T</td><td>S</td><td>H</td></tr><tr><td>1</td><td>A</td><td>H</td><td>T</td><td>E</td><td>S</td></tr><tr><td>2</td><td>E</td><td>H</td><td>A</td><td>S</td><td>T</td></tr><tr><td>3</td><td>H</td><td>E</td><td>A</td><td>T</td><td>S</td></tr><tr><td>4</td><td>S</td><td>H</td><td>T</td><td>A</td><td>E</td></tr></table><br><table><caption>Matrix II</caption><tr><td></td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>5</td><td>O</td><td>R</td><td>K</td><td>L</td><td>P</td></tr><tr><td>6</td><td>L</td><td>P</td><td>O</td><td>R</td><td>K</td></tr><tr><td>7</td><td>O</td><td>K</td><td>R</td><td>P</td><td>L</td></tr><tr><td>8</td><td>P</td><td>R</td><td>K</td><td>L</td><td>O</td></tr><tr><td>9</td><td>R</td><td>L</td><td>K</td><td>O</td><td>P</td></tr></table>REAP",
                        ],
                        from_question=1,
                    ),
                    Input.Group(
                        parent_question="Directions : In the following question, a word is represented by only one set of numbers as given in any of the alternatives. The sets of numbers given in the alternatives are represented by two classes of alphabets as in the two given matrices. The columns and rows of matrix I are numbered from 0 to 4 and that of matrix II from 5 to 9. A letter from these matrices can bre represented first by its row and next by column number e.g., in the matrices for question 1, A can be represented by 13, 23 etc. T can be represented by 58, 65 etc. Similary, you have to identify the set for the word given in the question.<br><br><table><caption>Matrix I</caption><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>E</td><td>A</td><td>H</td><td>T</td><td>S</td></tr><tr><td>1</td><td>A</td><td>T</td><td>S</td><td>H</td><td>E</td></tr><tr><td>2</td><td>E</td><td>S</td><td>T</td><td>H</td><td>A</td></tr><tr><td>3</td><td>T</td><td>H</td><td>A</td><td>E</td><td>S</td></tr><tr><td>4</td><td>S</td><td>T</td><td>H</td><td>E</td><td>A</td></tr></table><br><table><caption>Matrix II</caption><tr><td></td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>5</td><td>I</td><td>P</td><td>L</td><td>K</td><td>R</td></tr><tr><td>6</td><td>K</td><td>R</td><td>I</td><td>L</td><td>P</td></tr><tr><td>7</td><td>I</td><td>R</td><td>K</td><td>L</td><td>P</td></tr><tr><td>8</td><td>K</td><td>R</td><td>I</td><td>P</td><td>L</td></tr><tr><td>9</td><td>R</td><td>K</td><td>L</td><td>P</td><td>I</td></tr></table>",
                        questions=[
                            "RISK",
                            "STEP",
                        ],
                        from_question=4,
                    ),
                    Input.Group(
                        parent_question="Directions : In the following question, a word is represented by only one set of numbers as given in any of the alternatives. The sets of numbers given in the alternatives are represented by two classes of alphabets as in the two given matrices. The columns and rows of matrix I are numbered from 0 to 4 and that of matrix II from 5 to 9. A letter from these matrices can bre represented first by its row and next by column number e.g., in the matrices for question 1, A can be represented by 13, 23 etc. T can be represented by 58, 65 etc. Similary, you have to identify the set for the word given in the question.<br><br><table><caption>Matrix I</caption><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>F</td><td>A</td><td>N</td><td>O</td><td>I</td></tr><tr><td>1</td><td>I</td><td>O</td><td>F</td><td>A</td><td>N</td></tr><tr><td>2</td><td>A</td><td>N</td><td>O</td><td>I</td><td>F</td></tr><tr><td>3</td><td>O</td><td>F</td><td>I</td><td>N</td><td>A</td></tr><tr><td>4</td><td>N</td><td>I</td><td>A</td><td>F</td><td>O</td></tr></table><br><table><caption>Matrix II</caption><tr><td></td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>5</td><td>S</td><td>E</td><td>H</td><td>B</td><td>T</td></tr><tr><td>6</td><td>H</td><td>S</td><td>E</td><td>T</td><td>B</td></tr><tr><td>7</td><td>B</td><td>T</td><td>S</td><td>E</td><td>H</td></tr><tr><td>8</td><td>E</td><td>H</td><td>T</td><td>B</td><td>S</td></tr><tr><td>9</td><td>T</td><td>S</td><td>E</td><td>H</td><td>B</td></tr></table>",
                        questions=[
                            "NEST",
                            "FAITH",
                            "FINE",
                            "HEAT",
                            "BOTH",
                        ],
                        from_question=6,
                    ),
                    Input.Group(
                        parent_question="Directions : In the following question, a word is represented by only one set of numbers as given in any of the alternatives. The sets of numbers given in the alternatives are represented by two classes of alphabets as in the two given matrices. The columns and rows of matrix I are numbered from 0 to 4 and that of matrix II from 5 to 9. A letter from these matrices can bre represented first by its row and next by column number e.g., in the matrices for question 1, A can be represented by 13, 23 etc. T can be represented by 58, 65 etc. Similary, you have to identify the set for the word given in the question.<br><br><table><caption>Matrix I</caption><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td>D</td><td>O</td><td>B</td><td>A</td><td>I</td></tr><tr><td>1</td><td>O</td><td>B</td><td>A</td><td>I</td><td>D</td></tr><tr><td>2</td><td>B</td><td>A</td><td>I</td><td>D</td><td>O</td></tr><tr><td>3</td><td>A</td><td>I</td><td>D</td><td>O</td><td>B</td></tr><tr><td>4</td><td>I</td><td>D</td><td>O</td><td>B</td><td>A</td></tr></table><br><table><caption>Matrix II</caption><tr><td></td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>5</td><td>W</td><td>N</td><td>R</td><td>M</td><td>L</td></tr><tr><td>6</td><td>N</td><td>R</td><td>M</td><td>L</td><td>W</td></tr><tr><td>7</td><td>R</td><td>M</td><td>L</td><td>W</td><td>N</td></tr><tr><td>8</td><td>M</td><td>L</td><td>W</td><td>N</td><td>R</td></tr><tr><td>9</td><td>L</td><td>W</td><td>N</td><td>R</td><td>M</td></tr></table>",
                        questions=[
                            "DRAW",
                            "BAND",
                            "BLOW",
                            "RAIN",
                            "LAMB",
                        ],
                        from_question=11,
                    ),
                    Input.Group(
                        parent_question="Directions : In the following questions, a word is represented by only one set of numbers as given in any of the alternatives. The sets of numbers given in the alternatives are represented by two classes of alphabets as in the two given matrices. The columns and rows of matrix I are numbered from 0 to 4 and that of matrix II from 5 to 9. A letter from these matrices can bre represented first by its row and next by column number e.g., in the matrices for question 1, A can be represented by 13, 23 etc. T can be represented by 58, 65 etc. Similary, you have to identify the set for the word given in the question.<br><br><table><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>I</td><td>L</td><td>B</td><td>P</td><td>K</td><td>N</td><td>H</td><td>S</td><td>A</td><td>E</td></tr><tr><td>1</td><td>M</td><td>A</td><td>Q</td><td>G</td><td>T</td><td>V</td><td>I</td><td>O</td><td>N</td><td>U</td></tr><tr><td>2</td><td>H</td><td>R</td><td>W</td><td>J</td><td>A</td><td>X</td><td>B</td><td>E</td><td>C</td><td>I</td></tr><tr><td>3</td><td>T</td><td>Y</td><td>A</td><td>I</td><td>U</td><td>U</td><td>O</td><td>N</td><td>J</td><td>F</td></tr><tr><td>4</td><td>F</td><td>O</td><td>B</td><td>M</td><td>E</td><td>G</td><td>U</td><td>K</td><td>W</td><td>R</td></tr><tr><td>5</td><td>A</td><td>C</td><td>L</td><td>J</td><td>X</td><td>R</td><td>A</td><td>A</td><td>X</td><td>T</td></tr><tr><td>6</td><td>P</td><td>S</td><td>U</td><td>E</td><td>Z</td><td>K</td><td>V</td><td>W</td><td>D</td><td>L</td></tr><tr><td>7</td><td>Z</td><td>D</td><td>Y</td><td>V</td><td>F</td><td>O</td><td>H</td><td>Y</td><td>I</td><td>O</td></tr><tr><td>8</td><td>M</td><td>I</td><td>Z</td><td>Q</td><td>E</td><td>A</td><td>U</td><td>E</td><td>I</td><td>S</td></tr><tr><td>9</td><td>P</td><td>E</td><td>O</td><td>E</td><td>E</td><td>U</td><td>Q</td><td>O</td><td>C</td><td>G</td></tr></table>",
                        questions=[
                            "MIND",
                            "JAIL",
                            "BLOT",
                            "JOKE",
                            "OMIT",
                        ],
                        from_question=16,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Substitution",
        cases=[
            Input.Case(
                items=[
                    Input.IndividualQuestion(
                        question="If <em>white</em> is called <em>blue</em>, <em>blue</em> is called <em>red</em>, <em>red</em> is called <em>yellow</em>, <em>yellow</em> is called <em>green</em>, <em>green</em> is called <em>black</em>, <em>black</em> is called <em>violet</em> and <em>violet</em> is called <em>orange</em>, what would be the colour of human blood ?",
                        number=1,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>room</em> is called <em>bed</em>, <em>bed</em> is called <em>window</em>, <em>window</em> is called <em>flower</em> and <em>flower</em> is called <em>cooler</em>, on what would a man sleep ?",
                        number=2,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>orange</em> is called <em>butter</em>, <em>butter</em> is called <em>soap</em>, <em>soap</em> is called <em>ink</em>, <em>ink</em> is called <em>honey</em> and <em>honey</em> is called <em>orange</em>, which of the following is used for washing clothes ?",
                        number=3,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>sand</em> is called <em>air</em>, <em>air</em> is called <em>plateu</em>, <em>plateu</em> is called <em>well</em>, <em>well</em> is called <em>island</em> and <em>island</em> is called <em>sky</em>, then from where will a woman draw water ?",
                        number=4,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>bangle</em> is called <em>cassette</em>, <em>cassette</em> is called <em>table</em>, <em>table</em> is called <em>game</em> and <em>game</em> is called <em>cupboard</em>, then which is played in the tape recorder ?",
                        number=5,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>green</em> means <em>red</em>, <em>red</em> means <em>yellow</em>, <em>yellow</em> means <em>blue</em>, <em>blue</em> means <em>orange</em> and <em>orange</em> means <em>green</em>, what is the colour of clear sky ?",
                        number=6,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>cloud</em> is called <em>white</em>, <em>white</em> is called <em>rain</em>, <em>rain</em> is called <em>green</em>, <em>gren</em> is called <em>air</em>, <em>air</em> is called <em>blue</em> and <em>blue</em> is called <em>water</em>, where will the birds fly ?",
                        number=7,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>book</em> is called <em>watch</em>, <em>watch</em> is called <em>bag</em>, <em>bag</em> is called <em>dictionary</em> and <em>dictionary</em> is called <em>window</em>, which is used to carry the books ?",
                        number=8,
                    ),
                    Input.IndividualQuestion(
                        question="If the animals which can walk are called <em>swimmers</em>, animals who crawl are called <em>flying</em>, those living in water are called <em>snakes</em> and those which fly in the sky are called <em>hunters</em>, then what will a lizard be called ?",
                        number=9,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>rain</em> is <em>water</em>, <em>water</em> is <em>road</em>, <em>road</em> is <em>cloud</em>, <em>cloud</em> is <em>sky</em>, <em>sky</em> is <em>sea</em> and <em>sea</em> is <em>path</em>, where do aeroplanes fly ?",
                        number=10,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>water</em> is called <em>food</em>, <em>food</em> is called <em>tree</em>, <em>tree</em> is called <em>sky</em>, <em>sky</em> is called <em>wall</em>, on which of the following grows a fruit ?",
                        number=11,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>water</em> is called <em>blue</em>, <em>blue</em> is called <em>red</em>, <em>red</em> is called <em>white</em>, <em>white</em> is called <em>sky</em>, <em>sky</em> is called <em>rain</em>, rain si caled green and <em>green</em> is called <em>air</em>, which of the following if the colour of milk ?",
                        number=12,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>paper</em> is called <em>wood</em>, <em>wood</em> is called <em>straw</em>, <em>straw</em> is called <em>grass</em>, <em>grass</em> is called <em>rubber</em> and <em>rubber</em> is called <em>cloth</em>, what is the furniture made up of ?",
                        number=13,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>pen</em> is <em>table</em>, <em>table</em> is <em>fan</em>, <em>fan</em> is <em>chair</em> and <em>chair</em> is <em>roof</em>, on which of the following will a person sit ?",
                        number=14,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>bat</em> is called <em>racket</em>, <em>racket</em> is <em>football</em>, <em>football</em> is <em>shuttle</em>, <em>shuttle</em> is <em>ludo</em> and <em>ludo</em> is <em>carrom</em>, what is cricket played with ?",
                        number=15,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>banana</em> is <em>apple</em>, <em>apple</em> is <em>grapes</em>, <em>graphs</em> is <em>mango</em>, <em>mango</em> is <em>nuts</em>, <em>nuts</em> is <em>guava</em>, which of the following is a yellow fruit ?",
                        number=16,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>air</em> is called <em>green</em>, <em>green</em> is called <em>bule</em>, <em>blue</em> is called <em>sky</em>, <em>sky</em> is called <em>yello</em>, <em>yellow</em> is called <em>water</em> and <em>water</em> is called <em>pink</em>, then what is the colour of clear sky ?",
                        number=17,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>cushion</em> is called <em>pillow</em>, <em>pillow</em> is called <em>mat</em>, <em>mat</em> is called <em>bedsheet</em> and <em>bedsheet</em> is called <em>cover</em>, which will be spread on the floor ?",
                        number=18,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>wall</em> is called <em>window</em>, <em>window</em> is called <em>door</em>, <em>door</em> is called <em>fllor</em>, <em>floor</em> is called <em>roof</em> and <em>roof</em> is called <em>ventilator</em>, what will a person stand on ?",
                        number=19,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>eraser</em> is called <em>box</em>, <em>box</em> is called <em>pencil</em>, <em>pencil</em> is called <em>sharpener</em> and <em>sharpener</em> is called <em>bag</em>, what will a child write with ?",
                        number=20,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>clock</em> is called <em>television</em>, <em>television</em> is called <em>radio</em>, <em>radio</em> is called <em>oven</em>, <em>oven</em> is called <em>grinder</em> and <em>grinder</em> is called <em>iron</em>, in what will a lady bake ?",
                        number=21,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>sky</em> is called <em>sea</em>, <em>sea</em> is called <em>water</em>, <em>water</em> is called <em>air</em>, <em>air</em> is called <em>cloud</em> and <em>acloud</em> is called <em>river</em>, then what do we drink when thirsty ?",
                        number=22,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>man</em> is called <em>girl</em>, <em>girl</em> is called <em>woman</em>, <em>woman</em> is called <em>boy</em>, <em>boy</em> is called <em>butler</em> and <em>butler</em> is called <em>rogue</em>, who will serve in a restaurant ?",
                        number=23,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>train</em> is called <em>bus</em>, <em>bus</em> is called <em>tractor</em>, <em>tractor</em> is called <em>car</em>, <em>cari</em> is called <em>scooter</em>, <em>scooter</em> is called <em>bicycle</em>, <em>bicycle</em> is called <em>moped</em>, which is used to plough a field ?",
                        number=24,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>lead</em> is called <em>stick</em>, <em>stick</em> is called <em>nib</em>, <em>nib</em> is called <em>needle</em>, <em>needle</em> is called <em>rope</em> and <em>rope</em> is called <em>thread</em>, what will be fitted in a pen to write with it ?",
                        number=25,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>rose</em> is called <em>popy</em>, <em>popy</em> is called <em>lily</em>, <em>lily</em> is called <em>lotus</em> and <em>lotus</em> is called <em>glandiola</em>, which is the king of flowers ?",
                        number=26,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>rat</em> is called <em>dog</em>, <em>dog</em> is called <em>mongoose</em>, <em>mongoose</em> is called <em>lion</em>, <em>lion</em> is called <em>snake</em> and <em>snake</em> is called <em>elephant</em>, which is reared as a pet ?",
                        number=27,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>finger</em> is called <em>toe</em>, <em>toe</em> is called <em>foot</em>, <em>foot</em> is called <em>thumb</em>, <em>thumb</em> is called <em>ankle</em>, <em>ankle</em> is called <em>palm</em> and <em>palm</em> is called <em>knee</em>, which one finger has a different name ?",
                        number=28,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Mixed Letter Coding",
        cases=[
            Input.Case(
                items=[
                    Input.IndividualQuestion(
                        question="If <em>'ish lto inm'</em> stands for <em>'neat and tidy'</em>; <em>'qpr inm sen'</em> stands for <em>'small but neat'</em> and <em>'hsm sen rso'</em> stands for <em>'good but erratic'</em>, what would <em>'but'</em> stand for ?",
                        number=1,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, <em>'nee tim see'</em> means <em>'how are you'</em>; <em>'ble nee see'</em> means <em>'where are you'</em>, what is the code for <em>'where'</em> ?",
                        number=2,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code langauge, <em>'col tip mot'</em> means <em>'singing is appreciable'</em>; <em>'mot baj min'</em> means <em>'dancing is good'</em> and <em>'tip nop baj'</em> means <em>'singing and dancing'</em>, which of the following means <em>'good'</em> in that language ?",
                        number=3,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>'ski rps tri'</em> stands for <em>'nice Sunday morning'</em>; <em>'teh sti rps'</em> stands for <em>'every Tuesday morning'</em> and <em>'ski ptr qlm'</em> stands for <em>'nice market place'</em>, what would <em>'Sunday'</em> stand for ?",
                        number=4,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, <em>'bi nie pie'</em> means <em>'some good jokes'</em>; <em>'nie bat lik'</em>; means <em>'some real stories'</em>; <em>'pie lik tol'</em> means <em>'many good stories'</em>. Which word in that code means <em>'jokes'</em> ?",
                        number=5,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain language, <em>'pre nat bis'</em> means <em>'smoking is harmful'</em>; <em>'vog dor nat'</em> means <em>'avoid harmful habit'</em> and <em>'dor bis yel'</em> means <em>'please avoid smoking'</em>. Which of the following means <em>'habit'</em> in that language ?",
                        number=6,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>'gnr tag zog qmp'</em> stands for <em>'Seoul Olympic Organising Committee'</em>; <em>'hyto gnr emf'</em> stands for <em>'summer Olympic games'</em> and <em>'esm sdr hyto'</em> stands for <em>'modern games history'</em>, what would be the code for <em>'summer'</em> ?",
                        number=7,
                    ),
                    Input.IndividualQuestion(
                        question="If in a certain language, <em>'oka peru'</em> means <em>'fine cloth'</em>; <em>'meta lisa'</em> means <em>'clear water'</em> and <em>'dona lisa peru'</em> means <em>'fine clear weather'</em>, which word in that language means <em>'weather'</em> ?",
                        number=8,
                    ),
                    Input.IndividualQuestion(
                        question="In a code language, <em>'mok dan sil'</em> means <em>'nice big house'</em>; <em>'fit kon dan'</em> means <em>'house is good'</em> and <em>'warm tir fit'</em> means <em>'cost is high'</em>. Which word stands for <em>'good'</em> in that language ?",
                        number=9,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain language, <em>'Mink Yang Pe'</em> means <em>'Fruits are ripe'</em>; <em>'Pe Lao May Mink'</em> means <em>'Oranges are not ripe'</em> and <em>'May Pe Nue Mink'</em> means <em>'Mangoes are not ripe'</em>. Which word in that language means <em>'Mangoes'</em> ?",
                        number=10,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'Tom Kun Sud'</em> means <em>'Dogs are barking'</em>; <em>'Kun Jo Mop'</em> means <em>'Dogs and horses'</em> and <em>'Mut Tom Ko'</em> means <em>'Donkeys are mad'</em>. Which word in that language means <em>'barking'</em> ?",
                        number=11,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'put tir fin'</em> means <em>'delicious juicy fruit'</em>; <em>'tie dip sig'</em> means <em>'beautiful white lily'</em> and <em>'sig lon fin'</em> means '<em>lily and fruit'</em>. Which of the following stands for <em>'and'</em> in that language ?",
                        number=12,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>'nitco sco tingo'</em> stands for <em>'softer than flower'</em>; <em>'tingo rho mst'</em> stands for <em>'sweet flower fragrance'</em> and <em>'mst sco tmp'</em> stadns for <em>'sweet than smile'</em>, what would <em>'fragrance'</em> stand for ?",
                        number=13,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'dom pul ta'</em> means <em>'bring hot foot'</em>; <em>'pul tir sop'</em> means <em>'food is good'</em> and <em>'tak da sop'</em> means <em>'good bright boy'</em>. Which of the following does mean <em>'hot'</em> in that language ?",
                        number=14,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>'sti nro kti'</em> stands for <em>'clouds pour down'</em>; <em>'nro bsi mit'</em> stands for <em>'down he goes'</em> and <em>'bsi nro zpi'</em> stands for <em>'died down he'</em>, which word would mean <em>'goes'</em> ?",
                        number=15,
                    ),
                    Input.Group(
                        parent_question="Directions :<br>In a certain code language,<br>(A) <em>'pit dar na'</em> means <em>'you are good'</em>;<br>(B) <em>'dar tok pa'</em> means <em>'good and bad'</em>;<br>(C) <em>'tim na tok'</em> means <em>'they are bad'</em>.",
                        questions=[
                            "In that language, which word stands for <em>'they'</em> ?",
                            "To find the answer to the above question, which of the following statements can be dispensed with ?",
                        ],
                        from_question=16,
                    ),
                    Input.Group(
                        parent_question="Directions :<br>In a certain code language,<br>(A) <em>'pic vic nic'</em> means <em>'winter is cold'</em>;<br>(B) <em>'to nic re'</em> means <em>'summer is hot'</em>;<br>(C) <em>'re pic boo'</em> means <em>'winter and summer'</em>;<br>(D) <em>'vic tho pa'</em> means <em>'nights are code'</em>.",
                        questions=[
                            "Which word in that language means <em>'summer'</em> ?",
                            "Which of the given statements is superfluous ?",
                        ],
                        from_question=18,
                        skip=True,
                    ),
                    Input.Group(
                        parent_question="Directions :<br>In a certain code language,<br>(A) <em>'pit na som'</em> means <em>'bring me water'</em>;<br>(B) <em>'na jo tod'</em> means <em>'water is life'</em>;<br>(C) <em>'tub od pit'</em> means <em>'give me toy'</em>.<br>(D) <em>'jo lin kot'</em> means <em>'life and death'</em>.",
                        questions=[
                            "Which of the following represents <em>'is'</em> in that language ?",
                            "To find the answer to the above question, which of the following statements can be dispensed with ?",
                        ],
                        from_question=20,
                    ),
                    Input.Group(
                        parent_question="Directions :<br>In a certain code language,<br>(A) <em>'mxy das zci'</em> means <em>'good little frock'</em>;<br>(B) <em>'jmx cos zci'</em> means <em>'girl behaves good'</em>;<br>(C) <em>'nvg drs cos'</em> means <em>'girl makes mischief'</em><br>(D) <em>'das ajp cos'</em> means <em>'little girl fell'</em>.",
                        questions=[
                            "Which word in that language stands for <em>'frock'</em> ?",
                            "Which of the given statements is superfluous ?",
                        ],
                        from_question=22,
                        skip=True,
                    ),
                    Input.Group(
                        parent_question="Directions :<br>In a certain code language,<br>(A) <em>'pod na joc'</em> means <em>'very bright boy'</em>;<br>(B) <em>'tam nu pod'</em> means <em>'the boy comes'</em>;<br>(C) <em>'nu per ton'</em> means <em>'keep the doll'</em>;<br>(D) <em>'joc ton su'</em> means <em>'very good doll'</em>.",
                        questions=[
                            "Which of the following means <em>'bright'</em> in that language ?",
                            "Which of the following statements can be dispensed with for answering the above quetsion ?",
                        ],
                        from_question=24,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'po ki top ma'</em> means <em>'Usha is playing cards'</em>; <em>'kop ja ki ma'</em> means <em>'Asha is playing tennis'</em>; <em>'ki top sop ho'</em> means <em>'they are playing football'</em>; and <em>'po sur kop'</em> means <em>'cards and tennis'</em>. Which word in that language means <em>'Asha'</em> ?",
                        number=26,
                    ),
                    Input.Group(
                        parent_question="Directions :<br>In a certain code language,<br>(A) <em>'Kemp Lamp Tems'</em> means <em>'Speak the truth'</em>;<br>(B) <em>'Bis Tim Nak'</em> means <em>'Always seek knowledge'</em>;<br>(C) <em>'Tim Tems Sik'</em> means <em>'Knowledge is truth'</em>;<br>(D) <em>'Lik Bis Zap'</em> means <em>'Never seek violence'</em>.",
                        questions=[
                            "Which letter code stands for <em>'Always'</em> ?",
                            "To find the answer to the above question, which of the given statements is not necessary ?",
                        ],
                        from_question=27,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'nee muk pic'</em> means <em>'grave and concern'</em>; <em>'ill dic so'</em> means <em>'every body else'</em>; and <em>'tur muk so'</em> means <em>'body and soul'</em>. Which of the following would mean <em>'every concern'</em> ?",
                        number=29,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'Ka Bi Pu Ya'</em> means <em>'You are very intelligent'</em>; <em>'Ya Lo Ka Wo'</em> means <em>'They seem very intelligent'</em>; <em>'La Pu Le'</em> means <em>'You can see'</em> and <em>'Sun Pun Yun Ya'</em> means <em>'How intelligent she is'</em>. In that language which of the following words means <em>'are'</em> ?",
                        number=30,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'bir le nac'</em> means <em>'green and tasty'</em>; <em>'pic nac hor'</em> means <em>'tomato is green'</em> and <em>'coc bir hor'</em> means <em>'food is tasty'</em>. Which of the following means <em>'tomato is tasty'</em> in that code ?",
                        number=31,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'kew xas huma deko'</em> means <em>'she is eating apples'</em>; <em>'kew tepo qua'</em> means <em>'she sells toys'</em> and <em>'sul lim deko'</em> means <em>'I like apples'</em>. Which word in that language means <em>'she'</em> and <em>'apples'</em> ?",
                        number=32,
                    ),
                    Input.IndividualQuestion(
                        question="If <em>'cinto baoli tsi nzro'</em> means <em>'her village is Sarurpur'</em>; <em>'mhi cinto keepi tsi oind'</em> means <em>'her first love is literature'</em> and <em>'oind geit tsi cinto pki'</em> means <em>'literature collection is her hobby'</em>, which word would mean <em>'literature'</em> ?",
                        number=33,
                    ),
                    Input.Group(
                        parent_question="Questions :<br>In a certain code, <em>'il be pee'</em> means <em>'roses are blue'</em>; <em>'sik hee'</em> means <em>'red flowers'</em> and <em>'pee mit hee'</em> means <em>'flowers are vegetables'</em>.",
                        questions=[
                            "How is <em>'red'</em> written in that code ?",
                            "How is <em>'roses'</em> written in that code ?",
                            "How is <em>'vegetables are red flowers'</em> written in that code ?",
                        ],
                        from_question=34,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Mixed Number Coding",
        cases=[
            Input.Case(
                items=[
                    Input.IndividualQuestion(
                        question="In a certain code, '37' means <em>'which class'</em> and '583' means <em>'caste and class'</em>. What is the code for <em>'caste'</em> ?",
                        number=1,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, '743' means <em>'mangoes are good'</em>; '657' means <em>'eat good food'</em> and '934' means <em>'mangoes are ripe'</em>. Which digit means <em>'ripe'</em> in that language ?",
                        number=2,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, '134' means <em>'good and tasty'</em>; '478' means <em>'see good pictures'</em> and '729' means <em>'pictures are faint'</em>. Which of the following digit stands for <em>'see'</em> ?",
                        number=3,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, '247' means <em>'spread red carpet'</em>; '256' means <em>'dust one carpet'</em> and '234' means <em>'one red carpet'</em>. Which digit in that code means <em>'dust'</em> ?",
                        number=4,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, '123' means <em>'bright little boy'</em>, '145' means <em>'tall big boy'</em> and '637' means <em>'beautiful little flower'</em>. Which digit in that language means <em>'bright'</em> ?",
                        number=5,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, '256' means <em>'you are good'</em>; '637' means <em>'we are bad'</em> and '358' means <em>'good and bad'</em>. Which of the following represents <em>'and'</em> in that code ?",
                        number=6,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, '467' means <em>'leaves are green'</em>; '485' means <em>'green is good'</em> and '639' means <em>'they are playing'</em>. Which digit stands for <em>'leaves'</em> in that code ?",
                        number=7,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, '851' means <em>'good sweet fruit'</em>; '783' means <em>'good red rose'</em> and '341' means <em>'rose and fruit'</em>. Which of the following digit stands for <em>'sweet'</em> in that language ?",
                        number=8,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, '479' means <em>'fruit is sweet'</em>; '248' means <em>'very sweet voice'</em> and '637' means <em>'eat fruit daily'</em>. Which digit stands for <em>'is'</em> in that code ?",
                        number=9,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, '123' means <em>'hot filtered coffee'</em>; '356' means <em>'very hot day'</em> and '589' means <em>'day and night'</em>. Which digit stands for <em>'very'</em> ?",
                        number=10,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, '256' means <em>'red colour chalk'</em>; '589' means <em>'green colour flower'</em> and '245' means <em>'white colour chalk'</em>. Which digit in that code means <em>'white'</em> ?",
                        number=11,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code langauge, '526' means <em>'sky is blue'</em>; '24' means <em>'blue colour'</em> and '436' means <em>'colour is fun'</em>. Which digit in that language means <em>'fun'</em> ?",
                        number=12,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, '381' means <em>'Hari is honest'</em>; '162' means <em>'Shashi is intelligent'</em> and '948' means <em>'Hari should go'</em>. Which digit in that language means <em>'honest'</em> ?",
                        number=13,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, '253' means <em>'books are old'</em>; '546' means <em>'man is old'</em> and '378' means <em>'buy good books'</em>. What stands for <em>'are'</em> in that code ?",
                        number=14,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code, '975' means <em>'Throw away garbage'</em>; '528' means <em>'Give away smoking'</em> and '213' means <em>'Smoking is harmful'</em>. Which digit in that code means <em>'Give'</em> ?",
                        number=15,
                    ),
                    Input.Group(
                        parent_question="Directions :<br>In a certain code '289' means <em>'read from paper'</em>; '276' means <em>'tea from field'</em> and '85' means <em>'wall paper'</em>.",
                        questions=[
                            "Which of the following is the code for <em>'tea'</em> ?",
                            "Which of the following is the code for <em>'paper'</em> ?",
                        ],
                        from_question=16,
                    ),
                    Input.Group(
                        parent_question="Directions :<br>(A) '134' means <em>'you are well'</em>;<br>(B) '758' means <em>'they go home'</em>;<br>(C) '839' means <em>'we are home'</em>.",
                        questions=[
                            "Which of the following represents 'they' in that code language ?",
                            "Which of the statements can be dispensed with while answering the above question ?",
                        ],
                        from_question=18,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, '617' means <em>'sweet and hot'</em>; '735' means <em>'coffee is sweet'</em> and '263' means <em>'tea is hot'</em>. Which of the following would mean 'coffee is hot' ?",
                        number=20,
                    ),
                    Input.IndividualQuestion(
                        question="In a certain code language, <em>'3a, 2b, 7c'</em> means <em>'Truth is Eternal'</em>; <em>'7c, 9a, 8b, 3a'</em> means <em>'Enmity is not Eternal'</em> and <em>'9a, 4d, 2b, 8b'</em> means <em>'Truth does not perish'</em>. Which of the following means <em>'enmity'</em> in that language ?",
                        number=21,
                    ),
                ],
            ),
        ],
    ),
    Input.Type(
        type_name="Deciphering Individual Letter Codes by Analysis",
        cases=[
            Input.Case(
                skip=True,
                items=[
                    Input.Group(
                        parent_question="Directions : According to a code language, words in capital letters in column I are written in small letters in column II. The letters in column II are jumbled up. Decode the language and choose the correct code for the word given in the question.<br><br><table><thead><tr><th>Column I</th><th>Column II</th></tr></thead><tbody><tr><td>(1) CURSE</td><td>(A) opkif</td></tr><tr><td>(2) INCUR</td><td>(B) fbpoc</td></tr><tr><td>(3) TALLY</td><td>(C) ughvg</td></tr><tr><td>(4) CADET</td><td>(D) rkufh</td></tr><tr><td>(5) DRIP</td><td>(E) rotc</td></tr><tr><td>(6) TOIL</td><td>(F) jugc</td></tr><tr><td>(7) RACE</td><td>(G) vwoh</td></tr></tbody></table>",
                        questions=[
                            "DAIRY",
                            "TODAY",
                            "PIECE",
                            "CIVIL",
                            "SUSTAIN",
                            "TRIED",
                            "RACE",
                            "ENVOY",
                            "REVET",
                            "SUN",
                        ],
                        from_question=1,
                    ),
                    Input.Group(
                        parent_question="Directions : According to a code language, words in capital letters in column I are written in small letters in column II. The letters in column II are jumbled up. Decode the language and choose the correct code for the word given in each question.<br><br><table><thead><tr><th>Column I</th><th>Column II</th></tr></thead><tbody><tr><td>(1) SOUND</td><td>(A) abi</td></tr><tr><td>(2) ADDRESS</td><td>(B) cjmv</td></tr><tr><td>(3) CRUX</td><td>(C) ikmop</td></tr><tr><td>(4) NET</td><td>(D) ijktv</td></tr><tr><td>(5) CRONY</td><td>(E) jkgotv</td></tr><tr><td>(6) CROWDY</td><td>(F) blooppv</td></tr></tbody></table>",
                        questions=[
                            "A",
                            "C",
                            "D",
                            "N",
                            "O",
                            "R",
                            "S",
                            "T",
                        ],
                        from_question=11,
                    ),
                    Input.Group(
                        parent_question="Directions : According to a code language, words in capital letters in column I are written in small letters in column II. The letters in column II are jumbled up. Decode the language and choose the correct code for the word given in each question.<br><br><table><thead><tr><th>Column I</th><th>Column II</th></tr></thead><tbody><tr><td>(1) TAPE</td><td>(A) moij</td></tr><tr><td>(2) COUP</td><td>(B) lhhpok</td></tr><tr><td>(3) TIE</td><td>(C) nls</td></tr><tr><td>(4) ROTATE</td><td>(D) nhpk</td></tr><tr><td>(5) SAY</td><td>(E) nkpl</td></tr><tr><td>(6) TREAT</td><td>(F) msr</td></tr><tr><td>(7) YEAR</td><td>(G) khlph</td></tr><tr><td>(8) SIP</td><td>(H) hrp</td></tr><tr><td>(9) TYRE</td><td>(I) pmlh</td></tr></tbody></table>",
                        questions=[
                            "SOUP",
                            "REACT",
                            "TRACE",
                            "POSSESS",
                            "CREATE",
                            "EASY",
                            "CURE",
                        ],
                        from_question=19,
                    ),
                    Input.Group(
                        parent_question="Directions : According to a code language, words in capital letters in column I are written in small letters in column II. The letters in column II are jumbled up. Decode the language and choose the correct code for the word given in each question.<br><br><table><thead><tr><th>Column I</th><th>Column II</th></tr></thead><tbody><tr><td>(1) BID</td><td>(A) nnrw</td></tr><tr><td>(2) BAT</td><td>(B) emps</td></tr><tr><td>(3) BAD</td><td>(C) lwz</td></tr><tr><td>(4) CHEAP</td><td>(D) aejmnq</td></tr><tr><td>(5) HILL</td><td>(E) kms</td></tr><tr><td>(6) PORK</td><td>(F) emrux</td></tr><tr><td>(7) QUOTE</td><td>(G) ehqr</td></tr><tr><td>(8) ROSE</td><td>(H) iotx</td></tr><tr><td>(9) VEX</td><td>(I) aceenoww</td></tr><tr><td>(10) WAVE</td><td>(J) elu</td></tr><tr><td>(11) NAMELY</td><td>(K) befms</td></tr><tr><td>(12) FAMILIAR</td><td>(L) moty</td></tr><tr><td>(13) HAZY</td><td>(M) elz</td></tr><tr><td>(14) VAGUE</td><td>(N) dfmtu</td></tr></tbody></table>",
                        questions=[
                            "B",
                            "C",
                            "D",
                            "F",
                            "G",
                            "H",
                            "A",
                            "K",
                            "M",
                            "Z",
                        ],
                        from_question=26,
                        # letters C and E both have u as the code letter
                        skip=True,
                    ),
                    Input.Group(
                        parent_question="Directions : According to a code language, words in capital letters in column I are written in small letters in column II. The letters in column II are jumbled up. Decode the language and choose the correct code for the word given in each question.<br><br><table><thead><tr><th>Column I</th><th>Column II</th></tr></thead><tbody><tr><td>(1) CHIEF</td><td>(A) knqwy</td></tr><tr><td>(2) NIGHT</td><td>(B) akwjh</td></tr><tr><td>(3) THIRD</td><td>(C) kvhwg</td></tr><tr><td>(4) MONEY</td><td>(D) njumz</td></tr><tr><td>(5) WOMAN</td><td>(E) zcjms</td></tr><tr><td>(6) WORKS</td><td>(F) ctvzo</td></tr><tr><td>(7) BASIC</td><td>(G) dtwsq</td></tr><tr><td>(8) HENRY</td><td>(H) jvunk</td></tr><tr><td>(9) BASED</td><td>(I) gstnd</td></tr><tr><td>(10) PSYCO</td><td>(J) qutzb</td></tr><tr><td>(11) TOWEL</td><td>(K) nzche</td></tr><tr><td>(12) FALSE</td><td>(L) ynest</td></tr><tr><td>(13) DOWRY</td><td>(M) cvguz</td></tr><tr><td>(14) STOCK</td><td>(N) toqhz</td></tr><tr><td>(15) TRAIN</td><td>(O) swhvj</td></tr></tbody></table>",
                        questions=[
                            "AUGUST",
                            "BOARD",
                            "JUNIOR",
                            "DIGEST",
                            "DEAF",
                        ],
                        from_question=36,
                    ),
                    Input.Group(
                        parent_question="Directions : In each of the following questions, a word has been written in four different code languages. One of the code languages is common to all the five quetsions. The code equivalent of the word in that code language is your answer in each question.",
                        questions=[
                            "CLUSTER",
                            "LIGHT",
                            "TRIVIAL",
                            "NUMBER",
                            "BRAVE",
                        ],
                        from_question=41,
                        skip=True,
                    ),
                ],
            ),
        ],
    ),
]
