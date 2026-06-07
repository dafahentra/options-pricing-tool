# Options Pricing & Risk Analysis Tool

An institutional-grade web application for options pricing and risk assessment. This tool implements established quantitative models, including Black-Scholes and Monte Carlo simulations, to provide comprehensive options analysis and strategy building.

Designed for quantitative analysts, traders, and finance students who require a robust, transparent, and high-performance options pricing framework.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![Framework](https://img.shields.io/badge/streamlit-framework-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Why Fork This Project?

- **Transparent Implementation**: Direct Python implementations of Black-Scholes and Monte Carlo mathematical models without obfuscation.
- **Advanced Risk Metrics**: Built-in calculations for Option Greeks (Delta, Gamma, Theta, Vega) alongside Value at Risk (VaR) and Expected Shortfall (ES).
- **Strategy Builder**: Interactive visualization for complex positions like Covered Calls and Protective Puts.
- **High Performance**: Optimized with vectorized NumPy operations and intelligent caching for real-time interactivity.

## Core Capabilities

- **Stochastic Modeling**: Monte Carlo simulations for price path modeling and distribution analysis.
- **Theoretical Pricing**: Instant European options pricing using the Black-Scholes formula.
- **Interactive Visualizations**: Real-time Plotly charts for payoff diagrams and price distributions.
- **Extensible Architecture**: Clean separation between mathematical models (`models.py`) and visualization logic (`chart_utils.py`).

## Quick Start

### Requirements

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/dafahentra/options-pricing-tool.git
cd options-pricing-tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the application:
```bash
streamlit run main.py
```

Navigate to `http://localhost:8501` in your browser.

## Project Structure

```text
options-pricing-tool/
├── main.py              # Application entry point and UI layout
├── models.py            # Quantitative models and risk calculations
├── chart_utils.py       # Chart creation and styling utilities
├── requirements.txt     # Dependency specifications
├── .streamlit/          # Configuration and application theming
│   └── config.toml
└── README.md            # Project documentation
```

## Methodology

### Mathematical Models

- **Black-Scholes**: Standard theoretical pricing for European Call and Put options.
- **Monte Carlo**: Stochastic price simulations based on Geometric Brownian Motion (GBM).
- **Greeks**: First and second-order derivatives of the option value with respect to underlying parameters.

## Contributing

We welcome contributions from the quantitative finance and developer community.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AdvancedPricingModel`)
3. Commit your Changes (`git commit -m 'Add AdvancedPricingModel'`)
4. Push to the Branch (`git push origin feature/AdvancedPricingModel`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This software is provided for educational and research purposes only. It does not constitute financial advice. Always perform your own due diligence before making trading or investment decisions.