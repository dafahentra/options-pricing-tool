import numpy as np
from scipy.stats import norm 
import streamlit as st

@st.cache_data
def black_scholes(S, K, T, r, sigma, option_type='call'):
    """Cached Black-Scholes calculation"""
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

@st.cache_data
def calculate_greeks(S, K, T, r, sigma, option_type='call'):
    """Cached Greeks calculation"""
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    delta = norm.cdf(d1) if option_type == 'call' else norm.cdf(d1) - 1
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    
    theta_calc = -S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
    if option_type == 'call':
        theta = (theta_calc - r * K * np.exp(-r * T) * norm.cdf(d1 - sigma * np.sqrt(T))) / 365
    else:
        theta = (theta_calc + r * K * np.exp(-r * T) * norm.cdf(-(d1 - sigma * np.sqrt(T)))) / 365
    
    vega = S * norm.pdf(d1) * np.sqrt(T) / 100
    
    return {'Delta': delta, 'Gamma': gamma, 'Theta': theta, 'Vega': vega}

@st.cache_data
def get_price_range(S, factor=0.5):
    """Generate price range for charts"""
    return np.linspace(S * (1 - factor), S * (1 + factor), 100)

def option_payoff(S_range, K, option_type='call'):
    """Calculate option payoff"""
    return np.maximum(S_range - K, 0) if option_type == 'call' else np.maximum(K - S_range, 0)

def strategy_payoff(S_range, positions):
    """Calculate strategy payoff"""
    total_payoff = np.zeros_like(S_range)
    total_cost = 0
    
    for pos in positions:
        payoff_vals = option_payoff(S_range, pos['strike'], pos['type'])
        multiplier = pos['quantity'] * (1 if pos['action'] == 'buy' else -1)
        total_payoff += multiplier * payoff_vals
        total_cost += multiplier * pos['premium']
    
    return total_payoff - total_cost

@st.cache_data
def monte_carlo_option(S, K, T, r, sigma, simulations, option_type='call'):
    """Cached Monte Carlo calculation"""
    Z = np.random.standard_normal(simulations)
    S_T = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)
    
    payoffs = option_payoff(S_T, K, option_type)
    return np.exp(-r * T) * np.mean(payoffs), S_T