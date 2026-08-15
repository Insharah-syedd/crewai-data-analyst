# Sales Performance Report  
**Date range:** 2026‑08‑01 to 2026‑08‑08  
**Prepared for:** Business Leadership Team  
**Prepared by:** Data Reporting Team  

---  

## Executive Summary  

The week‑long sales dataset contains 8 daily transactions covering three product lines (Laptop, Phone, Tablet) across three major Pakistani cities (Karachi, Lahore, Islamabad). The data is structurally clean—no missing values, duplicates, or formatting issues.  

Key take‑aways:

| Insight | Business Impact |
|--------|-----------------|
| **Phone** accounts for the largest share of units sold (37) and contributes ~40 % of total revenue, despite a lower average price. | High volume driver; focus on scaling phone sales while protecting margin. |
| **Laptop** commands the highest average unit price (≈ 1 000) and provides the second‑largest revenue share. | Opportunity to increase profitability through upselling or premium offerings. |
| **Tablet** shows the lowest volume and price (≈ 400 per unit). | May require a distinct marketing or discount strategy to improve contribution. |
| **Karachi** leads in total volume (28 units) and revenue (17 200), but its average price (≈ 614) is lower than Lahore’s (≈ 747). | Leverage high volume while exploring price‑optimization tactics. |
| **Lahore** yields the highest average price, indicating a higher‑margin market even with fewer units. | Targeted premium campaigns could boost overall margin. |
| **Strong correlation** between units sold and revenue (0.83) confirms that volume drives most of the revenue, yet price variation across products means margin management remains critical. | Align sales incentives with both volume and price objectives. |

These findings suggest a balanced focus on maintaining high‑volume phone sales, increasing the share of higher‑margin laptops, and re‑examining the tablet offering. Regional tactics should exploit Karachi’s volume and Lahore’s price tolerance.

---  

## Dataset Overview  

| Characteristic | Detail |
|----------------|--------|
| **Rows** | 8 |
| **Columns** | 5 |
| **Column Names** | `Date` (string), `Product` (string), `Region` (string), `Units_Sold` (integer), `Revenue` (integer) |
| **Date Range** | 2026‑08‑01 → 2026‑08‑08 (one record per day) |
| **Distinct Products** | Laptop, Phone, Tablet |
| **Distinct Regions** | Karachi, Lahore, Islamabad |

The dataset captures daily sales activity for a single week, providing a snapshot of product‑mix performance across three cities.

---  

## Data Quality  

| Issue | Count | Comment |
|-------|-------|---------|
| Missing values | 0 | Complete data for all columns. |
| Duplicate rows | 0 | No identical records. |
| Inconsistent formatting | 0 | All categorical entries are consistently capitalized. |
| Out‑of‑range values | 0 | No negative or implausible numbers. |

**Conclusion:** The data is clean and ready for analysis. The only limitations stem from its small size (one week) and lack of additional contextual variables (e.g., promotions, inventory).  

---  

## Key Findings  

- **Overall sales volume:** 64 units sold across the week.  
- **Total revenue:** 42 200 (currency units).  
- **Average daily units sold:** 8 (SD = 4.14).  
- **Average daily revenue:** 5 250 (SD = 2 511).  

### Product‑level performance  

| Product | Total Units Sold | Total Revenue | Avg. Unit Price |
|---------|------------------|---------------|-----------------|
| Laptop | 15 | 15 000 | **1 000** |
| Phone | 37 | 22 200 | **600** |
| Tablet | 12 | 4 800 | **400** |

- Laptops deliver the highest price per unit.  
- Phones drive the bulk of sales volume.  
- Tablets generate the lowest revenue per unit.

### Region‑level performance  

| Region | Total Units Sold | Total Revenue | Avg. Unit Price |
|--------|------------------|---------------|-----------------|
| Karachi | 28 | 17 200 | ≈ 614 |
| Lahore | 19 | 14 200 | ≈ 747 |
| Islamabad | 17 | 10 600 | ≈ 624 |

- Karachi leads in volume and absolute revenue.  
- Lahore achieves the highest average price, indicating a premium market.  

### Daily highlights  

| Date | Product | Region | Units Sold | Revenue |
|------|---------|--------|------------|---------|
| 2026‑08‑01 | Laptop | Karachi | 5 | 5 000 |
| 2026‑08‑02 | Phone | Lahore | 12 | 7 200 |
| 2026‑08‑03 | Laptop | Islamabad | 3 | 3 000 |
| 2026‑08‑04 | Tablet | Karachi | 8 | 3 200 |
| 2026‑08‑05 | Phone | Karachi | 15 | 9 000 |
| 2026‑08‑06 | Laptop | Lahore | 7 | 7 000 |
| 2026‑08‑07 | Tablet | Islamabad | 4 | 1 600 |
| 2026‑08‑08 | Phone | Islamabad | 10 | 6 000 |

- **Peak performance day:** 2026‑08‑05 (Phone, Karachi) – 15 units, 9 000 revenue.  
- **Lowest revenue day:** 2026‑08‑07 (Tablet, Islamabad) – 4 units, 1 600 revenue.

---  

## Important Trends and Patterns  

1. **Volume vs. Price Trade‑off**  
   - Phones dominate volume but have a lower price (≈ 600).  
   - Laptops, though lower in volume, generate higher revenue per unit.  

2. **Regional Price Sensitivity**  
   - Lahore’s average unit price (~ 747) exceeds Karachi’s (~ 614) despite selling fewer units, suggesting higher willingness to pay or a more premium product mix.  

3. **Single‑Day Spike**  
   - The 15‑unit Phone sale on 2026‑08‑05 lifted both daily volume and revenue sharply, indicating that occasional bulk orders can markedly affect weekly performance.  

4. **Consistent Product Mix**  
   - Each day includes only one product type, meaning the week’s revenue composition reflects the order of daily product focus rather than simultaneous multi‑product sales.  

---  

## Correlations and Anomalies  

| Variable Pair | Correlation Coefficient |
|---------------|--------------------------|
| Units_Sold ↔ Revenue | **0.83** |

- The strong positive correlation confirms that higher unit counts generally translate to higher revenue. The coefficient is below 1.0 because unit price varies by product (e.g., Laptop vs. Tablet).  

### Notable Anomalies  

| Observation | Why it stands out |
|-------------|-------------------|
| **15 units of Phone (Karachi)** | Largest single‑day volume and revenue; a potential bulk or promotional order. |
| **Revenue of 1 600 for Tablet (Islamabad)** | Lowest revenue; reflects the lowest unit price (≈ 400). May indicate a discount or low‑margin SKU. |
| **Large price gap between Laptop (1 000) and Tablet (400)** | Signifies distinct market positioning; forecasting should treat them separately. |

All anomalies appear to be business‑driven rather than data‑quality issues.

---  

## Business Insights  

1. **Phone as the volume engine** – The Phone line contributes the most units and a sizable share of revenue, but its average price lags behind Laptop and Lahore’s overall average. Improving the price mix for phones (e.g., bundling accessories, premium models) could lift margin without sacrificing volume.  

2. **Laptop as the margin driver** – With the highest unit price, laptops have the best margin potential. The current volume is modest; targeted upsell or cross‑sell campaigns (e.g., “Buy a Laptop, get a discounted Tablet”) could boost overall profitability.  

3. **Tablet underperformance** – The low unit price and limited volume suggest that tablets are either a loss‑leader or a niche offering. The business should decide whether to push higher‑margin tablets, discontinue the line, or reposition it (e.g., targeting education or enterprise).  

4. **Regional strategy**  
   - **Karachi**: High volume but lower average price. Consider price‑optimization tests (e.g., small price increases, loyalty discounts) to improve margin while retaining volume.  
   - **Lahore**: Higher willingness to pay. Deploy premium messaging, limited‑edition models, or bundled offers to capitalize on price tolerance.  
   - **Islamabad**: Balanced performance; opportunities exist to replicate Lahore’s price sensitivity through targeted promotions.  

5. **Peak day analysis** – Understanding the driver behind the 15‑unit Phone sale (e.g., a bulk corporate order, promotional campaign, or stock clearance) can help replicate similar spikes.  

---  

## Practical Recommendations  

| Recommendation | Rationale | Suggested Actions |
|----------------|-----------|-------------------|
| **1. Introduce tiered Phone pricing** | Phones sell highest volume but at a lower price. | • Add a premium Phone variant (higher specs) with a price ≈ 800.<br>• Offer accessories bundles to increase average transaction value. |
| **2. Upsell Laptops to existing Phone buyers** | Laptop margin is high. | • Deploy post‑purchase email campaigns offering a discount on Laptops for recent Phone purchasers.<br>• Train sales staff to cross‑sell during in‑store visits. |
| **3. Re‑evaluate Tablet positioning** | Tablets have the lowest price and volume. | • Conduct a quick market survey to assess demand.<br>• If demand is low, consider phasing out or repositioning as an educational device with a different price point. |
| **4. Regional price‑testing** | Lahore shows higher average price tolerance. | • Run A/B price experiments in Karachi (e.g., +5 % price) while monitoring volume impact.<br>• Develop premium messaging for Lahore, emphasizing quality and service. |
| **5. Capture drivers of large sales spikes** | The 15‑unit Phone sale significantly lifted weekly revenue. | • Add a “promotion code” or “order source” field to future datasets.<br>• Track bulk‑order triggers (e.g., corporate contracts, seasonal promotions). |
| **6. Expand data collection** | Current dataset covers only one week. | • Extend tracking to at least 3‑6 months to smooth out daily variance.<br>• Include additional attributes: discount applied, sales channel (online vs. store), inventory levels. |
| **7. Implement a simple dashboard** | Stakeholders need quick visibility. | • Build a weekly KPI dashboard showing units, revenue, average price by product and region.<br>• Highlight variance from targets and flag unusually high/low days. |

---  

## Conclusion  

The week‑long sales snapshot is clean and reveals clear product‑ and region‑level dynamics:

- **Phone** provides volume; **Laptop** provides margin; **Tablet** is low‑performing.  
- **Karachi** drives volume; **Lahore** supports higher margins.  
- A strong units‑revenue correlation confirms that increasing sales quantity is effective, yet price optimization remains essential for profitability.

By focusing on premiumizing the Phone line, leveraging Laptop upsell opportunities, reassessing the Tablet strategy, and tailoring regional pricing, the business can improve both top‑line growth and margins. Extending data collection and enriching it with promotional and channel information will further empower data‑driven decision‑making.

---  

*Prepared by the Data Reporting Team – August 9 2026*