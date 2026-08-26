#!/usr/bin/env python3
"""
Agent 1: UK Accounting Product Generator
Generates accounting guides, templates, and tools daily
"""

import os
import json
from datetime import datetime
from typing import Dict, List
import openai
from dotenv import load_dotenv

load_dotenv()


class AccountingProductGenerator:
    """
    Generates UK accounting products (guides, templates, spreadsheets)
    using AI and templates.
    """
    
    # Categories of products to generate
    PRODUCT_CATEGORIES = [
        "Basic Accounting",
        "Self-Employed/Freelancer",
        "Limited Company",
        "VAT & Tax",
        "Financial Planning",
    ]
    
    # Product ideas for each category
    PRODUCT_IDEAS = {
        "Basic Accounting": [
            {"name": "Invoice Template (UK)", "type": "template", "price": 9},
            {"name": "Expense Tracker Spreadsheet", "type": "spreadsheet", "price": 11},
            {"name": "Income & Expense Guide", "type": "guide", "price": 12},
            {"name": "Quarterly Tax Checklist", "type": "checklist", "price": 8},
            {"name": "Receipt Organization System", "type": "guide", "price": 9},
        ],
        "Self-Employed/Freelancer": [
            {"name": "Self-Assessment Tax Return Guide", "type": "guide", "price": 15},
            {"name": "Deductions Checklist (UK)", "type": "checklist", "price": 12},
            {"name": "Client Invoice Templates", "type": "templates", "price": 14},
            {"name": "Tax-Efficient Business Structure", "type": "guide", "price": 17},
            {"name": "Freelancer Accounting Tracker", "type": "spreadsheet", "price": 16},
        ],
        "Limited Company": [
            {"name": "Company Accounts Explained", "type": "guide", "price": 18},
            {"name": "Dividend vs Salary Calculator", "type": "spreadsheet", "price": 19},
            {"name": "Corporation Tax Planning", "type": "guide", "price": 22},
            {"name": "Director's Tax Checklist", "type": "checklist", "price": 14},
            {"name": "Payroll Setup Guide", "type": "guide", "price": 16},
        ],
        "VAT & Tax": [
            {"name": "VAT Registration Guide", "type": "guide", "price": 13},
            {"name": "VAT Return Checklist", "type": "checklist", "price": 11},
            {"name": "Tax Deduction Swipe File", "type": "swipes", "price": 19},
            {"name": "IR35 Compliance Checklist", "type": "checklist", "price": 15},
            {"name": "Capital Allowances Guide", "type": "guide", "price": 17},
        ],
        "Financial Planning": [
            {"name": "Monthly Budget Planner (GBP)", "type": "spreadsheet", "price": 14},
            {"name": "Profit & Loss Tracker", "type": "spreadsheet", "price": 16},
            {"name": "Cash Flow Forecast Template", "type": "spreadsheet", "price": 18},
            {"name": "Business Health Dashboard", "type": "spreadsheet", "price": 21},
            {"name": "Financial Ratio Guide", "type": "guide", "price": 15},
        ],
    }
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set in .env")
        openai.api_key = self.api_key
        self.generated_products = []
    
    def generate_daily_product(self) -> Dict:
        """
        Generate one product per day.
        Each day picks a different category and product.
        """
        day_of_year = datetime.now().timetuple().tm_yday
        
        # Cycle through categories
        category_idx = (day_of_year - 1) % len(self.PRODUCT_CATEGORIES)
        category = self.PRODUCT_CATEGORIES[category_idx]
        
        # Cycle through products in category
        products_in_category = self.PRODUCT_IDEAS[category]
        product_idx = (day_of_year - 1) % len(products_in_category)
        product_template = products_in_category[product_idx]
        
        print(f"\n🎯 Generating: {product_template['name']}")
        
        # Generate the actual content
        content = self._generate_content(product_template, category)
        
        # Create product object
        product = {
            "id": f"product_{day_of_year}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "name": product_template["name"],
            "category": category,
            "type": product_template["type"],
            "price": product_template["price"],
            "description": content["description"],
            "content": content,
            "created_at": datetime.now().isoformat(),
            "status": "ready_for_upload",
        }
        
        self.generated_products.append(product)
        return product
    
    def _generate_content(self, product: Dict, category: str) -> Dict:
        """
        Use ChatGPT to generate product content.
        """
        prompt = f"""
        Create a comprehensive UK {category} product:
        
        Product: {product['name']}
        Type: {product['type']}
        Price: £{product['price']}
        
        Generate:
        1. Short description (2-3 sentences for Gumroad)
        2. Long description (detailed overview)
        3. Key benefits (5 bullet points)
        4. What's included (for templates/guides)
        5. Target audience
        
        Make it UK-specific, professional, and valuable.
        Format as JSON.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a UK accounting expert creating high-value products."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            content_text = response['choices'][0]['message']['content']
            
            # Parse JSON response
            try:
                content = json.loads(content_text)
            except:
                # Fallback if JSON parsing fails
                content = {
                    "description": content_text[:200],
                    "long_description": content_text,
                    "benefits": [
                        f"Benefit {i+1}" for i in range(5)
                    ],
                    "included": "Full UK accounting guide with templates",
                    "target_audience": "UK self-employed and business owners"
                }
            
            return content
        
        except Exception as e:
            print(f"❌ Error generating content: {e}")
            return {
                "description": f"UK {product['name']} - Professional accounting template",
                "long_description": f"Complete {product['name']} for UK business",
                "benefits": [
                    "Save time on accounting",
                    "UK tax compliant",
                    "Ready to use immediately",
                    "Professionally formatted",
                    "Regularly updated"
                ],
                "included": product['name'],
                "target_audience": "UK business owners"
            }
    
    def generate_all_products(self) -> List[Dict]:
        """
        Generate all products in the system (for bootstrap).
        """
        all_products = []
        
        for category, products in self.PRODUCT_IDEAS.items():
            for product_template in products:
                content = self._generate_content(product_template, category)
                
                product = {
                    "id": f"product_{len(all_products)}",
                    "name": product_template["name"],
                    "category": category,
                    "type": product_template["type"],
                    "price": product_template["price"],
                    "description": content.get("description", ""),
                    "content": content,
                    "created_at": datetime.now().isoformat(),
                    "status": "ready_for_upload",
                }
                
                all_products.append(product)
                print(f"✓ Generated: {product['name']} (£{product['price']})")
        
        return all_products
    
    def save_product(self, product: Dict) -> str:
        """
        Save product to file.
        """
        products_dir = "agents/accounting-business/generated_products"
        os.makedirs(products_dir, exist_ok=True)
        
        filepath = os.path.join(products_dir, f"{product['id']}.json")
        
        with open(filepath, 'w') as f:
            json.dump(product, f, indent=2)
        
        return filepath
    
    def get_daily_product(self) -> Dict:
        """
        Get today's product to upload.
        """
        return self.generate_daily_product()


if __name__ == "__main__":
    print("🚀 UK Accounting Product Generator")
    print("="*50)
    
    generator = AccountingProductGenerator()
    
    # Generate today's product
    product = generator.get_daily_product()
    
    print(f"\n✅ Generated: {product['name']}")
    print(f"   Category: {product['category']}")
    print(f"   Type: {product['type']}")
    print(f"   Price: £{product['price']}")
    print(f"   Description: {product['description'][:100]}...")
    
    # Save to file
    filepath = generator.save_product(product)
    print(f"\n💾 Saved to: {filepath}")
