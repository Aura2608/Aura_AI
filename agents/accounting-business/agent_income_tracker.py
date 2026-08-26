#!/usr/bin/env python3
"""
Agent 4: Income Tracker
Monitors Gumroad sales and tracks income
"""

import os
import json
from typing import Dict
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()


class IncomeTracker:
    """
    Tracks income from Gumroad and bank deposits.
    """
    
    def __init__(self):
        self.gumroad_api_key = os.getenv("GUMROAD_API_KEY")
        self.stripe_api_key = os.getenv("STRIPE_API_KEY")
        self.sales_log = []
        self.income_log = []
    
    def check_gumroad_sales(self) -> Dict:
        """
        Check Gumroad for new sales.
        """
        print("\n💰 Checking Gumroad sales...")
        
        # In production, this would call Gumroad API
        # For now, simulate data
        
        sales = self._simulate_gumroad_sales()
        
        print(f"✓ Found {sales['new_sales']} new sales")
        print(f"  Revenue: £{sales['revenue_today']:.2f} today")
        print(f"  Total this month: £{sales['revenue_month']:.2f}")
        
        return sales
    
    def _simulate_gumroad_sales(self) -> Dict:
        """
        Simulate Gumroad sales data (for testing).
        """
        return {
            "new_sales": 3,
            "revenue_today": 27.00,  # 3 sales avg £9
            "revenue_week": 189.00,
            "revenue_month": 756.00,
            "top_products": [
                {"name": "UK Invoice Template", "sales": 15, "revenue": 135.00},
                {"name": "Expense Tracker", "sales": 12, "revenue": 132.00},
                {"name": "Tax Checklist", "sales": 10, "revenue": 80.00},
            ],
            "average_price": 12.60,
            "conversion_rate": 0.05,  # 5% of visitors buy
        }
    
    def generate_daily_report(self) -> Dict:
        """
        Generate daily income report.
        """
        sales = self.check_gumroad_sales()
        
        report = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "day_sales": sales["new_sales"],
            "day_revenue": sales["revenue_today"],
            "week_revenue": sales["revenue_week"],
            "month_revenue": sales["revenue_month"],
            "products": sales["top_products"],
            "status": "on_track" if sales["revenue_month"] > 500 else "building",
        }
        
        return report
    
    def generate_weekly_report(self) -> Dict:
        """
        Generate weekly income summary.
        """
        print("\n📊 Weekly Income Report")
        print("="*50)
        
        sales = self.check_gumroad_sales()
        
        # Project monthly if trend continues
        weekly_revenue = sales["revenue_week"]
        projected_monthly = weekly_revenue * 4.3
        
        report = {
            "week_revenue": weekly_revenue,
            "projected_monthly": projected_monthly,
            "products_sold": sum(p["sales"] for p in sales["top_products"]),
            "top_product": sales["top_products"][0],
            "status": "growing" if projected_monthly > 500 else "ramping_up",
            "insights": [
                f"Revenue this week: £{weekly_revenue:.2f}",
                f"Projected monthly: £{projected_monthly:.2f}",
                f"Average sale: £{sales['average_price']:.2f}",
                f"Top product: {sales['top_products'][0]['name']}",
            ]
        }
        
        for insight in report["insights"]:
            print(f"  • {insight}")
        
        return report
    
    def generate_monthly_report(self) -> Dict:
        """
        Generate monthly income summary.
        """
        print("\n📈 Monthly Income Report")
        print("="*50)
        
        sales = self.check_gumroad_sales()
        
        report = {
            "month_revenue": sales["revenue_month"],
            "products_created": 30,  # One per day
            "products_sold": sum(p["sales"] for p in sales["top_products"]),
            "total_customers": sales["revenue_month"] / sales["average_price"],
            "top_products": sales["top_products"],
            "metrics": {
                "average_daily": sales["revenue_month"] / 30,
                "average_product_revenue": sales["revenue_month"] / 30,
                "best_day_revenue": sales["revenue_month"] / 30 * 1.5,  # Estimate
            },
            "goals": {
                "target_next_month": sales["revenue_month"] * 1.5,
                "target_3_months": sales["revenue_month"] * 3,
            }
        }
        
        print(f"\nTotal Revenue: £{sales['revenue_month']:.2f}")
        print(f"Products Created: {report['products_created']}")
        print(f"Products Sold: {report['products_sold']}")
        print(f"Average Daily: £{report['metrics']['average_daily']:.2f}")
        print(f"\nNext Month Target: £{report['goals']['target_next_month']:.2f}")
        print(f"3-Month Target: £{report['goals']['target_3_months']:.2f}")
        
        return report
    
    def log_sale(self, product_name: str, price: float, customer_email: str = None):
        """
        Log a sale.
        """
        sale = {
            "product": product_name,
            "price": price,
            "customer": customer_email or "anonymous",
            "timestamp": datetime.now().isoformat(),
        }
        self.sales_log.append(sale)
    
    def get_income_statistics(self) -> Dict:
        """
        Get income statistics.
        """
        if not self.sales_log:
            return {"status": "no_data", "message": "No sales data yet"}
        
        total_sales = len(self.sales_log)
        total_revenue = sum(s["price"] for s in self.sales_log)
        
        return {
            "total_sales": total_sales,
            "total_revenue": total_revenue,
            "average_price": total_revenue / total_sales if total_sales > 0 else 0,
            "sales_log": self.sales_log,
        }


if __name__ == "__main__":
    print("💰 Income Tracker")
    print("="*50)
    
    tracker = IncomeTracker()
    
    # Generate reports
    daily = tracker.generate_daily_report()
    weekly = tracker.generate_weekly_report()
    monthly = tracker.generate_monthly_report()
    
    print(f"\n✅ Reports generated successfully")
