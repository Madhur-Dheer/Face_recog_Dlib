
# Face Recognition use Dlib Feature Extraction


##Overview

The first part of the project uses dlib to extract a 128 feature-vector-array for every face that is avaialable in the image.
We created a face recognition csv using this method for around 10,000 people .

The second part of the project uses machine learning algorithm to create a classifier and store the results in a pickle file.The algorithm used is KNN(k_nearest neighbor) algorithm for classification purposes.

The third part of the project is to use flask to create a iteractive web-based gui for face-recgonition algorthim to work. 


# How to Run

1. Run Python_dlib.py : This will help in creating a feature.csv file to store the 128 feature-vector array for every face in the image.
2. Run ml_classify.py : It uses KNN algorithm to create a classiflier based in the feature.csv dataset . The results are store as a pickle modle for further use
3. Run basic1.py: It will give a http link through which a flask based gui can be accessed. Upload the image of user whose face should be detected. Press on the KNN button to analyze the results



 
