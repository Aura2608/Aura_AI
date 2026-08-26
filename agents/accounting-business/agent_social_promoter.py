#!/usr/bin/env python3
"""
Agent 3: Social Promoter
Automatically promotes products on UK communities
(Reddit, Twitter, Facebook groups)
"""

import os
import json
from typing import Dict, List
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class SocialPromoter:
    """
    Promotes products on UK social media communities.
    """
    
    # UK communities to post to
    COMMUNITIES = {
        "reddit": [
            {"subreddit": "r/UKPersonalFinance", "members": 450000},
            {"subreddit": "r/BritishProblems", "members": 500000},
            {"subreddit": "r/AskUK", "members": 300000},
            {"subreddit": "r/freelance", "members": 250000},
            {"subreddit": "r/Entrepreneur", "members": 1000000},
        ],
        "twitter": [
            {"hashtag": "#UKBusiness", "reach": 50000},
            {"hashtag": "#Freelance", "reach": 100000},
            {"hashtag": "#SelfEmployed", "reach": 75000},
            {"hashtag": "#UKEntrepreneur", "reach": 40000},
        ],
        "facebook": [
            "UK Freelancers",
            "UK Self Employed",
            "Small Business UK",
            "UK Accountants",
        ]
    }
    
    def __init__(self):
        self.reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
        self.reddit_secret = os.getenv("REDDIT_SECRET")
        self.twitter_key = os.getenv("TWITTER_API_KEY")
        self.twitter_secret = os.getenv("TWITTER_API_SECRET")
    
    def promote_product(self, product: Dict, gumroad_url: str) -> Dict:
        """
        Promote a product across all platforms.
        
        Args:
            product: Product dict
            gumroad_url: URL to promote
        
        Returns:
            Results of promotion
        """
        results = {
            "product": product['name'],
            "price": f"£{product['price']}",
            "timestamp": datetime.now().isoformat(),
            "platforms": {}
        }
        
        # Promote on Reddit
        print(f"\n📱 Promoting: {product['name']}")
        reddit_results = self._promote_on_reddit(product, gumroad_url)
        results["platforms"]["reddit"] = reddit_results
        
        # Promote on Twitter
        twitter_results = self._promote_on_twitter(product, gumroad_url)
        results["platforms"]["twitter"] = twitter_results
        
        # Promote on Facebook
        facebook_results = self._promote_on_facebook(product, gumroad_url)
        results["platforms"]["facebook"] = facebook_results
        
        return results
    
    def _promote_on_reddit(self, product: Dict, url: str) -> Dict:
        """
        Create promotion posts for relevant Reddit communities.
        """
        print(f"  🔴 Reddit: Creating posts...")
        
        posts = []
        
        for community in self.COMMUNITIES["reddit"]:
            post_title = self._generate_reddit_title(product)
            post_body = self._generate_reddit_body(product, url)
            
            post = {
                "subreddit": community["subreddit"],
                "title": post_title,
                "body": post_body,
                "status": "ready_to_post",  # In production: "posted"
            }
            
            posts.append(post)
            print(f"     ✓ {community['subreddit']}: '{post_title}'")
        
        return {
            "platform": "reddit",
            "posts_created": len(posts),
            "posts": posts
        }
    
    def _generate_reddit_title(self, product: Dict) -> str:
        """
        Generate Reddit-friendly post title.
        """
        titles = [
            f"[TEMPLATE] {product['name']} - Save hours on accounting",
            f"[RESOURCE] UK: {product['name']} Guide (£{product['price']})",
            f"[TIP] Struggling with {product['category']}? Check out {product['name']}",
            f"[HELP] {product['name']} - Ready-to-use template",
        ]
        return titles[hash(product['name']) % len(titles)]
    
    def _generate_reddit_body(self, product: Dict, url: str) -> str:
        """
        Generate Reddit post body.
        """
        return f"""
**{product['name']}** (£{product['price']})

{product['description']}

**Included:**
- Professional UK formatting
- Ready to use immediately
- Regularly updated

**Link:** {url}

*This is a resource I created to help UK business owners. Hope it's useful!*
        """
    
    def _promote_on_twitter(self, product: Dict, url: str) -> Dict:
        """
        Create promotion tweets.
        """
        print(f"  🐦 Twitter: Creating tweets...")
        
        tweets = []
        
        for hashtag_obj in self.COMMUNITIES["twitter"]:
            hashtag = hashtag_obj["hashtag"]
            tweet_text = self._generate_tweet(product, url, hashtag)
            
            tweet = {
                "text": tweet_text,
                "hashtag": hashtag,
                "status": "ready_to_post",
                "character_count": len(tweet_text)
            }
            
            tweets.append(tweet)
            print(f"     ✓ Tweet for {hashtag}")
        
        return {
            "platform": "twitter",
            "tweets_created": len(tweets),
            "tweets": tweets
        }
    
    def _generate_tweet(self, product: Dict, url: str, hashtag: str) -> str:
        """
        Generate tweet text (under 280 chars).
        """
        tweet = f"📊 New: {product['name']} (£{product['price']}) - Perfect for UK business owners. {hashtag} {url}"
        return tweet[:280]  # Twitter limit
    
    def _promote_on_facebook(self, product: Dict, url: str) -> Dict:
        """
        Create promotion posts for Facebook groups.
        """
        print(f"  📘 Facebook: Creating group posts...")
        
        posts = []
        
        for group in self.COMMUNITIES["facebook"]:
            post_text = f"""
🎯 {product['name']} (£{product['price']})

{product['description']}

Great for: {product['category']}

Link: {url}
            """
            
            post = {
                "group": group,
                "text": post_text,
                "status": "ready_to_post",
            }
            
            posts.append(post)
            print(f"     ✓ {group}")
        
        return {
            "platform": "facebook",
            "posts_created": len(posts),
            "posts": posts
        }
    
    def get_estimated_reach(self) -> Dict:
        """
        Calculate estimated reach of promotion.
        """
        reddit_reach = sum(c["members"] for c in self.COMMUNITIES["reddit"])
        twitter_reach = sum(h["reach"] for h in self.COMMUNITIES["twitter"])
        facebook_reach = len(self.COMMUNITIES["facebook"]) * 10000  # Estimate
        
        return {
            "total_reach": reddit_reach + twitter_reach + facebook_reach,
            "reddit": reddit_reach,
            "twitter": twitter_reach,
            "facebook": facebook_reach,
        }


if __name__ == "__main__":
    print("📱 Social Promoter")
    print("="*50)
    
    promoter = SocialPromoter()
    
    # Example product
    test_product = {
        "name": "UK Invoice Template",
        "category": "Basic Accounting",
        "description": "Professional UK-compliant invoice template",
        "price": 9,
    }
    
    # Promote
    results = promoter.promote_product(test_product, "https://gumroad.com/l/uk-invoice")
    
    print(f"\n✅ Promotion created:")
    print(json.dumps(results, indent=2))
    
    # Show reach
    reach = promoter.get_estimated_reach()
    print(f"\n📊 Estimated reach: {reach['total_reach']:,} people")
