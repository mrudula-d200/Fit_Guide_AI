import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found. Please add it to your .env file.")
    st.stop()

client = Groq(
    api_key=GROQ_API_KEY
)


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="FitGuide AI",
    page_icon="🌸",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff5fa, #ffe8f2);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* Main title */

.main-title {
    text-align: center;
    color: #d63384;
    font-size: 52px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 19px;
    margin-bottom: 25px;
}


/* Cards */

.card {
    background-color: white;
    padding: 25px;
    border-radius: 22px;
    margin: 15px 0;
    box-shadow: 0px 6px 20px rgba(214, 51, 132, 0.12);
}


/* Section title */

.section-title {
    color: #c2185b;
    font-size: 28px;
    font-weight: bold;
    margin-top: 25px;
}


/* Workout card */

.workout-card {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    margin: 15px 0;
    box-shadow: 0px 5px 18px rgba(214, 51, 132, 0.10);
    border-left: 6px solid #e83e8c;
}


/* Food card */

.food-card {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    margin: 15px 0;
    box-shadow: 0px 5px 18px rgba(214, 51, 132, 0.10);
    border-left: 6px solid #ff8fab;
}


/* Metric cards */

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 5px 18px rgba(214, 51, 132, 0.10);
}

.metric-title {
    color: #777;
    font-size: 15px;
}

.metric-value {
    color: #d63384;
    font-size: 28px;
    font-weight: bold;
}


/* Buttons */

.stButton > button {
    background-color: #d63384;
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: bold;
    padding: 10px;
}

.stButton > button:hover {
    background-color: #c2185b;
    color: white;
}


/* Sidebar */

[data-testid="stSidebar"] {
    background-color: #ffe6f0;
}


/* Chat */

[data-testid="stChatMessage"] {
    border-radius: 15px;
}


/* Divider */

hr {
    border: none;
    height: 2px;
    background-color: #f8bbd0;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🌸 FitGuide AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your Personal AI Fitness & Wellness Companion 💪✨'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# WELCOME CARD
# =========================================================

st.markdown("""
<div class="card">

<h2>🌷 Welcome to FitGuide AI</h2>

<p>
Your personal fitness companion designed to help you
with workouts, nutrition and healthy habits.
</p>

<p>
🏋️ Personalized Workouts &nbsp;&nbsp;&nbsp;
🍎 Smart Nutrition &nbsp;&nbsp;&nbsp;
🤖 AI Fitness Assistant
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# PROFILE
# =========================================================

st.markdown(
    '<div class="section-title">👤 Create Your Fitness Profile</div>',
    unsafe_allow_html=True
)

st.write(
    "Tell us about yourself so FitGuide AI can create "
    "a personalized plan. 🌸"
)


col1, col2, col3 = st.columns(3)


# =========================================================
# AGE
# =========================================================

with col1:

    age = st.number_input(
        "Age",
        min_value=13,
        max_value=100,
        value=20
    )


# =========================================================
# HEIGHT
# =========================================================

with col2:

    st.write("📏 Height")

    h1, h2 = st.columns(2)

    with h1:

        height_feet = st.number_input(
            "Feet",
            min_value=3,
            max_value=8,
            value=5
        )

    with h2:

        height_inches = st.number_input(
            "Inches",
            min_value=0,
            max_value=11,
            value=4
        )

    total_inches = (height_feet * 12) + height_inches

    height = total_inches * 2.54


# =========================================================
# WEIGHT
# =========================================================

with col3:

    weight = st.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=200.0,
        value=60.0
    )


# =========================================================
# FITNESS OPTIONS
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    goal = st.selectbox(
        "🎯 Fitness Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "Maintain Weight",
            "Improve Fitness"
        ]
    )


with col2:

    experience = st.selectbox(
        "🏋️ Gym Experience",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )


with col3:

    gym_days = st.slider(
        "📅 Gym Days / Week",
        min_value=1,
        max_value=7,
        value=4
    )


# =========================================================
# FOOD PREFERENCE
# =========================================================

st.markdown(
    '<div class="section-title">🥗 Food Preference</div>',
    unsafe_allow_html=True
)

food_preference = st.selectbox(
    "Choose your food preference",
    [
        "Vegetarian",
        "Non-Vegetarian",
        "Vegan"
    ]
)


# =========================================================
# BMI CALCULATION
# =========================================================

height_m = height / 100

bmi = weight / (height_m ** 2)

bmi = round(bmi, 1)


if bmi < 18.5:

    bmi_category = "Underweight"

elif bmi < 25:

    bmi_category = "Normal range"

elif bmi < 30:

    bmi_category = "Overweight"

else:

    bmi_category = "Obesity range"


# =========================================================
# CALORIE CALCULATION
# =========================================================

# Female Mifflin-St Jeor estimate

bmr = (
    (10 * weight)
    + (6.25 * height)
    - (5 * age)
    - 161
)


if gym_days <= 2:

    activity_factor = 1.30

elif gym_days <= 4:

    activity_factor = 1.45

elif gym_days <= 5:

    activity_factor = 1.55

else:

    activity_factor = 1.65


maintenance_calories = bmr * activity_factor


if goal == "Weight Loss":

    calorie_target = maintenance_calories - 300

elif goal == "Muscle Gain":

    calorie_target = maintenance_calories + 250

else:

    calorie_target = maintenance_calories


calorie_target = round(calorie_target)


# =========================================================
# PROTEIN
# =========================================================

if goal == "Muscle Gain":

    protein_min = round(weight * 1.6)

    protein_max = round(weight * 2.0)

elif goal == "Weight Loss":

    protein_min = round(weight * 1.2)

    protein_max = round(weight * 1.6)

else:

    protein_min = round(weight * 1.0)

    protein_max = round(weight * 1.4)


# =========================================================
# WATER
# =========================================================

water = round(weight * 0.033, 1)


# =========================================================
# GENERATE FITNESS PLAN
# =========================================================

generate_plan = st.button(
    "✨ Generate My Fitness Plan",
    use_container_width=True
)


if generate_plan:

    # =====================================================
    # FITNESS SUMMARY
    # =====================================================

    st.markdown(
        '<div class="section-title">📊 Your Fitness Summary</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3, m4 = st.columns(4)


    with m1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">BMI</div>
                <div class="metric-value">{bmi}</div>
                <div>{bmi_category}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with m2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Daily Calories</div>
                <div class="metric-value">{calorie_target}</div>
                <div>kcal/day</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with m3:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Protein</div>
                <div class="metric-value">{protein_min}-{protein_max}g</div>
                <div>per day</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with m4:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Water</div>
                <div class="metric-value">{water}L</div>
                <div>starting estimate</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # WORKOUT PLANS
    # =====================================================

    beginner_plan = {

        "Monday": {
            "title": "🦵 Lower Body",
            "exercises": [
                "Bodyweight Squats – 3 × 10",
                "Glute Bridges – 3 × 12",
                "Reverse Lunges – 2 × 10",
                "Leg Press – 2 × 10",
                "Calf Raises – 2 × 15"
            ]
        },

        "Tuesday": {
            "title": "💪 Upper Body",
            "exercises": [
                "Lat Pulldown – 3 × 10",
                "Chest Press – 3 × 10",
                "Seated Row – 2 × 10",
                "Shoulder Press – 2 × 10",
                "Bicep Curl – 2 × 12"
            ]
        },

        "Wednesday": {
            "title": "😴 Rest / Light Activity",
            "exercises": [
                "Light walking – 20–30 minutes",
                "Gentle stretching"
            ]
        },

        "Thursday": {
            "title": "🍑 Glutes & Legs",
            "exercises": [
                "Goblet Squats – 3 × 10",
                "Hip Thrust – 3 × 10",
                "Leg Curl – 2 × 12",
                "Step Ups – 2 × 10",
                "Calf Raises – 2 × 15"
            ]
        },

        "Friday": {
            "title": "🔥 Full Body",
            "exercises": [
                "Squats – 3 × 10",
                "Lat Pulldown – 3 × 10",
                "Chest Press – 3 × 10",
                "Seated Row – 2 × 10",
                "Plank – 3 × 20 seconds"
            ]
        },

        "Saturday": {
            "title": "🚶 Cardio & Core",
            "exercises": [
                "Walking – 20 minutes",
                "Cycling – 10 minutes",
                "Plank – 3 × 20 seconds",
                "Dead Bug – 2 × 10"
            ]
        },

        "Sunday": {
            "title": "😴 Rest Day",
            "exercises": [
                "Rest",
                "Optional light walking",
                "Gentle stretching"
            ]
        }
    }


    intermediate_plan = {

        "Monday": {
            "title": "🍑 Glutes & Hamstrings",
            "exercises": [
                "Hip Thrust – 4 × 10",
                "Romanian Deadlift – 3 × 10",
                "Bulgarian Split Squat – 3 × 10",
                "Leg Curl – 3 × 12",
                "Glute Abduction – 3 × 15"
            ]
        },

        "Tuesday": {
            "title": "💪 Upper Body",
            "exercises": [
                "Lat Pulldown – 4 × 10",
                "Chest Press – 3 × 10",
                "Seated Row – 3 × 10",
                "Shoulder Press – 3 × 10",
                "Bicep Curl – 3 × 12"
            ]
        },

        "Wednesday": {
            "title": "🔥 Cardio & Core",
            "exercises": [
                "Treadmill – 25 minutes",
                "Plank – 3 × 30 seconds",
                "Russian Twists – 3 × 15",
                "Leg Raises – 3 × 12"
            ]
        },

        "Thursday": {
            "title": "🦵 Quad Focus",
            "exercises": [
                "Squats – 4 × 10",
                "Leg Press – 3 × 12",
                "Walking Lunges – 3 × 12",
                "Leg Extension – 3 × 12",
                "Calf Raises – 3 × 15"
            ]
        },

        "Friday": {
            "title": "💪 Back & Shoulders",
            "exercises": [
                "Lat Pulldown – 4 × 10",
                "Seated Row – 3 × 10",
                "Face Pull – 3 × 12",
                "Lateral Raise – 3 × 12",
                "Shoulder Press – 3 × 10"
            ]
        },

        "Saturday": {
            "title": "🏋️ Full Body",
            "exercises": [
                "Squats – 3 × 10",
                "Hip Thrust – 3 × 10",
                "Chest Press – 3 × 10",
                "Lat Pulldown – 3 × 10",
                "Plank – 3 × 30 seconds"
            ]
        },

        "Sunday": {
            "title": "😴 Rest Day",
            "exercises": [
                "Rest",
                "Walking",
                "Stretching"
            ]
        }
    }


    advanced_plan = {

        "Monday": {
            "title": "🍑 Glutes",
            "exercises": [
                "Hip Thrust – 4 × 8",
                "Romanian Deadlift – 4 × 8",
                "Bulgarian Split Squat – 3 × 10",
                "Cable Kickback – 3 × 12",
                "Hip Abduction – 3 × 15"
            ]
        },

        "Tuesday": {
            "title": "💪 Push",
            "exercises": [
                "Bench Press – 4 × 8",
                "Shoulder Press – 4 × 8",
                "Chest Fly – 3 × 12",
                "Lateral Raise – 3 × 15",
                "Tricep Pushdown – 3 × 12"
            ]
        },

        "Wednesday": {
            "title": "🦵 Legs",
            "exercises": [
                "Squats – 4 × 8",
                "Leg Press – 4 × 10",
                "Leg Extension – 3 × 12",
                "Leg Curl – 3 × 12",
                "Calf Raises – 4 × 15"
            ]
        },

        "Thursday": {
            "title": "😴 Recovery",
            "exercises": [
                "Light walking – 30 minutes",
                "Mobility exercises",
                "Gentle stretching"
            ]
        },

        "Friday": {
            "title": "💪 Pull",
            "exercises": [
                "Deadlift – 3 × 6",
                "Lat Pulldown – 4 × 10",
                "Seated Row – 4 × 10",
                "Face Pull – 3 × 15",
                "Bicep Curl – 3 × 12"
            ]
        },

        "Saturday": {
            "title": "🔥 Full Body",
            "exercises": [
                "Squats – 3 × 10",
                "Hip Thrust – 3 × 10",
                "Chest Press – 3 × 10",
                "Lat Pulldown – 3 × 10",
                "Plank – 3 × 45 seconds"
            ]
        },

        "Sunday": {
            "title": "😴 Rest Day",
            "exercises": [
                "Rest",
                "Light walking",
                "Recovery"
            ]
        }
    }


    # =====================================================
    # SELECT WORKOUT PLAN
    # =====================================================

    if experience == "Beginner":

        selected_plan = beginner_plan

    elif experience == "Intermediate":

        selected_plan = intermediate_plan

    else:

        selected_plan = advanced_plan


    # =====================================================
    # WORKOUT DISPLAY
    # =====================================================

    st.markdown(
        '<div class="section-title">🏋️ Your Workout Plan</div>',
        unsafe_allow_html=True
    )

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]


    for index, day in enumerate(days):

        if index >= gym_days:
            break

        workout = selected_plan[day]

        st.markdown(
            f"""
            <div class="workout-card">
                <h3>{day} — {workout["title"]}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        for exercise in workout["exercises"]:

            st.write("•", exercise)


    # =====================================================
    # WORKOUT DURATION
    # =====================================================

    if experience == "Beginner":

        duration = "30–45 minutes"

    elif experience == "Intermediate":

        duration = "45–60 minutes"

    else:

        duration = "60–75 minutes"


    st.info(
        f"⏱️ Recommended workout duration: {duration}"
    )


    # =====================================================
    # NUTRITION PLAN
    # =====================================================

    st.markdown(
        '<div class="section-title">🍎 Your Nutrition Plan</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # VEGETARIAN
    # =====================================================

    if food_preference == "Vegetarian":

        if goal == "Weight Loss":

            breakfast = "🥣 Oats + milk/curd + berries or banana"
            lunch = "🍛 2 rotis + dal + mixed vegetables + curd"
            snack = "🍎 Fruit + roasted chana or a small handful of nuts"
            dinner = "🥗 2 rotis + paneer/tofu + vegetables"

        elif goal == "Muscle Gain":

            breakfast = "🥣 Oats + milk + banana + paneer/curd"
            lunch = "🍚 Rice/roti + dal + paneer + vegetables + curd"
            snack = "🥛 Milk/curd + banana + nuts"
            dinner = "🍛 Rice/roti + paneer/tofu + dal + vegetables"

        else:

            breakfast = "🥣 Oats + milk + fruit + nuts"
            lunch = "🍛 Rice/roti + dal + vegetables + curd"
            snack = "🍎 Fruit + roasted chana"
            dinner = "🥗 Roti + paneer/tofu + vegetables"


    # =====================================================
    # NON-VEGETARIAN
    # =====================================================

    elif food_preference == "Non-Vegetarian":

        if goal == "Weight Loss":

            breakfast = "🥣 Oats + milk/curd + fruit + eggs"
            lunch = "🍗 Rice/roti + grilled chicken/fish + dal + vegetables"
            snack = "🥚 Boiled eggs + fruit or curd"
            dinner = "🥗 Roti + vegetables + grilled chicken/fish"

        elif goal == "Muscle Gain":

            breakfast = "🥣 Oats + milk + banana + eggs"
            lunch = "🍗 Rice/roti + chicken/fish + dal + vegetables"
            snack = "🥛 Milk/curd + banana + eggs/nuts"
            dinner = "🍚 Rice/roti + chicken/fish + vegetables + dal"

        else:

            breakfast = "🥚 Eggs + oats + fruit"
            lunch = "🍗 Rice/roti + chicken/fish + vegetables"
            snack = "🍎 Fruit + curd"
            dinner = "🥗 Roti + vegetables + chicken/fish"


    # =====================================================
    # VEGAN
    # =====================================================

    else:

        if goal == "Weight Loss":

            breakfast = "🥣 Oats + fortified soy milk + fruit + chia seeds"
            lunch = "🍛 Roti/rice + dal + chickpeas/tofu + vegetables"
            snack = "🍎 Fruit + roasted chickpeas/nuts"
            dinner = "🥗 Roti + tofu + vegetables + dal"

        elif goal == "Muscle Gain":

            breakfast = "🥣 Oats + soy milk + banana + peanut butter"
            lunch = "🍛 Rice/roti + dal + tofu + chickpeas + vegetables"
            snack = "🥛 Soy milk + fruit + nuts"
            dinner = "🍚 Rice/roti + tofu + beans + vegetables"

        else:

            breakfast = "🥣 Oats + soy milk + fruit"
            lunch = "🍛 Rice/roti + dal + tofu + vegetables"
            snack = "🍎 Fruit + nuts"
            dinner = "🥗 Roti + beans/tofu + vegetables"


    # =====================================================
    # FOOD CARDS
    # =====================================================

    food_items = [
        ("🌅 Breakfast", breakfast),
        ("☀️ Lunch", lunch),
        ("🍎 Snack", snack),
        ("🌙 Dinner", dinner)
    ]


    for title, food in food_items:

        st.markdown(
            f"""
            <div class="food-card">
                <h3>{title}</h3>
                <p>{food}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.success(
        f"🎯 Estimated daily calorie target: "
        f"{calorie_target} kcal | "
        f"Protein: {protein_min}–{protein_max} g/day"
    )


# =========================================================
# AI CHATBOT
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">🤖 Chat With FitGuide AI</div>',
    unsafe_allow_html=True
)

st.write(
    "Ask me anything about workouts, nutrition, "
    "exercise or your fitness goals. 🌸"
)


# =========================================================
# QUICK QUESTIONS
# =========================================================

st.subheader("✨ Quick Questions")


q1, q2, q3 = st.columns(3)


with q1:

    quick1 = st.button(
        "🍎 What should I eat today?",
        use_container_width=True
    )


with q2:

    quick2 = st.button(
        "🏋️ Give me today's workout",
        use_container_width=True
    )


with q3:

    quick3 = st.button(
        "🥤 What should I eat before gym?",
        use_container_width=True
    )


q4, q5 = st.columns(2)


with q4:

    quick4 = st.button(
        "💪 How can I build muscle?",
        use_container_width=True
    )


with q5:

    quick5 = st.button(
        "📅 Give me a 7-day meal plan",
        use_container_width=True
    )


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# =========================================================
# QUICK QUESTION LOGIC
# =========================================================

quick_question = None


if quick1:

    quick_question = (
        "What should I eat today based on my fitness profile?"
    )


elif quick2:

    quick_question = (
        "Give me today's workout based on my "
        "experience and fitness goal."
    )


elif quick3:

    quick_question = (
        "What should I eat before going to the gym?"
    )


elif quick4:

    quick_question = (
        "How can I build muscle effectively?"
    )


elif quick5:

    quick_question = (
        "Give me a simple 7-day meal plan."
    )


# =========================================================
# DISPLAY OLD CHAT
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

user_question = st.chat_input(
    "💬 Ask FitGuide AI..."
)


# Use quick question if selected

if quick_question:

    user_question = quick_question


# =========================================================
# AI RESPONSE
# =========================================================

if user_question:

    # =====================================================
    # DISPLAY USER MESSAGE
    # =====================================================

    with st.chat_message("user"):

        st.markdown(user_question)


    # Save user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    # =====================================================
    # PERSONALIZED AI CONTEXT
    # =====================================================

    fitness_context = f"""

You are FitGuide AI, a friendly AI fitness and wellness assistant
designed especially for women.

You should give simple, friendly and practical answers.

USER PROFILE:

Age: {age}

Height: {height_feet} feet {height_inches} inches

Weight: {weight} kg

BMI: {bmi}

BMI Category: {bmi_category}

Fitness Goal: {goal}

Gym Experience: {experience}

Gym Days Per Week: {gym_days}

Food Preference: {food_preference}

Estimated Daily Calories: {calorie_target} kcal

Estimated Protein: {protein_min}-{protein_max} grams per day

Estimated Water: {water} liters per day


IMPORTANT:

Give answers based on the user's profile.

Keep explanations simple and practical.

Do not diagnose diseases.

Do not prescribe medication.

Do not claim that calorie, BMI or protein estimates
are medical prescriptions.

If the user has a medical condition, injury,
eating disorder, pregnancy-related concern,
or serious health concern, recommend speaking
with a qualified healthcare professional.

For exercise questions, remind the user to use
proper form and stop if they experience pain
or concerning symptoms.

The user asked:

{user_question}

"""


    # =====================================================
    # GROQ API
    # =====================================================

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        full_response = ""


        try:

            # System message
            groq_messages = [
                {
                    "role": "system",
                    "content": fitness_context
                }
            ]


            # Add previous conversation
            # Exclude the current user message because
            # it will be added separately below.

            for message in st.session_state.messages[:-1]:

                groq_messages.append(
                    {
                        "role": message["role"],
                        "content": message["content"]
                    }
                )


            # Add current user question

            groq_messages.append(
                {
                    "role": "user",
                    "content": user_question
                }
            )


            # =================================================
            # GROQ CHAT COMPLETION
            # =================================================

            stream = client.chat.completions.create(

                model="openai/gpt-oss-20b",

                messages=groq_messages,

                stream=True,

                temperature=0.7

            )


            # =================================================
            # STREAM RESPONSE
            # =================================================

            for chunk in stream:

                text = chunk.choices[0].delta.content

                if text:

                    full_response += text

                    response_placeholder.markdown(
                        full_response
                    )


            # =================================================
            # SAVE AI RESPONSE
            # =================================================

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )


        except Exception as e:

            st.error(
                "❌ Could not connect to Groq API."
            )

            st.write(
                "Please check your GROQ_API_KEY, "
                "internet connection and Groq model."
            )

            st.code(str(e))


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🌸 FitGuide AI")

    st.write("### ⚙️ Settings")

    st.write("🏋️ Workout")
    st.write("🍎 Nutrition")
    st.write("🤖 AI Chatbot")

    st.divider()

    st.write("### 📌 Your Goal")

    st.info(goal)

    st.write("### 🥗 Food")

    st.info(food_preference)

    st.divider()

    st.caption(
        "FitGuide AI provides general fitness information "
        "and estimates. It is not a substitute for "
        "professional medical advice."
    )
