from flask import Flask, render_template, jsonify
from emotion_detector import get_classroom_emotion
from audio_detector import check_classroom_audio
import threading
import time

app = Flask(__name__)

dashboard_data = {
    'emotion': 'neutral',
    'audio_state': 'quiet',
}
data_lock = threading.Lock()

def update_emotion_task():
    while True:
        emotion = get_classroom_emotion()  
        with data_lock:
            dashboard_data['emotion'] = emotion
        print(f"Updated emotion: {emotion}")
        time.sleep(1) 
def update_audio_task():
    while True:
        audio_state, _ = check_classroom_audio()
        with data_lock:
            dashboard_data['audio_state'] = audio_state
        print(f"Updated audio state: {audio_state}")
        time.sleep(1)


@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/data')
def get_data():
    with data_lock:
        
        current_emotion = dashboard_data['emotion']
        current_audio_state = dashboard_data['audio_state']
    
    score = 50  
    if current_emotion in ['happy', 'neutral', 'surprised']:
        score += 20
    elif current_emotion in ['sad', 'angry', 'fear']:
        score -= 20
        
    if current_audio_state == 'silent':
        score -= 20
    elif current_audio_state == 'active':
        score += 10
    
    score = max(0, min(100, score))  

   
    nudge = "Engagement is good. Keep up the great work! 👍"
    if score < 40:
        nudge = "⚠️ Engagement seems low. Try asking a question to the class."
    elif score < 60:
        nudge = "⚡ Consider a quick activity or recap to boost engagement."

   
    response_data = {
        'engagement_score': score,
        'emotion': current_emotion,
        'audio_state': current_audio_state,
        'nudge': nudge,
        'timestamp': time.time()
    }
    return jsonify(response_data)

if __name__ == '__main__':
    emotion_thread = threading.Thread(target=update_emotion_task, daemon=True)
    emotion_thread.start()
    audio_thread = threading.Thread(target=update_audio_task, daemon=True)
    audio_thread.start()
    app.run(debug=True, port=5000, use_reloader=False)
