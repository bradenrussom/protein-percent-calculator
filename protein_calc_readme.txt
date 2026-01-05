# High Protein Food Calculator

An interactive web calculator to help users determine whether a food is actually high in protein or just marketed that way. Built as part of the DIY Data content pillar.

## Project Structure

```
protein-calculator/
├── app.py                      # Main Streamlit application
├── config.json                 # Configuration (thresholds, validation rules)
├── requirements.txt            # Python dependencies
├── bradenrussomheadshot.jpg   # Author photo (for credibility section)
├── nutrition_label_numbers.jpg # Example nutrition label image
└── README.md                   # This file
```

## Features

- **Clean, responsive interface**: Works seamlessly on mobile and desktop
- **Author credibility section**: Photo and Twitter handle to build trust
- **Two input fields**: Calories (integers only) and grams of protein
- **Automatic calculation**: Shows protein percentage of total calories
- **Smart ranking system**: Categorizes foods as "Yes", "Sorta", "No", or "Hell No"
- **Input validation**: Rejects invalid inputs (non-numeric, zero, negative, or extremely high values)
- **Configurable logic**: Easy to adjust thresholds and limits via `config.json`
- **Clear visual hierarchy**: Light background with excellent contrast for clarity

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
- GitHub Desktop installed
- Text editor (Notepad, VS Code, or any text editor)

### Installation with GitHub Desktop

1. **Install GitHub Desktop**:
   - Go to [desktop.github.com](https://desktop.github.com)
   - Download and install

2. **Create a new repository**:
   - Open GitHub Desktop
   - Click **File** → **New Repository**
   - Name: `protein-calculator`
   - Click **Create Repository**

3. **Add files to the folder**:
   - Navigate to the folder that was created
   - Copy these 5 files into it:
     - `app.py`
     - `config.json`
     - `requirements.txt`
     - `bradenrussomheadshot.jpg` (your headshot photo)
     - `nutrition_label_numbers.jpg` (nutrition label example)

4. **Commit and push**:
   - In GitHub Desktop, you'll see all 5 files listed
   - Write Summary: `Initial commit: protein calculator MVP`
   - Click **Commit to main**
   - Click **Publish repository**

## Testing Locally

If you want to test locally without deploying first:

1. **Install Python** from [python.org](https://python.org) (if you don't have it)

2. **Open terminal/command prompt**:
   - Windows: Press `Win + R`, type `cmd`, press Enter
   - Mac: Press `Cmd + Space`, type `terminal`, press Enter

3. **Navigate to your folder**:
   - Type: `cd [path to your protein-calculator folder]`

4. **Install dependencies**:
   - Type: `pip install streamlit`

5. **Run the app**:
   - Type: `streamlit run app.py`
   - Your browser will open to `http://localhost:8501`

6. **Test these scenarios**:
   - 240 calories, 30g protein → Should show 50.0%, "Sorta"
   - 240 calories, 3g protein → Should show 5.0%, "Hell No"
   - Leave fields blank → Should show nothing
   - Fill only one field → Should show info message
   - Enter 6000 calories → Should show error message

## Deployment to Render.com

### Step 1: Prepare Your Repository
1. Make sure all 5 files are in your `protein-calculator` folder
2. Push to GitHub using GitHub Desktop (File → Push)

### Step 2: Deploy to Render
1. Go to [render.com](https://render.com)
2. Sign up (use GitHub to sign up quickly)
3. Click **New +** → **Web Service**
4. Connect your GitHub account if needed
5. Select `protein-calculator` repository
6. Fill in these settings:
   - **Name**: `protein-calculator`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=10000 --server.address=0.0.0.0`
   - **Instance Type**: Free
7. Click **Create Web Service**
8. Wait 2-3 minutes for deployment

### Step 3: Test Your Live App
Once deployed, your app is live. Test these scenarios:
- High protein food: 240 cal, 30g protein = 50.0%, "Sorta"
- Low protein food: 240 cal, 3g protein = 5.0%, "Hell No"
- Empty fields = No results shown
- One field filled = Info message
- Resize browser window = Instructions move below results on mobile

## Configuration

Edit `config.json` to customize:

### Thresholds & Rankings
Change what percentage means what:
```json
"thresholds": [
  {"min": 70, "label": "Yes"},
  {"min": 50, "label": "Sorta"},
  {"min": 25, "label": "No"},
  {"min": 0, "label": "Hell No"}
]
```

### Validation Limits
Set maximum allowed values:
```json
"validation": {
  "max_calories": 5000,
  "max_protein": 300
}
```

## Design & Styling

The app uses:
- **Light background** (#f8fafb): Suggests clarity and transparency
- **High contrast text**: Dark text on light backgrounds for readability
- **Clean white cards**: Input, results, and instructions sections
- **Author credibility section**: Photo + Twitter handle near the header
- **Responsive layout**: Adapts to mobile and desktop

## Updating Your App

### To make changes and deploy a new version:

1. **Edit your files**:
   - Open the file you want to change (e.g., `app.py`, `config.json`)
   - Make your edits
   - Save the file

2. **Update in GitHub Desktop**:
   - Open GitHub Desktop
   - You'll see the changed files
   - Write Summary: `Update: [what you changed]` (e.g., "Update: change header text")
   - Click **Commit to main**
   - Click **Push origin**

3. **Watch it deploy**:
   - Go to your [Render dashboard](https://dashboard.render.com)
   - Click your `protein-calculator` service
   - You'll see a new deployment starting
   - Wait for it to say "Your service is live"
   - Your changes are now live!

### Quick Examples

**Change the header text?**
- Edit the `<p>` tags in `app.py`, save, commit, push

**Change ranking thresholds?**
- Edit `config.json`, change the values, save, commit, push

**Update your Twitter handle?**
- Find `@bradenrrussom` in `app.py`, replace it, save, commit, push

**Change max calories allowed?**
- Edit `config.json`, change `"max_calories": 5000` to your value, save, commit, push

## Image Files

The app uses two image files that should be in your GitHub repository:

1. **bradenrussomheadshot.jpg** - Your headshot photo
   - Appears in the credibility section below the header
   - Recommended size: 600x600px or larger
   - Should be a professional headshot

2. **nutrition_label_numbers.jpg** - Example nutrition label
   - Shows in the instructions section
   - Should clearly show where calories and protein are located
   - Can be any reasonable size

If either image is missing, the app will still work but won't display that image.

## Modular Code Structure

The code is organized for easy maintenance:

- **Configuration**: Separated in `config.json` for tweaking without touching code
- **Styling**: Inline CSS using Streamlit's `st.markdown()` with `unsafe_allow_html=True`
- **Logic**: Clear separation between input validation, calculation, and ranking
- **UI**: Responsive layout that adapts to mobile and desktop

## Troubleshooting

**App won't start locally**:
- Make sure Python is installed: `python --version`
- Make sure Streamlit is installed: `pip install streamlit`
- Check that you're in the correct folder

**Render deployment fails**:
- Check Render logs in the dashboard
- Verify all 5 files are in your GitHub repository
- Ensure image filenames match exactly (`bradenrussomheadshot.jpg`, `nutrition_label_numbers.jpg`)

**Images not showing**:
- Make sure image files are in the same folder as `app.py`
- Check filenames match exactly (case-sensitive on some systems)
- Make sure images are pushed to GitHub

**Results look wrong**:
- Test with known values: 240 cal, 3g protein should = ~5%
- Check `config.json` thresholds are in correct order

## Contributing

To update text, headings, links, instructions, or styling, edit the HTML sections in `app.py`. To update calculation logic or thresholds, modify `config.json`.

## License

MIT License - feel free to use and adapt as needed.

---

**Next Steps**: Deploy to Render.com, test with real users, and iterate based on feedback!
