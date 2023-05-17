# Importing packages
from transformers import pipeline
import pandas as pd
import os
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


def pipeline_setup():
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        return_all_scores=False) # Only return the most likely label
    return classifier

def load_data():
    filename = os.path.join(os.getcwd(), "data", "fake_or_real_news.csv") # load the data
    data = pd.read_csv(filename, index_col=0)
    # data = data[0:20] ### TESTING ONLY, REMOVE THIS LINE
    return data

def perform_emotion_classification(data, classifier):
    emotion_classification = []
    count = 0
    
    print("[INFO]: Starting emotion classification of headlines...")

    for headline in data["title"]:
        headline_data = classifier(headline)
        headline_emotion = headline_data[0]["label"]
        emotion_classification.append(headline_emotion)
        count += 1
        print("[INFO]: Done with headline " + str(count) + " of " + str(len(data["title"])))
    
    # Add the emotion classification to the data
    data["emotion"] = emotion_classification

def plot_data(data):
    # Define list of emotions for ordering
    emotions = data["emotion"].unique().tolist()

    # Making plot with all data
    all_data_plot = sns.countplot(x="emotion", data=data, order = emotions)
    all_data_plot.set_title("Distribution of emotions in all news headlines")
    all_data_plot.set_xlabel("Emotion")
    all_data_plot.set_ylabel("Count")
    all_data_fig = all_data_plot.get_figure()
    all_data_fig.savefig(os.path.join(os.getcwd(), "plots", "all_data_plot.png"))
    all_data_fig.clf()

    # Plot with real news only
    separated_plot = sns.countplot(x="emotion", data=data, order = emotions, hue = "label")
    separated_plot.set_title("Distribution of emotions in real versus fake headlines")
    separated_plot.set_xlabel("Emotion")
    separated_plot.set_ylabel("Count")
    separated_fig = separated_plot.get_figure()
    separated_fig.savefig(os.path.join(os.getcwd(), "plots", "separated_plot.png"))
    separated_fig.clf()

def main(): # This is the main function that runs the program.
    classifier = pipeline_setup()
    data = load_data()
    perform_emotion_classification(data, classifier)
    print("[INFO]: Done with emotion classification of headlines.")
    plot_data(data)
    print("[INFO]: Plots saved to folder.")
    
if __name__ == "__main__":
    main()