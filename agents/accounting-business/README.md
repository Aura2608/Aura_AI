# UK Accounting Agent Business System

## Overview

Fully automated AI agent system that:
- Generates UK accounting guides, templates, and tools daily
- Uploads to Gumroad automatically
- Promotes across UK communities (Reddit, Twitter, Facebook)
- Tracks sales and payments
- Deposits money to UK bank account
- Makes £500-2000+/month passive recurring income

## Architecture

```
Agent System (24/7)
├─ Agent 1: Product Generator
│  └─ Creates accounting products using ChatGPT
│
├─ Agent 2: Gumroad Manager
│  └─ Uploads to Gumroad API
│
├─ Agent 3: Social Promoter
│  └─ Posts to Reddit, Twitter, Facebook groups
│
└─ Agent 4: Income Tracker
   └─ Monitors Gumroad sales + bank deposits
```

## Income Streams

### **Products (30-40 created, each £9-29)**

1. **Basic Accounting** (£9-15)
   - Invoice Template (UK compliant)
   - Expense Tracker Spreadsheet
   - Income & Expense Categorization Guide
   - Quarterly Tax Checklist

2. **Self-Employed/Freelancer** (£12-19)
   - Self-Assessment Tax Return Guide
   - Deductions Checklist (UK)
   - Client Invoice Templates
   - Tax-Efficient Business Structure Guide

3. **Limited Company** (£15-29)
   - Company Accounts Explained
   - Dividend vs Salary Calculator
   - Corporation Tax Planning Guide
   - Director's Tax Checklist

4. **VAT & Tax** (£11-19)
   - VAT Registration Guide
   - VAT Return Checklist
   - Tax Deduction Swipe File
   - IR35 Compliance Checklist

5. **Financial Planning** (£14-24)
   - Monthly Budget Planner (GBP)
   - Profit & Loss Tracker
   - Cash Flow Forecast Template
   - Business Health Dashboard

## Revenue Model

**Per Product:**
- Average price: £16
- Average monthly sales per product: 50 copies
- Revenue per product: £800/month

**At Scale (Month 3+):**
- 30 products × £800 = £24,000/month
- **Conservative estimate: £500-2000/month** (early months)
- **Target: £3000-5000/month** (after 3 months)

## Getting Started

1. Set up `.env` with:
   ```
   OPENAI_API_KEY=sk-...
   GUMROAD_API_KEY=...
   REDDIT_CLIENT_ID=...
   REDDIT_SECRET=...
   TWITTER_API_KEY=...
   TWITTER_API_SECRET=...
   STRIPE_API_KEY=...  # For Gumroad payments
   ```

2. Run agents:
   ```bash
   python -m agents.main
   ```

3. Agents run continuously (24/7)

## Next Steps

1. Build Agent 1: Product Generator
2. Build Agent 2: Gumroad Manager
3. Build Agent 3: Social Promoter
4. Build Agent 4: Income Tracker
5. Deploy on GitHub Actions (24/7)
