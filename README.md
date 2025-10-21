# AI-Based Classroom Engagement Nudger

A multimodal AI assistant that provides real-time feedback and "nudges" to teachers to help them gauge and improve student engagement.

## The Problem

[cite_start]In any classroom—physical, hybrid, or virtual—it's a significant challenge for educators to accurately gauge the engagement level of every student[cite: 80]. [cite_start]Teachers often rely on intuition, which can be misleading and may not capture the state of quieter students[cite: 81]. This information gap can lead to:
* [cite_start]**Missed Opportunities:** Bright but shy students may not get the encouragement they need[cite: 81].
* [cite_start]**Ineffective Pacing:** Lessons might be too fast for some or too slow for others[cite: 82].
* [cite_start]**Teacher Burnout:** The constant guesswork is emotionally taxing for educators[cite: 83].

## Our Solution

[cite_start]This platform acts as an objective partner for the teacher, providing a real-time, data-driven window into the classroom's engagement level[cite: 84]. [cite_start]By analyzing key visual and audio indicators, our tool translates complex classroom dynamics into simple, actionable insights without replacing the teacher's critical role[cite: 86, 89].

[cite_start]Our goal is to empower educators to do what they do best: inspire, connect, and unlock student potential[cite: 89, 90].

## Key Features

* [cite_start]🎥 **Real-Time Emotion Detection:** Uses the webcam to analyze student facial expressions (Happy, Sad, Neutral, Angry, etc.) to gauge the overall mood of the class.
* [cite_start]🎤 **Audio Analysis:** Monitors ambient classroom noise (Loud, Quiet) and analyzes the teacher's speech for tone and energy.
* [cite_start]💡 **Smart Nudging System:** Provides context-aware, three-tier alerts (good, warning, critical) to the teacher when engagement appears to be dropping.
* [cite_start]📊 **Live Dashboard:** A simple web interface built with Flask that displays four key engagement metrics in real-time.
* 🔒 **Privacy-First Design:** No video or audio is ever recorded or stored. [cite_start]The system processes data in real-time and only uses aggregated, anonymous metrics for analysis.

## Technology Stack

* **Backend:** Python, Flask
* **AI / Machine Learning:** OpenCV, DeepFace
* **Frontend:** HTML/CSS, JavaScript

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.8+
* pip

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/HarshRaj4343/iHUB-Hackathon.git](https://github.com/HarshRaj4343/iHUB-Hackathon.git)
    cd iHUB-Hackathon
    ```
2.  **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```sh
    python app.py
    ```

## Authors

* Harsh Raj
* Arpit Aggarwal
* Challa Kritin
* Sushant Garg
* Saurabh Singh

[cite_start][cite: 76]
