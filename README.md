# Electric Vehicle Market Performance & Insights

An interactive Tableau dashboard and data story analysing the global electric vehicle (EV) market across vehicle categories, manufacturers, battery technologies, manufacturing countries and customer satisfaction.

**Live demo:** https://public.tableau.com/app/profile/ujjawal.rathod4051/viz/ElectricVehicleMarketPerformanceInsights_17931389708610/EVMarketStory

## Problem Statement
Three stakeholders need data-driven insight into the EV market:
- **Emily Johnson, Market Strategy Director:** which vehicle categories drive sales, who the leading manufacturers are, and how customer satisfaction varies.
- **David Chen, Automotive BI Manager:** manufacturer market share, battery technology distribution, manufacturing country trends and expansion opportunities.
- **Dr. Sarah Williams, Sustainable Mobility Researcher:** how battery technology, driving range and manufacturing distribution relate to adoption and satisfaction.

## Dataset
- `ev_market_train.csv` (200,000 rows) and `ev_market_test.csv` (100,000 rows), 37 fields each, combined with a Union in Tableau (300,000 rows).
- Fields include manufacturer, category, battery type, range, charging, price, annual sales, customer rating, manufacturing country and market region.
- Data notes: missing values in `annual_sales_units`, `customer_rating`, `battery_cycle_life`, `resale_value_pct_3yr` and `infotainment_screen_inch` were left as nulls (Tableau ignores them in aggregations). One duplicate `vehicle_id` was found and has negligible impact.

## Tools
Tableau Public

## Visualizations
| # | Visual | Scenario |
|---|---|---|
| 1 | Annual sales by vehicle category | Emily |
| 2 | Top 10 manufacturers and market share | Emily, David |
| 3 | Annual sales trend by model year | Emily |
| 4 | Battery technology share of sales | Emily, David, Sarah |
| 5 | Average driving range by category | Emily, Sarah |
| 6 | Average range trend by battery type | Sarah |
| 7 | Annual sales by manufacturing country (map) | David, Sarah |
| 8 | Average customer rating by category | Emily, David, Sarah |
| 9 | Region x category sales heatmap | David |

The dashboard has filters for Market Region, Battery Type and Model Year, and the map, battery donut and category chart work as click-to-filter. The story has four points: an overview, then one per persona.

## Key Insights
- Two-Wheeler Scooter is the top-selling category, followed by Sedan, Hatchback and Compact SUV.
- The market is fragmented: the top manufacturer holds about 0.6% of sales.
- NMC (33.7%) and LFP (32.0%) lead battery technology, followed by NCA (17.3%), Sodium-Ion (9.9%) and Solid-State (7.1%).
- Range depends on vehicle category (Luxury Sedan about 550 km, Two-Wheeler Scooter about 105 km), not battery type: average range is about 324 km for every battery type.
- Customer rating is about 4.08 to 4.09 in every category, so satisfaction does not separate segments in this dataset.
- Sales are spread evenly across the 7 market regions; the differences are between categories.

## Challenges and Solutions
- **Market share of the Top 10 manufacturers:** a Top N filter distorts percentage-of-total, so I used a `FIXED` level-of-detail calculation to divide by total market sales.
- **Misleading line chart:** a zoomed-in axis made a 5 km range wobble look like a trend, so I fixed the axis at 0 to 400.
- **Overlapping text on the dashboards:** fixed by using tiled layouts, removing duplicate legends and moving text boxes to the bottom edge.

## Files
- `screenshots/`: images of each visual, the dashboard and the story
- Dataset: `ev_market_train.csv` and `ev_market_test.csv` are not included in this repository because of their size (200,000 and 100,000 rows). The full workbook with the data is available on Tableau Public (see the live demo link above).

## Author
Ujjawal Rathod
