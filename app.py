# app.py - Robust 80-question quiz runner (handles truncated question lists safely)
import streamlit as st
import random
import time
import json

st.set_page_config(page_title="80-Question Banking Accounting Quiz", layout="centered")

# ----------------------------
# QUESTIONS: replace/ensure your full QUESTIONS list is here
# ----------------------------
# NOTE: Ensure your QUESTIONS variable is a list of dicts with keys:
#   "q"  -> question text (string)
#   "opts" -> list of option strings
#   "a"  -> integer index (0-based) of correct option
#
# Example item:
# {"q":"Sample?", "opts":["A","B","C","D"], "a": 1}
#
# ***** IMPORTANT ***** If you used a different key name earlier (like "options"),
# make them all consistent to "opts".
#
QUESTIONS = [
{"q": "Income for performing assets is recognized on:", "opts": ["Cash basis", "Accrual basis", "Realization basis", "None"], "a": 1},
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
{"q": "Gratuity of overseas staff follows:", "opts": ["Indian GAAP", "IFRS", "Local regulations", "AS 15"], "a": 2},


# ---- Additional 40 advanced questions (from user) ----
{"q": "In the Bank’s accounting policies, which of the following combinations correctly reflects the applicable framework for financial statement preparation?", "opts": ["Indian AS + IFRS + RBI regulations","Indian GAAP + ICAI AS + RBI guidelines + statutory provisions","IFRS only + Banking Regulation Act","Indian GAAP only without RBI consideration"], "a": 1},
{"q": "Which of the following statements about the use of estimates is TRUE? /n1. Estimates affect only assets but not liabilities. /n2. Estimates affect reported assets, liabilities, contingent liabilities, income and expenses. /n3. The Bank acknowledges that future results may differ from the estimates.", "opts": ["Only 2","1 & 2","2 & 3","All three"], "a": 2},
{"q": "For NPAs, recovery received after the date of classification is appropriated:", "opts": ["First to charges, then interest","First to interest, then principal","First to principal, then interest/charges","Equally between interest & principal"], "a": 2},
{"q": "Which of the below incomes are accounted only on realization, not on accrual?/n1. Locker rent /n2. Commission other than LC/LG/Insurance/Govt business /n3. Dividend income /n4. Exchange income", "opts": ["1, 2 and 3","2 and 4","1, 2, 3 and 4","Only 3"], "a": 2},
{"q": "A foreign currency loan disbursed on 10th March is initially recorded at:", "opts": ["RBI reference rate of March 10","FEDAI weekly average rate applicable for the week","Monthly closing rate","Spot exchange rate on 10th March"], "a": 1},
{"q": "Overseas branches are classified as Non-Integral Operations. Which is the direct implication?", "opts": ["Exchange differences go to P&L immediately","Exchange differences accumulate in Foreign Currency Translation Reserve","Assets translated at average rates","Contingent liabilities not translated"], "a": 1},
{"q": "A Government security under AFS category is revalued quarterly. Net depreciation for the quarter across performing investments is:", "opts": ["Debited to P&L","Credited to P&L","Debited to AFS Reserve","Ignored until sale"], "a": 2},
{"q": "Which of the following investments must be valued at Re.1 in the absence of a reliable book value or NAV?", "opts": ["Quoted equity shares","Corporate bonds","Unquoted equity shares","Government securities"], "a": 2},
{"q": "Which one is the correct valuation hierarchy for Mutual Fund Units?", "opts": ["NAV → Market Price → Repurchase Price","Book Value → Market Price → NAV","Market Price → Repurchase Price → NAV","Market Price → Repurchase Price → NAV (as per availability)"], "a": 2},
{"q": "Which pair is correct regarding valuation frequency?", "opts": ["HFT – Quarterly; AFS – Daily","HFT – Daily; AFS – Quarterly","HFT – Half-yearly; AFS – Quarterly","HFT – Monthly; AFS – Monthly"], "a": 1},
{"q": "What happens to accumulated gain/loss in AFS-Reserve on sale of an equity instrument designated in AFS?", "opts": ["Transferred to P&L","Transferred to Capital Reserve","Transferred to Revaluation Reserve","Ignored"], "a": 1},
{"q": "Investment Fluctuation Reserve (IFR) must reach at least ______ of the combined AFS + HFT portfolio.", "opts": ["1%","2%","5%","10%"], "a": 1},
{"q": "Transfer to IFR is the lesser of:", "opts": ["Market appreciation or market depreciation","Net profit on sale of investments or net profit after mandatory appropriations","Book value or market value of investments","RBI rate or market rate"], "a": 1},
{"q": "Which category of investments is carried at acquisition cost / amortized cost?", "opts": ["AFS","HFT","HTM","FVTPL"], "a": 2},
{"q": "Profit on sale of HTM securities (after tax and required statutory transfers) is:", "opts": ["Credited to Capital Reserve","Credited to P&L","Credited to AFS Reserve","Ignored"], "a": 0},
{"q": "What is the accounting treatment for investments matured for payment?", "opts": ["Shown in \"Investments\"","Shown under \"Other Assets\"","Written off","Adjusted against HTM premium"], "a": 1},
{"q": "Fixed assets costing ≤ ₹1,000 are:", "opts": ["Capitalized and depreciated fully","Not capitalized, charged as revenue expenditure","Capitalized with 100% depreciation","Treated as inventory"], "a": 1},
{"q": "A single asset costing ₹3,800 is:", "opts": ["Expensed","Capitalized and depreciated over useful life","Capitalized and depreciated 100% to Re.1 at year-end","Recognized only when put to use next year"], "a": 2},
{"q": "Depreciation on revalued portion of fixed assets is:", "opts": ["Ignored","Charged to P&L and equivalent amount transferred from Revaluation Reserve","Adjusted against AFS Reserve","Added to carrying cost"], "a": 1},
{"q": "Which of the following are calculated using straight line method?/n 1. Depreciation on premises /n 2. Depreciation on computers /n 3. Depreciation on vehicles /n 4. Depreciation on software", "opts": ["1, 2 only","1, 3 only","1, 2, 3, 4","Only 4"], "a": 2},
{"q": "Advances are presented in the Balance Sheet:", "opts": ["Gross","Net of all provisions including standard asset provisions","Net of specific provisions but excluding general provision for standard assets","Net only if NPA"], "a": 2},
{"q": "Provision for diminution in fair value arising from restructuring is:", "opts": ["Added to capital","Reduced from advances","Shown under other liabilities","Adjusted against AFS-Reserve"], "a": 1},
{"q": "Which statements about derivatives are correct? /n 1. Hedging derivatives gains/losses are deferred and amortized. /n 2. Trading derivatives MTM impact goes to P&L. /n 3. Hedging derivatives are never marked to market.", "opts": ["Only 1","1 & 2","2 & 3","Only 3"], "a": 1},
{"q": "For trading derivatives, gain/loss on termination is:", "opts": ["Deferred","Recognized in P&L","Adjusted against reserves","Ignored"], "a": 1},
{"q": "Provision for pension and gratuity is determined based on:", "opts": ["Historical trend","Actuarial valuation","Company-specific policy","Board direction"], "a": 1},
{"q": "Deferred tax assets on carry-forward losses require:", "opts": ["Probability","Reasonable certainty","Virtual certainty with convincing evidence","Market evidence"], "a": 2},
{"q": "Which AS applies for accounting deferred taxes?", "opts": ["AS-11","AS-29","AS-20","AS-22"], "a": 3},
{"q": "EPS computation uses which denominator?", "opts": ["Total shares issued","Shares outstanding at year-end","Weighted average number of equity shares","Paid-up share capital"], "a": 2},
{"q": "Segment reporting is governed by:", "opts": ["AS-3","AS-17","AS-20","AS-11"], "a": 1},
]

# ----------------------------
# Helpful debug - show length of QUESTIONS in logs (visible in Streamlit Cloud logs)
# ----------------------------
# st.write can reveal this on the app itself; but we only show a warning message if short.
TOTAL_QUESTIONS = len(QUESTIONS)
EXPECTED_TOTAL = 80

# ----------------------------
# Session state init
# ----------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "index" not in st.session_state:
    st.session_state.index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "order" not in st.session_state or len(st.session_state.order) != TOTAL_QUESTIONS:
    # Reinitialize order if not present or if QUESTIONS length changed
    st.session_state.order = list(range(TOTAL_QUESTIONS))
    random.shuffle(st.session_state.order)

if "answers" not in st.session_state:
    st.session_state.answers = {}  # store selected option index per question index

if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Quiz configuration
QUIZ_DURATION_SECONDS = 20 * 60  # 20 minutes total (adjust if required)

# ----------------------------
# Start screen
# ----------------------------
if not st.session_state.started:
    st.title("🧾 80-Question Banking Accounting Quiz Game")

    st.markdown(
        """
        **Instructions**
        - Total questions: **{}** (app expects 80).
        - Time allowed: **20 minutes**.
        - Questions are randomized.
        - Use **Previous** to go back and change an answer.
        - Click **Submit** to lock-in answer for the current question.
        """.format(TOTAL_QUESTIONS)
    )

    # warn if questions truncated
    if TOTAL_QUESTIONS < EXPECTED_TOTAL:
        st.warning(
            f"⚠️ The QUESTIONS list currently has **{TOTAL_QUESTIONS}** entries (expected {EXPECTED_TOTAL}).\n\n"
            "If this is unexpected, your deployed file may be missing the full set of questions. "
            "Please update the QUESTIONS array with the full 80 questions and redeploy."
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🚀 Start Quiz"):
            if TOTAL_QUESTIONS == 0:
                st.error("No questions available. Add your QUESTIONS list to app.py and redeploy.")
            else:
                st.session_state.started = True
                st.session_state.start_time = time.time()
    with col2:
        if st.button("📝 Show QUESTION COUNT (debug)"):
            st.info(f"QUESTIONS length = {TOTAL_QUESTIONS}")
    st.stop()

# ----------------------------
# Helper functions
# ----------------------------
def get_time_left():
    if not st.session_state.start_time:
        return QUIZ_DURATION_SECONDS
    elapsed = time.time() - st.session_state.start_time
    return max(0, QUIZ_DURATION_SECONDS - int(elapsed))

def finish_quiz():
    st.success(f"🎓 Quiz completed! Your score: **{st.session_state.score} / {TOTAL_QUESTIONS}**")
    # Optionally show review
    if st.checkbox("Show review of answers"):
        for idx_q in range(TOTAL_QUESTIONS):
            q_global_idx = st.session_state.order[idx_q]
            q_item = QUESTIONS[q_global_idx]
            user_ans = st.session_state.answers.get(q_global_idx, None)
            correct_idx = q_item["a"]
            st.write(f"**Q{idx_q+1}.** {q_item['q']}")
            st.write(f"- Your answer: {q_item['opts'][user_ans] if user_ans is not None else 'No answer'}")
            st.write(f"- Correct answer: {q_item['opts'][correct_idx]}")
            st.markdown("---")
    # Downloadable result
    result = {
        "score": st.session_state.score,
        "total": TOTAL_QUESTIONS,
        "answers": st.session_state.answers
    }
    st.download_button("Download results (JSON)", data=json.dumps(result, indent=2), file_name="quiz_results.json")
    if st.button("🔁 Restart Quiz"):
        # reset everything
        st.session_state.started = False
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.order = list(range(TOTAL_QUESTIONS))
        random.shuffle(st.session_state.order)
        st.session_state.answers = {}
        st.session_state.start_time = None
        st.experimental_rerun()

# ----------------------------
# Timer - auto submit on expiry
# ----------------------------
time_left = get_time_left()
if time_left <= 0:
    st.error("⏳ Time's up!")
    finish_quiz()
    st.stop()

mins = time_left // 60
secs = time_left % 60
st.markdown(f"⏱️ **Time Remaining:** `{int(mins):02d}:{int(secs):02d}`")

# ----------------------------
# If index out of bounds -> finish gracefully
# ----------------------------
if st.session_state.index >= TOTAL_QUESTIONS:
    # Completed
    finish_quiz()
    st.stop()

# ----------------------------
# Show progress bar & question counter
# ----------------------------
progress_fraction = (st.session_state.index) / max(1, TOTAL_QUESTIONS)
st.progress(progress_fraction)
st.write(f"### Question {st.session_state.index + 1} / {TOTAL_QUESTIONS}")

# ----------------------------
# Safely fetch current question
# ----------------------------
try:
    q_global_idx = st.session_state.order[st.session_state.index]
except Exception as e:
    st.error("Internal indexing error: index out of range. Resetting quiz.")
    st.session_state.index = 0
    st.session_state.order = list(range(TOTAL_QUESTIONS))
    random.shuffle(st.session_state.order)
    st.session_state.answers = {}
    st.experimental_rerun()

q_item = QUESTIONS[q_global_idx]
st.subheader(q_item["q"])

# radio selection - keep user's previous selection if any
prev_sel = None
if q_global_idx in st.session_state.answers:
    prev_sel = st.session_state.answers[q_global_idx]

choice = st.radio("Choose one:", q_item["opts"], index=(prev_sel if prev_sel is not None else 0), key=f"choice_{st.session_state.index}")

# Buttons: Previous, Submit/Next, Quit & Submit
col_prev, col_submit, col_quit = st.columns([1, 1, 1])
with col_prev:
    if st.button("◀ Previous"):
        if st.session_state.index > 0:
            st.session_state.index -= 1
            st.experimental_rerun()
with col_submit:
    if st.button("Submit / Next"):
        # save answer for this global question
        try:
            sel_index = q_item["opts"].index(choice)
        except ValueError:
            sel_index = 0
        st.session_state.answers[q_global_idx] = sel_index
        # update score: recompute quickly to avoid double counting
        # we compute score fresh each time to avoid increment/decrement issues
        score_count = 0
        for gidx, qobj in enumerate(QUESTIONS):
            if gidx in st.session_state.answers:
                if st.session_state.answers[gidx] == qobj["a"]:
                    score_count += 1
        st.session_state.score = score_count

        st.session_state.index += 1
        if st.session_state.index >= TOTAL_QUESTIONS:
            finish_quiz()
            st.stop()
        else:
            st.experimental_rerun()
with col_quit:
    if st.button("Quit & Submit"):
        finish_quiz()
        st.stop()

# Small note / debug info
st.caption("Tip: Use 'Previous' to change an earlier answer. Your progress is saved in session.")
