from app import create_app
from datetime import timedelta
import os

app = create_app()

# --- PERFORMANCE ARCHITECTURE ---

# 1. Aggressive Browser Caching
# Tells the browser: "Keep static files (images, css, js) for 1 year"
# This makes subsequent redirects and page loads feel instant (0ms latency).
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(days=365)

# 2. Response Compression
# Compresses HTML/CSS/JS before sending it to the user.
# Note: Requires 'pip install flask-compress'
try:
    from flask_compress import Compress
    Compress(app)
except ImportError:
    print("Flash load tip: Install 'flask-compress' for even faster first-time visits.")

if __name__ == '__main__':
    app.run(debug=True)