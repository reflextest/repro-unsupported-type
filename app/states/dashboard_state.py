import reflex as rx
from typing import TypedDict
from datetime import datetime
from sqlalchemy import text


class OrderData(TypedDict):
    order_id: int
    order_date: str
    customer_name: str
    product_name: str
    quantity: int
    price: float
    total: float


class CategoryData(TypedDict):
    category: str
    total_sales: float
    order_count: int


class RevenueData(TypedDict):
    date: str
    revenue: float


class DashboardState(rx.State):
    orders: list[OrderData] = []
    revenue_trend: list[RevenueData] = []
    category_stats: list[CategoryData] = []
    total_orders: int = 0
    total_revenue: float = 0
    total_customers: int = 0
    loading: bool = True
    start_date: str = ""
    end_date: str = ""

    @rx.event(background=True)
    async def load_dashboard_data(self):
        self.loading = True
        await self.fetch_total_stats()
        await self.fetch_orders()
        await self.fetch_revenue_trend()
        await self.fetch_category_stats()
        async with self:
            self.loading = False

    @rx.event(background=True)
    async def fetch_total_stats(self):
        async with rx.asession() as session:
            result = await session.execute(
                text(
                    "\n                SELECT \n                    COUNT(DISTINCT o.orderid) as total_orders,\n                    COUNT(DISTINCT o.customerid) as total_customers,\n                    SUM(od.quantity * p.price) as total_revenue\n                FROM orders o\n                JOIN orderdetails od ON o.orderid = od.orderid\n                JOIN products p ON od.productid = p.productid\n                "
                )
            )
            row = result.first()
            if row:
                async with self:
                    self.total_orders = row[0]
                    self.total_customers = row[1]
                    self.total_revenue = float(
                        row[2] if row[2] else 0
                    )

    @rx.event(background=True)
    async def fetch_orders(self):
        async with rx.asession() as session:
            result = await session.execute(
                text(
                    "\n                SELECT \n                    o.orderid,\n                    o.orderdate,\n                    c.customername,\n                    p.productname,\n                    od.quantity,\n                    p.price,\n                    (od.quantity * p.price) as total\n                FROM orders o\n                JOIN customers c ON o.customerid = c.customerid\n                JOIN orderdetails od ON o.orderid = od.orderid\n                JOIN products p ON od.productid = p.productid\n                ORDER BY o.orderdate DESC\n                LIMIT 10\n                "
                )
            )
            rows = result.all()
            async with self:
                self.orders = [
                    {
                        "order_id": row[0],
                        "order_date": row[1].strftime(
                            "%Y-%m-%d"
                        ),
                        "customer_name": row[2],
                        "product_name": row[3],
                        "quantity": row[4],
                        "price": float(row[5]),
                        "total": float(row[6]),
                    }
                    for row in rows
                ]

    @rx.event(background=True)
    async def fetch_revenue_trend(self):
        async with rx.asession() as session:
            result = await session.execute(
                text(
                    "\n                SELECT \n                    DATE(o.orderdate) as date,\n                    SUM(od.quantity * p.price) as revenue\n                FROM orders o\n                JOIN orderdetails od ON o.orderid = od.orderid\n                JOIN products p ON od.productid = p.productid\n                GROUP BY DATE(o.orderdate)\n                ORDER BY date DESC\n                LIMIT 7\n                "
                )
            )
            rows = result.all()
            async with self:
                self.revenue_trend = [
                    {
                        "date": row[0].strftime("%Y-%m-%d"),
                        "revenue": float(row[1]),
                    }
                    for row in rows
                ]

    @rx.event(background=True)
    async def fetch_category_stats(self):
        async with rx.asession() as session:
            result = await session.execute(
                text(
                    "\n                SELECT \n                    c.categoryname as category,\n                    SUM(od.quantity * p.price) as total_sales,\n                    COUNT(DISTINCT o.orderid) as order_count\n                FROM categories c\n                JOIN products p ON c.categoryid = p.categoryid\n                JOIN orderdetails od ON p.productid = od.productid\n                JOIN orders o ON od.orderid = o.orderid\n                GROUP BY c.categoryname\n                "
                )
            )
            rows = result.all()
            async with self:
                self.category_stats = [
                    {
                        "category": row[0],
                        "total_sales": float(row[1]),
                        "order_count": row[2],
                    }
                    for row in rows
                ]