# Chest X-Ray Predictions using Machine Learning

## Folder Structure Explained

- ### Chest_Xray Folder - This is where all the python code to generate the model. Download this dataset into Data folder [Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia). Please run the python code first get the model_for_web folder put it in Backend Folder

- ### Backend Folder - This is where we put the generated model and create a localhost based or deployed in the web to publish the model in JSON. Use `npm install` to install all the dependencies and run the local server using `npm start`

  - #### Reason why we do at the time is Tensorflow JS receives model only from http protocol rather than file protocol

- ### Frontend Folder - This is where we created the folder using React JS to make a simplified web appication where we select the images and it will give the predictions

<br />
<br />

## Please click the link [Chest_Xray](https://chest-xray-chakara.web.app/) for my deployment online using Google Firebase

- ### Warning this app could take some time for loading the model from the web which is deployed in Heroku

- ### Please download images from this [Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) for testing.
