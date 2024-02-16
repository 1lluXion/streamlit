#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:16:50 2023

@author: markwin
"""

import streamlit as st

st.title("Welocme to BMI calculator")

#Input

weight = st.number_input("Enter your weight in KG", step = 0.1)

height = st.number_input("Enter your height in Meters", step = 0.01)

def calculate_bmi():
    bmi = weight/(height)**2
    bmi_thresholds = [18.5, 23, 27.5]
    level_labels = ['Risk of nutritional deficiency','Low Risk','Moderate Risk','High Risk']
    if bmi <= bmi_thresholds[0]:
        level = level_labels[0]
    elif bmi <= bmi_thresholds[1]:
        level = level_labels[1]
    elif bmi <= bmi_thresholds[2]:
        level = level_labels[2]
    else:
        level = level_labels[3]
    st. success(f"Your BMI is {bmi}. You are at {level}")

button = st.button("Calculate BMI")
if button:
    calculate_bmi()
