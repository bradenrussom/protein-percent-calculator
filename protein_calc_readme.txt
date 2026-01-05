# High Protein Food Calculator

An interactive web calculator to help users determine whether a food is actually high in protein or just marketed that way. Built as part of the DIY Data content pillar.

## Project Structure

```
protein-calculator/
├── app.py              # Main Streamlit application
├── config.json         # Configuration (thresholds, validation rules)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Features

- **Clean, responsive interface**: Works seamlessly on mobile and desktop
- **Two input fields**: Calories and grams of protein
- **Automatic calculation**: Shows protein percentage of total calories
- **Smart ranking system**: Categorizes foods as "Yes", "Sorta", "No", or "Hell No"
- **Input validation**: Rejects invalid inputs (non-numeric, zero, negative, or extremely high values)
- **Configurable logic**: Easy to adjust thresholds and limits via `config.json`

## Calculation

The calculator uses the formula:
```
(Grams of Protein × 4) ÷ Calories × 100%
```

Then ranks the result based on these thresholds:
- **70% or higher**: "Yes"
- **50-70%**: "Sorta"
- **25-50%**: "No"
- **Below 25%**: "Hell No"

## Local Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository** (or create the project directory):
```bash
git clone https://github.com/yourusername/protein-calculator.git
cd protein-calculator
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Running Locally

Start the Streamlit development server:
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your default browser.

## Configuration

Edit `config.json` to customize:

- **Thresholds**: Adjust the percentage values that determine rankings
- **Labels**: Change "Yes", "Sorta", "No", "Hell No" to different text
- **Validation limits**: Set `max_calories` and `max_protein` to control input constraints

Example:
```json
{
  "thresholds": [
    {"min": 70, "label": "Yes"},
    {"min": 50, "label": "Sorta"},
    {"min": 25, "label": "No"},
    {"min": 0, "label": "Hell No"}
  ],
  "validation": {
    "max_calories": 5000,
    "max_protein": 300
  }
}
```

## Deployment to Render.com

### Prerequisites
- GitHub account with the repository pushed
- Render.com account

### Steps

1. **Push code to GitHub**:
```bash
git init
git add .
git commit -m "Initial commit: protein calculator MVP"
git branch -M main
git remote add origin https://github.com/yourusername/protein-calculator.git
git push -u origin main
```

2. **Connect to Render.com**:
   - Log in to [Render.com](https://render.com)
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Select the `protein-calculator` repository

3. **Configure the deployment**:
   - **Name**: `protein-calculator` (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=10000 --server.address=0.0.0.0`
   - **Instance Type**: Free (for MVP testing) or Starter+ (for production)

4. **Deploy**:
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - Your app will be live at `https://protein-calculator.onrender.com` (or your custom subdomain)

### After Deployment

Your app will redeploy automatically whenever you push to the `main` branch on GitHub. This enables a smooth development workflow:

1. Code locally → Test with `streamlit run app.py`
2. Commit → `git commit -m "message"`
3. Push → `git push origin main`
4. Monitor deployment in Render.com dashboard

## Maintenance & Future Enhancements

### Current MVP includes:
- ✅ Two input fields with validation
- ✅ Percentage calculation
- ✅ Ranking system
- ✅ Responsive design
- ✅ Configuration-based flexibility
- ✅ Clean, modular code

### Potential future enhancements:
- Add food database for quick lookups
- Export calculation results
- Compare multiple foods side-by-side
- Integration with nutrition APIs
- Analytics tracking (which foods are calculated most)
- Dark mode toggle
- Mobile app version

## Modular Code Structure

The code is organized for maintainability:

- **Configuration**: Separated in `config.json` for easy tweaking
- **HTML/Styling**: Inline CSS in `app.py` using Streamlit's `st.markdown()` with `unsafe_allow_html=True`
- **Logic**: Clear separation between input validation, calculation, and ranking
- **UI**: Responsive layout using Streamlit columns that reflow on mobile

## Troubleshooting

**App won't start locally**:
- Ensure you're in the virtual environment
- Run `pip install -r requirements.txt` again
- Check Python version: `python --version` (needs 3.8+)

**Render deployment fails**:
- Check Render logs in the dashboard
- Verify `Start Command` includes `--server.port=10000 --server.address=0.0.0.0`
- Ensure `config.json` is in the root directory

**Results look wrong**:
- Verify calculation formula: (Protein × 4) ÷ Calories × 100%
- Check `config.json` thresholds are in descending order
- Test with known values (e.g., 240 cal, 3g protein = ~5%)

## Contributing

To update text, headings, links, or instructions, edit the HTML sections in `app.py` marked with `st.markdown()` calls. To update calculation logic or thresholds, modify `config.json`.

## License

MIT License - feel free to use and adapt as needed.

---

**Questions?** Test the MVP locally first, then deploy to Render for user feedback before adding major features.
