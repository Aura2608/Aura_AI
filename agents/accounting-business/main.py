#!/usr/bin/env python3
"""
Main Agent Orchestrator
Runs all agents in sequence or parallel
"""

import os
import sys
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv

from agent_product_generator import AccountingProductGenerator
from agent_gumroad_manager import GumroadManager
from agent_social_promoter import SocialPromoter
from agent_income_tracker import IncomeTracker

load_dotenv()


class AgentOrchestrator:
    """
    Orchestrates all agents to run the accounting business.
    """
    
    def __init__(self):
        print("🚀 Initializing Agent System...")
        
        try:
            self.product_generator = AccountingProductGenerator()
            self.gumroad_manager = GumroadManager()
            self.social_promoter = SocialPromoter()
            self.income_tracker = IncomeTracker()
            
            print("✅ All agents initialized")
        except Exception as e:
            print(f"❌ Error initializing agents: {e}")
            sys.exit(1)
    
    def daily_routine(self):
        """
        Run the complete daily routine.
        """
        print(f"\n{'='*60}")
        print(f"🌅 Daily Routine - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        try:
            # Step 1: Generate product
            print(f"\n[1/4] Generating product...")
            product = self.product_generator.generate_daily_product()
            self.product_generator.save_product(product)
            print(f"✅ Generated: {product['name']} (£{product['price']})")
            
            # Step 2: Upload to Gumroad
            print(f"\n[2/4] Uploading to Gumroad...")
            gumroad_result = self.gumroad_manager.upload_product(product)
            gumroad_url = gumroad_result.get('url', f"https://gumroad.com/l/{product['id']}")
            print(f"✅ Uploaded: {gumroad_url}")
            
            # Step 3: Promote on social media
            print(f"\n[3/4] Promoting on social media...")
            promotion_results = self.social_promoter.promote_product(product, gumroad_url)
            print(f"✅ Promoted:")
            print(f"   Reddit: {promotion_results['platforms']['reddit']['posts_created']} posts")
            print(f"   Twitter: {promotion_results['platforms']['twitter']['tweets_created']} tweets")
            print(f"   Facebook: {promotion_results['platforms']['facebook']['posts_created']} posts")
            
            # Step 4: Check income
            print(f"\n[4/4] Checking income...")
            daily_report = self.income_tracker.generate_daily_report()
            print(f"✅ Income Report:")
            print(f"   Today: £{daily_report['day_revenue']:.2f}")
            print(f"   This week: £{daily_report['week_revenue']:.2f}")
            print(f"   This month: £{daily_report['month_revenue']:.2f}")
            
            print(f"\n{'='*60}")
            print(f"✨ Daily routine completed successfully!")
            print(f"{'='*60}")
            
            return True
        
        except Exception as e:
            print(f"\n❌ Error in daily routine: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def weekly_routine(self):
        """
        Run weekly reporting and optimization.
        """
        print(f"\n{'='*60}")
        print(f"📊 Weekly Routine - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        self.income_tracker.generate_weekly_report()
    
    def monthly_routine(self):
        """
        Run monthly reporting and strategy review.
        """
        print(f"\n{'='*60}")
        print(f"📈 Monthly Routine - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        self.income_tracker.generate_monthly_report()
    
    def schedule_agents(self):
        """
        Schedule agents to run on regular intervals.
        """
        print(f"\n⏰ Scheduling agents...")
        
        # Daily routine at 9am
        schedule.every().day.at("09:00").do(self.daily_routine)
        print(f"✓ Daily routine scheduled for 09:00")
        
        # Weekly routine on Monday at 10am
        schedule.every().monday.at("10:00").do(self.weekly_routine)
        print(f"✓ Weekly routine scheduled for Mondays 10:00")
        
        # Monthly routine on 1st of month at 10am
        schedule.every().day.do(self._check_monthly)
        print(f"✓ Monthly routine scheduled for 1st of month")
    
    def _check_monthly(self):
        """
        Check if it's the first day of month and run monthly routine.
        """
        if datetime.now().day == 1:
            self.monthly_routine()
    
    def run_once(self):
        """
        Run the system once (for testing).
        """
        print(f"\n🎯 Running agent system (one cycle)...")
        self.daily_routine()
    
    def run_continuous(self):
        """
        Run the system continuously with scheduled tasks.
        """
        print(f"\n🚀 Starting continuous agent system...")
        print(f"   Agents will run on schedule")
        print(f"   Press Ctrl+C to stop\n")
        
        self.schedule_agents()
        
        # Run immediately for testing
        print(f"Running initial cycle...")
        self.daily_routine()
        
        # Then keep running scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute


if __name__ == "__main__":
    print(f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     🎯 UK Accounting Agent Business System               ║
    ║     Fully Automated Monthly Income Generator             ║
    ║                                                           ║
    ║     Creates products, uploads, promotes, tracks income   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    orchestrator = AgentOrchestrator()
    
    # Run once for demonstration
    orchestrator.run_once()
    
    # Uncomment to run continuously:
    # orchestrator.run_continuous()
