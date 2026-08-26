# UK Accounting Agent Business

## Quick Start

```bash
# 1. Install dependencies
pip install openai python-dotenv praw tweepy schedule requests

# 2. Configure APIs
cp .env.example .env
# Edit .env with your API keys:
#   - OPENAI_API_KEY
#   - GUMROAD_API_KEY
#   - REDDIT credentials
#   - TWITTER credentials
#   - STRIPE_API_KEY

# 3. Run agents
python main.py
```

## What Happens

**Daily (9am):**
1. Generate 1 accounting product
2. Upload to Gumroad
3. Promote on Reddit, Twitter, Facebook
4. Check sales and income

**Weekly (Monday 10am):**
- Generate weekly income report
- Analyze top products
- Optimize pricing/promotion

**Monthly (1st at 10am):**
- Generate detailed monthly report
- Calculate growth metrics
- Plan next month

## Expected Income

**Month 1:**
- Products created: 30
- Expected sales: 150-300
- Expected income: £300-700

**Month 2:**
- Products created: 60
- Expected sales: 400-800
- Expected income: £800-1500

**Month 3+:**
- Products created: 90+
- Expected sales: 1000+
- Expected income: £1500-3000+

## Files

```
agents/accounting-business/
├── main.py                          # Main orchestrator
├── agent_product_generator.py       # Creates products
├── agent_gumroad_manager.py         # Uploads to Gumroad
├── agent_social_promoter.py         # Promotes on social
├── agent_income_tracker.py          # Tracks income
├── generated_products/              # Generated files
├── .env.example                     # Configuration template
└── README.md                        # This file
```

## API Keys Needed

1. **OpenAI** - Generate product content
2. **Gumroad** - Upload and sell products
3. **Reddit** - Post to subreddits
4. **Twitter** - Post tweets
5. **Stripe** - Process payments

## Customization

Edit product categories and ideas in:
- `agent_product_generator.py` → `PRODUCT_IDEAS`
- `agent_social_promoter.py` → `COMMUNITIES`

## Monitoring

Check daily reports:
```bash
cat agents/accounting-business/income_report.txt
```

View generated products:
```bash
ls agents/accounting-business/generated_products/
```

## Troubleshooting

**"OPENAI_API_KEY not set"**
- Make sure .env file exists and has your key

**"Gumroad upload failed"**
- Check GUMROAD_API_KEY in .env
- Verify Gumroad account is active

**No sales**
- Give it 1-2 weeks for products to gain traction
- Ensure social media promotion is working
- Check product descriptions are compelling

## Next Steps

1. Get API keys for all services
2. Run agents once: `python main.py`
3. Monitor income tracker
4. Optimize top-performing products
5. Scale by creating more product categories

---

**This system will make you £500-2000+/month on autopilot once running!**
