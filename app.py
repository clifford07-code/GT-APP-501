

from program_runner import run_program, patch_input_calls
from experiment_info import EXPERIMENT_META
from file_scanner import scan_experiments
import streamlit as st
import matplotlib.pyplot as plt
import os
import sys
import re
import io
import traceback

import matplotlib
matplotlib.use("Agg")


EXPERIMENTS_DIR = os.path.join(os.path.dirname(__file__), "experiments")
sys.path.insert(0, os.path.dirname(__file__))


st.set_page_config(
    page_title="Graph Theory Experiments",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    /* -- Global fonts -- */
    html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }

    /* -- Sidebar -- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
        padding-top: 1rem;
    }
    section[data-testid="stSidebar"] * { color: #e0e0e0 !important; }
    section[data-testid="stSidebar"] .stRadio label {
        border-radius: 8px;
        padding: 4px 8px;
        transition: background 0.2s;
    }
    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255,255,255,0.1);
    }

    /* -- Page header -- */
    .lab-header {
        background: linear-gradient(135deg, #001a4d, #003d99, #0052cc);
        border-radius: 16px;
        padding: 1.2rem 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        position: sticky;
        top: 60px;
        z-index: 999;
        display: flex;
        align-items: center;
        gap: 1.4rem;
    }
    .lab-header-logo {
        flex-shrink: 0;
        width: 72px;
        height: 72px;
        border-radius: 12px;
        object-fit: contain;
        background: rgba(255,255,255,0.12);
        padding: 6px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .lab-header-text { flex: 1; min-width: 0; }
    .lab-header h1 {
        color: #ffffff !important;
        font-size: 1.75rem;
        font-weight: 800;
        margin: 0 0 0.25rem;
        letter-spacing: -0.4px;
        line-height: 1.2;
    }
    .lab-header p { color: #e0e7ff !important; margin: 0; font-size: 0.88rem; }

    /* -- Sticky footer -- */
    .sticky-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: linear-gradient(90deg, #001a4d 0%, #0f3460 50%, #001a4d 100%);
        border-top: 1px solid rgba(124,58,237,0.45);
        padding: 0.55rem 2rem;
        text-align: center;
        font-size: 0.82rem;
        color: #c4b5fd !important;
        font-weight: 600;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.6rem;
        box-shadow: 0 -4px 24px rgba(0,0,0,0.35);
    }
    .sticky-footer span.sep {
        color: rgba(196,181,253,0.4);
        font-weight: 300;
    }
    /* push page content above sticky footer */
    .main .block-container { padding-bottom: 4rem !important; }

    /* -- Experiment card -- */
    .exp-card {
        background: linear-gradient(135deg, #0f3460 0%, #533483 100%);
        border-radius: 14px;
        padding: 1.4rem 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }
    .exp-card h2 { color: #ffffff !important; font-size: 1.5rem; margin: 0 0 0.5rem; }
    .exp-card p  { color: #cbd5e0 !important; font-size: 0.92rem; margin: 0; }

    /* -- Program title bar -- */
    .prog-title {
        background: rgba(83, 52, 131, 0.25);
        border-left: 4px solid #7c3aed;
        border-radius: 0 8px 8px 0;
        padding: 0.6rem 1rem;
        margin-bottom: 0.8rem;
    }
    .prog-title h3 { color: #c4b5fd !important; margin: 0 0 0.2rem; font-size: 1.1rem; }
    .prog-title p  { color: #94a3b8 !important; margin: 0; font-size: 0.82rem; }

    /* -- Output box -- */
    .output-box {
        background: #0d1117;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        font-family: 'JetBrains Mono', 'Fira Code', monospace;
        font-size: 0.82rem;
        color: #c9d1d9;
        white-space: pre-wrap;
        max-height: 400px;
        overflow-y: auto;
    }

    /* -- Error box -- */
    .error-box {
        background: #1a0a0a;
        border: 1px solid #f85149;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        font-family: monospace;
        font-size: 0.78rem;
        color: #f85149;
        white-space: pre-wrap;
        max-height: 300px;
        overflow-y: auto;
    }

    /* -- Divider -- */
    .prog-divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.08);
        margin: 2rem 0;
    }

    /* -- Search result card -- */
    .search-card {
        background: rgba(15, 52, 96, 0.4);
        border: 1px solid rgba(124, 58, 237, 0.3);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }

    /* -- Badge -- */
    .badge {
        display: inline-block;
        background: #7c3aed;
        color: #fff !important;
        font-size: 0.7rem;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 999px;
        margin-left: 8px;
        vertical-align: middle;
    }

    /* -- Section label -- */
    .section-label {
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 0.68rem;
        font-weight: 700;
        color: #6b7280;
        margin-bottom: 0.4rem;
    }

    /* Make st.code blocks a bit taller */
    .stCodeBlock { max-height: 520px; overflow-y: auto; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_experiments():
    """Scan folder once and cache the result."""
    return scan_experiments(EXPERIMENTS_DIR)


def read_source(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def get_meta(exp_num: int) -> dict:
    return EXPERIMENT_META.get(exp_num, {})


def get_prog_meta(exp_num: int, prog_num: int) -> dict:
    m = get_meta(exp_num)
    return m.get("programs", {}).get(prog_num, {})


def fig_to_bytes(fig) -> bytes:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=120, bbox_inches="tight")
    buf.seek(0)
    return buf.read()


def execute_program(path: str, user_inputs: dict = None) -> dict:
    """
    Run a program file.  If user_inputs is provided (for input() calls),
    patch the source before executing.
    """
    source = read_source(path)

    has_input_call = bool(re.search(r'\binput\s*\(', source))

    if has_input_call and user_inputs:
        patched = patch_input_calls(source, user_inputs)
        import tempfile
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write(patched)
            tmp_path = tmp.name
        result = run_program(tmp_path)
        os.unlink(tmp_path)
        return result

    return run_program(path)


def render_output(result: dict, key_prefix: str):
    """Render text output and/or figures."""
    if result["error"]:
        st.markdown(
            f'<div class="error-box">❌ Runtime Error\n\n{result["error"]}</div>',
            unsafe_allow_html=True,
        )
    if result["text"].strip():
        st.markdown('<p class="section-label">📤 Text Output</p>',
                    unsafe_allow_html=True)
        st.markdown(
            f'<div class="output-box">{result["text"]}</div>',
            unsafe_allow_html=True,
        )
    if result["figures"]:
        st.markdown('<p class="section-label">📊 Chart Output</p>',
                    unsafe_allow_html=True)
        for idx, fig in enumerate(result["figures"]):
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
    if not result["error"] and not result["text"].strip() and not result["figures"]:
        st.info("✅ Program executed successfully (no output produced).")


def experiment_matches(exp_num: int, exp_data: dict, query: str) -> bool:
    """Return True if this experiment matches the search query."""
    if not query:
        return True
    meta = get_meta(exp_num)
    title = meta.get("title", "").lower()
    desc = meta.get("description", "").lower()
    theory = meta.get("theory", "").lower()

    if query in title or query in desc or query in theory:
        return True

    for prog_num in exp_data["files"]:
        pm = get_prog_meta(exp_num, prog_num)
        pt = pm.get("title", "").lower()
        po = pm.get("objective", "").lower()
        if query in pt or query in po:
            return True

    return False


def get_matched_programs(exp_num: int, exp_data: dict, query: str) -> list:
    """Return list of (prog_num, title, objective) that match the query."""
    results = []
    for prog_num in exp_data["files"]:
        pm = get_prog_meta(exp_num, prog_num)
        pt = pm.get("title", f"Program {prog_num}")
        po = pm.get("objective", "")
        if query in pt.lower() or query in po.lower():
            results.append((prog_num, pt, po))
    return results


experiments = load_experiments()


with st.sidebar:
    st.markdown(
        "<h2 style='color:#c4b5fd;margin-bottom:0.2rem;'>🔬 Graph Theory Lab Navigator</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:#94a3b8;font-size:0.8rem;margin-bottom:1rem;'>"
        "Graph Theory Experiments</p>",
        unsafe_allow_html=True,
    )

    raw_query = st.text_input(
        "Search",
        placeholder="e.g. isomorphism, kruskal, coloring …",
        key="search_box",
        label_visibility="collapsed",
    )
    search_query = raw_query.strip().lower()

    st.markdown("---")

    matching_exp_nums = [
        n for n in experiments
        if experiment_matches(n, experiments[n], search_query)
    ]

    if not matching_exp_nums:

        matching_exp_nums = list(experiments.keys())
        st.warning(f'No match for "{raw_query}"')

    exp_labels = {
        n: f"Experiment {n}  —  {get_meta(n).get('title', f'Experiment {n}')}"
        for n in matching_exp_nums
    }
    sidebar_options = [exp_labels[n] for n in matching_exp_nums]

    jump_to = st.session_state.get("jump_to_exp", None)
    if jump_to and jump_to in matching_exp_nums:
        default_idx = matching_exp_nums.index(jump_to)

        st.session_state.pop("jump_to_exp", None)
    else:
        default_idx = 0

    selected_label = st.radio(
        "Select Experiment",
        options=sidebar_options,
        index=default_idx,
        label_visibility="collapsed",
    )
    selected_exp = matching_exp_nums[sidebar_options.index(selected_label)]

    st.markdown("---")

    total_progs = sum(len(v["files"]) for v in experiments.values())
    match_info = (
        f"{len(matching_exp_nums)} of {len(experiments)}"
        if search_query
        else str(len(experiments))
    )
    st.markdown(
        f"<p style='color:#6b7280;font-size:0.72rem;text-align:center;'>"
        f"📁 {match_info} Experiments • {total_progs} Programs</p>",
        unsafe_allow_html=True,
    )


import base64 as _b64
_logo_path = os.path.join(os.path.dirname(__file__), "image.png")
try:
    with open(_logo_path, "rb") as _lf:
        _logo_b64 = _b64.b64encode(_lf.read()).decode()
    _logo_html = f'<img class="lab-header-logo" src="data:image/png;base64,{_logo_b64}" alt="GEC Logo">'
except FileNotFoundError:
    _logo_html = ""

st.markdown(
    f"""
    <div class="lab-header">
        {_logo_html}
        <div class="lab-header-text">
            <h1>CMP226 Graph Theory and Combinatronics Lab</h1>
            <p>Government Engineering College &nbsp;|&nbsp; Department of Computer Engineering</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if search_query:
    real_matches = [
        n for n in experiments
        if experiment_matches(n, experiments[n], search_query)
    ]

    if not real_matches:
        st.error(
            f'❌ No experiments found for **"{raw_query}"**. '
            "Try a different keyword like `kruskal`, `euler`, `coloring`, `path` …"
        )
    else:
        st.markdown(
            f"### 🔍 Results for `{raw_query}` &nbsp;"
            f"<span style='font-size:0.85rem;color:#94a3b8;font-weight:normal;'>"
            f"{len(real_matches)} experiment(s) found</span>",
            unsafe_allow_html=True,
        )

        for exp_num in real_matches:
            exp_data_s = experiments[exp_num]
            meta = get_meta(exp_num)
            title = meta.get("title", f"Experiment {exp_num}")
            desc = meta.get("description", "")
            theory = meta.get("theory", "")

            match_reasons = []
            if search_query in title.lower():
                match_reasons.append("title")
            if search_query in desc.lower():
                match_reasons.append("description")
            if search_query in theory.lower():
                match_reasons.append("theory")

            matched_progs = get_matched_programs(
                exp_num, exp_data_s, search_query)
            if matched_progs:
                match_reasons.append(f"{len(matched_progs)} program(s)")

            badge_html = "".join(
                f"<span style='background:#7c3aed;color:#fff;font-size:0.68rem;"
                f"font-weight:700;padding:2px 9px;border-radius:999px;margin-right:5px;'>"
                f"{r}</span>"
                for r in match_reasons
            )

            with st.expander(
                f"📌 Experiment {exp_num} — {title}",
                expanded=(len(real_matches) <= 4),
            ):
                st.markdown(badge_html + "<br>", unsafe_allow_html=True)
                st.markdown(
                    f'<p style="text-align:left;margin:0;font-size:0.95rem;color:#cbd5e0;">_{desc}_</p>',
                    unsafe_allow_html=True,
                )

                if matched_progs:
                    st.markdown("**Matching programs:**")
                    for pn, pt, po in matched_progs:
                        st.markdown(f"- **Program {pn} — {pt}:** _{po}_")

                if st.button(
                    f"➜ Open Experiment {exp_num}",
                    key=f"jump_{exp_num}",
                    use_container_width=True,
                    type="primary",
                ):
                    st.session_state["jump_to_exp"] = exp_num
                    st.rerun()

    st.divider()

exp_data = experiments[selected_exp]
meta = get_meta(selected_exp)
exp_title = meta.get("title", f"Experiment {selected_exp}")
exp_desc = meta.get("description", "No description available.")
exp_date = meta.get("date", "")


st.markdown(
    f"""
    <div class="exp-card">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
            <h2 style="margin:0;">Experiment {selected_exp} &mdash; {exp_title}</h2>
            {f'<span style="background:rgba(255,255,255,0.12);color:#e2e8f0;font-size:0.82rem;font-weight:600;padding:4px 12px;border-radius:999px;white-space:nowrap;border:1px solid rgba(255,255,255,0.2);">📅 {exp_date}</span>' if exp_date else ''}
        </div>
        <p style="text-align:left;">{exp_desc}</p>
    </div>
    """,
    unsafe_allow_html=True,
)


with st.expander("📚 Experiment Theory ", expanded=True):
    st.markdown(meta.get("theory", "No theory available for this experiment."))


sorted_progs = sorted(exp_data["files"].keys())
tab_labels = [
    f"Program {pn} — {get_prog_meta(selected_exp, pn).get('title', f'Program {pn}')}"
    for pn in sorted_progs
]

tabs = st.tabs(tab_labels)

for tab, prog_num in zip(tabs, sorted_progs):
    path = exp_data["files"][prog_num]
    pm = get_prog_meta(selected_exp, prog_num)
    prog_title = pm.get("title", f"Program {prog_num}")
    objective = pm.get("objective", "Execute the program to see its output.")
    has_input = pm.get("has_input", False)
    input_widgets = pm.get("input_widgets", [])
    source_code = read_source(path)

    with tab:

        toolbar_col1, toolbar_col2, toolbar_col3 = st.columns([4, 1, 1])
        with toolbar_col2:
            st.download_button(
                label="⬇ Source",
                data=source_code,
                file_name=os.path.basename(path),
                mime="text/x-python",
                key=f"dl_{selected_exp}_{prog_num}",
                use_container_width=True,
            )
        with toolbar_col3:
            run_key = f"run_{selected_exp}_{prog_num}"
            run_btn = st.button(
                "▶ Run",
                key=run_key,
                use_container_width=True,
                type="primary",
            )

        st.markdown("<hr class='prog-divider'>", unsafe_allow_html=True)

        left_col, right_col = st.columns(2, gap="medium")

        with left_col:
            st.markdown('<p class="section-label">📄 Source Code</p>',
                        unsafe_allow_html=True)
            with st.expander("Show / Hide Code", expanded=True):
                st.code(source_code, language="python")

        with right_col:
            st.markdown(
                '<p class="section-label">🖥 Program Output</p>', unsafe_allow_html=True)

            user_inputs = {}
            if has_input and input_widgets:
                st.markdown("**⚙️ Program Inputs**")
                for widget_cfg in input_widgets:
                    wkey = widget_cfg["key"]
                    wlbl = widget_cfg["label"]
                    wtype = widget_cfg.get("type", "text")
                    wdef = widget_cfg.get("default", "")
                    wph = widget_cfg.get("placeholder", "")
                    wmin = widget_cfg.get("min", 0)
                    wmax = widget_cfg.get("max", 100)

                    if wtype == "text":
                        val = st.text_input(
                            wlbl,
                            value=wdef,
                            placeholder=wph,
                            key=f"inp_{selected_exp}_{prog_num}_{wkey}",
                        )
                    elif wtype == "number":
                        val = str(
                            st.number_input(
                                wlbl,
                                value=int(wdef) if wdef else wmin,
                                min_value=wmin,
                                max_value=wmax,
                                key=f"inp_{selected_exp}_{prog_num}_{wkey}",
                            )
                        )
                    elif wtype == "select":
                        val = st.selectbox(
                            wlbl,
                            options=widget_cfg.get("options", []),
                            key=f"inp_{selected_exp}_{prog_num}_{wkey}",
                        )
                    else:
                        val = st.text_input(
                            wlbl,
                            value=wdef,
                            key=f"inp_{selected_exp}_{prog_num}_{wkey}",
                        )
                    user_inputs[wkey] = val
                    for kw in ["degree", "sequence", "input", ""]:
                        user_inputs[kw] = val

            state_key = f"result_{selected_exp}_{prog_num}"

            if run_btn:
                with st.spinner("⚙️ Executing …"):
                    res = execute_program(
                        path, user_inputs if user_inputs else None)
                st.session_state[state_key] = res

            if state_key in st.session_state:
                render_output(st.session_state[state_key], state_key)
            else:
                st.markdown(
                    """
                    <div style="
                        border: 2px dashed #374151;
                        border-radius: 12px;
                        padding: 2.5rem 1.5rem;
                        text-align: center;
                        color: #6b7280;
                    ">
                        <p style="font-size:2rem;margin:0">▶</p>
                        <p style="margin:0.4rem 0 0;font-size:0.9rem">
                            Click <b>Run</b> to execute this program
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        with st.expander("✅ Conclusion", expanded=False):
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #052e16 0%, #064e3b 100%);
                    border: 1px solid #16a34a;
                    border-radius: 12px;
                    padding: 1.2rem 1.5rem;
                ">
                    <h4 style="color:#4ade80;margin:0 0 0.6rem;"> Description</h4>
                    <p style="color:#d1fae5;margin:0 0 1rem;font-size:0.93rem;line-height:1.6;">
                        {exp_desc}
                    </p>
                    <hr style="border:none;border-top:1px solid #16a34a;margin:0.8rem 0;">
                    <h4 style="color:#4ade80;margin:0 0 0.5rem;"> Successfully Implemented</h4>
    
                </div>
                """,
                unsafe_allow_html=True,
            )


st.markdown(
    """
    <div class="sticky-footer">
        <span>Clifford Fernandes</span>
        <span class="sep">|</span>
        <span>24B-CO-501</span>
        <span class="sep">|</span>
        <span>Semester 4</span>
        <span class="sep">|</span>
    </div>
    """,
    unsafe_allow_html=True,
)
