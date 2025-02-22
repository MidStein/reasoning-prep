import models.Input as Input

TYPES: list[Input.Type] = [
    Input.Type(
        type_name="LETTER CODING",
        cases=[
            Input.Case(
                case_name="To form the code for another word (CODING)",
                items=[
                    Input.Individual_Question(
                        question="If in a certain language, MADRAS is coded as NBESBT, how is bombay coded in that code ?",
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
                        question="If DIAMOND is coded as VQYMKLV, how is FEMALE coded ?",
                        number=39,
                    ),
                    Input.Individual_Question(
                        question="Which of the followsing words would be correctly decode the word ZHOFRPH if the simple alphabet shifting code is used ?",
                        number=40,
                    ),
                    Input.Group(
                        parent_question="Directions : Below, the word EXPAND has been written four different codes by applying four different rules which are given as four alternatives against it. In each of the questions which follow, a word has been written in one of these codes. Find the alternative applicable to each word and mark your answer.<br>EXPAND<br>(a) FYQBOE	(b) EPDTCR	(c) GYRBPE (d) CWNZLC",
                        questions=[
                            "CONSULATE	FVDPZYUWL",
                            "PERCIEVE	NDPBCHTD",
                            "MUSHROOM	KTQGPNML",
                            "MICROWAVE	FXDATXJQV",
                            "HARMONIOUS	FZPLMMGNSR",
                            "TRAVELLER	USBWFMMFS",
                            "TRANSLATE	USBOTMBUF",
                            "HURRICANE	JVTSKDCOG",
                            "EARTHQUAKE	FBSUIRVBLF",
                            "CONSULT	EPPTWMV",
                        ],
                        from_question=41,
                    ),
                ],
            ),
        ],
    ),
]
