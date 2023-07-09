# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 21:39:54 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('C:/Users/HP/OneDrive/Desktop/ML/trained_model.sav','rb'))
#creating a function for prediction
def breastcancer_prediction(input_data):
    #input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259)

# change the input data to a numpy array
   input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one datapoint
   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

   prediction = loaded_model.predict(input_data_reshaped)
   print(prediction)

   if (prediction[0] == 0):
      return 'The Breast cancer is Malignant'

   else:
      return 'The Breast Cancer is Benign'


def main():
    
   st.title('Breast cancer prediction Web App')
    
    #getting thr input data from the user
  
    
   mean_radius = st.text_input('mean_radius')
   mean_texture= st.text_input('mean texture')
   mean_perimeter = st.text_input('mean perimeter')
   mean_area = st.text_input('mean area')
   mean_smoothness = st.text_input('mean smoothness')
   mean_compactness = st.text_input('mean compactness')
   mean_concavity = st.text_input('mean concavity')
   mean_concavepoints = st.text_input('mean_concavepoints')
   mean_symmetry = st.text_input('mean_symmetry')
   mean_fractal_dimension = st.text_input('mean_fractal_dimension')
   worst_radius = st.text_input('worst_radius')
   worst_texture = st.text_input('worst_texture')
   worst_perimeter = st.text_input('worst_perimeter')
   worst_area = st.text_input('worst_area')
   worst_smoothness = st.text_input('worst_smoothness')
   worst_compactness = st.text_input('worst_compactness')
   worst_concavity = st.text_input('worst_concavity')
   worst_concave_points = st.text_input('worst_concave_points')
   worst_symmetry	 = st.text_input('worst_symmetry	')
   worst_fractal_dimension = st.text_input('worst_fractal_dimension')
   
   # code for Prediction
   diagnosis = ''
    
    # creating a button for Prediction
    
   if st.button('Breast_cancer Test Result'):#can be any name of button
        diagnosis = breastcancer_prediction([mean_radius,mean_texture,	mean_perimeter,	mean_area	,mean_smoothness,	mean_compactness,	mean_concavity	,mean_concavepoints,	mean_symmetry,	mean_fractal_dimension,	worst_radius,	worst_texture,	worst_perimeter,	worst_area
   , worst_smoothness	,worst_compactness,	worst_concavity	,worst_concave_points,	worst_symmetry	,worst_fractal_dimension])
        
        
   st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    