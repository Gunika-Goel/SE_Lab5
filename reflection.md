# Reflection - Lab 5: Static Code Analysis

**1. Which issues were the easiest to fix, and which were the hardest? Why?**

- **Easiest:** Mutable default argument and bare except — both had clear fixes recommended by Pylint.  
- **Hardest:** Input validation and removing `eval()` — required understanding where invalid inputs could break the program and replacing dangerous functionality safely.

**2. Did the static analysis tools report any false positives? If so, describe one example.**

- No major false positives were observed. Most warnings were valid and corresponded to actual potential bugs or security risks.

**3. How would you integrate static analysis tools into your actual software development workflow?**

- Run **Pylint, Flake8, and Bandit locally** before committing code.  
- Integrate these tools in **Continuous Integration (CI) pipelines** (e.g., GitHub Actions) to automatically check new code for issues.  
- Fix high and medium severity issues before merging branches to ensure code quality and security.

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

- Code is **safer** (removed `eval`, validated inputs).  
- **More maintainable** due to proper exception handling and improved file handling.  
- **More readable**: consistent formatting, f-strings, and clear logs.  
- Avoided runtime errors (like TypeError from adding `int` + `str`).
