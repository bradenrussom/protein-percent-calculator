import streamlit as st
import json
from pathlib import Path

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Page configuration
st.set_page_config(
    page_title="High Protein Food Calculator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling and responsiveness
st.markdown("""
<style>
    /* ============== GENERAL STYLES ============== */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
        background-color: #f8fafb;
    }
    
    [data-testid="stAppViewContainer"] {
        background-color: #f8fafb;
    }
    
    /* ============== HEADER SECTION ============== */
    .header-section {
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .header-section h1 {
        margin-bottom: 1rem;
        font-size: 2.5rem;
        color: #1a1a1a;
    }
    
    .header-section p {
        margin-bottom: 0.75rem;
        font-size: 1rem;
        color: #333;
    }
    
    .header-section a.cta-button {
        display: inline-block;
        margin-top: 1rem;
        padding: 0.75rem 1.5rem;
        background-color: #000;
        color: #fff;
        text-decoration: none;
        border-radius: 4px;
        font-weight: bold;
        transition: background-color 0.2s;
    }
    
    .header-section a.cta-button:hover {
        background-color: #333;
    }
    
    /* ============== AUTHOR BIO SECTION ============== */
    .author-bio {
        margin-top: 1.5rem;
    }
    
    .author-photo {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        flex-shrink: 0;
    }
    
    .author-info p {
        margin: 0;
        color: #333;
        font-weight: 500;
    }
    
    .author-info a {
        color: #1da1f2;
        text-decoration: none;
        font-weight: 600;
    }
    
    .author-info a:hover {
        text-decoration: underline;
    }
    
    /* ============== INPUT SECTION ============== */
    .input-section {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    
    /* ============== RESULTS SECTION ============== */
    .results-section {
        margin: 2rem 0;
        padding: 2rem;
        background-color: #ffffff;
        border-radius: 8px;
        border-left: 4px solid #000;
    }
    
    .result-item h3 {
        font-size: 0.85rem;
        color: #666;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .result-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #000;
    }
    
    /* ============== INSTRUCTIONS SECTION ============== */
    .instructions {
        padding: 2rem;
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin-top: 2rem;
    }
    
    .instructions h2 {
        margin-bottom: 1rem;
        font-size: 1.5rem;
        color: #1a1a1a;
    }
    
    .instructions ol {
        margin-left: 1.5rem;
        color: #333;
    }
    
    .instructions li {
        margin-bottom: 0.75rem;
        color: #333;
    }
    
    .instructions img {
        width: 100%;
        max-width: 400px;
        margin-top: 1.5rem;
        border-radius: 4px;
        border: 1px solid #e0e0e0;
    }
    
    /* ============== MESSAGES (ERROR, INFO) ============== */
    .error-message {
        color: #c41e3a;
        padding: 1rem;
        background-color: #fff5f5;
        border-radius: 4px;
        margin-top: 1rem;
        border-left: 4px solid #c41e3a;
    }
    
    .info-message {
        color: #1976d2;
        padding: 1rem;
        background-color: #f0f8ff;
        border-radius: 4px;
        margin-top: 1rem;
        border-left: 4px solid #1976d2;
    }
    
    /* ============== RESPONSIVE (MOBILE) ============== */
    @media (max-width: 768px) {
        .header-section h1 {
            font-size: 1.8rem;
        }
        
        .header-section p {
            font-size: 0.95rem;
        }
        
        .author-photo {
            width: 70px;
            height: 70px;
        }
        
        .author-info p {
            font-size: 0.85rem;
        }
        
        .result-value {
            font-size: 2rem;
        }
        
        .results-section {
            padding: 1.5rem;
        }
        
        .instructions {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header with branding - Left column text, right column photo
header_col1, header_col2 = st.columns([2, 1])

with header_col1:
    st.markdown("""
    <div class="header-section">
        <h1>Get the Truth about High Protein Foods</h1>
        <p>Use this calculator to find out whether a food is actually high in protein or just marketed that way.</p>
        <p>By the way, I'm a marketer who lost 30+ lbs on my own terms. I teach people how to see through ads, track what works, and lose weight your way.</p>
        <p>And if you like this calculator, you'll love my other stuff. Follow me on X to graduate from weight loss programs forever.</p>
        <a href="https://x.com/bradenrrussom" target="_blank" class="cta-button">Graduate Forever  👉</a>
    </div>
    """, unsafe_allow_html=True)

with header_col2:
    if Path('bradenrussomheadshot.jpg').exists():
        st.image('bradenrussomheadshot.jpg', use_container_width=False, width=120)
        st.markdown("""
        <div class="author-info">
            <p><strong>Braden Russom</strong></p>
            <p><a href="https://x.com/bradenrrussom" target="_blank">@bradenrrussom</a></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="padding: 1rem; background-color: #fff5f5; border-radius: 4px; border-left: 4px solid #c41e3a;">
            <p style="color: #c41e3a; margin: 0; font-size: 0.85rem;"><strong>⚠️ Photo missing</strong><br>Add bradenrussomheadshot.jpg to your repo</p>
        </div>
        """, unsafe_allow_html=True)

# Input section
st.markdown("<div class='input-section'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    calories = st.number_input(
        "Calories",
        min_value=0,
        value=0,
        step=1,
        help="Enter calories here"
    )

with col2:
    protein = st.number_input(
        "Grams of Protein",
        min_value=0.0,
        value=0.0,
        step=1.0,
        help="Enter protein here"
    )

st.markdown("</div>", unsafe_allow_html=True)

# Calculation logic
if calories > 0 and protein > 0:
    # Input validation
    max_cal = config['validation']['max_calories']
    max_prot = config['validation']['max_protein']
    
    if calories > max_cal:
        st.markdown(
            f'<div class="error-message">❌ Calories must be {max_cal} or less</div>',
            unsafe_allow_html=True
        )
    elif protein > max_prot:
        st.markdown(
            f'<div class="error-message">❌ Protein must be {max_prot}g or less</div>',
            unsafe_allow_html=True
        )
    else:
        # Calculate protein percentage
        protein_calories = protein * 4
        percentage = (protein_calories / calories) * 100
        
        # Determine ranking based on thresholds
        ranking = None
        for threshold in config['thresholds']:
            if percentage >= threshold['min']:
                ranking = threshold['label']
                break
        
        # Display results
        st.markdown("""
        <div class="results-section">
        """, unsafe_allow_html=True)
        
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.markdown("""
            <div class="result-item">
                <h3>% of Calories from Protein</h3>
                <div class="result-value">{:.1f}%</div>
            </div>
            """.format(percentage), unsafe_allow_html=True)
        
        with res_col2:
            st.markdown("""
            <div class="result-item">
                <h3>Is this a High Protein Food?</h3>
                <div class="result-value">{}</div>
            </div>
            """.format(ranking), unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

elif (calories > 0 or protein > 0):
    st.markdown(
        '<div class="info-message">ℹ️ Enter values in both fields to calculate</div>',
        unsafe_allow_html=True
    )

# Instructions section (always visible)
st.markdown("""
<div class="instructions">
    <h2>Instructions:</h2>
    <ol>
        <li>Find the nutrition label on any food</li>
        <li>Enter the calories in the first field</li>
        <li>Enter the grams of protein in the second field</li>
    </ol>
    <p style="margin-top: 1rem; font-size: 0.9rem; color: #666;">
        <strong>Where to find these numbers:</strong><br>
        Look at the nutrition facts label. Calories are usually at the top, and protein is listed below with other nutrients. Here's an example:
    </p>
</div>
""", unsafe_allow_html=True)

# Display nutrition label image if it exists
if Path('nutrition_label_numbers.jpg').exists():
    st.image('nutrition_label_numbers.jpg', use_container_width=True)
else:
    st.markdown("""
    <div style="padding: 1rem; background-color: #fff5f5; border-radius: 4px; border-left: 4px solid #c41e3a; margin-top: 1rem;">
        <p style="color: #c41e3a; margin: 0; font-size: 0.85rem;"><strong>⚠️ Image missing</strong><br>Add nutrition_label_numbers.jpg to your repo</p>
    </div>
    """, unsafe_allow_html=True)