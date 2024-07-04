import streamlit as st


# Creating a title for a quiz app
st.title("Techno Trivo quiz")
st.header("Test Your Knowledge in Basics of Computer Science")

#INFO OF THE GAME
st.info("""
Welcome to Techno Trivo Quiz, where you can test your knowledge in the fascinating realm of Computer Science. This quiz comprises Multiple Choice Questions (MCQs) designed to assess your understanding of fundamental concepts.

Instructions:
- Read each question carefully.
- Select the correct answer from the given options.
- A total of 10 questions await your expertise.

Best of luck! Let's begin the journey into the world of Computer Science.
""")


# Initialize the score
if 'total_score' not in st.session_state:
    st.session_state.total_score = 0

if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0


# Display the question
# Display the question
def display_question(question, options, correct_answer, question_number):
    st.session_state.total_questions += 1
    # Display the question
    st.write(f"**Question {question_number}:** {question}")
     # Display a container for radio buttons
    options_container = st.empty()

    # Display a radio button for selecting an option
    selected_option = st.selectbox(f"Select an option for Question {question_number}:", options)

    # Display a submit button
    if st.button(f"Submit for Question {question_number}"):
        # Check if the selected option is correct
        if selected_option == correct_answer:
            st.session_state.total_score += 1  # Increment total_score for correct answers
            st.success("Correct! 🎉")
        # st.session_state.total_questions += 1
        else:
            st.error(f"Wrong! The correct answer is {correct_answer}.")

            
# question
question_1 = "Which among the following is not an operating system?"
options_1 = ["UNIX", "LINUX", "OS X", "PITEX"]
correct_answer_1 = "PITEX"


question_2= "1 Terabyte (Tb) ="
options_2="A - 1,024GB","B - 1,000 Gb","C - 1,200 Gb","D -1,275 GB"
correct_answer_2= "A - 1,024 GB"

question_3=" Which among the following is incorrectly matched?"
options_3="A LAN Local Area Network","B - WAN Wide Area Network","C - MAN Main Area Network","D - IP Internet Protocol"
correct_answer_3="C - MAN Main Area Network"

question_4="Which among the following is the shortcut key to refresh the active window in your computer system?"
options_4="A - F5","B - F9","C - F10", "D - Ctrl + P"
correct_answer_4="A - F5"


question_5="If you need to paste the contents of MS Word, which command will you give?"
options_5="A - Ctrl + A","B - Ctrl + C","C - Ctrl + V","D - Ctrl + Z"
correct_answer_5="C - Ctrl + V"

question_6="What do you call a portable computer?"
options_6="A.Laptop","Bookshop","RAM","Computer"
correct_answer_6="A.Laptop"

question_7="7What do you use to read CDs/DVDs?"
options_7="A.Monitor","B.Keyboard","C.CD/DVD PLAYER","D.Mouse"
correct_answer_7="C.CD/DVD PLAYER"

question_8="You need an internet browser to access the Internet."
options_8="A.True","B.False"
correct_answer_8="A.True"

question_9="What does a Control Panel do?"
options_9="A.Controls your computer","B.Change settings","C.Play games","D.None of the above"
correct_answer_9="B.Change settings"

question_10="What is the most used search engine ?"
options_10="A.Yahoo","B.Bing","C.Google","D.SOSO"
correct_answer_10="C.Google"



# Display the question with options and submit button
display_question(question_1, options_1, correct_answer_1, question_number=1)
display_question(question_2,options_2,correct_answer_2,question_number=2)
display_question(question_3,options_3,correct_answer_3,question_number=3)
display_question(question_4,options_4,correct_answer_4,question_number=4)
display_question(question_5,options_5,correct_answer_5,question_number=5)
display_question(question_6,options_6,correct_answer_6,question_number=6)
display_question(question_7,options_7,correct_answer_7,question_number=7)
display_question(question_8,options_8,correct_answer_8,question_number=8)
display_question(question_9,options_9,correct_answer_9,question_number=9)
display_question(question_10,options_10,correct_answer_10,question_number=10)


# Calculate the total score
total_score = st.session_state.total_score

# Display the total score
st.info(f"Total Score: {total_score}/10")

# Display pass/fail message
if st.session_state.total_questions == 10:  # Check if all questions are attempted
    if total_score == 10: 
        st.success("Congratulations! You have passed the test.")
