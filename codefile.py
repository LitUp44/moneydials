import streamlit as st
import pandas as pd
import altair as alt

st.markdown(
    """
    <style>
    div[data-baseweb="radio"] label {
        font-size: 60px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def app_header():
    """Display a persistent header with the logo and main title."""
    st.image("Aligned White.png", width=200)  # Adjust width as needed.
    st.markdown(
        """
        <div style="background-color: #f5724b; padding: 10px; text-align: center; border-radius: 8px;">
            <h1 style="color: #ffeae6; margin: 0;">What are your Money Dials?</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

def quiz_subheader():
    """Display the sub-header for the quiz only."""
    st.markdown(
        """
        <div style="background-color: #8f4e52; padding: 10px; text-align: center; border-radius: 8px;">
            <p style="color: #ffeae6; margin: 5px 0 0 0; font-size: 32px;">
                Where do you get the most JOY spending money? Take the quiz and find out!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Data Definitions (Quiz)
# -----------------------------

# List of quiz questions and answers.
# Each answer is a tuple: (category, answer_text)
questions = [
    ("1. When it comes to lunch, what’s your preference?", [
        ("Convenience", "Grab something quick and easy to save time"),
        ("Experiences", "Try out a new spot nearby!"),
        ("Health", "Meal-prep at home so I know it’s healthy"),
        ("Relationships", "Doesn't matter as long as I have a friend to eat with!"),
        ("None", "Mmm... none of the above really fits!")
    ]),
    ("2. It’s Saturday night! How do you like to spend it?", [
        ("Generosity", "Easy - I love to play host for my friends or family."),
        ("Experiences", "Get to do something cool - like a concert or a play."),
        ("Self Improvement", "Work on a project; Saturday night crafts has a great ring to it."),
        ("Freedom", "I like not having a set plan and deciding last minute."),
        ("None", "I like to do something else!")
    ]),
    ("3. For you, what's the most important thing about travelling?", [
        ("Travel", "Getting to go in the first place, I just want to see and experience the world"),
        ("Freedom", "Knowing I can go where I like, when I like."),
        ("Health", "The opportunity to be active beyond just going to the gym!"),
        ("Luxury", "Getting to travel in style and splurging on quality experiences."),
        ("Convenience", "Making sure everything that can be taken care of for me, is."),
        ("None", "None of the above"),
    ]),
    ("4. What’s your ideal work environment?", [
        ("Freedom", "A job that allows me to work my own hours, in whichever location I choose."),
        ("Relationships", "An office where I can meet new people and network."),
        ("Travel", "Any job that lets me have long weekends away or the occasional work from abroad."),
        ("Self Improvement", "Anywhere, as long as I’m always learning and developing."),
        ("None", "None of the above"),
    ]),
    ("5. How do you use money to approach fitness and health?", [
        ("Convenience", "Convenience matters — I'll pay for options that fit my schedule."),
        ("Health", "There's no budget when it comes to my health."),
        ("Relationships", "It’s more of a social thing; I love group classes or going with friends!"),
        ("Experiences", "Fitness isn’t my main focus, but I'm usually up to give something new a try."),
        ("None", "None of these are really 'Me'!")
    ]),
    ("6. What do you spend the most 'splurge' money on every month?", [
        ("Convenience", "Making my life easier - meal kits, Ubers, help with cleaning, or any combo of the above."),
        ("Travel", "Flights or trips, even if they’re short – I love to get away!"),
        ("Health", "My health. Gym membership, quality food, workout clothes."),
        ("Self Improvement", "My hobbies! I like to invest in things I'm learning / working on."),
        ("Experiences", "Experiences. I like to use my money to feel I've done soemthing different than usual."),
        ("None", "Something else!")
    ]),
    ("7. You come across a windfall of cash. What’s your first thought on how to use it?", [
        ("Luxury", "Treat myself! Soemthing boujie I normally can’t afford."),
        ("Experiences", "Wahoo more money to add to my 'fun' fund."),
        ("Freedom", "Straight to the bank! It'll go a long way to giving me more financial flexibility!"),
        ("Generosity", "Wow - great opportunity to donate part of it to causes I care about!"),
        ("None", "None of these feel right!")
    ]),
    ("8. Which best describes your spending philosophy?", [
        ("Luxury", "Quality, even if it means spending a lot more."),
        ("Experiences", "Easy - experiences over stuff."),
        ("Self Improvement", "There’s no budget if it helps me learn and grow."),
        ("Relationships", "I would usually use it to treat my loved ones."),
        ("Travel", "Straight to the vacation fund."),
        ("None", "None of these are really 'me'!")
    ]),
    ("9. How do you typically approach learning or personal growth?", [
        ("Self Improvement", "I try to carve out the time daily or monthly to learn something new."),
        ("Travel", "I usually prefer learning about new places, languages or cultures"),
        ("Health", "I focus on self-care practices and my mental and physical wellness."),
        ("Relationships", "I learn through people, whether meeting new people or learning from people already in my life."),
        ("None", "...none of these are quite right"),
    ]),
    ("10. What’s one thing you’re willing to spend more on to treat others?", [
        ("Generosity", "Hosting dinner or treating my friends to a night out."),
        ("Convenience", "Getting them something to make their life easier; a baby-sitter or something they'll actually use."),
        ("Luxury", "Easy, I’ll splurge on something extravagant for them!"),
        ("Experiences", "I would usually get something we can do together"),
        ("None", "Something different!"),
    ]),
    ("11. When it comes to your personal style, what’s most important?", [
        ("Luxury", "The brand – I like to wear pieces that make an impression"),
        ("Convenience", "Comfort and convenience; I don’t like to overthink it"),
        ("Generosity", "Buying things that reflect my values, like eco-friendly or locally made products"),
        ("Health", "Practicality, I like to be able to walk a lot or go to a workout class in my usual clothes"), 
        ("None", "None of these are quite right"),
    ]),
    ("12. If you could improve one area of your life, what would it be?", [
        ("Convenience", "Automate and simplify my life"),
        ("Relationships", "Building stronger connections with friends, family, or a partner"),
        ("Generosity", "Living more generously by giving more time or money to causes I care about"),
        ("Freedom", "Having more control over my time"), 
        ("Travel", "Take more vacations, we don't do enough"),
        ("None", "No none of these are right"),
    ]),
    ("13. What’s your favourite way to celebrate a personal milestone?", [
        ("Luxury", "Treat myself to something luxurious and indulgent"),
        ("Generosity", "Reflect on how lucky I am and think about how I can give back to my community"),
        ("Self Improvement", "Reflect on what I’ve achieved and set new goals for growth"),
        ("Freedom", "Take a day off to enjoy the freedom to do whatever I want"),
        ("Relationships", "Celebrate with my friends and family"), 
        ("None", "Something else!")
    ])
]

# Explanatory texts for each category.
explanatory_texts = {
    "Travel": """**Travel:** Travel is your top money dial!! You find joy in exploring new places and cultures, valuing experiences that broaden your horizons and love to create lasting memories. You prioritise using your money to see the world even if that means you need to save in other places. Amazing - keep exploring the world!""",
    "Experiences": """**Experiences:** You have Experiences as a top money dial! It means you like to use your hard earned money to be able to do activities that bring you excitement and fulfilment, from concerts and adventures to simple moments that create meaningful stories. Your motto is likely: “let’s try something new”.""",
    "Convenience": """**Convenience:** You have Convenience as a top money dial! Convenience is all about using money to save yourself time and reduce stress; streamlining your life so you can focus on what matters most. Whether that means taking ride shares instead of transport, ordering food, or hiring a cleaner - you aim to use money to make life as easy as possible.""",
    "Luxury": """**Luxury:** You have Luxury as a top money dial! This means you appreciate high-quality items and experiences, value comfort, elegance, and the finer things in life. Nothing wrong with appreciating beauty in your life and really loving special things. Keep using your money to make your life luxurious!""",
    "Relationships": """**Relationships:** You have Relationships as a top money dial! If relationships are your priority, that means you probably enjoy using money to spend time with your family and friends. Whether hosting a dinner, buying presents for every loved one or using money to help you free up time to see them - you put people above all else.""",
    "Self Improvement": """**Self-Improvement:** You have self-improvement as a top money dial! You like to invest in personal growth through education, skills, and tools that help you become the best version of yourself. Incredibly admirable - keep calm and carry on learning & growing!""",
    "Health": """**Health & Wellness:** You have health & wellness as a top money dial! You value spending your cash on fitness, nutrition, and mental well-being to support a vibrant, balanced lifestyle. You know better than anyone that if we don’t have our health we don’t have anything. Keep getting those expensive workout classes and treating yourself to new gym clothes!""",
    "Generosity": """**Generosity:** You have generosity as a top money dial!  This means you find fulfilment in giving to others, whether through gifts, donations, or acts of kindness that make a positive impact. This is a lovely way to spend your hard earned money - keep finding ways to give money to causes and people you care about!""",
    "Freedom": """**Freedom:** You have Freedom as a top money dial! The best way to use your money is to buy yourself flexibility, autonomy, and the ability to live life on your own terms. Whether the ability to work your own hours or change jobs as you please you like to be in control of your own time. Keep living free!"""
}

# -----------------------------
# Session State Initialization (for multi-phase flow)
# -----------------------------
if "phase" not in st.session_state:
    # "quiz" → answering quiz questions.
    # "results" → showing the top money dials (quiz results) with explanatory text.
    # "spending" → entering spending amounts for each top dial.
    # "final" → final results page.
    st.session_state.phase = "quiz"

if st.session_state.phase == "quiz":
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
if "scores" not in st.session_state:
    # Gather all categories (ignore None values).
    all_categories = {cat for _, answers in questions for cat, _ in answers if cat is not None}
    st.session_state.scores = {cat: 0 for cat in all_categories}


# For spending input pages:
if st.session_state.phase == "spending":
    if "spending_index" not in st.session_state:
        st.session_state.spending_index = 0  # index for the current money dial (0, 1, 2)
    if "spending_data" not in st.session_state:
        # Will store ideal and actual amounts for each dial.
        st.session_state.spending_data = {}  # key: money dial name, value: dict with "ideal" and "actual"
    if "spending_subphase" not in st.session_state:
        # "ideal" or "actual" for the current money dial.
        st.session_state.spending_subphase = "ideal"
        
# -----------------------------
# Page Functions
# -----------------------------


def show_quiz():
    """Display the initial quiz page.
    
    Initially shows the header, subheader, and a 'Start Now' button.
    Once the button is clicked, the quiz starts and the subheader is hidden.
    """
    # Always show the persistent header.
    app_header()
    
    # Check if the quiz has started.
    if not st.session_state.get("quiz_started", False):
        # Quiz has not started: show the subheader and a 'Start Now' button.
        quiz_subheader()
        st.markdown("<div style='padding-bottom: 20px;'></div>", unsafe_allow_html=True)
        if st.button("Start Now"):
            st.session_state.quiz_started = True
            st.rerun()
        return  # do not show any quiz questions yet.
    
    # If quiz has started, only display the header (no subheader) and then the quiz questions.
    # (Here we assume the quiz questions are managed via st.session_state.current_question.)
    if st.session_state.current_question < len(questions):
        question_text, answers = questions[st.session_state.current_question]
        st.markdown(f"### {question_text}")
        options = [answer_text for _, answer_text in answers]
        choice = st.radio("Select your answer:", options, key=f"question_{st.session_state.current_question}")
        if st.button("Next"):
            # Only update score if the answer has a valid category.
            for cat, answer_text in answers:
                if answer_text == choice:
                    if cat is not None:  # Do nothing for 'Not applicable'
                        st.session_state.scores[cat] += 1
                    break
            st.session_state.current_question += 1
            st.rerun()
    else:
        st.write("Quiz finished!")
        st.write("Scores:", st.session_state.scores)

# show_quiz()

def show_quiz_results():
    """Display the quiz results with the top money dial, a vertical bar chart of all scores,
    and explanatory text for the 2nd and 3rd top money dials."""
    app_header()  # persistent header
    
    # Retrieve scores from session state; if not defined, provide an empty dict.
    scores = st.session_state.get("scores", {})

    if not scores:
        st.write("No scores found. It appears you have not completed the quiz.")
        return

    # Optionally, remove any None keys (just in case).
    filtered_scores = {cat: score for cat, score in scores.items() if cat is not "None"}

    # Sort the scores in descending order.
    sorted_scores = sorted(filtered_scores.items(), key=lambda item: item[1], reverse=True)
    
    # Get the top three categories with non-zero scores.
    top_categories = [cat for cat, score in sorted_scores if score > 0][:3]
    
    if not top_categories:
        st.write("It looks like you did not answer any questions.")
        return
    
    # Display the top money dial and its explanatory text.
    st.markdown(f"## Your top money dial is: **{top_categories[0]}**")
    st.markdown(explanatory_texts.get(top_categories[0], ""))
    
    # Create a DataFrame from the filtered scores dictionary.
    data = pd.DataFrame(list(filtered_scores.items()), columns=["Money Dial", "Score"])
    
    # Create a vertical bar chart with Altair.
    chart = alt.Chart(data).mark_bar(color="#682d24").encode(
        x=alt.X(
            "Money Dial:N",
            title="Money Dial",
            sort=alt.EncodingSortField(field="Score", op="sum", order="descending"),
            axis=alt.Axis(grid=False)
        ),
        y=alt.Y(
            "Score:Q",
            title="Points",
            axis=alt.Axis(grid=False, format="d", tickMinStep=1)
        )
    ).properties(
        width=600,
        height=400,
        title="Money Dial Scores"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    # Display the explanatory text for the 2nd and 3rd top money dials (if available).
    if len(top_categories) > 1:
        others = top_categories[1:]
        others_str = " & ".join([f"**{cat}**" for cat in others])
        st.markdown(f"### Your other top money dials are: {others_str}")
        for cat in others:
            st.markdown(explanatory_texts.get(cat, ""))
    
    # Button to proceed to the spending inputs phase.
    if st.button("See how your spending compares!"):
        st.session_state.top_dials = top_categories
        st.session_state.spending_data = {dial: {"ideal": None, "actual": None} for dial in top_categories}
        st.session_state.phase = "spending"
        st.session_state.spending_index = 0
        st.session_state.spending_subphase = "ideal"
        st.rerun()


def prepare_spending_phase():
    """After the quiz is done, compute the top three money dials and transition to spending input."""
    # Sort categories by score (highest first) and get top three (ignoring zeros).
    sorted_scores = sorted(
        st.session_state.scores.items(), key=lambda item: item[1], reverse=True
    )
    top_categories = [cat for cat, score in sorted_scores if score > 0][:3]
    if not top_categories:
        st.write("It looks like you did not answer any questions.")
        return
    
    # Save the top dials in session state.
    st.session_state.top_dials = top_categories
    
    # Initialize spending_data if it doesn't exist.
    if "spending_data" not in st.session_state:
        st.session_state.spending_data = {}
    
    # Initialize spending data for each dial.
    for dial in top_categories:
        st.session_state.spending_data[dial] = {"ideal": None, "actual": None}
    
    st.session_state.phase = "spending"
    st.session_state.spending_index = 0
    st.session_state.spending_subphase = "ideal"
    st.rerun()

def show_spending_input():
    """Display input pages for ideal and actual spending for each top money dial."""
    # Display the persistent header.
    app_header()
    
    current_index = st.session_state.spending_index
    top_dials = st.session_state.top_dials
    current_dial = top_dials[current_index]
    subphase = st.session_state.spending_subphase

    if subphase == "ideal":
        st.title(f"Ideal spending for {current_dial}")
        st.subheader(f"How much would you ideally like to allocate to {current_dial} per year?")
        ideal = st.number_input("Ideal amount:", min_value=0.0, value=0.0, step=1.0, key=f"ideal_{current_dial}")
        if st.button("Next"):
            st.session_state.spending_data[current_dial]["ideal"] = ideal
            # Switch to actual spending input for the same dial.
            st.session_state.spending_subphase = "actual"
            st.rerun()
    elif subphase == "actual":
        st.title(f"Actual spending for {current_dial}")
        st.subheader(f"If you had to guess, how much do you currently spend on {current_dial} per year?")
        actual = st.number_input("Current amount:", min_value=0.0, value=0.0, step=1.0, key=f"actual_{current_dial}")
        if st.button("Next"):
            st.session_state.spending_data[current_dial]["actual"] = actual
            # Move to the next dial if available.
            if current_index + 1 < len(top_dials):
                st.session_state.spending_index += 1
                st.session_state.spending_subphase = "ideal"
            else:
                # Finished input for all dials. Move to final results.
                st.session_state.phase = "final"
            st.rerun()

import requests
import json
import streamlit as st
import altair as alt
import pandas as pd

def send_results_via_google_app_script(recipient_email, subject, html_body):
    # Replace with your actual Google Apps Script URL
    web_app_url = "https://script.google.com/macros/s/AKfycbw4mMc-fBfc1r6DBgP3nwEKdycuZufUGjm8sUAr89PGfYcYVKDHAjKzvT3W_wbRMeVq/exec"
    
    payload = {
        "email": recipient_email,
        "subject": subject,
        "body": html_body
    }
    
    try:
        response = requests.post(web_app_url, data=json.dumps(payload))
        response_data = response.json()
        
        if response_data.get("status") == "success":
            st.success("Email sent successfully!")
        else:
            st.error("Error sending email: " + response_data.get("message", "Unknown error"))
    except Exception as e:
        st.error(f"An exception occurred: {e}")

def show_final_results():
    """Display the final summary page with a grouped bar chart for the top 3 money dials,
    a custom explanatory message including insights based on spending differences,
    a horizontal rule, an email input, and a reference image."""
    
    # Display the persistent header.
    app_header()
    st.title("Your Money Dial Spending Summary")
    
    # Ensure that top_dials is available.
    if "top_dials" not in st.session_state:
        st.error("Top money dials not found.")
        return
    
    # Prepare the data for the grouped bar chart.
    data = []
    for dial in st.session_state.top_dials:
        ideal = st.session_state.spending_data[dial]["ideal"]
        actual = st.session_state.spending_data[dial]["actual"]
        data.append({"Money Dial": dial, "Allocation": "Ideal", "Amount": ideal})
        data.append({"Money Dial": dial, "Allocation": "Actual", "Amount": actual})
    
    df = pd.DataFrame(data)
    
    # Create a grouped (side-by-side) bar chart using Altair.
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Money Dial:N", 
                title="Money Dial", 
                sort=st.session_state.top_dials,
                axis=alt.Axis(grid=False)
        ),
        xOffset=alt.X("Allocation:N", title="Allocation"),
        y=alt.Y("Amount:Q", 
                title="Amount", 
                axis=alt.Axis(grid=False, format="d", tickMinStep=1)
        ),
        color=alt.Color("Allocation:N", 
                        scale=alt.Scale(
                            domain=["Ideal", "Actual"],
                            range=["#682d24", "#ff9e70"]
                        ), 
                        title="Allocation"
        ),
        tooltip=["Money Dial", "Allocation", "Amount"]
    ).properties(
        width=200,
        height=400,
        title="Ideal vs. Actual Spending"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    # ----- New Insight Calculation -----
    count_ideal_gt_actual = 0
    for dial in st.session_state.top_dials:
        ideal = st.session_state.spending_data[dial]["ideal"]
        actual = st.session_state.spending_data[dial]["actual"]
        if ideal > actual:
            count_ideal_gt_actual += 1
    
    insight_style = (
        '<div style="background-color: #ff9e70; padding: 15px; border-radius: 5px; '
        'font-size: 20px; line-height: 1.5; margin-bottom: 20px;">'
    )
    
    if count_ideal_gt_actual >= 2:
        insight_message = (
            insight_style +
            "<strong>Insight:</strong><br>"
            "It looks like you're spending less in the areas you really care about than you wish you were.  "
            "This is a great financial goal to work towards! It may not always be possible, but it's worth thinking about "
            "if you can free up money from somewhere you care about less to be able to spend more on these!"
            "</div>"
        )
    else:
        insight_message = (
            insight_style +
            "<strong>Insight:</strong><br>"
            "Wow - it looks like you already spend as much or more than you would like to on your top money dials!  "
            "This is generally very good, the goal is to get maximum satisfaction from your money and feel like you're able to really "
            "spend on the things you love. One thing to think about is which money dials does your partner or loved ones have? Are you spending enough on these?"
            "</div>"
        )
    
    st.markdown(insight_message, unsafe_allow_html=True)
    
    # Display a horizontal rule.
    st.markdown("___")
    
    # ----- Email Section -----
    st.markdown("### Get a copy of your results by email:")
    user_email = st.text_input("Enter your email address:")
    
    # Prepare email subject and message.
    email_subject = "Your Money Dial Results"
    email_body = f"""
    <html>
      <body>
        <h2>Your Money Dial Results</h2>
        <p>Top Money Dial: {st.session_state.top_dials[0]}</p>
        <p>Other top money dials: {" ,".join(st.session_state.top_dials[1:])}</p>
        <hr>
        <p>Thank you for taking the quiz!</p>
      </body>
    </html>
    """
    
    if st.button("Send Email"):
        send_results_via_google_app_script(user_email, email_subject, email_body)
    
    # Display the reference image.
    st.subheader("Reference")
    st.image("MoneyDials2.png", caption="Reference Image", width=700)
    
    # Optional: A button to restart the entire app.
    if st.button("Restart All"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

    
    # Display the reference image.
    st.subheader("Reference")
    st.image("MoneyDials2.png", caption="Reference Image", width=700)
    
    # Optional: A button to restart the entire app.
    if st.button("Restart All"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# -----------------------------
# Main App Logic (Page Flow)
# -----------------------------
if st.session_state.phase == "quiz":
    if st.session_state.current_question < len(questions):
        show_quiz()
    else:
        # When all quiz questions are answered, show the results page.
        show_quiz_results()

elif st.session_state.phase == "spending":
    show_spending_input()

elif st.session_state.phase == "final":
    show_final_results()


