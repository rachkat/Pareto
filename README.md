----
# Pareto Analysis Project

**Author:** Rachel Goldsbury  
**Date:** September 2025  

---

## Overview
This project demonstrates a **Pareto analysis (80/20 rule)** using Python.  
Pareto analysis is a decision-making technique that shows how a small number of categories often account for the majority of effects.  

In this example, issue categories (like billing, defects, and delivery) are analyzed to highlight which ones contribute most to customer problems.  
The goal is to identify high-impact areas where improvements will yield the greatest benefits.  

---

## Files
- `issues_pareto.csv` — sample dataset (Issue, Count)  
- `pareto_analysis.py` — Python script to generate the Pareto chart  
- `pareto_chart.png` — output visualization of the analysis  

---

## How to Run

### Run Locally
1. Clone this repo:
   ```bash
   git clone https://github.com/rachkat/Pareto.git
   cd Pareto
```

2. Install requirements:

   ```bash
   pip install pandas matplotlib
   ```
3. Run the script:

   ```bash
   python pareto_analysis.py
   ```
4. The chart `pareto_chart.png` will be created in the repo.

### Run in GitHub Codespaces

1. Click **Code → Create codespace on main**
2. In the terminal inside Codespaces, run:

   ```bash
   pip install pandas matplotlib
   python pareto_analysis.py
   ```
3. Commit & push the generated chart.

---

## Results

The analysis shows that a few categories (Billing + Product Defect) account for most issues.
This aligns with the **Pareto Principle (80/20 rule)** — where focusing on a small set of problems yields the biggest improvements.

---
Here’s the resulting chart:

![Pareto Chart](https://raw.githubusercontent.com/rachkat/Pareto/main/pareto_chart.png)


---

## Next Steps

* Replace `issues_pareto.csv` with your own dataset (must include columns `Issue` and `Count`).
* Extend the script to handle weighted metrics (e.g., cost or severity).
* Build a dashboard (e.g., in Power BI, Tableau, or Streamlit) for interactive exploration.

---

## License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

```

---





