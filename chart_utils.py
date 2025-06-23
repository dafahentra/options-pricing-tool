import plotly.graph_objects as go

# Chart configuration
CHART_CONFIG = {
    'primary_color': '#c584f7',
    'secondary_color': '#ff6b6b', 
    'accent_color': '#4ecdc4',
    'grid_color': '#666666',
    'bg_color': '#1a1a1a',
    'font_color': '#ffffff'
}

def get_chart_layout(title, xaxis_title, yaxis_title):
    """Standard chart layout template"""
    return {
        'title': title,
        'xaxis_title': xaxis_title,
        'yaxis_title': yaxis_title,
        'plot_bgcolor': CHART_CONFIG['bg_color'],
        'paper_bgcolor': CHART_CONFIG['bg_color'],
        'font_color': CHART_CONFIG['font_color'],
        'hovermode': 'x unified',
        'showlegend': False
    }

def create_payoff_chart(S_range, payoff, profit_loss, current_price, option_type):
    """Create standardized payoff chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=S_range, y=payoff, 
        name="Payoff at Expiration",
        line=dict(color=CHART_CONFIG['primary_color'], width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=S_range, y=profit_loss,
        name="Profit/Loss", 
        line=dict(color=CHART_CONFIG['secondary_color'], width=2)
    ))
    
    fig.add_hline(y=0, line_dash="dash", line_color=CHART_CONFIG['grid_color'])
    fig.add_vline(x=current_price, line_dash="dot", line_color=CHART_CONFIG['accent_color'], 
                  annotation_text="Current Price")
    
    fig.update_layout(**get_chart_layout(
        f"{option_type.capitalize()} Option Payoff Diagram",
        "Stock Price", "Payoff ($)"
    ))
    
    return fig

def create_strategy_chart(S_range, total_pl, current_price, strategy):
    """Create standardized strategy chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=S_range, y=total_pl,
        name=f"{strategy} P&L",
        line=dict(color=CHART_CONFIG['primary_color'], width=4)
    ))
    
    fig.add_hline(y=0, line_dash="dash", line_color=CHART_CONFIG['grid_color'])
    fig.add_vline(x=current_price, line_dash="dot", line_color=CHART_CONFIG['accent_color'],
                  annotation_text="Current Price")
    
    fig.update_layout(**get_chart_layout(
        f"{strategy} Strategy Profit/Loss",
        "Stock Price at Expiration", "Profit/Loss ($)"
    ))
    
    return fig

def create_histogram_chart(data, title="Distribution"):
    """Create standardized histogram"""
    fig = go.Figure()
    
    fig.add_trace(go.Histogram(
        x=data, nbinsx=50,
        marker_color=CHART_CONFIG['primary_color'],
        marker_line_width=0,  # Remove outline
        opacity=0.8
    ))
    
    fig.update_layout(**get_chart_layout(
        title, "Price", "Frequency"
    ))
    fig.update_layout(bargap=0.05)
    
    return fig