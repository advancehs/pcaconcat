#!/usr/bin/env python

"""Tests for `pcaconcat` package."""


import os
import pandas as pd 
from pcaconcat import pcaconcat







def test_pcaconcat( ):
    pwd_path = os.path.abspath(os.path.dirname(__file__))
    pca_path = os.path.join(pwd_path, 'aaa.xlsx')
    df = pd.read_excel(pca_path)
    print(df)
    df2 = pcaconcat(df,"city")
    print(df2)
    
