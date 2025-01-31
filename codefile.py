import streamlit as st

# Define quiz questions and categories
def quiz():
    st.title("Personality Quiz")

    questions = [
        ("1. When it comes to lunch, what’s your preference?", [
            ("Convenience", "Grab something quick and easy to save time"),
            ("Experiences", "Try out a new restaurant or café every time"),
            ("Health", "Meal-prep at home so I know it’s healthy"),
            ("Relationships", "Meet a friend or family member for lunch")
        ]),
        ("2. It’s Saturday night! How do you like to spend it?", [
            ("Generosity", "I love to host my friends or family."),
            ("Experiences", "Plan a special experience like a concert."),
            ("SelfImprovement", "Definitely work on a personal project."),
            ("Freedom", "I like not having a set plan.")
        ]),
        ("3. How do you feel about traveling?", [
            ("Travel", "Love it! I want to explore as many places as possible."),
            ("Freedom", "Always happy with a weekend away to recharge."),
            ("Health", "Any adventure with lots of hiking or sports works for me!"),
            ("Luxury", "I love traveling in style and splurging on luxury experiences."),
            ("Convenience", "Nah, not for me – lots to do at home!")
        ]),
        ("4. What’s your ideal work environment?", [
            ("Freedom", "A job that allows me to work my own hours and in whichever location I choose."),
            ("Relationships", "An office where I can meet new people and network."),
            ("Travel", "Any job that lets me have long weekends for traveling or the occasional work from abroad."),
            ("SelfImprovement", "Most important for me is feeling like I’m always improving my skills and developing.")
        ]),
        ("5. How do you approach fitness and health?", [
            ("Convenience", "Convenience matters—I like online classes or easy workout options that fit my schedule."),
            ("Health", "I’m happy to invest in a great gym or workout clothing/equipment."),
            ("Relationships", "It’s more of a social thing; I love group classes or going with friends!"),
            ("Experiences", "Fitness isn’t my main focus, but I love splurging on a wellness retreat or trying a new sport now and then.")
        ]),
        ("6. What do you spend the most 'splurge' money on every month?", [
            ("Convenience", "Meal kits to make food easier, being able to take Ubers, someone to help with cleaning or any of the above."),
            ("Travel", "Flights or trips, even if they’re short – I can’t get enough travel!"),
            ("Health", "High-quality fitness classes, health foods, or wellness apps."),
            ("SelfImprovement", "A hobby, course, or app that builds my skills."),
            ("Experiences", "Doing something new and exciting – I like to explore wherever I am and find something unique to try.")
        ]),
        ("7. You come across a windfall of cash. What’s your first thought on how to use it?", [
            ("Luxury", "No question - buy a luxury item I normally can’t afford."),
            ("Experiences", "Wahoo more money to add to my 'fun' fund for experiences with friends."),
            ("Freedom", "Straight to the bank! Best thing I can do is have more financial flexibility in the future."),
            ("Generosity", "Wow - great opportunity to donate part of it to causes I care about!")
        ]),
        ("8. Which best describes your spending philosophy?", [
            ("Luxury", "Focus on quality, even if it means spending a lot more."),
            ("Experiences", "Money is best spent on experiences over stuff. I’ll scrimp unless I get to experience something new."),
            ("SelfImprovement", "There’s no budget if it’s something that feels like it’s helping me grow and develop."),
            ("Relationships", "Extra money goes to improving relationships and treating my loved ones."),
            ("Travel", "Travel. All day. Everyday. I want to see the world.")
        ]),
        ("9. How do you typically approach learning or personal growth?", [
            ("SelfImprovement", "I regularly take online courses or attend workshops."),
            ("Travel", "I travel and experience new cultures to learn more about the world."),
            ("Health", "I engage in self-care practices or focus on activities that support my mental and physical wellness."),
            ("Relationships", "I attend networking events and connect with others who have similar goals.")
        ]),
        ("10. What’s one thing you’re willing to spend more on to treat others?", [
            ("Generosity", "I love to host dinner or throw a fun party."),
            ("Relationships", "Giving gifts or doing something special for a loved one."),
            ("Luxury", "I’ll splurge on a high-end experience or something extravagant for them."),
            ("Experiences", "Taking people on exciting adventures or trips.")
        ]),
        ("11. When it comes to your personal style, what’s most important?", [
            ("Luxury", "The brand – I like to wear pieces that make an impression"),
            ("Convenience", "Comfort and convenience; I don’t like to overthink it"),
            ("Generosity", "Buying things that reflect my values, like eco-friendly or locally made products"),
            ("Health", "Practicality, I like to be able to walk a lot or go to a workout class in my usual clothes")
        ]),
        ("12. If you could improve one area of your life, what would it be?", [
            ("Convenience", "Freeing up more time for things I enjoy by automating daily tasks"),
            ("Relationships", "Building stronger connections with friends, family, or a partner"),
            ("Generosity", "Living more generously by giving more time or money to causes I care about"),
            ("Freedom", "Increasing my ability to travel and explore new places regularly")
        ]),
        ("13. What’s your favourite way to celebrate a personal milestone?", [
            ("Luxury", "Treat myself to something luxurious and indulgent"),
            ("Travel", "Go on an exciting trip or adventure"),
            ("Generosity", "Host a gathering to share the joy with friends or family"),
            ("SelfImprovement", "Reflect on what I’ve achieved and set new goals for growth"),
            ("Freedom", "Take a day off to enjoy the freedom to do whatever I want")
        ])
    ]

    # Initialize session state
    if "step" not in st.session_state:
        st.session_state.step = "quiz"
        st.session_state.answers = {}
        st.session_state.category_scores = {category: 0 for question, options in questions for category, _ in options}

    # Step 1: Take the Quiz
    if st.session_state.step == "quiz":
        st.title("📝 Money Dials Quiz - find out what motivates you with money!")

        # Initialize answer counter
        answered_count = 0

        for idx, (question, options) in enumerate(questions):
            st.write(f"**{idx + 1}. {question}**")
            selected = st.radio(f"Q{idx + 1}", [opt[1] for opt in options], key=f"q{idx}", index=None)  # Show longer text options

            if selected:
                # Track the selected answer
                for category, opt_text in options:
                    if selected == opt_text:
                        # Update category score
                        st.session_state.category_scores[category] += 1
                answered_count += 1  # Increment the counter for each answered question

        # Only show the "Submit Quiz" button once all questions are answered
        if answered_count == len(questions):
            if st.button("Submit Quiz"):
                st.session_state.step = "show_results"
                st.rerun()

    # Step 2: Show Top 3 Categories
    elif st.session_state.step == "show_results":
        # Sort categories by score and get top 3
        top_categories = sorted(st.session_state.category_scores.items(), key=lambda x: x[1], reverse=True)[:3]
        st.session_state.top_categories = top_categories

        st.write("### Your top 3 spending categories are:")
        for idx, (category, score) in enumerate(top_categories, 1):
            st.write(f"{idx}. **{category}** (Score: {score})")

        st.write("### Now, let's explore how much you spend on these categories.")

        if st.button("Continue"):
            st.session_state.step = "ask_ideal_spending"
            st.rerun()

    # Step 3: Ask for Ideal and Actual Spending for Top 3 Categories
    elif st.session_state.step == "ask_ideal_spending":
        st.write("### Please enter your ideal and actual spending for the top 3 categories:")

        ideal_spending = {}
        actual_spending = {}

        for category, _ in st.session_state.top_categories:
            ideal_spending[category] = st.number_input(f"Enter your ideal spending for **{category}** per month ($)", min_value=0, step=10)
            actual_spending[category] = st.number_input(f"Enter your actual spending for **{category}** per month ($)", min_value=0, step=10)

        if st.button("See Results"):
            st.session_state.ideal_spending = ideal_spending
            st.session_state.actual_spending = actual_spending
            st.session_state.step = "show_comparison"
            st.rerun()

    # Step 4: Show Spending Comparison
    elif st.session_state.step == "show_comparison":
        st.write("### Spending Comparison for Your Top 3 Categories")

        total_difference = 0
        for category in st.session_state.top_categories:
            category_name = category[0]
            ideal = st.session_state.ideal_spending.get(category_name, 0)
            actual = st.session_state.actual_spending.get(category_name, 0)
            difference = actual - ideal

            st.write(f"**{category_name}:**")
            st.write(f"💡 *Ideal Spending:* **${ideal}**")
            st.write(f"💰 *Actual Spending:* **${actual}**")

            if difference > 0:
                st.write(f"🔴 You're spending **${difference} more** than your ideal budget.")
            elif difference < 0:
                st.write(f"🟢 You're spending **${abs(difference)} less** than you expected.")
            else:
                st.write("✅ Your spending perfectly aligns with your ideal budget!")

            total_difference += difference

        st.write(f"### Total Difference: **${total_difference}**")

        if st.button("Restart Quiz"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    quiz()
