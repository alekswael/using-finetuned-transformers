# Create a virtual environment
python -m venv emotion_classification_venv

# Activate the virtual environment
source ./emotion_classification_venv/Scripts/activate

# Install requirements
python -m pip install --upgrade pip
python -m pip install -r ./requirements.txt

# deactivate
deactivate

#rm -rf emotion_classification_venv