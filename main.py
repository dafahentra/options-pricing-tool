import streamlit as st
import numpy as np
from models import black_scholes, monte_carlo_option, calculate_greeks, option_payoff, strategy_payoff, get_price_range
from chart_utils import create_payoff_chart, create_strategy_chart, create_histogram_chart

st.set_page_config(page_title="Options Pricing & Analysis", layout="wide")

# Info tooltips
TOOLTIPS = {
    'bs': "The Black-Scholes Model calculates theoretical option prices using current stock price, strike price, time to expiration, volatility, and risk-free rate.",
    'greeks': "**Greeks** measure option price sensitivities:\n- **Delta**: Price change per $1 stock move\n- **Gamma**: Delta change per $1 stock move\n- **Theta**: Price decay per day\n- **Vega**: Price change per 1% volatility change",
    'mc': "Monte Carlo simulation estimates option prices by simulating thousands of possible future stock price paths.",
    'risk': "**VaR (Value at Risk)**: Maximum expected loss at 95% confidence level\n**ES (Expected Shortfall)**: Average loss when VaR threshold is exceeded"
}

def info_header(title, tooltip_key):
    """Create header with info popover"""
    c1, c2 = st.columns([10, 1])
    c1.subheader(title)
    with c2.popover(":material/info:"):
        st.markdown(TOOLTIPS[tooltip_key])

# App Title
st.title("Options Pricing and Risk Assessment Tool")
with st.expander("About This Tool"):
    st.caption("Options Pricing Tool with Greeks calculation, payoff diagrams, and strategy analysis.")

# Sidebar Parameters
st.sidebar.header("Option Parameters")
params = {
    'S': st.sidebar.number_input("Current Stock Price (S)", min_value=0.0, value=100.0),
    'K': st.sidebar.number_input("Strike Price (K)", min_value=0.0, value=100.0),
    'T': st.sidebar.number_input("Time to Maturity (T, in years)", min_value=0.01, value=1.0),
    'r': st.sidebar.number_input("Risk-Free Rate (r)", min_value=0.0, value=0.05, step=0.01),
    'sigma': st.sidebar.number_input("Volatility (σ)", min_value=0.01, value=0.2, step=0.01),
    'option_type': st.sidebar.selectbox("Option Type", ["call", "put"]),
    'simulations': st.sidebar.slider("Monte Carlo Simulations", 1000, 50000, 10000)
}

# Calculate core values
bs_price = black_scholes(**{k: v for k, v in params.items() if k != 'simulations'})
greeks = calculate_greeks(**{k: v for k, v in params.items() if k != 'simulations'})
mc_price, S_T = monte_carlo_option(**params)

# Black-Scholes Pricing
with st.container(border=True):
    info_header("Black-Scholes Pricing", 'bs')
    st.write(f"The {params['option_type'].capitalize()} option price: **${bs_price:.2f}**")

# Option Greeks
with st.container(border=True):
    info_header("Option Greeks", 'greeks')
    cols = st.columns(4)
    greek_names = ['Delta', 'Gamma', 'Theta', 'Vega']
    for col, greek in zip(cols, greek_names):
        with col:
            st.metric(greek, f"{greeks[greek]:.3f}" if greek != 'Gamma' else f"{greeks[greek]:.4f}")

# Monte Carlo Simulation
with st.container(border=True):
    info_header("Monte Carlo Simulation", 'mc')
    st.write(f"The {params['option_type'].capitalize()} option price: **${mc_price:.2f}**")

# Payoff Diagram
with st.container(border=True):
    st.subheader("Option Payoff Diagram")
    S_range = get_price_range(params['S'])
    payoff = option_payoff(S_range, params['K'], params['option_type'])
    profit_loss = payoff - bs_price
    
    fig = create_payoff_chart(S_range, payoff, profit_loss, params['S'], params['option_type'])
    st.plotly_chart(fig, use_container_width=True)

# Strategy Builder
with st.container(border=True):
    st.subheader("Option Strategy Builder")
    
    col1, col2 = st.columns(2)
    with col1:
        strategy = st.selectbox("Select Strategy", ["Covered Call", "Protective Put"])
    with col2:
        contracts = st.number_input("Number of Contracts", min_value=1, value=1)
    
    # Strategy logic
    if strategy == "Covered Call":
        strike = st.number_input("Call Strike Price", value=params['K'] + 5)
        premium = black_scholes(params['S'], strike, params['T'], params['r'], params['sigma'], 'call')
        positions = [{'type': 'call', 'strike': strike, 'action': 'sell', 'quantity': contracts, 'premium': premium}]
        st.write(f"**Call Premium Received**: ${premium:.2f} per share")
    else:
        strike = st.number_input("Put Strike Price", value=params['K'] - 5)
        premium = black_scholes(params['S'], strike, params['T'], params['r'], params['sigma'], 'put')
        positions = [{'type': 'put', 'strike': strike, 'action': 'buy', 'quantity': contracts, 'premium': premium}]
        st.write(f"**Put Premium Paid**: ${premium:.2f} per share")
    
    # Calculate and plot strategy
    stock_pl = (S_range - params['S']) * contracts * 100
    option_pl = strategy_payoff(S_range, positions) * 100
    total_pl = stock_pl + option_pl
    
    fig_strategy = create_strategy_chart(S_range, total_pl, params['S'], strategy)
    st.plotly_chart(fig_strategy, use_container_width=True)

# Price Distribution
with st.container(border=True):
    st.subheader("Price Distribution")
    fig_hist = create_histogram_chart(S_T, "Simulated Asset Prices")
    st.plotly_chart(fig_hist, use_container_width=True)

# Risk Assessment
with st.container(border=True):
    info_header("Risk Metrics", 'risk')
    VaR_95 = np.percentile(S_T, 5)
    ES_95 = S_T[S_T <= VaR_95].mean()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("VaR (95%)", f"${VaR_95:.2f}")
    with col2:
        st.metric("Expected Shortfall", f"${ES_95:.2f}")