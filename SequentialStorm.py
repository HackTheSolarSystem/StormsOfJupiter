from __future__ import print_function
import numpy as np 
import pandas as pd
import math

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

def featureGeneration(data):
# Purpose: create distance feature / Input: initial dataframe / Output: dataframe with new distance feature

	col_list = list(data)
	data['centroid_x'] = data['East'] - data['West']
	data['centroid_y'] = data['North'] = data['South']
	# print(data['centroid_x'])
	# print(data)
	data['next_centroid_x'] = data['centroid_x'].diff()
	data['next_centroid_y'] = data['centroid_y'].diff()
	data.at[0, 'next_centroid_x'] = 0
	data.at[0, 'next_centroid_y'] = 0

	data['next_centroid_x_pow'] = data['next_centroid_x'].pow(2)
	data['next_centroid_y_pow'] = data['next_centroid_y'].pow(2)

	data['x_y_addition'] = data['next_centroid_x_pow'] + data['next_centroid_y_pow']
	data['distance_traveled'] = data['x_y_addition'].apply(np.sqrt)

	col_list.append('distance_traveled')

	return data.loc[:, data.columns.isin(col_list)]

def scaleData(data, scale):

	data = scale.fit_transform(data)

	return data

def splitTraining(data, scale):

	split_value = int(len(data) * 0.75)

	data_train_np = scaleData(data_with_features[0:split_value], scale)
	data_test_np = scaleData(data_with_features[split_value:len(data)], scale)

	return data_train_np[:, 0:4], data_train_np[:, 4], data_test_np[:, 0:4], data_test_np[:, 4] 


def reshapeFeatures(data_train_feature, data_test_feature):

	data_train_feature = np.reshape(data_train_feature, (data_train_feature.shape[0], data_train_feature.shape[1], 1))
	data_test_feature = np.reshape(data_test_feature, (data_test_feature.shape[0], data_test_feature.shape[1], 1))
	
	return data_train_feature, data_test_feature





if __name__ == '__main__':

	data = pd.read_csv("Storm1_Coordinates.csv")

	data_with_features = featureGeneration(data)

	scale = MinMaxScaler(feature_range = (0,1))

	data_train_feature, data_train_label, data_test_feature, data_test_label = splitTraining(data_with_features, scale)


	data_train_feature, data_test_feature = reshapeFeatures(data_train_feature, data_test_feature)

	model = Sequential()

	model.add(LSTM(units=5, return_sequences=True, input_shape=(data_train_feature.shape[1], 1))) 

	model.add(Dropout(0.2))  

	model.add(LSTM(units=5, return_sequences=True))  
	model.add(Dropout(0.2))

	model.add(LSTM(units=5, return_sequences=True))  
	model.add(Dropout(0.2))

	model.add(LSTM(units=5))  
	model.add(Dropout(0.2))  

	model.add(Dense(units = 1)) 
	model.compile(optimizer = 'adam', loss = 'mean_squared_error')  

	model.fit(data_train_feature, data_train_label, epochs = 100, batch_size = 5)  

	predictions = model.predict(data_test_feature)  

	print(predictions)


















