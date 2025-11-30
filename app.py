import streamlit as st
import random
import json
from datetime import datetime

st.set_page_config(page_title="Banking Accounting Quiz Game", layout="centered")

# ---- QUESTIONS BANK (40 MCQs) ----
QUESTIONS = [
    {
        "q": "In the Bank’s accounting policies, which... applicable framework?",
        "options": ["Indian AS + IFRS + RBI regulations","Indian GAAP + ICAI AS + RBI guidelines + statutory provisions","IFRS only + Banking Regulation Act","Indian GAAP only without RBI"],
        "answer": 1
    },
    {
        "q": "Which statement about the use of estimates is TRUE?",
        "options": ["Only 2","1 & 2","2 & 3","All three"],
        "answer": 2
    },
    {
        "q": "For NPAs, recovery received after classification is appropriated:",
        "options": ["Charges → Interest","Interest → Principal","Principal → Interest/Charges","Equally split"],
        "answer": 1
    },
    {
        "q": "Which incomes are on realization basis?",
        "options": ["1,2,3","2 & 4","All","Only 3"],
        "answer": 0
    },
    {
        "q": "A foreign currency loan is recorded at:",
        "options": ["RBI reference rate","FEDAI weekly avg","Monthly closing","Spot rate"],
        "answer": 1
    },
    {
        "q": "Overseas branches (Non-integral) → exchange differences go to:",
        "options": ["P&L","FCTR","Average rate","Not translated"],
        "answer": 1
    },
    {
        "q": "Net depreciation for AFS is:",
        "options": ["P&L","Credit P&L","AFS Reserve","Ignored"],
        "answer": 0
    },
    {
        "q": "Unquoted equity is valued at:",
        "options": ["Quoted price","Debt valuation","Re.1","Indexed"],
        "answer": 2
    },
    {
        "q": "MF valuation hierarchy:",
        "options": ["NAV→Market→Repo","Book→Market→NAV","Market→Repo→NAV","Market→Repurchase→NAV"],
        "answer": 3
    },
    {
        "q": "Valuation frequency: HFT vs AFS",
        "options": ["Q,D","D,Q","HY,Q","M,M"],
        "answer": 1
    },
    ... (Remaining 30 MCQs inserted similarly) ...
], "a": 1},
    {"q": "In NPAs, recoveries are appropriated first towards:", "opts": ["Interest", "Charges", "Principal", "Court fee"], "a": 2},
    {"q": "OTS recoveries go first to:", "opts": ["Interest", "Principal", "Penalties", "Charges"], "a": 1},
    {"q": "Back-dated NPA classification: past recoveries go first to:", "opts": ["Principal", "Interest", "Charges", "Penalty"], "a": 1},
    {"q": "NCLT admitted accounts are treated as:", "opts": ["Standard accounts", "Suit filed accounts", "ARC transferred accounts", "Write-offs"], "a": 1},
    {"q": "Income on items like locker rent/dividend is recognized:", "opts": ["Accrual", "Realization", "Either", "Never"], "a": 1},
    {"q": "Foreign currency deposits initially recorded at:", "opts": ["Spot rate", "FEDAI weekly average", "RBI reference rate", "Closing rate"], "a": 1},
    {"q": "NOSTRO balances at quarter end are valued at:", "opts": ["Transaction rate", "Historical rate", "Closing rate", "Weekly average"], "a": 2},
    {"q": "Overseas branches are treated as:", "opts": ["Integral operations", "Non-integral operations", "Joint operations", "Independent operations"], "a": 1},
    {"q": "Exchange differences of foreign branches are transferred to:", "opts": ["P&L", "OCI", "Reserves", "FCTR"], "a": 3},
    {"q": "Classification of advances includes:", "opts": ["Standard, Substandard, Doubtful, Loss", "Good, Bad, Medium", "High risk, Low risk", "None"], "a": 0},
    {"q": "Restructured assets require provision for:", "opts": ["Interest earned", "Diminution in fair value", "Extra profit", "Nil"], "a": 1},
    {"q": "Hedging derivatives are accounted on:", "opts": ["Settlement basis", "Accrual basis", "Cash basis", "Realization"], "a": 1},
    {"q": "Trading derivatives MTM gains/losses go to:", "opts": ["Balance sheet", "P&L", "Capital", "OCI"], "a": 1},
    {"q": "Depreciation method used:", "opts": ["WDV", "Units of production", "Straight line", "None"], "a": 2},
    {"q": "Assets costing ≤ ₹1000 are:", "opts": ["Capitalized", "Expensed", "Partially depreciated", "Deferred"], "a": 1},
    {"q": "Small assets between ₹1000–₹5000 are depreciated at:", "opts": ["5%", "10%", "100%", "33%"], "a": 2},
    {"q": "Depreciation on revalued portion is adjusted via:", "opts": ["Capital reserve", "P&L", "Revaluation reserve", "FCTR"], "a": 2},
    {"q": "Pension & gratuity liability measured using:", "opts": ["Straight-line method", "Actuarial valuation", "Cash basis", "Random estimates"], "a": 1},
    {"q": "Deferred tax is based on:", "opts": ["Permanent differences", "Timing differences", "Both", "None"], "a": 1},
    {"q": "DTA on losses needs:", "opts": ["Reasonable certainty", "Virtual certainty + convincing evidence", "Assumptions", "Historical data only"], "a": 1},
    {"q": "Diluted EPS is excluded when:", "opts": ["Anti-dilutive", "Dilutive", "Higher than basic EPS", "Lower than basic EPS"], "a": 0},
    {"q": "Impairment loss recognized when:", "opts": ["Recoverable > carrying", "Carrying > recoverable", "Both equal", "Never"], "a": 1},
    {"q": "Primary segment per AS-17:", "opts": ["Customer", "Business", "Geography", "Product"], "a": 1},
    {"q": "Provision recognized only when:", "opts": ["Possible obligation", "Probable outflow + reliable estimate", "Remote loss", "No outflow expected"], "a": 1},
    {"q": "Contingent assets are:", "opts": ["Recognized", "Disclosed", "Neither recognized nor disclosed", "Deferred"], "a": 2},
    {"q": "ARC sale income recognized only to extent of:", "opts": ["Total sale value", "Cash component above NBV", "Total cash", "Difference between book value and sale value"], "a": 1},
    {"q": "Forward contracts revalued at:", "opts": ["Spot rate", "FEDAI rate", "Historical rate", "Market rate"], "a": 1},
    {"q": "Interest on MBS recognized on:", "opts": ["Accrual", "Realization", "Settlement", "MTM basis"], "a": 1},
    {"q": "Provision for leave encashment is based on:", "opts": ["Management estimate", "Actuarial valuation", "Cash payout", "Historical cost"], "a": 1},
    {"q": "If derivative is designated with an MTM asset:", "opts": ["MTM ignored", "Derivative MTM is recognized", "Loss deferred", "None"], "a": 1},
    {"q": "Depreciation for any asset purchased during year is for:", "opts": ["Partial year", "Full year", "Half-year", "Pro-rata"], "a": 1},
    {"q": "Consignment precious metal income recognized:", "opts": ["On dispatch", "On sale completion", "On receipt", "On invoice"], "a": 1},
    {"q": "Income of foreign branches recognized as per:", "opts": ["ICAI", "RBI", "Local laws", "AS 11 only"], "a": 2},
    {"q": "Deferred tax measured using:", "opts": ["Future tax rates", "Enacted/substantively enacted rates", "RBI rates", "Average rates"], "a": 1},
    {"q": "Leave encashment is a:", "opts": ["Defined contribution", "Defined benefit", "Contingent liability", "Provision"], "a": 1},
    {"q": "Depreciation rate for computers:", "opts": ["20%", "33.33%", "25%", "15%"], "a": 1},
    {"q": "Furniture depreciation rate:", "opts": ["5%", "10%", "20%", "100%"], "a": 1},
    {"q": "Contingent liabilities disclosed when:", "opts": ["Remote", "Reasonably possible but not measurable", "Certain", "Probable"], "a": 1},
    {"q": "Gratuity of overseas staff follows:", "opts": ["Indian GAAP", "IFRS", "Local regulations", "AS 15"], "a": 2}
]

# ---- Helper functions ----

def init_state():
    if 'order' not in st.session_state:
        st.session_state.order = list(range(len(QUESTIONS)))
        random.shuffle(st.session_state.order)
    if 'idx' not in st.session_state:
        st.session_state.idx = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'start_time' not in st.session_state:
        st.session_state.start_time = datetime.utcnow().isoformat()


init_state()

st.title("🏦 Banking Accounting Quiz Game")
st.markdown("A quick 40-question multiple choice quiz — mobile friendly. Good luck! \n\nUse the **Next** button to save an answer and move on.")

cols = st.columns([3,1])
with cols[1]:
    st.metric("Progress", f"{st.session_state.idx}/{len(QUESTIONS)}")

# Show question
q_idx = st.session_state.order[st.session_state.idx]
qobj = QUESTIONS[q_idx]
st.subheader(f"Q{st.session_state.idx + 1}. {qobj['q']}")
choice = st.radio("", qobj['opts'], key=f"q_{st.session_state.idx}")

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Previous"):
        if st.session_state.idx > 0:
            st.session_state.idx -= 1

with col2:
    if st.button("Next"):
        # save answer
        selected = qobj['opts'].index(choice)
        st.session_state.answers[q_idx] = selected
        # score update (simple): score counted at end, but we maintain running score
        st.session_state.idx += 1
        if st.session_state.idx >= len(QUESTIONS):
            st.session_state.idx = len(QUESTIONS)

with col3:
    if st.button("Quit & Submit"):
        st.session_state.idx = len(QUESTIONS)

# If completed
if st.session_state.idx >= len(QUESTIONS):
    # calculate final score
    final_score = 0
    for i, q in enumerate(QUESTIONS):
        ans = st.session_state.answers.get(i, None)
        if ans is not None and ans == q['a']:
            final_score += 1

    st.markdown("---")
    st.success(f"Quiz Completed! Your score: {final_score} / {len(QUESTIONS)}")

    # Review
    if st.checkbox("Show review of answers"):
        for i, q in enumerate(QUESTIONS):
            user_ans = st.session_state.answers.get(i, None)
            correct = q['a']
            col_a, col_b = st.columns([4,1])
            with col_a:
                st.write(f"**Q{i+1}.** {q['q']}")
                st.write("- Your answer: " + (q['opts'][user_ans] if user_ans is not None else "No answer"))
                st.write("- Correct answer: " + q['opts'][correct])
            with col_b:
                if user_ans == correct:
                    st.write(":white_check_mark:")
                else:
                    st.write(":x:")

    # Download results
    result_data = {
        'score': final_score,
        'total': len(QUESTIONS),
        'answers': st.session_state.answers,
        'timestamp': datetime.utcnow().isoformat()
    }
    st.download_button("Download Results (JSON)", data=json.dumps(result_data, indent=2), file_name="quiz_results.json")

    if st.button("Play Again"):
        # reset
        st.session_state.order = list(range(len(QUESTIONS)))
        random.shuffle(st.session_state.order)
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.answers = {}
        st.experimental_rerun()

# Footer / help
st.markdown("---")
st.caption("Built for quick revision. Works on mobile. To host: push this file to a GitHub repo and deploy on Streamlit Community Cloud or Hugging Face Spaces.")
