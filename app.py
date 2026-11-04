import streamlit as st
import pandas as pd
import os
from datetime import datetime 

st.set_page_config(
   page_title="Studysense AI",
   page_icon="🧠",
   layout="wide"
)

st.markdown("""
<style>
/*Main application background*/
.stApp {
   background:linear-gradient(
     135deg,#0b1020 0%,#11172b 55%,#17132e 100%
   );
   color:#f1f5f9;
}

/*Main content width and spacing */
.block-container {
   max-width: 1100px;
   padding-top:2.5rem;
   padding-bottom:3rem;
}

/*Heading*/
h1,h2,h3{
   color:#f8fafc !important;
   letter-spacing:-0.5px;
}

/*Select boxes and text inputs*/
.stSelectbox div[data-baseweb="select"]>div,
.stTextInput input{
   background-color:#171f35;
   color:#f8fafc;
   border:1px solid#35415f;
   border-radius:10px;
}

/*Button*/
.stButton>button{
   background:linear-gradient(90deg,#6d5ae6,#8b5cf6);
   color:white;
   border:none;
   border-radius:10px;
   padding:0.65rem 1.3rem;
   font-weight:600;
   transition:0.2s ease;
}

.stButton>button:hover{
   border:1px solid#c4b5fd;
   color:white;
   filter:brightness(1.12);
} 

/*cards for metrics*/
div[data-testid="stMetric"]{
   background:#171f35;
   padding:18px;
   border-radius:14px;
}

/*Dividers*/
hr{
  border-color:#303b58;
}

/*Quiz questions containers*/
div[data-testid="stVerticalBlockBorderWrapper"]{
   border-color:#303b58;
   border-radius:14px;
}

/*Sidebar*/
section[data-testid="stSidebar"]{
  background-color:#0a0f1d;
}

/*Hide Streamlit's default toolbar decorations*/
#MainMenu{
 visibility:hidden;
}
footer{
  visibility:hidden;

}
</style>
""",unsafe_allow_html=True)

st.title("🧠 Studysense AI")
st.subheader("Learn smarter.Discover your potential.")
st.markdown(
   "Your personal learning dashboard for"
   "practice,performance,and progress."
)

st.divider()
st.header("🎯 Build Your Practice Session")

subject=st.selectbox(
  "Select Subject",
  ["physics","chemistry","mathematics"]
)

topic=st.text_input(
  "Enter topic",
  placeholder="e.g. Moving charges and magnetism"
)

difficulty=st.selectbox(
   "Select Difficulty",
   ["Easy"]
)

st.write(
   "Take a quiz,discover your weak topics,"
   "and improve your performance."
)

st.divider()

questions=[
  {
    "subject":"physics",
    "topic":"current electricity",
    "question":"what is the si unit of resistance?",
    "options":["ampere","volt","ohm","watt"],
    "difficulty":"Easy",
    "answer":"ohm",
    "explanaition":"Electrical resistance is the opposition offered by a conductor to the flow of electric current.Its SI unit is ohm."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"what is the SI unit of current?",
   "options":["volt","ampere","ohm","watt"],
   "difficulty":"Easy",
   "answer":"ampere",
   "explanaition":"Electric current is the rate of flow of electric charge through a conductor. Its SI unit is ampere (A)."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"According to Ohm's law,what is the relation  between voltage,current and resistance?",
   "options":["V=IR","I=VR","R=VI","V=I+R"],
   "difficulty":"Easy",
   "answer":"V=IR",
   "explanaition":"Ohm's law states that V = IR, where V is voltage, I is current and R is resistance, provided the physical conditions remain constant."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"What is the resistance of two resistors of 2 ohm and 3 ohm connected in series?",
   "options":["1 ohm","5 ohm","6 ohm","2.5 ohm"],
   "difficulty":"Easy",
   "answer":"5 ohm",
   "explanaition":"In a series combination, resistances add directly. Equivalent resistance = 2 + 3 = 5 ohm."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"What is the equivalent resistance of two 6 ohm resistors connected in parallel?",
   "options":["12 ohm","6 ohm","3 ohm","2 ohm"],
   "difficulty":"Easy",
   "answer":"3 ohm",
   "explanaition":"For two resistors in parallel, 1/R = 1/6 + 1/6 = 2/6. Therefore, equivalent resistance R = 3 ohm."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"A 12v battery is connected accross a 4 ohm resistor.What is the current?",
   "options":["2A","3A","4A","6A"],
   "difficulty":"Easy",
   "answer":"3A",
   "explanaition":"Using Ohm's law, I = V/R = 12/4 = 3 A."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"What is the SI unit of resistivity?",
   "options":["Ohm","Ohm meter","Ampere","Volt"],
   "difficulty":"Easy",
   "answer":"Ohm meter",
   "explanaition":"Resistivity is an intrinsic property of a material. Its SI unit is ohm metre (Ω m)."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"If the length of a wire is doubled while its area and material remain unchnaged,what happens to its resistance?",
   "options":["It becomes half","It doubles","It remains unchanged","it becomes four times"],
   "difficulty":"Easy",
   "answer":"It doubles",
   "explanaition":"Resistance is directly proportional to the length of a wire when its material and cross-sectional area remain constant. Doubling the length doubles the resistance."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"A charge of 20 coulombs flows through a condutor in 5 seconds.What is the current?",
   "options":["2A","4A","5A","10A"],
   "difficulty":"Easy",
   "answer":"4A",
   "explanaition":"Current is charge flowing per unit time. I = Q/t = 20/5 = 4 A."
  },
  {
   "subject":"physics",
   "topic":"current electricity",
   "question":"What is the elctric power when a current of 2A flows through a device at 5V?",
   "options":["5W","7W","10W","15W"],
   "difficulty":"Easy",
   "answer":"10W",
   "explanaition":"Electrical power is calculated using P = VI. Therefore, P = 5 × 2 = 10 W."
  },
  {
   "subject":"chemistry",
   "topic":"coordinate compound",
   "question":"what is the coordination number of cobalt in [Co(NH3)6]3+?",
   "options":["2","4","6","8"],
   "difficulty":"Easy",
   "answer":"6"
 },
 {
  "subject":"mathematics",
  "topic":"differentiation",
  "question":"what is the derivative of x2?",  "options":["x","2x","x2","2"],
  "difficulty":"Easy",
  "answer":"2x"
 }

]


import random

# -------------------------------
# PHYSICS QUESTION GENERATOR
# -------------------------------

def generate_physics_question():

    voltage = random.randint(2, 20)
    current = random.randint(1, 10)

    power = voltage * current

    options = [
        power,
        power + 5,
        max(1, power - 5),
        power + 10
    ]

    random.shuffle(options)

    return {
        "subject": "physics",
        "topic": "current electricity",
        "question": (
            f"A device operates at {voltage}V "
            f"with a current of {current}A. "
            "Calculate its electrical power."
        ),
        "options": [f"{x}W" for x in options],
        "difficulty": "Easy",
        "answer": f"{power}W",
        "explanaition": (
            f"Using P = VI, P = {voltage} x "
            f"{current} = {power}W."
        )
    }


# -------------------------------
# CHEMISTRY QUESTION GENERATOR
# -------------------------------


def generate_chemistry_question(question_type):

    if question_type == 0:
        metal, ligands, number = random.choice([
            ("Co", "NH3", 6),
            ("Ag", "NH3", 2),
            ("Pt", "NH3 and Cl", 4),
            ("Fe", "CN", 6)
        ])

        question = (
            f"What is the coordination number "
            f"of {metal} in its complex with {ligands}?"
        )
        answer = str(number)
        explanation = (
            f"The metal is attached to {number} "
            f"donor atoms. Coordination number = {number}."
        )

    elif question_type == 1:
        question = (
            "What is the oxidation state of cobalt "
            "in [Co(NH3)5Cl]Cl2?"
        )
        answer = "+3"
        explanation = (
            "NH3 is neutral and coordinated Cl has charge -1. "
            "The complex ion has charge +2, so cobalt is +3."
        )

    elif question_type == 2:
        question = "Which of these is a neutral ligand?"
        answer = "NH3"
        explanation = (
            "NH3 (ammonia) is a neutral ligand."
        )

    elif question_type == 3:
        question = "What is the charge on a cyanide ligand (CN)?"
        answer = "-1"
        explanation = (
            "Cyanide is a negatively charged ligand with charge -1."
        )

    else:
        question = (
            "What is the denticity of ethylenediamine (en)?"
        )
        answer = "2"
        explanation = (
            "Ethylenediamine has two donor atoms, "
            "so it is a bidentate ligand."
        )

    options = {
        0: ["2", "4", "6", "8"],
        1: ["+1", "+2", "+3", "+4"],
        2: ["NH3", "Cl-", "CN-", "OH-"],
        3: ["0", "-1", "+1", "-2"],
        4: ["1", "2", "3", "4"]
    }[question_type]

    random.shuffle(options)

    return {
        "subject": "chemistry",
        "topic": "coordination compounds",
        "question": question,
        "options": options,
        "difficulty": "Easy",
        "answer": answer,
        "explanaition": explanation
    }



# -------------------------------
# MATHEMATICS QUESTION GENERATOR
# -------------------------------

def generate_mathematics_question(question_type):

    if question_type == 0:
        n = random.randint(2, 6)

        question = f"What is the derivative of x^{n}?"
        answer = f"{n}x^{n-1}"
        explanation = (
            f"Using the power rule, "
            f"d(x^{n})/dx = {n}x^{n-1}."
        )

        options = [
            answer,
            f"x^{n-1}",
            f"{n}x^{n}",
            f"{n-1}x^{n}"
        ]

    elif question_type == 1:
        question = "What is the derivative of 15?"
        answer = "0"
        explanation = "The derivative of a constant is zero."

        options = ["0", "1", "15", "x"]

    elif question_type == 2:
        a = random.randint(2, 8)

        question = f"What is the derivative of {a}x?"
        answer = str(a)
        explanation = (
            f"The derivative of ax is a. "
            f"Therefore, the answer is {a}."
        )

        options = [
            str(a), str(a + 1), "0", f"{a}x"
        ]

    elif question_type == 3:
        question = "Differentiate x^2 + 3x + 2."
        answer = "2x+3"
        explanation = (
            "The derivative of x^2 is 2x, "
            "of 3x is 3, and of 2 is 0."
        )

        options = ["2x+3", "x+3", "2x+2", "x^2+3"]

    else:
        question = "What is the derivative of 3x^3?"
        answer = "9x^2"
        explanation = (
            "Using the power rule, "
            "3 x 3x^2 = 9x^2."
        )

        options = ["9x^2", "3x^2", "9x^3", "6x"]

    random.shuffle(options)

    return {
        "subject": "mathematics",
        "topic": "differentiation",
        "question": question,
        "options": options,
        "difficulty": "Easy",
        "answer": answer,
        "explanaition": explanation
    }



# -------------------------------
# GENERATE QUESTIONS
# -------------------------------

# -------------------------------
# GENERATE QUESTIONS
# -------------------------------

if "generated_questions" not in st.session_state:

    generated_questions = []

    # Generate 10 Physics questions
    for i in range(10):
        generated_questions.append(
            generate_physics_question()
        )

    # Generate 10 Chemistry questions
    for i in range(10):
        question_type = random.randint(0, 4)

        generated_questions.append(
            generate_chemistry_question(question_type)
        )

    # Generate 10 Mathematics questions
    for i in range(10):
        question_type = random.randint(0, 4)

        generated_questions.append(
            generate_mathematics_question(question_type)
        )

    st.session_state.generated_questions = generated_questions

questions.extend(st.session_state.generated_questions)


filtered_questions=[]

for q in questions:
   subject_match=(
     q["subject"].strip().lower()
     ==subject.strip().lower()
   )

   topic_match=(
     not topic.strip()
     or topic.strip().lower()in q["topic"].strip().lower()
   )

   difficulty_match=(
      q["difficulty"].strip().lower()
      ==difficulty.strip().lower()
   )

   if subject_match and topic_match and difficulty_match:
      filtered_questions.append(q)

st.header("📝 take your quiz")

answers={}

for i,q in enumerate(filtered_questions):
   st.write(f"### question{i+1}")
   st.write(q["question"])

   answers[i]= st.radio(
     "choose your answer:",
     q["options"],
     index=None,

     key=f"question_{i}"
   )
if st.button("submit quiz & analyze",type="primary"):
    correct=0
    unanswered=0

    for i,q in enumerate(filtered_questions):
        ans=answers.get(i)
        if ans is None:
            unanswered +=1
        elif ans == q["answer"]:
            correct += 1

    if unanswered > 0:
        st.warning(
            f"please answer all questions first."
            f"unanswered:{unanswered}"
                                      )
    elif len(filtered_questions) == 0:
        st.warning(
            "No questions found for these selections."
            "Try another topic or difficulty."
                                          )

    else:
        total = len(filtered_questions)
        percentage=(correct/total)*100
        # Save performance history
        history_file = "performance_history.csv"

        
        topic_scores = {}

        for i, q in enumerate(filtered_questions):
            topic_name = q["topic"]

            if topic_name not in topic_scores:
                topic_scores[topic_name] = {
                    "correct": 0,
                    "total": 0
                }

            topic_scores[topic_name]["total"] += 1

            if answers.get(i) == q["answer"]:
                topic_scores[topic_name]["correct"] += 1

        new_result = pd.DataFrame([
            {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "subject": subject,
                "topic": topic_name,
                "correct": scores["correct"],
                "total": scores["total"],
                "percentage": round(
                    scores["correct"] / scores["total"] * 100, 1
                )
            }
            for topic_name, scores in topic_scores.items()
        ])

        if os.path.exists(history_file):
            new_result.to_csv(
                history_file,
                mode="a",
                header=False,
                index=False
            )
        else:
            new_result.to_csv(
                history_file,
                index=False
            )


        # -------------------------------
        # PERSONALIZED RECOMMENDATIONS
        # -------------------------------

        st.divider()
        st.header("🧠 AI Study Recommendations")

        if percentage < 40:

            st.warning(
                "Your fundamentals need more attention."
            )

            st.write(
                "Recommendation: Revise basic concepts "
                "and study the topic again."
            )

        elif percentage < 70:

            st.info(
                "You're making progress! Keep practising."
            )

            st.write(
                "Recommendation: Solve more practice "
                "questions and review your mistakes."
            )

        else:

            st.success(
                "Excellent performance! Keep it up."
            )

            st.write(
                "Recommendation: Try challenging questions "
                "and explore advanced concepts."
            )

    st.divider()
    st.header("📊 your Performance dashboard")

    incorrect = total - correct

    col1, col2, col3, col4 = st.columns(4)

    with col1:
      st.metric(  "🎯 Accuracy",f"{percentage:.1f}%"
    )

    with col2:
      st.metric(  "📝 Attempted",total
    )

    with col3:
      st.metric(  "✅ Correct",correct
    )

    with col4:
      st.metric(  "❌ Incorrect",incorrect
    )

    st.subheader("Overall Performance")

    st.progress(percentage / 100)

    if percentage >= 80:
        st.success("Outstanding performance!")
    elif percentage >= 60:
        st.info("Good progress! Keep practising.")
    elif percentage >= 40:
        st.warning("You can improve with more practice.")
    else:
        st.error("Focus on revising your fundamentals.")


        st.divider()
        st.subheader("📖 Detailed answer Analysis")

        for i,q in enumerate(filtered_questions):

            st.write(f"### Question {i+1}")
            st.write(q["question"])

            student_answer=answers.get(i)
            correct_answer=q["answer"]

            st.write(f"Your answer:{student_answer}")
            st.write(f"correct answer:{correct_answer}")

            if student_answer==correct_answer:
              st.success("Correct answer!🎉")
            else:
              st.error("Incorrect answer.Keep learning!")

            st.info(
              q.get(
                "explanaition"
              )
            )
# -------------------------------
# PERFORMANCE HISTORY
# -------------------------------

st.divider()
st.header("📈 Performance History")

history_file = "performance_history.csv"

if os.path.exists(history_file):

    history = pd.read_csv(history_file)

    if not history.empty:

        st.subheader("Your Previous Attempts")

        st.dataframe(
            history,
            use_container_width=True
        )

        st.subheader("📊 Score Progress")

        subject_history = history[
            history["subject"] == subject
        ]

        if not subject_history.empty:

            st.line_chart(
                subject_history["percentage"]
            )

        else:
            st.info("No history available for this subject yet.")
        
    st.divider()
    st.header("🧠 Weak Topic Detection")

    topic_history = subject_history[
        ~subject_history["topic"].astype(str).str.lower().isin(
            ["all topics", "nan", ""]
        )
    ]

    if not topic_history.empty:

        topic_summary = topic_history.groupby(
            "topic",
            as_index=False
        ).agg({
            "correct": "sum",
            "total": "sum"
        })

        topic_summary["accuracy"] = (
            topic_summary["correct"] /
            topic_summary["total"] * 100
        )

        for _, row in topic_summary.iterrows():

            st.subheader(row["topic"].title())

            accuracy = row["accuracy"]

            st.progress(float(accuracy) / 100)

            st.write(
                f"Accuracy: {accuracy:.1f}%"
            )

            if accuracy < 50:
                st.error("Weak topic - Needs revision")

            elif accuracy < 75:
                st.warning("Needs more practice")

            else:
                st.success("Strong topic - Excellent work!")

        else:
          st.info(
            "Complete topic-specific quizzes "
            "to identify your weak areas."
        )

   else:
        st.info("Complete a quiz to see your history.")

else:
    st.info("Your quiz history will appear here after your first completed quiz.")
