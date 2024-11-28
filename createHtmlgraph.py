import os
import json
import pandas as pd
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go

# Collect data from Mythril analysis
error_counts = Counter()
file_error_summary = []

for file in os.listdir("mythril_results"):
    if file.endswith(".json"):
        with open(os.path.join("mythril_results", file), "r") as f:
            try:
                data = json.load(f)
                issues = data.get("issues", [])
                error_types = [issue.get("title", "Unknown Error") for issue in issues]
                error_counts.update(error_types)
                file_error_summary.append((file.replace(".json", ""), len(issues)))
            except json.JSONDecodeError:
                continue

# Create a DataFrame for the HTML table
df = pd.DataFrame(file_error_summary, columns=["File", "Error Count"])

# Calculate summary statistics
total_files = len(file_error_summary)
total_errors = sum(df["Error Count"])
avg_errors_per_file = total_errors / total_files if total_files else 0

# Create a pie chart using Plotly
pie_chart = px.pie(
    names=error_counts.keys(),
    values=error_counts.values(),
    title="Distribution of Error Types",
)

# Create a bar chart using Plotly
bar_chart = go.Figure(
    data=[
        go.Bar(
            x=list(error_counts.keys()),
            y=list(error_counts.values()),
            marker_color="skyblue",
        )
    ]
)
bar_chart.update_layout(
    title="Frequency of Error Types",
    xaxis_title="Error Type",
    yaxis_title="Frequency",
    xaxis_tickangle=-45,
)

# Generate the HTML content with embedded charts and more details
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Mythril Analysis Report</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f9f9f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        header {{
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        .container {{
            width: 90%;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2, h3 {{
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: white;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        .chart-container {{
            width: 100%;
            margin: 20px 0;
            text-align: center;
        }}
        .summary {{
            background-color: #e0f7e9;
            padding: 15px;
            margin: 20px 0;
            border: 1px solid #c3e6cb;
            border-radius: 5px;
            text-align: center;
        }}
        footer {{
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            color: #666;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Mythril Analysis Report</h1>
        <p>A comprehensive analysis of Solidity smart contracts using Mythril</p>
    </header>
    <div class="container">
        <h2>Overview</h2>
        <p>This report provides an analysis of 100 Solidity smart contracts, highlighting common security vulnerabilities and coding errors detected using Mythril. The results are summarized in tables and visualized through interactive charts.</p>
        
        <div class="summary">
            <h3>Summary Statistics</h3>
            <p><strong>Total Files Analyzed:</strong> {total_files}</p>
            <p><strong>Total Errors Detected:</strong> {total_errors}</p>
            <p><strong>Average Errors Per File:</strong> {avg_errors_per_file:.2f}</p>
        </div>
        
        <h2>Error Summary Table</h2>
        {df.to_html(index=False, border=0)}

        <div class="chart-container">
            <h2>Error Distribution</h2>
            <div id="pie_chart"></div>
        </div>
        <div class="chart-container">
            <h2>Error Frequency</h2>
            <div id="bar_chart"></div>
        </div>
    </div>
    <footer>
        <p>Generated using Mythril and Plotly | &copy; 2024 Your Company</p>
    </footer>
    <script>
        {pie_chart.to_html(full_html=False, include_plotlyjs=False)}
        {bar_chart.to_html(full_html=False, include_plotlyjs=False)}
    </script>
</body>
</html>
"""

# Save the HTML report
with open("mythril_analysis_report.html", "w") as file:
    file.write(html_content)

print("Report generated: mythril_analysis_report.html")
