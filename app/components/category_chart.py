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


def category_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Sales by Category",
                class_name="text-xl font-bold mb-4",
            ),
            rx.recharts.pie_chart(
                rx.recharts.graphing_tooltip(
                    **TOOLTIP_PROPS
                ),
                rx.recharts.pie(
                    rx.foreach(
                        DashboardState.category_stats,
                        lambda _, index: rx.recharts.cell(
                            fill=rx.Var.create(
                                [
                                    "#2B79D1",
                                    "#2469B3",
                                    "#1E5AA1",
                                    "#3D8EE1",
                                    "#61A9E4",
                                ]
                            )[index]
                        ),
                    ),
                    data=DashboardState.category_stats,
                    data_key="total_sales",
                    name_key="category",
                    stroke="0",
                    label=True,
                ),
                width="100%",
                height=350,
                margin={"left": 20, "right": 20, "top": 25},
            ),
            class_name="bg-white p-6 rounded-xl shadow-lg",
        ),
        class_name="mt-6",
    )