import reflex as rx
from app.states.dashboard_state import DashboardState


def stats_cards() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(
                [
                    (
                        "Total Orders",
                        DashboardState.total_orders,
                        "text-blue-600",
                    ),
                    (
                        "Total Revenue",
                        f"${DashboardState.total_revenue:,.2f}",
                        "text-green-600",
                    ),
                    (
                        "Total Customers",
                        DashboardState.total_customers,
                        "text-purple-600",
                    ),
                ],
                lambda x: rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            x[0],
                            class_name="text-gray-600 text-sm font-semibold mb-2",
                        ),
                        rx.el.p(
                            x[1],
                            class_name=f"text-2xl font-bold {x[2]}",
                        ),
                        class_name="p-6 bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-200",
                    ),
                    class_name="w-full",
                ),
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6",
        )
    )