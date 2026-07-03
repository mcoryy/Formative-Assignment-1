# Formative Assignment: Linear Equation's Quiz
A coding tool that gives you five linear equation question's to answer. The tool will tell you whether you are right or wrong and give you a score out of five at the end.


## User Documentation

### How to Download and Run the Code


**💻 Step 1: Download the Code**

Download the files from GitHub into one folder.


**📂 Step 2: Open in VSCode**

- Open **VSCode**
- Click **File** in the top right hand corner
- click **Open Folder**
- Select the project folder


**▶️ Step 3: Run the Code**

Open the main.py file in VSCode and press the **Play** icon on the right hand side of the code.

<img width="1341" height="787" alt="Screenshot 2026-07-03 at 15 02 36" src="https://github.com/user-attachments/assets/80355489-4695-4de7-9d6a-3624efc1708e" />
Figure 1: User guide showing where the Play icon is in VSCode.

### How to Play the Quiz


**❓ Step 4: Answering the First Question**

When prompted, answer the first question in the terminal. Press **Enter** to submit. If you are incorrect, the code will prompt you to try again. You get an unlimited number of attempts until you answer correctly.


**✍️ Step 4: Answer Every Question**

Continue answering the next 4 questions. Once all have been answered correctly, the quiz will finish, letting you know your score out of 5.


**🔁 Step 5: Replay Anytime**

To replay, type "clear" in your terminal, press **Enter** and then press the play icon to run the quiz again, again and again...

<img width="1341" height="787" alt="Screenshot 2026-07-03 at 15 40 05" src="https://github.com/user-attachments/assets/6c3fb95c-6f45-4c2f-80ee-78a272a5ef10" />
Figure 2: Clearning the terminal


## Technical Documentation


### File Overview


**main.py**

Controls the entire programme.

- Imports the questions and functions from their respective files
- Runs the quiz loop
- Calculates the final score


**functions.py**

Contains the logic for the quiz

- User input prompts
- Validated user answer
- Repetition until the correct answer is given
- Returns the score, 1 point per correct question


**questions.py**

Stores the quiz data.

- Contains the questions string
- Contains the correct integer answers
- For example, ("Solve: 2x + 8 = 20", 6)

### Cloning the Repo

#### To Work with the Existing App


**Step 1: Copy and Paste the Link into Your Terminal to Create a Local Copy**

**Step 2: Open the project in VSCode**

<img width="1341" height="787" alt="Screenshot 2026-07-03 at 15 50 33" src="https://github.com/user-attachments/assets/e73e71e3-cddf-40c8-86b6-180f0bd8c883" />
Figure 4: Opening the project in VSCode

**Step 3:Run the programme**

<img width="1341" height="787" alt="Screenshot 2026-07-03 at 15 02 36" src="https://github.com/user-attachments/assets/80355489-4695-4de7-9d6a-3624efc1708e" />
Figure 5: Running the programme

**Step 4: Use 'cd' to Change Directory into Your Project Folder**

## Editing the Code

**Adding More Questions**

Edit 'questions.py'
- Add lines to the script, increasing the question number by 1 each line

**Increase Difficulty**

Create another question file:
- Different files for easy and hard questions
- Update the coding within 'main.py' to reflect where the questions should be drawn from


## Known Limitations

- Only supports integer answers
- After a correct answer the score automatically increases by one, so score is always 5/5
