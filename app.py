import streamlit as st
import random
import time

# ---------------------------------------------------
# 80 QUESTIONS BANK (YOUR EXACT PROVIDED QUESTIONS)
# ---------------------------------------------------

QUESTIONS = [

    # -------------------- FIRST 40 MCQs --------------------
    {
        "q": "Income for performing assets is recognized on:",
        "options": ["Cash basis", "Accrual basis", "Realization basis", "None"],
        "answer": 1,
    },
    {
        "q": "In NPAs, recoveries are appropriated first towards:",
        "options": ["Interest", "Charges", "Principal", "Court fee"],
        "answer": 2,
    },
    {
        "q": "OTS recoveries go first to:",
        "options": ["Interest", "Principal", "Penalties", "Charges"],
        "answer": 1,
    },
    {
        "q": "Back-dated NPA classification: past recoveries go first to:",
        "options": ["Principal", "Interest", "Charges", "Penalty"],
        "answer": 1,
    },
    {
        "q": "NCLT admitted accounts are treated as:",
        "options": ["Standard accounts", "Suit filed accounts", "ARC transferred accounts", "Write-offs"],
        "answer": 1,
    },
    {
        "q": "Income on locker rent/dividend recognized on:",
        "options": ["Accrual", "Realization", "Either", "Never"],
        "answer": 1,
    },
    {
        "q": "Foreign currency deposits initially recorded at:",
        "options": ["Spot rate", "FEDAI weekly average", "RBI reference rate", "Closing rate"],
        "answer": 1,
    },
    {
        "q": "NOSTRO balances at quarter end valued at:",
        "options": ["Transaction rate", "Historical rate", "Closing rate", "Weekly average"],
        "answer": 2,
    },
    {
        "q": "Overseas branches are treated as:",
        "options": ["Integral operations", "Non-integral operations", "Joint operations", "Independent ops"],
        "answer": 1,
    },
    {
        "q": "Exchange differences of foreign branches go to:",
        "options": ["P&L", "OCI", "Reserves", "FCTR"],
        "answer": 3,
    },
    {
        "q": "Classification of advances includes:",
        "options": ["Standard, Substandard, Doubtful, Loss", "Good, Bad, Medium", "High risk, Low risk", "None"],
        "answer": 0,
    },
    {
        "q": "Restructured assets require provision for:",
        "options": ["Interest earned", "Diminution in fair value", "Extra profit", "Nil"],
        "answer": 1,
    },
    {
        "q": "Hedging derivatives are accounted on:",
        "options": ["Settlement basis", "Accrual basis", "Cash basis", "Realization"],
        "answer": 1,
    },
    {
        "q": "Trading derivatives MTM gains/losses go to:",
        "options": ["Balance sheet", "P&L", "Capital", "OCI"],
        "answer": 1,
    },
    {
        "q": "Depreciation method used:",
        "options": ["WDV", "Units of production", "SLM", "None"],
        "answer": 2,
    },
    {
        "q": "Assets costing ≤ ₹1000 are:",
        "options": ["Capitalized", "Expensed", "Partially depreciated", "Deferred"],
        "answer": 1,
    },
    {
        "q": "Small assets between ₹1000–₹5000 depreciated at:",
        "options": ["5%", "10%", "100%", "33%"],
        "answer": 2,
    },
    {
        "q": "Depreciation on revalued portion adjusted via:",
        "options": ["Capital reserve", "P&L", "Revaluation reserve", "FCTR"],
        "answer": 2,
    },
    {
        "q": "Pension & gratuity liability measured using:",
        "options": ["SLM", "Actuarial valuation", "Cash basis", "Random estimate"],
        "answer": 1,
    },
    {
        "q": "Deferred tax is based on:",
        "options": ["Permanent differences", "Timing differences", "Both", "None"],
        "answer": 1,
    },
    {
        "q": "DTA on losses needs:",
        "options": ["Reasonable certainty", "Virtual certainty + Convincing evidence", "Assumptions", "History only"],
        "answer": 1,
    },
    {
        "q": "Diluted EPS is excluded when:",
        "options": ["Anti-dilutive", "Dilutive", "Higher than basic", "Lower than basic"],
        "answer": 0,
    },
    {
        "q": "Impairment loss recognized when:",
        "options": ["Recoverable > carrying", "Carrying > recoverable", "Equal", "Never"],
        "answer": 1,
    },
    {
        "q": "Primary segment per AS-17:",
        "options": ["Customer", "Business", "Geography", "Product"],
        "answer": 1,
    },
    {
        "q": "Provision recognized only when:",
        "options": ["Possible obligation", "Probable + Reliable estimate", "Remote loss", "No outflow"],
        "answer": 1,
    },
    {
        "q": "Contingent assets are:",
        "options": ["Recognized", "Disclosed", "Neither", "Deferred"],
        "answer": 2,
    },
    {
        "q": "ARC sale income recognized only to extent of:",
        "options": ["Total sale value", "Cash above NBV", "Total cash", "Difference in values"],
        "answer": 1,
    },
    {
        "q": "Forward contracts revalued at:",
        "options": ["Spot rate", "FEDAI rate", "Historical rate", "Market rate"],
        "answer": 1,
    },
    {
        "q": "Interest on MBS recognized on:",
        "options": ["Accrual", "Realization", "Settlement", "MTM"],
        "answer": 1,
    },
    {
        "q": "Leave encashment provision based on:",
        "options": ["Estimate", "Actuarial valuation", "Cash payout", "History"],
        "answer": 1,
    },
    {
        "q": "If derivative designated with MTM asset:",
        "options": ["Ignore MTM", "MTM recognized", "Loss deferred", "None"],
        "answer": 1,
    },
    {
        "q": "Depreciation for asset purchased during year:",
        "options": ["Partial year", "Full year", "Half-year", "Pro-rata"],
        "answer": 1,
    },
    {
        "q": "Consignment precious metal income recognized:",
        "options": ["Dispatch", "Sale completion", "Receipt", "Invoice"],
        "answer": 1,
    },
    {
        "q": "Income of foreign branches recognized as per:",
        "options": ["ICAI", "RBI", "Local laws", "AS 11"],
        "answer": 2,
    },
    {
        "q": "Deferred tax measured using:",
        "options": ["Future tax rates", "Enacted/substantively enacted rates", "RBI rates", "Average rates"],
        "answer": 1,
    },
    {
        "q": "Leave encashment is a:",
        "options": ["Defined contribution", "Defined benefit", "Contingent liability", "Provision"],
        "answer": 1,
    },
    {
        "q": "Depreciation rate for computers:",
        "options": ["20%", "33.33%", "25%", "15%"],
        "answer": 1,
    },
    {
        "q": "Furniture depreciation rate:",
        "options": ["5%", "10%", "20%", "100%"],
        "answer": 1,
    },
    {
        "q": "Contingent liabilities disclosed when:",
        "options": ["Remote", "Reasonably possible not measurable", "Certain", "Probable"],
        "answer": 1,
    },
    {
        "q": "Gratuity of overseas staff follows:",
        "options": ["Indian GAAP", "IFRS", "Local regulations", "AS 15"],
        "answer": 2,
    },

    # -------------------- NEXT 40 ADVANCED MCQs --------------------
    {
        "q": "The applicable framework for Bank financials includes:",
        "options": [
            "Indian AS + IFRS + RBI",
            "Indian GAAP + ICAI AS + RBI + Statutory laws",
            "IFRS only",
            "Indian GAAP only",
        ],
        "answer": 1,
    },
    {
        "q": "Which statements about estimates are TRUE?",
        "options": [
            "Estimates affect only assets.",
            "Estimates affect assets, liabilities, contingent liabilities, income, expenses.",
            "Future results may differ from estimates.",
            "All are false"
        ],
        "answer": 2,
    },
    {
        "q": "Recovery in NPAs appropriated to:",
        "options": ["Charges", "Interest", "Principal", "Equally"],
        "answer": 2,
    },
    {
        "q": "Which incomes recognized only on realization?",
        "options": ["Locker rent", "Commission", "Dividend", "All 3"],
        "answer": 3,
    },
    {
        "q": "Foreign currency lending uses:",
        "options": ["Daily RBI rate", "Spot rate", "FEDAI weekly avg", "Monthly avg"],
        "answer": 2,
    },
    {
        "q": "Overseas branches as Non-Integral → Exchange differences go to:",
        "options": ["P&L", "FCTR", "Average rate", "Not translated"],
        "answer": 1,
    },
    {
        "q": "AFS quarterly depreciation goes to:",
        "options": ["P&L", "Capital", "AFS Reserve", "Ignored"],
        "answer": 2,
    },
    {
        "q": "Valued at Re.1 when no data is available:",
        "options": ["Quoted equity", "Corporate bonds", "Unquoted equity", "Govt securities"],
        "answer": 2,
    },
    {
        "q": "Correct mutual fund hierarchy:",
        "options": [
            "NAV → Market → Repurchase",
            "Book → Market → NAV",
            "Market → NAV → Repo",
            "Market → Repurchase → NAV"
        ],
        "answer": 3,
    },
    {
        "q": "Valuation frequency: HFT = Daily, AFS = Quarterly?",
        "options": ["Yes", "No", "Half-yearly", "Monthly"],
        "answer": 0,
    },
    {
        "q": "AFS gain/loss on sale of equity goes to:",
        "options": ["P&L", "Capital Reserve", "AFS Reserve", "None"],
        "answer": 1,
    },
    {
        "q": "IFR target:",
        "options": ["1% HTM", "2% AFS+HFT", "5% all", "10% AFS"],
        "answer": 1,
    },
    {
        "q": "Transfer to IFR is lower of:",
        "options": [
            "Market appreciation",
            "Net profit on sale OR net profit after appropriations",
            "Book or market value",
            "RBI or market"
        ],
        "answer": 1,
    },
    {
        "q": "HTM valued at:",
        "options": ["Market value", "Fair value", "Amortized cost", "MTM"],
        "answer": 2,
    },
    {
        "q": "Profit on HTM sale goes to:",
        "options": ["Capital Reserve", "P&L", "AFS Reserve", "Revenue Reserve"],
        "answer": 0,
    },
    {
        "q": "Matured investments shown under:",
        "options": ["Investments", "Other Assets", "CL", "Misc Income"],
        "answer": 1,
    },
    {
        "q": "Asset ≤ 1000:",
        "options": ["Capitalized", "Expensed", "100% dep", "Re.1"],
        "answer": 1,
    },
    {
        "q": "Asset costing 3800:",
        "options": ["Expensed", "Capitalized", "100% dep + Re.1", "Deferred"],
        "answer": 2,
    },
    {
        "q": "Depreciation on revalued portion charged to:",
        "options": ["Not charged", "P&L + Reserve adjusted", "AFS", "Capital"],
        "answer": 1,
    },
    {
        "q": "SLM used for:",
        "options": ["Premises only", "Premises + vehicles", "All FA", "Only software"],
        "answer": 2,
    },
    {
        "q": "Advances shown:",
        "options": ["Gross", "Net only", "Net of specific; standard separate", "Only net if NPA"],
        "answer": 2,
    },
    {
        "q": "Provision for diminution on restructuring:",
        "options": ["Capital", "Reduced from advances", "Other liability", "Reserves"],
        "answer": 1,
    },
    {
        "q": "Which about derivatives is correct?",
        "options": ["Hedging deferred", "Trading MTM → P&L", "Both 1 & 2", "None"],
        "answer": 2,
    },
    {
        "q": "Trading derivative termination gain/loss:",
        "options": ["Deferred", "P&L", "Capital reserve", "Ignored"],
        "answer": 1,
    },
    {
        "q": "Gratuity/pension provision via:",
        "options": ["History", "Actuarial", "RBI", "Board"],
        "answer": 1,
    },
    {
        "q": "DTA on losses requires:",
        "options": ["Probability", "Reasonable certainty", "Virtual certainty", "Approval"],
        "answer": 2,
    },
    {
        "q": "Deferred tax standard:",
        "options": ["AS 11", "AS 29", "AS 20", "AS 22"],
        "answer": 3,
    },
    {
        "q": "EPS denominator uses:",
        "options": ["Total shares", "Year-end shares", "Weighted avg shares", "Paid-up capital"],
        "answer": 2,
    },
    {
        "q": "Segment reporting standard:",
        "options": ["AS 3", "AS 17", "AS 20", "AS 11"],
        "answer": 1,
    },
    {
        "q": "Provision recognized when:",
        "options": ["1 & 2", "2 & 3", "All 3", "Only 1"],
        "answer": 2,
    },
    {
        "q": "Contingent liabilities are:",
        "options": ["Recognized", "Disclosed", "Ignored", "Provided"],
        "answer": 1,
    },
    {
        "q": "Contingent assets are:",
        "options": ["Recognized", "Disclosed", "Ignored", "Recognized when certain"],
        "answer": 2,
    },
    {
        "q": "NOSTRO/ACU Dollar translated at:",
        "options": ["FEDAI avg", "Closing rate", "Monthly", "RBI"],
        "answer": 1,
    },
    {
        "q": "Forward contracts revalued at:",
        "options": ["Initial rate", "FEDAI year-end", "RBI rate", "Midpoint"],
        "answer": 1,
    },
    {
        "q": "Book value of securities changes due to:",
        "options": ["Revaluation", "RBI", "Market only", "Settlement"],
        "answer": 0,
    },
    {
        "q": "Shifting categories allowed:",
        "options": ["Anytime", "Once yearly with Board OK", "Never", "Only HTM→AFS"],
        "answer": 1,
    },
    {
        "q": "Income on T-Bills:",
        "options": ["Interest", "Discount income", "Fair value gain", "Capital reserve"],
        "answer": 1,
    },
    {
        "q": "Investments accounted on:",
        "options": ["Trade date", "Settlement date", "RBI", "Either"],
        "answer": 1,
    },
    {
        "q": "Govt business commission:",
        "options": ["Accrual", "Realization", "Settlement", "Approval"],
        "answer": 0,
    },
    {
        "q": "If NPA retrospective, recovery goes first to:",
        "options": ["Principal", "Interest", "Charges", "Overdue"],
        "answer": 1,
    }
]

TOTAL_QUESTIONS = len(QUESTIONS)

# ---------------------------------------------------
# INITIALIZE SESSION STATE
# ---------------------------------------------------
if "started" not in st.session_state:
    st.session_state.started = False
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected" not in st.session_state:
    st.session_state.selected = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# ---------------------------------------------------
# START SCREEN
# ---------------------------------------------------
if not st.session_state.started:
    st.title("📘 Bank Accounting Policy Quiz — 80 Questions")
    st.subheader("Single-Question Interactive Mode")

    st.write("""
    **How it works:**  
    - 80 MCQs  
    - One question at a time  
    - Submit → get instant feedback → Next  
    - Progress bar  
    - Mobile responsive  
    """)

    if st.button("🚀 Start Quiz"):
        st.session_state.started = True
        st.session_state.start_time = time.time()

    st.stop()

# ---------------------------------------------------
# QUIZ DISPLAY
# ---------------------------------------------------

# Progress bar
st.progress((st.session_state.q_index + 1) / TOTAL_QUESTIONS)

st.write(f"### Question {st.session_state.q_index + 1} of {TOTAL_QUESTIONS}")

question = QUESTIONS[st.session_state.q_index]

# Radio buttons
st.session_state.selected = st.radio(
    question["q"],
    question["options"],
    index=None,
    key=f"radio_{st.session_state.q_index}"
)

# Submit button
if not st.session_state.answered:
    if st.button("Submit"):
        if st.session_state.selected is None:
            st.warning("Please select an option!")
            st.stop()
        st.session_state.answered = True

# After answering
if st.session_state.answered:
    correct_idx = question["answer"]
    correct_answer = question["options"][correct_idx]

    if st.session_state.selected == correct_answer:
        st.success("Correct! ✅")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect ❌\n\n**Correct Answer: {correct_answer}**")

    if st.button("Next Question →"):
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.session_state.selected = None

        if st.session_state.q_index == TOTAL_QUESTIONS:
            st.success("🎉 Quiz Completed!")
            st.balloons()
            st.write(f"### Your final score: **{st.session_state.score} / {TOTAL_QUESTIONS}**")
            st.stop()

        st.experimental_rerun()
