import streamlit as st
import json

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
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
    }
    
    .header-section {
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .header-section h1 {
        margin-bottom: 1rem;
        font-size: 2.5rem;
    }
    
    .header-section p {
        margin-bottom: 0.75rem;
        font-size: 1rem;
        color: #333;
    }
    
    .header-section a {
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
    
    .header-section a:hover {
        background-color: #333;
    }
    
    .input-section {
        margin-bottom: 2rem;
    }
    
    .results-section {
        margin-top: 2rem;
        padding: 2rem;
        background-color: #f8f9fa;
        border-radius: 8px;
        border-left: 4px solid #000;
    }
    
    .result-item h3 {
        font-size: 1rem;
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
    
    .instructions {
        padding: 1.5rem;
        background-color: #f8f9fa;
        border-radius: 8px;
        margin-bottom: 2rem;
    }
    
    .instructions h2 {
        margin-bottom: 1rem;
        font-size: 1.5rem;
    }
    
    .instructions ol {
        margin-left: 1.5rem;
    }
    
    .instructions li {
        margin-bottom: 0.5rem;
    }
    
    .instructions img {
        width: 100%;
        max-width: 300px;
        margin-top: 1rem;
        border-radius: 4px;
    }
    
    .error-message {
        color: #d32f2f;
        padding: 1rem;
        background-color: #ffebee;
        border-radius: 4px;
        margin-top: 1rem;
    }
    
    .info-message {
        color: #1976d2;
        padding: 1rem;
        background-color: #e3f2fd;
        border-radius: 4px;
        margin-top: 1rem;
    }
    
    @media (max-width: 768px) {
        .header-section h1 {
            font-size: 1.8rem;
        }
        
        .result-value {
            font-size: 2rem;
        }
        
        .results-section {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header with branding and CTA
st.markdown("""
<div class="header-section">
    <h1>Get the Truth about High Protein Foods</h1>
    <p>Use this calculator to find out whether a food is actually high in protein or just marketed that way.</p>
    <p>By the way, I'm a marketer who lost 30+ lbs on my own terms. I teach people how to see through ads, track what works, and lose weight your way.</p>
    <p>And if you like this calculator, you'll love my other stuff. Follow me on X to graduate from weight loss programs forever.</p>
    <a href="https://x.com/bradenrrussom" target="_blank">Graduate Forever  👉</a>
</div>
""", unsafe_allow_html=True)

# Create responsive two-column layout
col_input, col_instructions = st.columns([1, 1], gap="medium")

# Left column: Input fields
with col_input:
    st.markdown("<div class='input-section'>", unsafe_allow_html=True)
    
    calories = st.number_input(
        "Calories",
        min_value=0.0,
        value=0.0,
        step=1.0,
        help="Enter calories here"
    )
    
    protein = st.number_input(
        "Grams of Protein",
        min_value=0.0,
        value=0.0,
        step=1.0,
        help="Enter protein here"
    )
    
    st.markdown("</div>", unsafe_allow_html=True)

# Right column: Instructions
with col_instructions:
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
            Look at the nutrition facts label. Calories are usually at the top, and protein is listed below with other nutrients.
        </p>
    </div>
    """, unsafe_allow_html=True)

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