import reflex as rx
from app.states.dashboard_state import DashboardState

TOOLTIP_PROPS = {
    "separator": ": ",
    "cursor": False,
    "is_animation_active": False,
    "label_style": {"fontWeight": "500"},
    "item_style": {
        "color": "currentColor",
        "display": "flex",
        "paddingBottom": "0px",
        "justifyContent": "space-between",
        "textTransform": "capitalize",
    },
    "content_style": {
        "borderRadius": "5px",
        "padding": "0.5rem",
        "backgroundColor": "white",
        "border": "1px solid #e2e8f0",
    },
}


def revenue_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Revenue Trend",
                class_name="text-xl font-bold mb-4",
            ),
            rx.recharts.line_chart(
                rx.recharts.graphing_tooltip(
                    **TOOLTIP_PROPS
                ),
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    class_name="opacity-25",
                ),
                rx.recharts.line(
                    data_key="revenue",
                    stroke="#2B79D1",
                    dot=False,
                    type_="natural",
                ),
                rx.recharts.x_axis(
                    data_key="date",
                    tick_line=False,
                    axis_line=False,
                    tick_size=10,
                    type_="category",
                ),
                rx.recharts.y_axis(
                    data_key="revenue",
                    tick_line=False,
                    axis_line=False,
                    tick_size=10,
                ),
                data=DashboardState.revenue_trend,
                width="100%",
                height=350,
                margin={"left": 20, "right": 20, "top": 25},
                class_name="[&_.recharts-tooltip-item-separator]:w-full",
            ),
            class_name="bg-white p-6 rounded-xl shadow-lg",
        ),
        class_name="mt-6",
    )