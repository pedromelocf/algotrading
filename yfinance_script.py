#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:59:51 2023

@author: pmelo-ca
"""
import yfinance as yf

data = yf.download('AAPL', start='2023-01-01', end='2023-01-31')
print(data)
