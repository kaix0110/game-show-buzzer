# Game Show Buzzer System

A real-time, interactive game show buzzer application with host-controlled point awarding mechanism. Perfect for quiz competitions, game shows, and classroom activities.

## Features

- **Multi-Table Support**: Handles up to 11 participant tables simultaneously
- **Real-Time Buzzer System**: Instant buzz registration with order tracking
- **Host-Controlled Points**: 
  - Manual point awarding system
  - Customizable points (0-10)
  - Real-time ranking updates
- **Live Rankings Display**:
  - Gold, silver, and bronze medals for top 3
  - Dynamic score tracking
  - Instant updates for all participants
- **Theatrical Interface**:
  - Game show inspired design
  - Visual feedback and animations
  - Sound effects

## Setup

1. Clone the repository:
```bash
git clone [your-repository-url]
cd buzzer_app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## Dependencies

- Python 3.13.0
- Flask 2.3.3
- Flask-SocketIO 5.3.6
- Python-SocketIO 5.9.0
- Python-EngineIO 4.7.1

## Usage

### Host Interface
1. Access `/host` endpoint
2. Monitor all tables
3. Process for awarding points:
   - Wait for tables to buzz in
   - Click "Check Answer" for the responding table
   - Enter points (0-10)
   - Click "Award Points"
4. Use "Reset Buzzers" to start new round
5. Use "Reset Points" to clear all scores

### Participant Interface
1. Access root endpoint (`/`)
2. Select table number
3. Click "BUZZ!" when ready to answer
4. View current points and ranking

## Deployment

Currently deployed on PythonAnywhere. For deployment:

1. Create a PythonAnywhere account
2. Upload project files
3. Set up a web app with Flask
4. Configure WSGI file:
```python
import sys
path = '/home/yourusername/buzzer_app'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

## Project Structure

```
buzzer_app/
├── app.py              # Flask application and Socket.IO events
├── requirements.txt    # Project dependencies
├── README.md          # Documentation
└── templates/         # HTML templates
    ├── host.html     # Host interface
    └── index.html    # Participant interface
```

## Future Enhancements

- User authentication
- Persistent score tracking
- Multiple game modes
- Custom sound effects
- Advanced scoring mechanisms
- Volume controls

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

[Your chosen license]

## Author

[Your name]
