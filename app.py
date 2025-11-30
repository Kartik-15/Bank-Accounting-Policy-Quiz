import streamlit as st
import random

st.set_page_config(page_title="Bank Accounting Policy Quiz", layout="centered")

# -----------------------------
# 80 MCQs (FULL SET)
# -----------------------------
QUESTIONS = [

# First 40 MCQs
{"q": "Income for performing assets is recognized on:", "options": ["Cash basis", "Accrual basis", "Realization basis", "None"], "answer": 1},

{"q": "In NPAs, recoveries are appropriated first towards:", "options": ["Interest", "Charges", "Principal", "Court fee"], "answer": 2},

{"q": "OTS recoveries go first to:", "options": ["Interest", "Principal", "Penalties", "Charges"], "answer": 1},

{"q": "Back-dated NPA classification: past recoveries go first to:", 
 "options": ["Principal", "Interest", "Charges", "Penalty"], "answer": 1},

{"q": "NCLT admitted accounts are treated as:", 
 "options": ["Standard accounts", "Suit filed accounts", "ARC transferred accounts", "Write-offs"], "answer": 1},

{"q": "Income on items like locker rent/dividend is recognized:", 
 "options": ["Accrual", "Realization", "Either", "Never"], "answer": 1},

{"q": "Foreign currency deposits initially recorded at:", 
 "options": ["Spot rate", "FEDAI weekly average", "RBI reference rate", "Closing rate"], "answer": 1},

{"q": "NOSTRO balances at quarter end are valued at:", 
 "options": ["Transaction rate", "Historical rate", "Closing rate", "Weekly average"], "answer": 2},

{"q": "Overseas branches are treated as:", 
 "options": ["Integral operations", "Non-integral operations", "Joint operations", "Independent operations"], "answer": 1},

{"q": "Exchange differences of foreign branches are transferred to:", 
 "options": ["P&L", "OCI", "Reserves", "FCTR"], "answer": 3},

{"q": "Classification of advances includes:", 
 "options": ["Standard, Substandard, Doubtful, Loss", "Good, Bad, Medium", "High risk, Low risk", "None"], "answer": 0},

{"q": "Restructured assets require provision for:", 
 "options": ["Interest earned", "Diminution in fair value", "Extra profit", "Nil"], "answer": 1},

{"q": "Hedging derivatives are accounted on:", 
 "options": ["Settlement basis", "Accrual basis", "Cash basis", "Realization"], "answer": 1},

{"q": "Trading derivatives MTM gains/losses go to:", 
 "options": ["Balance sheet", "P&L", "Capital", "OCI"], "answer": 1},

{"q": "Depreciation method used:", 
 "options": ["WDV", "Units of production", "Straight line", "None"], "answer": 2},

{"q": "Assets costing ≤ ₹1000 are:", "options": ["Capitalized", "Expensed", "Partially depreciated", "Deferred"], "answer": 1},

{"q": "Small assets between ₹1000–₹5000 are depreciated at:", 
 "options": ["5%", "10%", "100%", "33%"], "answer": 2},

{"q": "Depreciation on revalued portion is adjusted via:", 
 "options": ["Capital reserve", "P&L", "Revaluation reserve", "FCTR"], "answer": 2},

{"q": "Pension & gratuity liability measured using:", 
 "options": ["Straight-line method", "Actuarial valuation", "Cash basis", "Random estimates"], "answer": 1},

{"q": "Deferred tax is based on:", 
 "options": ["Permanent differences", "Timing differences", "Both", "None"], "answer": 1},

{"q": "DTA on losses needs:", 
 "options": ["Reasonable certainty", "Virtual certainty + convincing evidence", "Assumptions", "Historical data only"], "answer": 1},

{"q": "Diluted EPS is excluded when:", 
 "options": ["Anti-dilutive", "Dilutive", "Higher than basic EPS", "Lower than basic EPS"], "answer": 0},

{"q": "Impairment loss recognized when:", 
 "options": ["Recoverable > carrying", "Carrying > recoverable", "Both equal", "Never"], "answer": 1},

{"q": "Primary segment per AS-17:", 
 "options": ["Customer", "Business", "Geography", "Product"], "answer": 1},

{"q": "Provision recognized only when:", 
 "options": ["Possible obligation", "Probable outflow + reliable estimate", "Remote loss", "No outflow expected"], "answer": 1},

{"q": "Contingent assets are:", 
 "options": ["Recognized", "Disclosed", "Neither recognized nor disclosed", "Deferred"], "answer": 2},

{"q": "ARC sale income recognized only to extent of:", 
 "options": ["Total sale value", "Cash component above NBV", "Total cash", "Difference between book value and sale value"], "answer": 1},

{"q": "Forward contracts revalued at:", 
 "options": ["Spot rate", "FEDAI rate", "Historical rate", "Market rate"], "answer": 1},

{"q": "Interest on MBS recognized on:", 
 "options": ["Accrual", "Realization", "Settlement", "MTM basis"], "answer": 1},

{"q": "Provision for leave encashment is based on:", 
 "options": ["Management estimate", "Actuarial valuation", "Cash payout", "Historical cost"], "answer": 1},

{"q": "If derivative is designated with an MTM asset:", 
 "options": ["MTM ignored", "Derivative MTM is recognized", "Loss deferred", "None"], "answer": 1},

{"q": "Depreciation for any asset purchased during year is for:", 
 "options": ["Partial year", "Full year", "Half-year", "Pro-rata"], "answer": 1},

{"q": "Consignment precious metal income recognized:", 
 "options": ["On dispatch", "On sale completion", "On receipt", "On invoice"], "answer": 1},

{"q": "Income of foreign branches recognized as per:", 
 "options": ["ICAI", "RBI", "Local laws", "AS 11 only"], "answer": 2},

{"q": "Deferred tax measured using:", 
 "options": ["Future tax rates", "Enacted/substantively enacted rates", "RBI rates", "Average rates"], "answer": 1},

{"q": "Leave encashment is a:", 
 "options": ["Defined contribution", "Defined benefit", "Contingent liability", "Provision"], "answer": 1},

{"q": "Depreciation rate for computers:", 
 "options": ["20%", "33.33%", "25%", "15%"], "answer": 1},

{"q": "Furniture depreciation rate:", 
 "options": ["5%", "10%", "20%", "100%"], "answer": 1},

{"q": "Contingent liabilities disclosed when:", 
 "options": ["Remote", "Reasonably possible but not measurable", "Certain", "Probable"], "answer": 1},

{"q": "Gratuity of overseas staff follows:", 
 "options": ["Indian GAAP", "IFRS", "Local regulations", "AS 15"], "answer": 2},


# NEXT 40 ADVANCED MCQs
{"q":"The applicable framework for preparing the Bank’s financial statements is:",
 "options":["Indian AS + IFRS + RBI",
            "Indian GAAP + ICAI AS + RBI guidelines + statutory provisions",
            "IFRS only","Indian GAAP only"],"answer":1},

{"q":"Which statements about estimates are TRUE?",
 "options":["Estimates affect only assets.",
            "Estimates affect assets, liabilities, contingent liabilities, income, expenses.",
            "Future results may differ from estimates."],"answer":2},

{"q":"Recovery in NPAs after classification is appropriated first to:",
 "options":["Charges","Interest","Principal","Equally"],"answer":2},

{"q":"Which incomes are recognized only on realization?",
 "options":["Locker rent","Commission except LC/LG/Insurance/Govt business","Dividend","Exchange"],
 "answer":0},

{"q":"Foreign currency lending/deposits initial recognition uses:",
 "options":["Daily RBI rate","Spot rate","FEDAI weekly average rate","Monthly average"],"answer":2},

{"q":"Overseas branches (Non-Integral Operations) — exchange differences go to:",
 "options":["P&L","FCTR","Reserves","OCI"],"answer":1},

{"q":"AFS quarterly net depreciation is:",
 "options":["Taken to P&L","Added to P&L","Debited to AFS Reserve","Ignored"],"answer":2},

{"q":"Unquoted equity valued at if no data:",
 "options":["Quoted equity","Corporate bonds","Unquoted equity","Govt securities"],"answer":2},

{"q":"Correct valuation hierarchy for Mutual Fund Units:",
 "options":["NAV → Market → Repurchase","Book → Market → NAV",
            "Market → NAV → Repo","Market → Repurchase → NAV"], "answer":3},

{"q":"Valuation frequency:",
 "options":["HFT: Quarterly, AFS: Daily","HFT: Daily, AFS: Quarterly",
            "HFT: Half-yearly","Both monthly"],"answer":1},

{"q":"AFS gain/loss on sale of equity instruments goes to:",
 "options":["P&L","Capital Reserve","AFS Reserve","Revaluation Reserve"],"answer":1},

{"q":"IFR target is:",
 "options":["1% of HTM","2% of AFS + HFT","5% of all investments","10% of AFS"],"answer":1},

{"q":"Transfer to IFR is lower of:",
 "options":["Market appreciation or depreciation",
            "Net profit on investment sale OR net profit after mandatory appropriations",
            "Book or market value",
            "RBI or market rate"],"answer":1},

{"q":"HTM investments valued at:",
 "options":["Market value","Fair value","Amortized cost","MTM"],"answer":2},

{"q":"Profit on HTM sale goes to:",
 "options":["Capital Reserve","P&L","AFS Reserve","Revenue Reserve"],"answer":0},

{"q":"Matured investments shown under:",
 "options":["Investments","Other Assets","Contingent Liabilities","Misc Income"],"answer":1},

{"q":"Fixed assets costing ≤ ₹1,000 are:",
 "options":["Capitalized","Not capitalized, expensed","Depreciated fully","Capitalized at Re.1"],
 "answer":1},

{"q":"Asset costing ₹3,800 is:",
 "options":["Expensed","Capitalized","Capitalized & 100% depreciated","Deferred"],
 "answer":2},

{"q":"Depreciation on revalued portion:",
 "options":["Not charged","Charged to P&L; withdrawn from Revaluation Reserve",
            "Added to AFS reserve","Deducted from capital"],
 "answer":1},

{"q":"Which use SLM depreciation?",
 "options":["Only premises","Premises & vehicles only",
            "All fixed assets incl. computers & software","Only software"],
 "answer":2},

{"q":"Advances are shown:",
 "options":["Gross","Net of all provisions",
            "Net of specific provisions; standard provision separately","Only net if NPA"],
 "answer":2},

{"q":"Provision for diminution on restructuring:",
 "options":["Added to capital","Reduced from advances","Other liability","Reserves"],
 "answer":1},

{"q":"Derivative statements — correct?",
 "options":["Hedging derivative gains/losses deferred","Trading MTM → P&L",
            "Hedging derivatives never MTM"],"answer":1},

{"q":"Trading derivative termination gain/loss:",
 "options":["Deferred","P&L","Capital reserve","Ignored"],"answer":1},

{"q":"Gratuity/pension provision based on:",
 "options":["Historical trend","Actuarial valuation","RBI circular","Board policy"],
 "answer":1},

{"q":"DTA on losses require:",
 "options":["Probability","Reasonable certainty",
            "Virtual certainty + convincing evidence","RBI approval"],"answer":2},

{"q":"Deferred tax standard:",
 "options":["AS-11","AS-29","AS-20","AS-22"],"answer":3},

{"q":"EPS denominator uses:",
 "options":["Shares issued","Shares year-end","Weighted average shares","Paid-up capital"],
 "answer":2},

{"q":"Segment reporting per:",
 "options":["AS-3","AS-17","AS-20","AS-11"],"answer":1},

{"q":"Provision recognized when:",
 "options":["Obligation","Probable outflow","Reliable estimate"],"answer":2},

{"q":"Contingent liabilities:",
 "options":["Recognized","Disclosed when reasonably possible","Ignored","Always provided"],
 "answer":1},

{"q":"Contingent assets:",
 "options":["Recognized","Disclosed","Not recognized or disclosed","Recognized when certain"],
 "answer":2},

{"q":"NOSTRO accounts translated at:",
 "options":["FEDAI avg","Closing rate","Monthly avg","RBI rate"],"answer":1},

{"q":"Foreign currency forward contracts revalued at:",
 "options":["Initial rate","FEDAI year-end","RBI rate","Market midpoint"],"answer":1},

{"q":"Book value changes due to:",
 "options":["Revaluation","RBI rates","Market changes alone","Settlement timing"],
 "answer":0},

{"q":"Shifting between categories allowed:",
 "options":["Anytime","Once a year with Board approval","Never","Only HTM→AFS"],
 "answer":1},

{"q":"Income on T-bills:",
 "options":["Interest","Discount income","Fair value gain","Capital reserve"],
 "answer":1},

{"q":"Investments accounted on:",
 "options":["Trade date","Settlement date","RBI date","Either"],"answer":1},

{"q":"Govt business commission recognized:",
 "options":["Accrual","Realization","Settlement","Approval"],"answer":0},

{"q":"If account becomes NPA retrospectively, recovery goes first to:",
 "options":["Principal","Interest","Charges","Overdue"],"answer":1},
]

TOTAL_QUESTIONS = len(QUESTIONS)

# -----------------------------
# INIT SESSION STATE
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False
if "current" not in st.session_state:
    st.session_state.current = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# -----------------------------
# START SCREEN
# -----------------------------
if not st.session_state.started:
    st.title("📘 Bank Accounting Policy Quiz")
    st.subheader(f"✔ 80 Questions • Multiple Choice • Instant Feedback")

    if st.button("Start Quiz", use_container_width=True):
        st.session_state.started = True
    st.stop()

# -----------------------------
# END OF QUIZ
# -----------------------------
if st.session_state.current >= TOTAL_QUESTIONS:
    st.title("🏁 Quiz Completed!")
    st.subheader(f"Your Score: **{st.session_state.score} / {TOTAL_QUESTIONS}**")

    if st.button("Restart Quiz"):
        for key in ["started", "current", "score", "answers"]:
            st.session_state[key] = 0 if key != "answers" else {}
        st.session_state.started = True
    st.stop()

# -----------------------------
# SHOW QUESTION
# -----------------------------
Q = QUESTIONS[st.session_state.current]

st.markdown(f"### Question {st.session_state.current + 1} of {TOTAL_QUESTIONS}")

st.progress((st.session_state.current + 1) / TOTAL_QUESTIONS)

user_choice = st.radio(Q["q"], Q["options"], index=None)

if st.button("Submit"):
    if user_choice is not None:
        correct = Q["options"][Q["answer"]]
        if user_choice == correct:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect. Correct answer is: **{correct}**")

        st.session_state.current += 1
        st.rerun()

