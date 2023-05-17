# Create a virtual environment
python3 -m venv emotion_classification_venv

# Activate the virtual environment
source ./emotion_classification_venv/bin/activate

# Install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r ./requirements.txt

# deactivate
deactivate

#rm -rf emotion_classification_venv