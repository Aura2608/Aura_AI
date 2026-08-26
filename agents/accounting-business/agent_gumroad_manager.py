#!/usr/bin/env python3
"""
Agent 2: Gumroad Manager
Uploads products to Gumroad and manages listings
"""

import os
import json
import requests
from typing import Dict
from dotenv import load_dotenv

load_dotenv()


class GumroadManager:
    """
    Manages Gumroad product uploads and listings.
    """
    
    GUMROAD_API_BASE = "https://api.gumroad.com/v2"
    
    def __init__(self):
        self.api_token = os.getenv("GUMROAD_API_KEY")
        if not self.api_token:
            raise ValueError("GUMROAD_API_KEY not set in .env")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
    
    def upload_product(self, product: Dict) -> Dict:
        """
        Upload a product to Gumroad.
        
        Args:
            product: Product dict with name, description, price, etc.
        
        Returns:
            Response from Gumroad API
        """
        
        print(f"\n📤 Uploading to Gumroad: {product['name']}")
        
        # Format product for Gumroad
        gumroad_payload = {
            "name": product['name'],
            "description": product['description'],
            "price": product['price'],
            "currency": "GBP",
            "shown_on_profile": True,
            "require_email": True,
        }
        
        # Add tags based on category
        tags = self._get_tags(product['category'])
        gumroad_payload["tags"] = ",".join(tags)
        
        try:
            # In production, this would call actual Gumroad API
            # For now, we'll simulate the response
            response = self._simulate_gumroad_upload(gumroad_payload)
            
            if response.get("success"):
                print(f"✅ Successfully uploaded: {product['name']}")
                print(f"   URL: {response.get('url')}")
                return response
            else:
                print(f"❌ Upload failed: {response.get('error')}")
                return None
        
        except Exception as e:
            print(f"❌ Error uploading to Gumroad: {e}")
            return None
    
    def _simulate_gumroad_upload(self, payload: Dict) -> Dict:
        """
        Simulate Gumroad upload (for testing without real API key).
        """
        return {
            "success": True,
            "product_id": f"prod_{hash(payload['name']) % 10000}",
            "url": f"https://gumroad.com/l/{payload['name'].replace(' ', '-').lower()}",
            "message": "Product uploaded successfully"
        }
    
    def _get_tags(self, category: str) -> list:
        """
        Get appropriate tags for product category.
        """
        tags_map = {
            "Basic Accounting": ["accounting", "uk-business", "invoicing", "templates"],
            "Self-Employed/Freelancer": ["freelance", "self-employed", "tax", "uk"],
            "Limited Company": ["limited-company", "accounting", "tax-planning", "uk"],
            "VAT & Tax": ["vat", "tax", "uk-tax", "compliance"],
            "Financial Planning": ["finance", "budgeting", "business-planning", "spreadsheet"],
        }
        return tags_map.get(category, ["uk", "business"])
    
    def get_product_url(self, product_name: str) -> str:
        """
        Generate Gumroad URL for product.
        """
        slug = product_name.lower().replace(" ", "-")
        return f"https://gumroad.com/l/{slug}"
    
    def update_product_price(self, product_id: str, new_price: float) -> bool:
        """
        Update product price on Gumroad.
        """
        # In production, would call Gumroad API
        print(f"💷 Would update {product_id} price to £{new_price}")
        return True
    
    def get_sales(self) -> Dict:
        """
        Get sales data from Gumroad.
        """
        # In production, would call Gumroad API
        print("📊 Fetching sales data from Gumroad...")
        
        return {
            "total_sales": 0,
            "total_revenue": 0.0,
            "products_sold": {},
            "last_updated": "just now"
        }


if __name__ == "__main__":
    print("🎯 Gumroad Manager")
    print("="*50)
    
    manager = GumroadManager()
    
    # Example product
    test_product = {
        "name": "UK Invoice Template",
        "category": "Basic Accounting",
        "description": "Professional UK-compliant invoice template for small businesses",
        "price": 9,
    }
    
    # Upload
    result = manager.upload_product(test_product)
    print(f"\nResult: {json.dumps(result, indent=2)}")
