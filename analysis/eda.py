import numpy as np

def dataoveriew(df, message):
    print(f'{message}:\n')
    print('Number of rows: ', df.shape[0])
    print("\nNumber of features:", df.shape[1])
    print("\nData Features:")
    print(df.columns.tolist())
    print("\nMissing values:", df.isnull().sum().values.sum())
    print("\nUnique values:")
    print(df.nunique())

def calc_outlier_range_iqr(col, times_IQR=1.5):
    # Intervalo Interquartil
    # times_IQR - Define how many times IQR will used to calc Lower and Upper Range
    sorted(col)                              # Sorted series object
    Q1,Q3 = np.percentile(col,[25,75])       # Calc Q1 and Q3
    IQR = Q3-Q1                              # Calc the distance between Q3 and Q1
    lr= Q1-(times_IQR * IQR)                 # Calc Lower Range
    ur= Q3+(times_IQR * IQR)                 # Calc Upper Range
    return lr, ur