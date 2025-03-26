import reflex as rx
from app.states.dashboard_state import DashboardState


def orders_table() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Recent Orders",
                class_name="text-xl font-bold mb-4",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.foreach(
                                [
                                    "Order ID",
                                    "Date",
                                    "Customer",
                                    "Product",
                                    "Quantity",
                                    "Price",
                                    "Total",
                                ],
                                lambda x: rx.el.th(
                                    x,
                                    class_name="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider",
                                ),
                            ),
                            class_name="bg-gray-50",
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(
                            DashboardState.orders,
                            lambda item: rx.el.tr(
                                rx.el.td(
                                    item["order_id"],
                                    class_name="px-4 py-3",
                                ),
                                rx.el.td(
                                    item["order_date"],
                                    class_name="px-4 py-3",
                                ),
                                rx.el.td(
                                    item["customer_name"],
                                    class_name="px-4 py-3",
                                ),
                                rx.el.td(
                                    item["product_name"],
                                    class_name="px-4 py-3",
                                ),
                                rx.el.td(
                                    item["quantity"],
                                    class_name="px-4 py-3",
                                ),
                                rx.el.td(
                                    f"${item['price']:,.2f}",
                                    class_name="px-4 py-3",
                                ),
                                rx.el.td(
                                    f"${item['total']:,.2f}",
                                    class_name="px-4 py-3 font-semibold text-blue-600",
                                ),
                                class_name="hover:bg-gray-50",
                            ),
                        ),
                        class_name="bg-white divide-y divide-gray-200",
                    ),
                    class_name="min-w-full divide-y divide-gray-200",
                ),
                class_name="overflow-x-auto",
            ),
            class_name="bg-white p-6 rounded-xl shadow-lg",
        ),
        class_name="mt-6",
    )