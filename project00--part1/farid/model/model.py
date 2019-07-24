from keras.models import Sequential
from keras.layers.core import Dense

def creat_mlp(dim,regress=False):
	model = Sequential()
	model.add(Dense(8,inpute_dim=dim,activation='relu'))
	model.add(Dense(4,activation='relu'))

	if regress:
		model.add(Dense(1,activation='relu'))
		return model