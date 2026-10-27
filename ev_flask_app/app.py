from flask import Flask, render_template

app = Flask(__name__)

# Paste your Tableau Public embed URLs here.
# Tableau Public -> open your viz -> Share -> "Embed Code" -> copy the src="..." URL.
BASE = "https://public.tableau.com/views/ElectricVehicleMarketPerformanceInsights_17931389708610"
OPTIONS = "?:showVizHome=no&:embed=true&:toolbar=yes"

STORY_URL = f"{BASE}/EVMarketStory{OPTIONS}"
# If the dashboard does not load, copy its embed URL from Tableau Public the same way
# (it only works if "Show Sheets as Tabs" was ticked when you published).
DASHBOARD_URL = f"{BASE}/EVMarketDashboard{OPTIONS}"


@app.route("/")
def home():
    return render_template("index.html", dashboard_url=DASHBOARD_URL, story_url=STORY_URL)


if __name__ == "__main__":
    app.run(debug=True)
