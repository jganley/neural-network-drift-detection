
# Automatic Neural Network Drift Detection

This repository contains a short research paper that investigates cheap frame filtering techniques to predict model drift in neural network models. This project was completed as part of UCLA's ML-driven Video Analytics Systems class in Winter 2020. The abstract is provided below.

## Abstract

> Widespread deployment of video cameras has fueled the growth in research into efficient video analytics systems. Many of these systems involve the use of specialized neural networks which are trained on the data coming from a specific video feed. One of the primary limitations of these systems is that the video feed can change, leaving the specialized model ill-equipped to make predictions. This paper proposes and motivates further research into systems that can cheaply track model drift and indicate when the specialized neural network needs to be retrained.

## Code

The code to train and test the Tiny-YOLO model was based on a tutorial by [The AI Guy](https://youtu.be/10joRJt39Ns) on YouTube. His [GitHub repository](https://github.com/theAIGuysCode/YOLOv3-Cloud-Tutorial) contains the example Google Colab notebooks from which my notebooks are based.

#### Run YOLOv3 Jupyter Notebook

This script allows the user to run a pre-trained YOLOv3 model to label objects in video frames. These labels will serve as a ground truth value for the specialized TinyYOLO model.

#### Train TinyYOLO Jupyter Notebook

This script takes the images labeled by the YOLOv3 model and uses them to train a specialized TinyYOLO model. TinyYOLO models have a much smaller architecture than full YOLOv3 models which allows them to run much faster, even on edge devices with limited compute power.

#### Test Tiny YOLO Jupyter Notebook

This script takes the specialized TinyYOLO model trained by the last script and uses it to make predictions on new input frames. We can then take these results and compare them to the ground truth labels produced by the full YOLOv3 model.
