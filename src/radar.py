import plotly.graph_objects as go

def radar_chart(title: str, scores: dict):
    labels = list(scores.keys())
    values = list(scores.values())
    labels_closed = labels + [labels[0]]
    values_closed = values + [values[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=values_closed, theta=labels_closed, fill="toself"))
    fig.update_layout(
        title=title,
        polar=dict(radialaxis=dict(visible=True, range=[1, 5], dtick=1)),
        showlegend=False,
        margin=dict(l=30, r=30, t=50, b=30),
    )
    return fig
