import reflex as rx
from app.components.stats_cards import stats_cards
from app.components.revenue_chart import revenue_chart
from app.components.category_chart import category_chart
from app.components.orders_table import orders_table
from app.states.dashboard_state import DashboardState


def index() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Sales Dashboard",
                class_name="text-3xl font-bold text-gray-800 mb-8",
            ),
            stats_cards(),
            rx.el.div(
                rx.el.div(
                    revenue_chart(),
                    class_name="w-full lg:w-2/3",
                ),
                rx.el.div(
                    category_chart(),
                    class_name="w-full lg:w-1/3",
                ),
                class_name="flex flex-col lg:flex-row gap-6",
            ),
            orders_table(),
            class_name="max-w-7xl mx-auto px-4 py-8",
            on_mount=DashboardState.load_dashboard_data,
        ),
        class_name="min-h-screen bg-gray-50",
    )


app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index)