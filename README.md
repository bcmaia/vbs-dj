# HacktonSemcomp2023
## Corvus
## Participants
* Bernardo Maia Coelho
* Gustavo Wadas Lopes
* Pedro Guilherme Teixeira dos Reis
* Pedro Henrique Vilela do Nascimento

## Project Description

For our project at Hackton Semcomp 2023, we aimed to create a web application that functions as a personal DJ, with a particular focus on its ability to recommend songs based solely on the vibes of a given track, using Cohere's LLM tools.

The repository mentioned below played a pivotal role in aiding the recommendations of our application, serving as a significant source of data that could be utilized in preprocessing recommendations generated by Cohere's AI.

Repository Credits: [https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019/data](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019/data)

---

In this expanded version of the README, we will provide additional information and details about the project:

### Project Overview

Our project, named "Corvus," was developed as part of the Hackton Semcomp 2023 event. The primary goal of Corvus was to create a web application that could act as a personal DJ, offering music recommendations based on the mood and vibes of a user's current song. This innovative recommendation system was made possible through the use of Cohere's LLM (Language Model) tools, an intuitive and powerfull api

### Setup
To run the our application locally, make sure you have python3 installed and also install the following libraries:

```bash
pip install cohere
pip install random2
pip install fuzzywuzzy
pip install pandas
pip install streamlit
pip install numpy
pip install python-dotenv
pip install pytube
pip install pydub
pip install youtube-search-python
pip install ffmpeg-python
```

alternatively, you can install those libraries with:
```bash
pip install -r requirements.txt
```

To run the aplication, you can use either:
```bash
streamlib run main.py
```

or
```bash
python3 -m streamlib run main.py
```

### Project Details

Our application's core functionality involved the ability to recommend songs based on the emotional and stylistic characteristics of a given track. This was achieved by leveraging Cohere's LLM tools, which allowed us to analyze the textual descriptions and attributes of songs to determine their mood and vibe.

### Data Source

A crucial aspect of our project was the availability of an extensive dataset. We utilized the music dataset provided in the Kaggle repository. This dataset spans from 1950 to 2019 and contains a wealth of information about various songs, including their attributes, genres, and descriptions.

### How We Used the Data

We integrated the Kaggle dataset into our application to enhance the accuracy of our recommendations. By pre-processing the data and using it to train our recommendation model, we were able to provide users with highly tailored song suggestions that resonated with the mood of the music they were currently enjoying.

### Acknowledgments

We extend our appreciation to the creators and maintainers of the Kaggle dataset for their valuable contribution, which played a pivotal role in the success of our project. The dataset's detailed information greatly enriched the recommendations generated by our application.

For more details about the dataset, you can refer to the following link: [https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019/data](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019/data)

Corvus was a collaborative effort, and we are proud to have taken part in the Hackton Semcomp 2023 event. We believe that our project, with its unique music recommendation capabilities, has the potential to enhance the way people discover and enjoy music.