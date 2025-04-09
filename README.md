# Reasoning Prep for Competitive Exams with Anki and Moodle 

Practice reasoning ability questions with the help of
[Anki](https://apps.ankiweb.net/) and [Moodle](https://moodle.org/) Quizzes.

This project aggregrates reasoning abililty questions and transforms it into
importable data to be used by Anki and Moodle, which are learning software. The
questions come from [A Modern Approach to Verbal & Non-Verbal Reasoning by R.S.
Aggarwal](https://www.amazon.in/dp/9352832167), a very popular book among
Indian universities to prepare students for reasoning ability tests and exams.
These tools (Anki and Moodle) do not replace the book. They are are meant to be
used as practice material after reading the appropriate theory from the book.

## Anki

### Why use Anki over the book

- Anki can randomize question order

On the other hand, revising repeatedly from the book can make the learner more
dependent on the order of questions. Also, most books increase the difficulty
of questions in a particular exercise. Coming across questions of random
difficulty increases the preparedness for different levels of difficulty during
exams.

- Built-in timer in Anki.

- Anki's feature to bring up a question again after a short interval of time if
  the user is unable to solve it on first try.

Practicing from the book will make the learner anticipate the question if he was
about to revise one he marked as unsolved.

### Recommended way of using with Anki

1. Use Anki's import file feature to import anki.csv after running `make`
2. Set the time you wish to solve each question in:
  - Hover over the Reasoning Deck
  - Click on the gear icon that appears at the right end and click on Options.
  - In the Timers card
    - Set Maximum answer seconds to the number of seconds you wish to take to
       answer each question. Recommended time: 60 seconds.
    - Enable "Show on-screen timer"
    - Enable "Stop on-screen timer on answer"
3. Create a Custom Study Session for a particular chapter or problem type.
  - Click on a chapter or problem type subdeck.
  - Click on Custom Study.
  - Select the "Study by card state or tag" radio button.
  - Fill in 9999 in the "Select _____ cards from the deck" field.
  - Select "All cards in random order (don't reschedule)"
  - Click on "Choose Tags" and click "OK" on the resulting popup dialog.
4. Study
  - Go back to the Decks tab. Now you have a Custom Study Session to study
    random questions from that chapter or problem type. Click on it and click on
    "Study Now".
  - Solve the question displayed on the screen, decide upon an option as your
    answer and click on "Show Answer".
  - This will show the option which has the correct answer for the question.
    The timer at the bottom right of the screen will also stop. This timer will
    have the time in black if you answered the question before the maximum you set
    earlier expiring, otherwise it will be in red.
      - If you answered correctly within the maximum time, click on Easy (or
        Good) to move to the next question and (end) this question from the
        custom study session.
      - If you answered it incorrectly or took longer than the maximum time,
        firstly understand your mistake and decide how would you solve this
        question correctly next time within the maximum time and then:
          - If you answered it incorrectly but within the maximum time, click
            "Hard". This will make the question reappear later in the session.
          - If you took longer than the maximum time to answer, click "Again".
            This will make the question reappear very soon in the session. You
            can also increase the maximum time if you think there should be
            more time per question to practice.

### Screenshots
**Creating a Custom Study Session**

![creating-a-custom-study-session](https://github.com/user-attachments/assets/a708b517-eeb8-4dc9-a96f-e68de860d02a)

**Timer Options**

![timer-options](https://github.com/user-attachments/assets/25be7753-ebe5-4115-81d5-44a62292574a)

**Solve**

![solve](https://github.com/user-attachments/assets/c1008400-141e-48c8-b93b-885da5405431)

**Evaluate**

![evaluate](https://github.com/user-attachments/assets/1a24845c-b25d-48b8-bf04-8438545e6447)

## Moodle

### Why use Moodle over the book

Moodle quizzes simulate online exams.
- It allows time limits on quizzes
- Questions can be randomized
- Questions can be marked for review
- Navigation between questions is allowed
- Questions can be flagged as marked for review

### Recommended way of using with Moodle

1. Goto My courses and create a new course.
2. Import data to Moodle's question bank
  - Click on the more button and then on Question bank that appears in the menu
  - Click on the select menu that says Question currently, and select Import
  - Select Moodle XML format in File Format
  - Import the moodle.xml file, which was created on running `make` in this
    project
3. Create a quiz
  - Go back to the Course tab and enable Edit mode
  - Click on Add an activity or resource and select Quiz
  - Set preferred time limit / test duration from the Timing section
  - Click on Save and display
4. Add questions to the quiz
  - On the quiz page, go to the questions tab
  - Click on Add and select a random question
  - Select Reasoning or one of it's subcategories if you only want questions
    from a particular subcategory
  - Tick the Also show questions from subcategories checkbox
  - Click on Apply filters
  - Scroll to the bottom and select the number of questions you want to have in
    the quiz in the Number of random questions select menu
  - Click on Add random question
5. Take the quiz

### Screenshots

**Creating Question bank**

![import-questions-from-file](https://github.com/user-attachments/assets/b7a46475-56e9-4f48-a96c-6b7fdc2d2d5f)

**New Quiz**

![new-quiz](https://github.com/user-attachments/assets/c4750c7d-eebe-4ffd-9d6f-1068e83484de)

**Add Questions to Quiz**

![add-random-questions](https://github.com/user-attachments/assets/73f232b3-66cb-49f1-8032-5c9b8413a6c7)

**Taking the Quiz**

![taking-the-quiz](https://github.com/user-attachments/assets/e6b6ced2-71fa-4e23-adef-0c2357ce58fd)
