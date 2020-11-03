# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:15:03 2019

@author: 69709

This function calculates the accuracies for a prediction based on different metrics
"""

from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import pandas as pd

def mape_cal_lv7(df):
    '''
    This function compute the mean absolute percentage error for the predictions for lv7.
    
    :param y_predicted: prediction results
    :type y_predicted: nd array or dataframes
    :param y_actual: reference values or true values
    :type y_actual: nd array or dataframes

    :return: The mpe for each company_ptype combination.
    :rtype: ??
    
    example:
         
    '''
    #df['predict_error'] = (abs(df['forecast_hirachical'] - df['actual_sale']))/df['actual_sale']
    #df['DP_error'] = (abs(df['forecast_demand_planning'] - df['actual_sale']))/df['actual_sale']
    df_tmp = df[df['actual_sale'] == 0]
    mape_predict = np.mean((abs(df['forecast_hirachical'] - df['actual_sale']))/df['actual_sale'])
    mape_demandPlan = np.mean((abs(df['forecast_demand_planning'] - df['actual_sale']))/df['actual_sale'])
    return mape_predict,mape_demandPlan


def mpe_cal_lv7(y_predicted,y_actual):
    '''
    This function compute the mean percentage error (bias) for the predictions.
    
    :param y_predicted: prediction results
    :type y_predicted: nd array or dataframes
    :param y_actual: reference values or true values
    :type y_actual: nd array or dataframes

    :return: The mpe for each company_ptype combination.
    :rtype: ??
    
    example:
         
    '''
    mpe = sum(np.divide((y_predicted-y_actual),y_actual))
    return mpe

from sklearn.metrics import mean_squared_error
def predict_rmse( g,actual = 'actual_sale',predict = 'forecast_hirachical'):
    rmse = np.sqrt( mean_squared_error( g[actual], g[predict] ) )
    return rmse

def DP_rmse( g,actual = 'actual_sale',predict = 'forecast_demand_planning'):
    rmse = np.sqrt( mean_squared_error( g[actual], g[predict] ) )
    return rmse

def rmse_cal_lv7(df):
    '''
    This function compute the RMSE for the predictions.
    
    :param y_predicted: prediction results
    :type y_predicted: nd array or dataframes
    :param y_actual: reference values or true values
    :type y_actual: nd array or dataframes

    :return: The average MSE for the proposed methods.
    :rtype: float with 3 digits
    The average MSE for the SAP forecast.
    :rtype: float with 3 digits
    
    example:
         
    '''    
    rmse_predict = np.mean(df.groupby(['C','L7']).apply(predict_rmse).reset_index().iloc[:,2])
    rmse_demandPlan = np.mean(df.groupby(['C','L7']).apply(DP_rmse).reset_index().iloc[:,2])
    return round(rmse_predict,3),round(rmse_demandPlan,3)

def mAe_cal_lv7(df):
    '''
    This function compute the mean error for the predictions.
    
    :param df: dataframe contains the product level structure and the realized sales, predicted sales from SAP and hiraechical forecasting
    :type df:  dataframe

    :return: The mean error  for the proposed methods.
    :rtype: float with 3 digits
    The mean error for the SAP forecast.
    :rtype: float with 3 digits
    
    example:
    '''
    mae_predict = np.mean((df['forecast_hirachical'] - df['actual_sale']))
    mae_demandPlan = np.mean((abs(df['forecast_demand_planning'] - df['actual_sale'])))    
    return round(mae_predict,3),round(mae_demandPlan,3)

def mAse_cal_lv7(df):
    '''
    This function compute the mean absolute scaled error for the predictions.
    
    :param y_predicted: prediction results
    :type y_predicted: nd array or dataframes
    :param y_actual: reference values or true values
    :type y_actual: nd array or dataframes

    :return: The mean absolute error for the proposed methods.
    :rtype: float with 3 digits
    The mean absolute error for the SAP forecast.
    :rtype: float with 3 digits
    example:
         
    '''
    mase_predict = np.mean((abs(df['forecast_hirachical'] - df['actual_sale'])))
    mase_demandPlan = np.mean((abs(df['forecast_demand_planning'] - df['actual_sale'])))
    return round(mase_predict,3),round(mase_demandPlan,3)
