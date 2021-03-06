import numpy as np
import statsmodels.api as sm
import pandas

#data = pandas.read_csv("tumor_size.csv").as_matrix()

def logistic_regression(data):
  '''takes a pandas dataframe, and regresses columns 2-n against column 1, producing a binary classifier
  returns a statsmodels fitted model'''
  dependents = np.float64(data[:,0])
  independents = np.float64(data[:,range(1,data.shape[1])])
  logit_model = sm.Logit(dependents,independents)
  fitted_model = logit_model.fit(disp=0)
  return fitted_model
