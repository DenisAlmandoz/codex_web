from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    profile = {
        "name": "Alex Carter",
        "title": "Senior Data Engineer",
        "location": "Seattle, WA",
        "tagline": "Building reliable data platforms that power analytics, AI, and product growth.",
        "email": "alex.carter@email.com",
        "linkedin": "https://www.linkedin.com/in/alexcarter",
        "github": "https://github.com/alexcarter",
    }
    highlights = [
        "10+ years designing cloud-scale data platforms",
        "Led migrations to modern lakehouse architectures",
        "Trusted partner for analytics, ML, and product teams",
    ]
    skills = [
        "Python", "SQL", "Spark", "Airflow", "Kafka", "dbt", "Snowflake", "AWS", "Terraform", "Docker"
    ]
    experience = [
        {
            "role": "Senior Data Engineer",
            "company": "Northwind Analytics",
            "time": "2020 - Present",
            "details": [
                "Architected an AWS lakehouse with Iceberg + Spark, reducing query costs by 32%.",
                "Built a self-serve metrics layer with dbt and Looker, accelerating executive reporting.",
                "Mentored a team of 6 engineers, establishing standards for data quality and governance.",
            ],
        },
        {
            "role": "Data Platform Engineer",
            "company": "Aurora Commerce",
            "time": "2016 - 2020",
            "details": [
                "Implemented streaming pipelines with Kafka and Flink for real-time personalization.",
                "Automated infrastructure with Terraform, cutting environment setup time by 80%.",
            ],
        },
    ]
    projects = [
        {
            "name": "Telemetry Lakehouse",
            "summary": "Unified telemetry from 15+ services into a governed lakehouse for ML teams.",
        },
        {
            "name": "Growth Analytics Hub",
            "summary": "Created a curated data mart powering weekly growth experiments and KPIs.",
        },
        {
            "name": "Reliability Scorecard",
            "summary": "Built a data quality scorecard with automated alerts and incident workflows.",
        },
    ]
    return render_template(
        "index.html",
        profile=profile,
        highlights=highlights,
        skills=skills,
        experience=experience,
        projects=projects,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
