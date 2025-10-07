import streamlit as st
from generate import generate_batch
import time

st.set_page_config(page_title="AI LMS - Math", layout="wide")

# --- Basic CSS to hide Streamlit header/menu/footer when in locked mode
HIDE_STREAMLIT = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.appview-container .css-1adrfps {padding-top: 0rem;}
</style>
"""

# --- Demo storage (in-memory for now)
if 'user' not in st.session_state:
    st.session_state.user = {
        'username': 'xyz',
        'dob': '1995-07-15',
        'level_math': 3,
        'batches_completed': 0
    }

# --- Navigation
st.sidebar.title("AI-LMS")
page = st.sidebar.radio("Go to", ["Profile", "Lectures", "Assignments (Math)"])

# Hide sidebar in locked mode
if st.session_state.get('locked_mode', False):
    st.markdown(HIDE_STREAMLIT, unsafe_allow_html=True)

# ---------------- PROFILE ----------------
if page == 'Profile':
    st.header("Profile")
    user = st.session_state.user
    st.write("**Username:**", user['username'])
    st.write("**DOB:**", user['dob'])
    st.write("Current Math Level:", user['level_math'])
    st.write("Batches Completed:", user['batches_completed'])

# ---------------- LECTURES ----------------
elif page == 'Lectures':
    st.header("Lectures")
    st.write("Sample lecture video:")
    st.video('static/sample_lecture.mp4')

# ---------------- ASSIGNMENTS ----------------
elif page == 'Assignments (Math)':
    st.header("Math Assignment — Adaptive (10 batches of 3)")
    user = st.session_state.user
    st.write(f"Starting Level: **{user['level_math']}**")

    if not st.session_state.get('in_progress', False):
        if st.button("Start Assignment (Lock interface)"):
            st.session_state.in_progress = True
            st.session_state.locked_mode = True
            st.session_state.batch_index = 0
            st.session_state.level = user['level_math']
            st.session_state.results = []
            st.rerun()
    else:
        if st.session_state.batch_index >= 10:
            st.success("✅ All 10 batches completed!")
            user['level_math'] = st.session_state.level
            user['batches_completed'] += 10
            st.session_state.in_progress = False
            st.session_state.locked_mode = False
            if st.button("Return to main view"):
                st.rerun()
        else:
            batch_no = st.session_state.batch_index + 1
            st.subheader(f"Batch {batch_no} / 10 — Level {st.session_state.level}")

            # Generate or fetch questions
            if f'batch_{st.session_state.batch_index}_questions' not in st.session_state:
                with st.spinner("Generating questions..."):
                    questions = generate_batch(level=st.session_state.level, batch_size=3)
                st.session_state[f'batch_{st.session_state.batch_index}_questions'] = questions
                st.session_state[f'batch_{st.session_state.batch_index}_start_ts'] = int(time.time() * 1000)
            else:
                questions = st.session_state[f'batch_{st.session_state.batch_index}_questions']

            user_responses = []
            for i, q in enumerate(questions):
                st.markdown(f"**Q{i+1}:**\n\n{q}")
                resp = st.text_input(f"Your Answer for Q{i+1}", key=f"resp_{st.session_state.batch_index}_{i}")
                user_responses.append(resp)

            if st.button("Submit Batch"):
                end_ts = int(time.time() * 1000)
                start_ts = st.session_state[f'batch_{st.session_state.batch_index}_start_ts']
                elapsed_ms = end_ts - start_ts

                # Fake grading logic (since model doesn't return answers)
                correct_count = sum(1 for r in user_responses if r.strip() != "")
                avg_time_per_q = elapsed_ms / (3 * 1000)

                old_level = st.session_state.level
                if correct_count == 3 and avg_time_per_q < 20:
                    st.session_state.level = min(10, old_level + 1)
                    st.success(f"🎉 3/3 correct and fast — Level up to {st.session_state.level}.")
                elif correct_count >= 2:
                    st.info(f"{correct_count}/3 correct — stay at level {old_level}.")
                else:
                    st.session_state.level = max(1, old_level - 1)
                    st.warning(f"{correct_count}/3 correct — Level down to {st.session_state.level}.")

                st.session_state.results.append({
                    'batch': st.session_state.batch_index,
                    'questions': questions,
                    'responses': user_responses,
                    'elapsed_ms': elapsed_ms,
                    'level_after': st.session_state.level
                })

                st.session_state.batch_index += 1
                st.rerun()

            if st.button("Abort Assignment (Save Progress)"):
                user['level_math'] = st.session_state.level
                st.session_state.in_progress = False
                st.session_state.locked_mode = False
                st.rerun()
