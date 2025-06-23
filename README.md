# 📈 Options Pricing & Risk Analysis Tool

A comprehensive web application for options pricing and risk assessment using mathematical models and Monte Carlo simulations.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Features

### Core Pricing Models
- **Black-Scholes Model** - Theoretical European options pricing
- **Monte Carlo Simulation** - Stochastic price path modeling
- **Real-time Calculations** - Interactive parameter adjustments

### Advanced Analytics
- **Option Greeks** - Delta, Gamma, Theta, Vega sensitivity analysis
- **Payoff Diagrams** - Visual profit/loss at expiration
- **Risk Metrics** - Value at Risk (VaR) and Expected Shortfall (ES)

### Strategy Builder
- **Covered Call Strategy** - Long stock + Short call position
- **Protective Put Strategy** - Long stock + Long put position
- **Interactive Visualization** - Real-time P&L charts

### Enhanced UI/UX
- **Dark Theme** - Professional financial dashboard aesthetic
- **Interactive Charts** - Plotly-powered visualizations
- **Responsive Design** - Clean, intuitive interface
- **Educational Tooltips** - Mathematical explanations and formulas

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/options-pricing-tool.git
   cd options-pricing-tool
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📊 Usage

### Basic Options Pricing
1. Set option parameters in the sidebar:
   - Current stock price (S)
   - Strike price (K)
   - Time to maturity (T)
   - Risk-free rate (r)
   - Volatility (σ)
   - Option type (Call/Put)

2. View calculated prices using both Black-Scholes and Monte Carlo methods

### Greeks Analysis
Monitor option sensitivities:
- **Delta**: Price sensitivity to underlying asset
- **Gamma**: Delta sensitivity to underlying asset
- **Theta**: Time decay effect
- **Vega**: Volatility sensitivity

### Strategy Analysis
1. Select a strategy (Covered Call or Protective Put)
2. Set strike prices and contract quantities
3. Analyze profit/loss scenarios across different stock prices

### Risk Assessment
- **VaR (95%)**: Maximum expected loss at 95% confidence
- **Expected Shortfall**: Average loss beyond VaR threshold
- **Price Distribution**: Histogram of simulated future prices

## 🏗️ Project Structure

```
options-pricing-tool/
├── main.py              # Main Streamlit application
├── models.py            # Mathematical models and calculations
├── chart_utils.py       # Chart creation and styling utilities
├── requirements.txt     # Python dependencies
├── .streamlit/
│   └── config.toml     # Streamlit configuration and theming
├── README.md           # Project documentation
└── LICENSE             # MIT License
```

## 🧮 Mathematical Models

### Black-Scholes Formula

**Call Option:**
```
C = S₀ × N(d₁) - K × e^(-rT) × N(d₂)
```

**Put Option:**
```
P = K × e^(-rT) × N(-d₂) - S₀ × N(-d₁)
```

Where:
- `d₁ = [ln(S₀/K) + (r + σ²/2)T] / (σ√T)`
- `d₂ = d₁ - σ√T`

### Monte Carlo Simulation
```
S_T = S₀ × exp[(r - σ²/2)T + σ√T × Z]
```

Where `Z ~ N(0,1)` is a standard normal random variable.

## 🎨 Customization

### Theme Configuration
Modify `.streamlit/config.toml` to customize colors and appearance:

```toml
[theme]
base = "dark"
primaryColor = "#c584f7"
backgroundColor = "#1a1a1a"
secondaryBackgroundColor = "#2d2d2d"
textColor = "#ffffff"
font = "serif"
```

### Chart Styling
Update `chart_utils.py` to modify chart colors and layouts.

## 📈 Performance Features

- **Caching**: Expensive calculations cached with `@st.cache_data`
- **Optimized Computing**: Vectorized NumPy operations
- **Efficient UI**: Minimal re-renders and smart state management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [Black-Scholes Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
- [Monte Carlo Methods in Finance](https://en.wikipedia.org/wiki/Monte_Carlo_methods_in_finance)
- [Option Greeks](https://en.wikipedia.org/wiki/Greeks_(finance))
- [Streamlit Documentation](https://docs.streamlit.io/)

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please open an issue or reach out via GitHub.

---

⭐ **Star this repository if you find it helpful!**