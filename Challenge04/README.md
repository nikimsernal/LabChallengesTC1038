# Challenges Week 5

## 🟢 Challenge 1 Checking Leap Years

A year is a leap year if it is divisible by 4, **except** when it is divisible by 100, **unless** it is also divisible by 400. Define a function `is_leap_year(year)` returning a boolean (`True` or `False`). 

You will need an additional function `valid_year(year)` to check whether the input is an integer, positive number. 

Using `is_leap_year(year)` and `valid_year(year)`, make a menu where a year is provided as a user input and a message declaring whether said year is a leap year. 

Runs should look like this (denoting user input with `>`):
```
Hello. Provide a year to check if it is a leap year.
> 2000
2000 is a leap year.
```

```
Hello. Provide a year to check if it is a leap year.
> 2026
2000 is not a leap year.
```

```
Hello. Provide a year to check if it is a leap year.
> 123.45
Please provide a valid year.
```
## 🟡 Challenge 2 Temperature Unit Converter & Safety Alert

You will create a function to convert temperatures from the three main units: °C, °F and K. Consider the following formulas:
$$
^\circ\text{C} = (^\circ\text{F} - 32) \times \frac{5}{9}
$$
$$
^\circ\text{C} = K+273.15
$$

The function `temp_converter(temperature, unit)` will take the following arguments:

- `temperature`: A number representing the temperature values.
- `current_unit`: A string representing the unit in which `temperature` was provided. It can be `"C"` for °C, `"F"` for °F or "K" for K.
- `target_unit`: A string representing the output's unit. It can be either `"C"`, `"F"` or `"K"`

This function will return a number representing the converted temperature value, given that both the current and target units are valid, otherwise, it should return a `None` and print a message letting the user know the units are not valid.

Then, define `check_temp(temperature)` taking a temperature in  °C as an input and returning a string according to the following safety rules:
- Below 0 °C: `"Freezing Warning"`
- 0 °C to 37 °C (inclusive): `"Normal"`
- Above 37 °C: `"Fever / Heat Warning"`

Following this, make a menu taking a temperature and any valid unit as user input. Then, print a status message.

Runs should look like this (denoting user input with `>`):
```
Provide a temperature to check status
> 25.7
> C
Temperature: 25.7 °C. Status: Normal
```

```
Provide a temperature to check status
> 104
> F
Temperature: 40 °C. Status: Fever / Heat Warning
```

```
Provide a temperature to check status
> 0
> K
Temperature: -273.15 °C. Status: Freezing Warning
```

```
Provide a temperature to check status
> 25
> X
Please provide a valid temperature unit from the following options: C, F or K.
```

## 🟠 Challenge 3 Automated Loan & Credit Risk Classifier

Financial institutions use rule-based engines to evaluate loan applications. Write a complete credit evaluation program that uses functions to calculate two key financial ratios and assign a risk tier. You will use the following metrics
1. **Debt-to-Income (DTI) Ratio:**

$$
\text{DTI} = \frac{\text{monthly debt}}{\text{monthly income}}
$$

2. **Loan-to-Value (LTV) Ratio:**

$$
\text{LTV} = \frac{\text{requested loan}}{\text{collateral value}}
$$

According to these metrics, you may classify the risks as:

- **Approved (Tier 1):** $\text{DTI} \le 0.35$ **AND** $\text{LTV} \le 0.80$
- **Conditional (Tier 2):** $(\text{DTI} \le 0.45 \text{ AND } \text{LTV} \le 0.80)$ **OR** $(\text{DTI} \le 0.35 \text{ AND } \text{LTV} \le 0.90)$
- **Rejected (Tier 3):** All other combinations. 

Write modular helper functions: `calculate_dti(debt, income)` and `calculate_ltv(loan, collateral)`to help you classify the risk. Then, write a main evaluation function `evaluate_loan(income, debt, loan, collateral)` that calls the helper functions and uses boolean operators (`and`, `or`, `not`) with conditionals to determine eligibility. Include validation: If any financial input is $\le 0$, return `"Invalid Input Values"`.

Finally, make a menu taking income, debt, loan and collateral as user inputs. and printing the DTI, LTV and a decision.

Runs should look like this (denoting user input with `>`):

```
Provide the monthly income
> 5000
Provide the monthly debt
> 1200
Provide the requested loan
> 150000
Provide the collateral value
> 200000
DTI: 0.24 | LTV: 0.75 | Decision: Approved (Tier 1)
```

```
Provide the monthly income
> 4000
Provide the monthly debt
> 1700
Provide the requested loan
> 170000
Provide the collateral value
> 200000
DTI: 0.425 | LTV: 0.85 | Decision: Rejected (Tier 3)
```

## 🔴 Challenge 4 Choice-Based Text Adventure Game Engine

Build a text-driven interactive story or mini RPG combat calculator that processes a player's choices and combat stats through a series of chained functions!

### Scenario: The Dungeon Encounter

A player encounters a monster. The player can choose an action: `"attack"`, `"magic"`, or `"heal"`.

### Game Rules

1. **Player Stats:** `health` (0–100), `mana` (0–50), `attack_power`.
2. **Monster Stats:** `monster_health` (0–100), `monster_attack`.
3. **Actions:**
    - `"attack"`: Deals player's `attack_power` to monster. Monster counter-attacks for full `monster_attack`.
    - `"magic"`: Costs 15 `mana`. Deals $2.5 \times$ `attack_power` to the monster. Monster counter-attacks for half `monster_attack`. (If player has $< 15$ mana, the spell fails, player loses turn, and monster hits for full attack!).
    - `"heal"`: Restores 30 `health` (max cap 100). Monster counter-attacks for half `monster_attack`.

### Objective
Write a function `turn_resolution(player_hp, player_mana, player_atk, monster_hp, monster_atk, choice)` that calculates and prints the resulting state after one round of combat.

#### Requirements
- Break down the logic into clear helper functions (e.g., `calculate_damage()`, `apply_healing()`, `check_battle_status()`).
- Ensure player health cannot exceed 100 or fall below 0.
- Handle invalid action strings gracefully.
- Determine the battle outcome status at the end of the round: `"VICTORY"`, `"DEFEAT"`, `"MUTUAL DEFEAT"`, or `"Battle Continues"`.
