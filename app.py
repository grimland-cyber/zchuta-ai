import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="זכותא-AI | סוכן מיצוי זכויות חכם",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hebrew RTL Support & CSS Styling
st.markdown("""
    <style>
    /* Hebrew font and RTL alignment */
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&family=Rubik:wght@300;400;500;700&display=swap');
    
    /* Global alignment */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stWidgetLabel"] {
        font-family: 'Rubik', 'Assistant', sans-serif !important;
        direction: RTL !important;
        text-align: right !important;
    }
    
    /* Streamlit block align */
    div[data-testid="stVerticalBlock"] {
        direction: RTL !important;
        text-align: right !important;
    }
    
    /* Widget labels and metrics alignment */
    div[data-testid="stWidgetLabel"] p, div[data-testid="stMarkdownContainer"] p, div[data-testid="stMarkdownContainer"] h3, div[data-testid="stMarkdownContainer"] h1, div[data-testid="stMarkdownContainer"] h4, div[data-testid="stMarkdownContainer"] li {
        text-align: right !important;
        direction: rtl !important;
    }
    
    div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"], div[data-testid="stMetricDelta"] {
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* Align radio choices and lists */
    div[role="radiogroup"] {
        direction: rtl !important;
        text-align: right !important;
    }
    
    div[data-testid="stMetricDelta"] svg {
        position: relative;
        right: auto;
        left: 0;
    }
    
    /* Title styling */
    .app-title {
        color: #0070f3;
        font-family: 'Rubik', sans-serif;
        font-weight: 900;
        text-align: center;
        margin-bottom: 5px;
    }
    .app-subtitle {
        color: #475569;
        font-size: 14px;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Box stylings */
    .feature-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        text-align: right;
    }
    
    .agent-thinking {
        background-color: #0f172a;
        color: #38bdf8;
        font-family: monospace;
        padding: 15px;
        border-radius: 10px;
        font-size: 12px;
        direction: ltr;
        text-align: left;
    }
    
    /* Align buttons */
    div.stButton > button {
        width: 100%;
        background-color: #0070f3;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 10px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #0056b3;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 class='app-title'>זכותא-AI 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p class='app-subtitle'>מיצוי זכויות פרואקטיבי בעידן סוכני ה-AI האוטונומיים</p>", unsafe_allow_html=True)

# Intro Card for Social Workers and Welfare Professionals
st.markdown("""
<div class='feature-box' style='background: linear-gradient(135deg, #0f172a, #1e293b); color: white;'>
    <h3 style='margin-top: 0; color: #38bdf8; font-weight: 700; font-size: 16px;'>מיצוי זכויות אקטיבי בעידן ה-AI: חזון חדש לעבודה סוציאלית דיגיטלית</h3>
    <p style='font-size: 12.5px; color: #cbd5e1; line-height: 1.6; text-align: justify;'>
        פרויקט זה מציג חזון טכנולוגי-חברתי שבו סוכני בינה מלאכותית אוטונומיים משנים את פני השירות הסוציאלי ומקלים על הנטל הבירוקרטי של הפונים. <br>
        במקום התמודדות מפרכת של האזרח (או העובד הסוציאלי המלווה אותו) עם מערכות טפסים מסורבלות, חוקים דינמיים ותקופות שלילה, סוכן ה-AI סורק באופן פרואקטיבי (תחת הרשאה) את מרחב הנתונים, מצליב אותם מול מאגר חוקים מעוגן דטרמיניסטית (ללא הזיות, מעודכן לתעריפי 2026), ומאכלס את התביעות במלואן.<br>
        הסימולטור שלפניכם ממחיש כיצד טכנולוגיה ממוקדת-אדם יכולה לצמצם פערים דיגיטליים, להגדיל את שיעורי מיצוי הזכויות בפועל, ולפנות לעובדים הסוציאליים זמן יקר המוקדש כיום לבירוקרטיה - לטובת התערבות טיפולית ותמיכה רגשית מעמיקה.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("### 💬 שלב 1: הזנת מקרה הפונה")
st.write("בחר באחד מסיפורי המקרה המובנים להלן להרצה מהירה, או בחר באפשרות האחרונה להקלדת מקרה חדש:")

# Predefined Scenarios for easy testing
scenarios = {
    "🤰 דמי לידה ותאומים (אמא שכירה)": {
        "text": "ילדתי תאומים בשעה טובה! עבדתי שנתיים ברצף עם שכר של 14,000 ש\"ח לחודש. מה מגיע לי ומתי?",
        "type": "maternity",
        "salary": 14000,
        "payout": "58,800 ש\"ח דמי לידה + 10,514 ש\"ח מענק לידה חד-פעמי לתאומים + 392 ש\"ח קצבת ילדים חודשית",
        "form": "טופס 356 (תביעה משולבת לדמי לידה ומענק לידה)",
        "fields": {
            "שם המבוטחת": "שירה כהן-אביגל",
            "סוג התביעה": "דמי לידה (טופס 356)",
            "מספר ילדים בלידה": "2 (תאומים)",
            "שבועות זכאות": "18 שבועות (126 ימי תשלום מלאים)",
            "חשבון בנק לזיכוי": "בנק לאומי (10), סניף 800, ח\"פ 123456"
        },
        "logs": [
            "[SYSTEM] מאתחל סוכן זכויות... זיהוי כוונה מתוך שפה חופשית.",
            "[EXTRACTOR] זיהוי ישויות: אירוע [לידה], מספר ילדים [2 - תאומים], שכר [14,000 ש\"ח], ותק [24 חודשים].",
            "[RULES_DB] מצליב נתונים מול תקנות 2026: ותק עולה על 10 חודשים מזכה ב-15 שבועות מלאים.",
            "[RULES_DB] לידת תאומים מזכה בהארכה חוקית אוטומטית של 3 שבועות נוספים (סה\"כ 18 שבועות).",
            "[CALCULATOR] שכר יומי: 14,000 / 30 = 466.67 ש\"ח (מתחת לתקרת 2026 של 1,752.33 ש\"ח).",
            "[CALCULATOR] סך דמי לידה מחושב: 126 ימים * 466.67 = 58,800 ש\"ח.",
            "[CALCULATOR] מענק לידה חד-פעמי לתאומים: 10,514 ש\"ח (משולם אוטומטית לבית החולים).",
            "[CALCULATOR] קצבת ילדים מובנית לתאומים: 392 ש\"ח לחודש + חיסכון אוטומטי של 116 ש\"ח לחודש.",
            "[FORM_ENGINE] מאכלס 100% משדות טופס 356 על בסיס הצלבת נתוני מעסיק ורשות המיסים.",
            "[API_CLIENT] מבצע לחיצת יד דיגיטלית מול האזור האישי בביטוח לאומי (ps.btl.gov.il)...",
            "[SUCCESS] התביעה מולאה בהצלחה ומוכנה לשגר!"
        ]
    },
    "🚗 מעבר דירה והתפטרות מוצדקת (שכיר)": {
        "text": "התפטרתי מהעבודה בגלל שאשתי קיבלה הצעת עבודה בחיפה ועברנו מראש העין. עבדתי שם שנה וחצי, שכר של 11,000 ש\"ח. מתי אקבל אבטלה?",
        "type": "unemployment",
        "salary": 11000,
        "payout": "7,920 ש\"ח לחודש הראשון (ללא תקופת המתנה של 90 יום!)",
        "form": "טופס 1500 (תביעת אבטלה) + מכתב ערעור והצדקה",
        "fields": {
            "שם המבוטח": "ששון מזרחי",
            "סוג התביעה": "דמי אבטלה (טופס 1500)",
            "סיבת סיום עבודה": "התפטרות מוצדקת (מעבר דירה בעקבות תעסוקת בת זוג)",
            "מרחק המעבר": "84 ק\"מ (מעל הרף החוקי של 40 ק\"מ)",
            "נספחים שאומתו ע\"י הסוכן": "חוזה שכירות בחיפה, חוזה עבודה של בת הזוג באינטל חיפה"
        },
        "logs": [
            "[SYSTEM] מאתחל סוכן זכויות... זיהוי כוונה מתוך שפה חופשית.",
            "[EXTRACTOR] זיהוי ישויות: אירוע [סיום עבודה - התפטרות], ותק [18 חודשים], שכר [11,000 ש\"ח], מרחק מעבר [84 ק\"מ].",
            "[RULES_DB] בדיקת אכשרה: 18 חודשי עבודה עונים על דרישת הסף (מינימום 12 מתוך 18 חודשים).",
            "[RULES_DB] מכשול התפטרות זוהה! התפטרות גוררת שלילה של 90 ימים.",
            "[RULES_DB] הפעלת סוכן הצדקה: מעבר דירה מעל 40 ק\"מ בעקבות עבודת בת הזוג מהווה 'התפטרות מוצדקת'.",
            "[RULES_DB] עוקף אוטומטית את תקופת השלילה של ה-90 יום ומאשר תשלום מהיום הראשון!",
            "[CALCULATOR] שכר יומי ממוצע: 11,000 / 25 = 440 ש\"ח. שיעור גמלה מחושב: 440 * 60% = 264 ש\"ח ליום.",
            "[CALCULATOR] סך דמי אבטלה לחודש ראשון (30 יום): 7,920 ש\"ח.",
            "[LETTER_GEN] סוכן מכתבים מנסח אוטומטית מכתב פנייה רשמי למחלקת אבטלה המפנה לסעיף 166 לחוק.",
            "[FORM_ENGINE] מאכלס טופס 1500 ומצרף אוטומטית את חוזה השכירות בחיפה וחוזה העבודה של בת הזוג.",
            "[API_CLIENT] הגשת מסמכים ישירה לרכזת ביטוח לאומי דרך API.",
            "[SUCCESS] הערעור ומכתב ההצדקה מולאו והתביעה מוכנה להגשה ללא תקופת המתנה!"
        ]
    },
    "👴 פרישה ומבחן הכנסה (אזרח ותיק עובד)": {
        "text": "הגעתי לגיל 67 ואני רוצה להתחיל לקבל קצבת זיקנה, אבל אני עדיין עובד ומרוויח 7,200 ש\"ח לחודש. אשתי בת 64 ולא עובדת.",
        "type": "pension",
        "salary": 7200,
        "payout": "3,590.60 ש\"ח לחודש קבוע (קצבה זוגית מלאה כולל תוספת ותק)",
        "form": "טופס 480 (תביעה לקצבת אזרח ותיק)",
        "fields": {
            "שם המבוטח": "שלמה גרוניך",
            "סוג התביעה": "קצבת אזרח ותיק (טופס 480)",
            "גיל": "67 שנים",
            "שכר חודשי קיים": "7,200 ש\"ח (עובר מבחן הכנסה לזוג - תקרת 2026 היא 10,436 ש\"ח)",
            "תוספת ותק מאושרת": "30% תוספת בגין 25 שנות ביטוח"
        },
        "logs": [
            "[SYSTEM] מאתחל סוכן זכויות... זיהוי כוונה מתוך שפה חופשית.",
            "[EXTRACTOR] זיהוי ישויות: אירוע [פרישה], גיל [67], שכר [7,200 ש\"ח], ותק ביטוחי [25 שנים], בת זוג [בת 64, לא עובדת].",
            "[RULES_DB] גיל 67 מאפשר הגשת תביעה לגמלת אזרח ותיק.",
            "[RULES_DB] בדיקת מבחן הכנסה בין גיל פרישה ל-70: שכר של 7,200 ש\"ח נמוך מתקרת זוג של 10,436 ש\"ח לשנת 2026.",
            "[RULES_DB] אושר! זכאי לקבלת קצבה מלאה למרות שהוא ממשיך לעבוד.",
            "[CALCULATOR] קצבה בסיסית זוגית (כולל תוספת בת זוג שאינה עובדת): 2,762 ש\"ח.",
            "[CALCULATOR] חישוב תוספת ותק: 25 שנות ביטוח -> 15 שנים מעבר ל-10 הראשונות -> 15 * 2% = 30% תוספת.",
            "[CALCULATOR] סכום תוספת ותק: 2,762 * 30% = 828.60 ש\"ח.",
            "[CALCULATOR] סך קצבה חודשית קבועה: 3,590.60 ש\"ח לחודש.",
            "[FORM_ENGINE] מילוי אוטומטי של טופס 480 כולל פרטי בן/בת זוג וחשבון בנק.",
            "[SUCCESS] טופס התביעה מוכן ומאושר דיגיטלית להגשה!"
        ]
    },
    "✍️ הקלד מקרה חדש בלשון חופשית": {
        "text": "",
        "type": "custom",
        "salary": 0,
        "payout": "",
        "form": "",
        "fields": {},
        "logs": []
    }
}

# User Selection
choice = st.radio("בחר תרחיש להרצה מהירה:", list(scenarios.keys()))
selected_data = scenarios[choice]

# Manual Input Box
if choice == "✍️ הקלד מקרה חדש בלשון חופשית":
    user_story = st.text_area("הקלד כאן את סיפור המקרה (בעברית חופשית):", "", height=100, placeholder="לדוגמה: עבדתי שנה וחצי, אשתי קיבלה עבודה בחיפה ונאלצנו לעבור...")
else:
    user_story = st.text_area("טקסט המקרה כפי שנקלט בסוכן (ניתן לעריכה):", selected_data["text"], height=100)

# Trigger Button
if st.button("🤖 הפעל את סוכן ה-AI האוטונומי"):
    if not user_story.strip():
        st.warning("אנא הזן או בחר מקרה לסימולציה לפני ההפעלה.")
    else:
        st.write("### 🧠 שלב 2: סוכן ה-AI פועל ומקבל החלטות (בזמן אמת)")
        
        # Determine which scenario logic to run based on free-text routing if "custom" is selected
        active_scen = selected_data
        scen_type = selected_data["type"]
        
        if scen_type == "custom":
            # Semantic routing logic based on keywords
            text_lower = user_story.lower()
            if "לידה" in text_lower or "תאומים" in text_lower or "ילדתי" in text_lower or "הריון" in text_lower:
                active_scen = scenarios["🤰 דמי לידה ותאומים (אמא שכירה)"]
                st.info("💡 סוכן ה-AI זיהה בהצלחה כוונת 'חופשת לידה והורות' מתוך הטקסט החופשי שהקלדת.")
            elif "התפטר" in text_lower or "אבטלה" in text_lower or "מעבר" in text_lower or "דירה" in text_lower:
                active_scen = scenarios["🚗 מעבר דירה והתפטרות מוצדקת (שכיר)"]
                st.info("💡 סוכן ה-AI זיהה בהצלחה כוונת 'סיום העסקה ואבטלה' מתוך הטקסט החופשי שהקלדת.")
            elif "זקנה" in text_lower or "זיקנה" in text_lower or "67" in text_lower or "פרישה" in text_lower or "פנסיה" in text_lower:
                active_scen = scenarios["👴 פרישה ומבחן הכנסה (אזרח ותיק עובד)"]
                st.info("💡 סוכן ה-AI זיהה בהצלחה כוונת 'פרישה וקצבת אזרח ותיק' מתוך הטקסט החופשי שהקלדת.")
            else:
                # Fallback to unemployment if unknown, with a nice note
                active_scen = scenarios["🚗 מעבר דירה והתפטרות מוצדקת (שכיר)"]
                st.info("💡 סוכן ה-AI סיווג את המקרה תחת תוכנית 'אבטלה וזכויות תעסוקה' על בסיס ניתוח הטקסט.")

        # Progress Bar and Live Animated Terminal Logs
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        log_area = st.empty()
        logs_generated = []
        
        total_steps = len(active_scen["logs"])
        
        for idx, log in enumerate(active_scen["logs"]):
            logs_generated.append(log)
            
            # Display accumulating logs
            log_html = "<div class='agent-thinking'>" + "<br>".join(logs_generated) + "</div>"
            log_area.markdown(log_html, unsafe_allow_html=True)
            
            # Update progress
            progress = int((idx + 1) / total_steps * 100)
            progress_bar.progress(progress)
            status_text.text(f"מעבד... {progress}%")
            
            time.sleep(0.6)  # Pause to simulate active reasoning
            
        status_text.text("הסוכן השלים את פעולתו בהצלחה! 🎉")
        st.balloons()
        
        # Step 3: Result Dashboard for the Citizen
        st.write("### 💰 שלב 3: התוצאה הסופית עבור המבוטח")
        st.success(f"**נמצאו זכויות כספיות מותאמות אישית!**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="סך הכל כסף שחולץ עבור המבוטח", value="מחושב אוטומטית" if active_scen["type"] != 'unemployment' else f"{active_scen['salary']} ש\"ח", delta=active_scen["payout"])
        with col2:
            st.metric(label="טופס התביעה המשויך", value=active_scen["form"])
            
        # Pre-filled form showcase
        st.write("#### 📄 תצוגה מקדימה של שדות הטופס המלאים:")
        fields_html = "<div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; background-color: #f1f5f9; padding: 15px; border-radius: 10px; font-size: 13px;'>"
        for key, val in active_scen["fields"].items():
            fields_html += f"<div style='background: white; padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1;'><b>{key}:</b><br>{val}</div>"
        fields_html += "</div>"
        st.markdown(fields_html, unsafe_allow_html=True)
        
        # Final call to action
        st.markdown("""
        <div style='background-color: #ecfdf5; border: 1px solid #10b981; padding: 15px; border-radius: 12px; margin-top: 20px; text-align: center;'>
            <h4 style='color: #065f46; margin-top: 0; font-weight: bold;'>הכל מוכן לשיגור!</h4>
            <p style='color: #047857; font-size: 13px;'>סוכן ה-AI איגד את כל המסמכים המאמתים ומוכן להגיש את התביעה לאזור האישי הממשלתי.</p>
            <button style='background-color: #10b981; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; cursor: pointer;'>שגר תביעה כעת לאזור האישי (ps.btl.gov.il)</button>
        </div>
        """, unsafe_allow_html=True)

# Sidebar / Footer Guide
st.sidebar.markdown("""
### 🚀 איך להעלות את האפליקציה לרשת בחינם?
אתה יכול לקבל **קישור חי ומשותף בנייד** שתוכל להראות לכל אדם ברחוב תוך 2 דקות:

1. שמור את קוד ה-Python של קובץ זה (`app.py`).
2. העלה אותו לתיקייה חדשה (Repository) בחינם ב-**GitHub**.
3. כנס לאתר **[Streamlit Community Cloud](https://streamlit.io/cloud)**, התחבר עם GitHub.
4. לחץ **New App**, בחר את התיקייה ואת הקובץ `app.py` ולעשות **Deploy**.
5. **זהו!** תקבל לינק ישיר (למשל `zchuta-ai.streamlit.app`) שפועל מכל טלפון או מחשב.
""")
