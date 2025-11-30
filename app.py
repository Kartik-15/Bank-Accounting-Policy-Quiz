# app.py - Robust 80-question Banking Accounting Quiz (stable, single-file)
import streamlit as st
import random
import time
import json
from typing import List, Dict

st.set_page_config(page_title="80-Question Banking Accounting Quiz", layout="centered")

# ----------------------------
# RAW QUESTION BANK (as you provided earlier)
# Each entry uses "question", "options", and "answer" fields (answer = exact option text)
# ----------------------------
RAW_QUESTIONS = [
    # ---------- SET 1 (40) ----------
    {"question":"Income for performing assets is recognized on:",
     "options":["Cash basis","Accrual basis","Realization basis","None"],
     "answer":"Accrual basis"},
    {"question":"In NPAs, recoveries are appropriated first towards:",
     "options":["Interest","Charges","Principal","Court fee"],
     "answer":"Principal"},
    {"question":"OTS recoveries go first to:",
     "options":["Interest","Principal","Penalties","Charges"],
     "answer":"Principal"},
    {"question":"Back-dated NPA classification: past recoveries go first to:",
     "options":["Principal","Interest","Charges","Penalty"],
     "answer":"Interest"},
    {"question":"NCLT admitted accounts are treated as:",
     "options":["Standard accounts","Suit filed accounts","ARC transferred accounts","Write-offs"],
     "answer":"Suit filed accounts"},
    {"question":"Income on items like locker rent/dividend is recognized:",
     "options":["Accrual","Realization","Either","Never"],
     "answer":"Realization"},
    {"question":"Foreign currency deposits initially recorded at:",
     "options":["Spot rate","FEDAI weekly average","RBI reference rate","Closing rate"],
     "answer":"FEDAI weekly average"},
    {"question":"NOSTRO balances at quarter end are valued at:",
     "options":["Transaction rate","Historical rate","Closing rate","Weekly average"],
     "answer":"Closing rate"},
    {"question":"Overseas branches are treated as:",
     "options":["Integral operations","Non-integral operations","Joint operations","Independent operations"],
     "answer":"Non-integral operations"},
    {"question":"Exchange differences of foreign branches are transferred to:",
     "options":["P&L","OCI","Reserves","FCTR"],
     "answer":"FCTR"},
    {"question":"Classification of advances includes:",
     "options":["Standard, Substandard, Doubtful, Loss","Good, Bad, Medium","High risk, Low risk","None"],
     "answer":"Standard, Substandard, Doubtful, Loss"},
    {"question":"Restructured assets require provision for:",
     "options":["Interest earned","Diminution in fair value","Extra profit","Nil"],
     "answer":"Diminution in fair value"},
    {"question":"Hedging derivatives are accounted on:",
     "options":["Settlement basis","Accrual basis","Cash basis","Realization"],
     "answer":"Accrual basis"},
    {"question":"Trading derivatives MTM gains/losses go to:",
     "options":["Balance sheet","P&L","Capital","OCI"],
     "answer":"P&L"},
    {"question":"Depreciation method used:",
     "options":["WDV","Units of production","Straight line","None"],
     "answer":"Straight line"},
    {"question":"Assets costing ≤ ₹1000 are:",
     "options":["Capitalized","Expensed","Partially depreciated","Deferred"],
     "answer":"Expensed"},
    {"question":"Small assets between ₹1000–₹5000 are depreciated at:",
     "options":["5%","10%","100%","33%"],
     "answer":"100%"},
    {"question":"Depreciation on revalued portion is adjusted via:",
     "options":["Capital reserve","P&L","Revaluation reserve","FCTR"],
     "answer":"Revaluation reserve"},
    {"question":"Pension & gratuity liability measured using:",
     "options":["Straight-line method","Actuarial valuation","Cash basis","Random estimates"],
     "answer":"Actuarial valuation"},
    {"question":"Deferred tax is based on:",
     "options":["Permanent differences","Timing differences","Both","None"],
     "answer":"Timing differences"},
    {"question":"DTA on losses needs:",
     "options":["Reasonable certainty","Virtual certainty + convincing evidence","Assumptions","Historical data only"],
     "answer":"Virtual certainty + convincing evidence"},
    {"question":"Diluted EPS is excluded when:",
     "options":["Anti-dilutive","Dilutive","Higher than basic EPS","Lower than basic EPS"],
     "answer":"Anti-dilutive"},
    {"question":"Impairment loss recognized when:",
     "options":["Recoverable > carrying","Carrying > recoverable","Both equal","Never"],
     "answer":"Carrying > recoverable"},
    {"question":"Primary segment per AS-17:",
     "options":["Customer","Business","Geography","Product"],
     "answer":"Business"},
    {"question":"Provision recognized only when:",
     "options":["Possible obligation","Probable outflow + reliable estimate","Remote loss","No outflow expected"],
     "answer":"Probable outflow + reliable estimate"},
    {"question":"Contingent assets are:",
     "options":["Recognized","Disclosed","Neither recognized nor disclosed","Deferred"],
     "answer":"Neither recognized nor disclosed"},
    {"question":"ARC sale income recognized only to extent of:",
     "options":["Total sale value","Cash component above NBV","Total cash","Difference between book value & sale value"],
     "answer":"Cash component above NBV"},
    {"question":"Forward contracts revalued at:",
     "options":["Spot rate","FEDAI rate","Historical rate","Market rate"],
     "answer":"FEDAI rate"},
    {"question":"Interest on MBS recognized on:",
     "options":["Accrual","Realization","Settlement","MTM basis"],
     "answer":"Realization"},
    {"question":"Provision for leave encashment is based on:",
     "options":["Management estimate","Actuarial valuation","Cash payout","Historical cost"],
     "answer":"Actuarial valuation"},
    {"question":"If derivative is designated with an MTM asset:",
     "options":["MTM ignored","Derivative MTM is recognized","Loss deferred","None"],
     "answer":"Derivative MTM is recognized"},
    {"question":"Depreciation for any asset purchased during year is for:",
     "options":["Partial year","Full year","Half-year","Pro-rata"],
     "answer":"Full year"},
    {"question":"Consignment precious metal income recognized:",
     "options":["On dispatch","On sale completion","On receipt","On invoice"],
     "answer":"On sale completion"},
    {"question":"Income of foreign branches recognized as per:",
     "options":["ICAI","RBI","Local laws","AS 11 only"],
     "answer":"Local laws"},
    {"question":"Deferred tax measured using:",
     "options":["Future tax rates","Enacted/substantively enacted rates","RBI rates","Average rates"],
     "answer":"Enacted/substantively enacted rates"},
    {"question":"Leave encashment is a:",
     "options":["Defined contribution","Defined benefit","Contingent liability","Provision"],
     "answer":"Defined benefit"},
    {"question":"Depreciation rate for computers:",
     "options":["20%","33.33%","25%","15%"],
     "answer":"33.33%"},
    {"question":"Furniture depreciation rate:",
     "options":["5%","10%","20%","100%"],
     "answer":"10%"},
    {"question":"Contingent liabilities disclosed when:",
     "options":["Remote","Reasonably possible but not measurable","Certain","Probable"],
     "answer":"Reasonably possible but not measurable"},
    {"question":"Gratuity of overseas staff follows:",
     "options":["Indian GAAP","IFRS","Local regulations","AS 15"],
     "answer":"Local regulations"},

    # ---------- SET 2 (40 advanced) ----------
    {"question":"Applicable framework for Bank financial statements:",
     "options":["Indian AS + IFRS + RBI","Indian GAAP + ICAI AS + RBI + statutory provisions","IFRS only","Indian GAAP only"],
     "answer":"Indian GAAP + ICAI AS + RBI + statutory provisions"},
    {"question":"Correct statements about estimates:",
     "options":["Only 2","1 & 2","2 & 3","All three"],
     "answer":"2 & 3"},
    {"question":"Recovery in NPAs after classification is appropriated first to:",
     "options":["Charges","Interest","Principal","Equally"],
     "answer":"Principal"},
    {"question":"Which incomes recognized only on realization?",
     "options":["1, 2, 3","2, 4","All four","Only 3"],
     "answer":"1, 2, 3"},
    {"question":"Foreign currency lending/deposits initial recognition uses:",
     "options":["Daily RBI rate","Spot rate","FEDAI weekly average rate","Monthly average"],
     "answer":"FEDAI weekly average rate"},
    {"question":"Overseas branches as Non-Integral Operations implies:",
     "options":["Exchange differences → P&L","Exchange differences → FCTR","Assets at average rates","Contingent liabilities not translated"],
     "answer":"Exchange differences → FCTR"},
    {"question":"AFS quarterly net depreciation:",
     "options":["Taken to P&L","Added to P&L","Debited to AFS Reserve","Ignored"],
     "answer":"Debited to AFS Reserve"},
    {"question":"Which valued at Re.1 if no reliable data?",
     "options":["Quoted equity","Corporate bonds","Unquoted equity","Government securities"],
     "answer":"Unquoted equity"},
    {"question":"Correct valuation hierarchy for MF Units:",
     "options":["NAV → Market → Repurchase","Book → Market → NAV","Market → NAV → Repo","Market Price → Repurchase Price → NAV"],
     "answer":"Market Price → Repurchase Price → NAV"},
    {"question":"Valuation frequency:",
     "options":["HFT Quarterly, AFS Daily","HFT Daily, AFS Quarterly","HFT Half-yearly","Both monthly"],
     "answer":"HFT Daily, AFS Quarterly"},
    {"question":"Accumulated AFS gain/loss on sale of equity instruments goes to:",
     "options":["P&L","Capital Reserve","AFS Reserve only","Revaluation Reserve"],
     "answer":"Capital Reserve"},
    {"question":"IFR target is:",
     "options":["1% of HTM","2% of AFS + HFT","5% of all investments","10% of AFS"],
     "answer":"2% of AFS + HFT"},
    {"question":"Transfer to IFR is lower of:",
     "options":["Market appreciation or depreciation","Profit on sale OR net profit after mandatory appropriations","Book or market value","RBI or market rate"],
     "answer":"Profit on sale OR net profit after mandatory appropriations"},
    {"question":"Investments in HTM valued at:",
     "options":["Market value","Fair value","Amortized cost","MTM"],
     "answer":"Amortized cost"},
    {"question":"Profit on HTM sale goes to:",
     "options":["Capital Reserve","P&L","AFS Reserve","Revenue Reserve"],
     "answer":"Capital Reserve"},
    {"question":"Matured investments appear under:",
     "options":["Investments","Other Assets","Contingent Liabilities","Misc Income"],
     "answer":"Other Assets"},
    {"question":"Fixed assets ≤ ₹1,000:",
     "options":["Capitalized","Not capitalized, expensed","100% depreciated","Capitalized at Re.1"],
     "answer":"Not capitalized, expensed"},
    {"question":"Asset costing ₹3,800 is:",
     "options":["Expensed","Normal capitalization","Capitalized & 100% depreciated","Deferred"],
     "answer":"Capitalized & 100% depreciated"},
    {"question":"Depreciation on revalued portion:",
     "options":["Not charged","Charged to P&L; adjusted from Revaluation Reserve","Added to AFS reserve","Deducted from capital"],
     "answer":"Charged to P&L; adjusted from Revaluation Reserve"},
    {"question":"Which use SLM depreciation?",
     "options":["Only premises","Premises & vehicles","All fixed assets incl. computers","Only software"],
     "answer":"All fixed assets incl. computers"},
    {"question":"Advances shown:",
     "options":["Gross","Net of all provisions","Net of specific provision; standard provision separate","Only net if NPA"],
     "answer":"Net of specific provision; standard provision separate"},
    {"question":"Provision for diminution on restructuring:",
     "options":["Added to capital","Reduced from advances","Other liability","Adjusted in reserves"],
     "answer":"Reduced from advances"},
    {"question":"Correct statements on derivatives:",
     "options":["Only 1","1 & 2","2 & 3","Only 3"],
     "answer":"1 & 2"},
    {"question":"Termination gain/loss of trading derivative:",
     "options":["Deferred","P&L","Capital Reserve","Ignored"],
     "answer":"P&L"},
    {"question":"Gratuity/pension provision based on:",
     "options":["Historical","Actuarial valuation","RBI circular","Board policy"],
     "answer":"Actuarial valuation"},
    {"question":"DTA on losses requires:",
     "options":["Probability","Reasonable certainty","Virtual certainty + evidence","RBI approval"],
     "answer":"Virtual certainty + evidence"},
    {"question":"Deferred tax AS is:",
     "options":["AS 11","AS 29","AS 20","AS 22"],
     "answer":"AS 22"},
    {"question":"EPS denominator uses:",
     "options":["Total shares","Year-end shares","Weighted average equity shares","Paid-up capital"],
     "answer":"Weighted average equity shares"},
    {"question":"Segment reporting per:",
     "options":["AS-3","AS-17","AS-20","AS-11"],
     "answer":"AS-17"},
    {"question":"Provision recognized when:",
     "options":["1 & 2","2 & 3","All three","Only 1"],
     "answer":"All three"},
    {"question":"Contingent liabilities are:",
     "options":["Recognized","Disclosed when reasonably possible","Ignored","Always provided"],
     "answer":"Disclosed when reasonably possible"},
    {"question":"Contingent assets are:",
     "options":["Recognized","Disclosed","Not recognized or disclosed","Recognized when certain"],
     "answer":"Not recognized or disclosed"},
    {"question":"NOSTRO/ACU accounts translated at:",
     "options":["FEDAI quarterly","Closing rate","Monthly average","RBI rate"],
     "answer":"Closing rate"},
    {"question":"Foreign currency forward contracts revalued at:",
     "options":["Initial rate","FEDAI year-end","RBI rate","Market midpoint"],
     "answer":"FEDAI year-end"},
    {"question":"Book value of securities changes due to:",
     "options":["Revaluation at intervals","RBI alone","Market only","Settlement timing"],
     "answer":"Revaluation at intervals"},
    {"question":"Shifting between categories allowed:",
     "options":["Anytime","Once a year with Board approval","Never","Only HTM→AFS"],
     "answer":"Once a year with Board approval"},
    {"question":"Income on T-Bills recognized as:",
     "options":["Interest","Discount income","Fair value gain","Capital reserve"],
     "answer":"Discount income"},
    {"question":"Investments accounted on:",
     "options":["Trade date","Settlement date","RBI date","Either"],
     "answer":"Settlement date"},
    {"question":"Government business commission recognized:",
     "options":["Accrual","Realization","Settlement","Approval"],
     "answer":"Accrual"},
    {"question":"If account becomes NPA retrospectively, recovery during the period goes first to:",
     "options":["Principal","Interest","Charges","Overdue balance"],
     "answer":"Interest"}
]

# ----------------------------
# NORMALIZE & VALIDATE: convert RAW -> QUESTIONS where answer index 'a' is integer
# ----------------------------
QUESTIONS: List[Dict] = []
errored = []
for idx, r in enumerate(RAW_QUESTIONS):
    qtext = r.get("question")
    opts = r.get("options") or []
    ans_text = r.get("answer")
    if not qtext or not isinstance(opts, list) or len(opts) < 2 or ans_text is None:
        errored.append((idx, "missing fields"))
        continue
    try:
        a_idx = opts.index(ans_text)
    except ValueError:
        # try trimmed match
        found = None
        for i, o in enumerate(opts):
            if (o.strip().lower() == str(ans_text).strip().lower()):
                found = i
                break
        if found is None:
            errored.append((idx, f"answer '{ans_text}' not found in options {opts}"))
            continue
        a_idx = found
    QUESTIONS.append({"q": qtext, "opts": opts, "a": a_idx})

if errored:
    st.error("QUESTION BANK ERROR: some questions failed validation. See details below.")
    for e in errored:
        st.write(f"- Question index {e[0]}: {e[1]}")
    st.stop()

TOTAL_QUESTIONS = len(QUESTIONS)
EXPECTED_TOTAL = 80

# ----------------------------
# SESSION STATE INIT
# ----------------------------
if "started" not in st.session_state:
    st.session_state.started = False
if "index" not in st.session_state:
    st.session_state.index = 0
if "order" not in st.session_state or len(st.session_state.order) != TOTAL_QUESTIONS:
    st.session_state.order = list(range(TOTAL_QUESTIONS))
    random.shuffle(st.session_state.order)
if "answers" not in st.session_state:
    st.session_state.answers = {}  # map global question index -> selected option index
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Quiz settings
QUIZ_DURATION_SECONDS = 40 * 60  # 40 minutes

# ----------------------------
# Helper functions
# ----------------------------
def get_time_left():
    if st.session_state.start_time is None:
        return QUIZ_DURATION_SECONDS
    elapsed = int(time.time() - st.session_state.start_time)
    return max(0, QUIZ_DURATION_SECONDS - elapsed)

def recompute_score():
    sc = 0
    for gidx, q in enumerate(QUESTIONS):
        sel = st.session_state.answers.get(gidx, None)
        if sel is not None and 0 <= sel < len(q["opts"]) and sel == q["a"]:
            sc += 1
    st.session_state.score = sc

# ----------------------------
# START SCREEN
# ----------------------------
if not st.session_state.started:
    st.title("🧾 80-Question Banking Accounting Quiz Game")
    st.markdown(
        f"""
**Instructions**

- Total questions: **{TOTAL_QUESTIONS}** (expected 80).  
- Time allowed: **40 minutes**.  
- Questions presented in randomized order per session.  
- Use **Previous** to review; **Submit** records your answer and moves to next.  
- You can download your responses at the end.
"""
    )
    if TOTAL_QUESTIONS < EXPECTED_TOTAL:
        st.warning(f"⚠️ QUESTIONS list length = {TOTAL_QUESTIONS} (expected {EXPECTED_TOTAL}).")

    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("🚀 Start Quiz"):
            st.session_state.started = True
            st.session_state.start_time = time.time()
    with col2:
        if st.button("📝 Debug: show question count"):
            st.info(f"QUESTIONS = {TOTAL_QUESTIONS}")
    st.stop()

# ----------------------------
# MAIN QUIZ FLOW
# ----------------------------
time_left = get_time_left()
mins = time_left // 60
secs = time_left % 60

# If time expired -> compute final and show finish
if time_left <= 0:
    recompute_score()
    st.title("⏳ Time's up — Quiz ended")
    st.success(f"Final Score: **{st.session_state.score} / {TOTAL_QUESTIONS}**")
    if st.checkbox("Show review of answers"):
        for i in range(TOTAL_QUESTIONS):
            q = QUESTIONS[i]
            st.write(f"**Q{i+1}. {q['q']}**")
            chosen = st.session_state.answers.get(i, None)
            st.write(f"- Your answer: {q['opts'][chosen] if chosen is not None else 'No answer'}")
            st.write(f"- Correct answer: {q['opts'][q['a']]}")
            st.markdown("---")
    st.download_button("Download results (JSON)", data=json.dumps({"score":st.session_state.score,"answers":st.session_state.answers}, indent=2), file_name="quiz_results.json")
    if st.button("🔁 Restart"):
        for k in ("started","index","order","answers","score","start_time"):
            st.session_state.pop(k, None)
        st.experimental_rerun()
    st.stop()

# Top bar
st.markdown(f"⏱️ **Time Remaining:** `{int(mins):02d}:{int(secs):02d}`")
st.progress(st.session_state.index / max(1, TOTAL_QUESTIONS))
st.write(f"### Question {st.session_state.index + 1} / {TOTAL_QUESTIONS}")

# Safety: if index out of range, finish gracefully
if st.session_state.index >= TOTAL_QUESTIONS:
    recompute_score()
    st.success(f"Quiz complete — Score: **{st.session_state.score} / {TOTAL_QUESTIONS}**")
    if st.button("🔁 Restart"):
        for k in ("started","index","order","answers","score","start_time"):
            st.session_state.pop(k, None)
        st.experimental_rerun()
    st.stop()

# Fetch question by shuffled order
global_q_idx = st.session_state.order[st.session_state.index]
qitem = QUESTIONS[global_q_idx]
st.subheader(qitem["q"])

# previous selection (for this global question)
prev = st.session_state.answers.get(global_q_idx, None)
selected = st.radio("Choose one:", qitem["opts"], index=prev if prev is not None else 0, key=f"radio_{global_q_idx}")

# Buttons
col_prev, col_submit, col_quit = st.columns([1,1,1])

with col_prev:
    if st.button("◀ Previous"):
        if st.session_state.index > 0:
            st.session_state.index -= 1

with col_submit:
    if st.button("Submit / Next"):
        # store selected index
        sel_index = qitem["opts"].index(selected)
        st.session_state.answers[global_q_idx] = sel_index
        recompute_score()
        # move next or finish
        if st.session_state.index < TOTAL_QUESTIONS - 1:
            st.session_state.index += 1
        else:
            # finished
            recompute_score()
            st.success(f"Quiz complete — Score: **{st.session_state.score} / {TOTAL_QUESTIONS}**")
            if st.checkbox("Show review of answers"):
                for i in range(TOTAL_QUESTIONS):
                    q = QUESTIONS[i]
                    chosen = st.session_state.answers.get(i, None)
                    st.write(f"**Q{i+1}. {q['q']}**")
                    st.write(f"- Your answer: {q['opts'][chosen] if chosen is not None else 'No answer'}")
                    st.write(f"- Correct answer: {q['opts'][q['a']]}")
                    st.markdown("---")
            st.download_button("Download results (JSON)", data=json.dumps({"score":st.session_state.score,"answers":st.session_state.answers}, indent=2), file_name="quiz_results.json")
            if st.button("🔁 Restart"):
                for k in ("started","index","order","answers","score","start_time"):
                    st.session_state.pop(k, None)
                st.experimental_rerun()
            st.stop()

with col_quit:
    if st.button("Quit & Submit"):
        # store current selection before quitting
        sel_index = qitem["opts"].index(selected)
        st.session_state.answers[global_q_idx] = sel_index
        recompute_score()
        st.session_state.index = TOTAL_QUESTIONS  # cause finish block above on next run
        # rely on rerun behavior of Streamlit automatically on button press (no explicit experimental_rerun)

# small help
st.caption("Tip: Use Previous to change earlier answer. Your progress is stored in this browser session.")
