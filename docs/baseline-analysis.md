# Baseline Analysis and Design Model

## 1. Project Overview

**Project:** Supermarket Receipt Refactoring Kata  
**Group:** 7  
**Repository:** https://github.com/AsimJuna/SCD-Group-7-Refactoring  
**Refactoring Focus:** Duplicated Pricing Logic and Extract Pricing Rules

The purpose of this project is to improve the internal structure of an existing supermarket receipt application without changing its externally observable behavior.

The current implementation supports four special offers:

- Three products for the price of two.
- Percentage-based discounts.
- Two products for a fixed amount.
- Five products for a fixed amount.

The main objective is to separate pricing rules from the shopping cart logic, improve maintainability, and make the system easier to extend.

## 2. Baseline Testing

Before making any refactoring changes, characterization tests were executed to record the existing system behavior.

**Testing framework:** Pytest  
**Test file:** `python_pytest/tests/test_supermarket.py`

The following scenarios are currently covered:

| Test Case | Purpose | Result |
|---|---|---|
| Product without matching offer | Verifies normal pricing when no offer applies | PASSED |
| Ten percent discount | Verifies percentage-based discount calculation | PASSED |
| Three-for-two offer | Verifies the three-for-two pricing rule | PASSED |
| Two-for-amount offer | Verifies a fixed-price offer for two products | PASSED |
| Five-for-amount offer | Verifies a fixed-price offer for five products | PASSED |

**Baseline test result: 5 passed, 0 failed.**

These tests provide a reference point for verifying that future refactoring operations preserve the existing behavior.

## 3. Identified Code Smells and Refactoring Techniques

### 3.1 Long Method

**Location:** `ShoppingCart.handle_offers()`

The `handle_offers()` method performs several responsibilities in one place. It retrieves product quantities, checks available offers, calculates discounts, and creates discount objects.

This makes the method lengthy and difficult to understand, test, and maintain.

**Proposed Refactoring Technique:** Extract Method

The offer-specific calculations will be separated into smaller methods or dedicated pricing-rule classes.

### 3.2 Complex Conditional Logic

**Location:** `ShoppingCart.handle_offers()`

The method contains multiple conditional statements that check different values of `SpecialOfferType`, including `THREE_FOR_TWO`, `TWO_FOR_AMOUNT`, `FIVE_FOR_AMOUNT`, and `TEN_PERCENT_DISCOUNT`.

Whenever a new pricing rule is introduced, additional conditional logic must be added to this method.

**Proposed Refactoring Technique:** Replace Conditional with Polymorphism

Different pricing rules will be represented by separate classes that implement their own discount-calculation behavior.

### 3.3 Duplicated Calculation Structure

**Location:** `ShoppingCart.handle_offers()`

The three-for-two and five-for-amount branches both calculate a discount by comparing the normal product cost with the promotional cost.

Although their formulas differ, the same general pricing-calculation structure is repeated.

This makes future changes to discount calculations more difficult and increases the possibility of inconsistent logic.

**Proposed Refactoring Technique:** Extract Method

Common calculation responsibilities will be extracted into reusable methods or pricing components where appropriate.

### 3.4 Primitive Obsession

**Location:** `Offer` class in `model_objects.py`

The `Offer` class uses a generic `argument` attribute to represent different types of pricing information.

For example, the argument represents a percentage for a percentage discount but represents a fixed promotional price for two-for-amount and five-for-amount offers.

The meaning of this value depends on the offer type, which makes the model less expressive.

**Proposed Refactoring Technique:** Replace Primitive with Object

Pricing information will be represented through more meaningful pricing-rule objects rather than relying on one generic argument.

### 3.5 Poor Encapsulation

**Location:** `ShoppingCart.items` and `ShoppingCart.product_quantities`

Both properties return their internal collections directly.

As a result, external classes can potentially modify the shopping cart's internal list or dictionary without using its defined methods.

This weakens data protection and makes the class harder to maintain.

**Proposed Refactoring Technique:** Encapsulate Collection

The internal collections will be protected by returning controlled copies or providing suitable access methods.

## 4. Baseline Design Observations

The current implementation has the following design responsibilities:

- `ShoppingCart` stores products and quantities and also contains the special-offer calculation logic.
- `Offer` stores the offer type, product, and a generic pricing argument.
- `Teller` manages offers and processes checkout operations.
- `Receipt` stores receipt items and discounts.
- `SupermarketCatalog` provides product prices.

The main design weakness is that pricing-rule calculations are concentrated inside `ShoppingCart`, rather than being represented as independent components.

## 5. Proposed Refactoring Direction

The improved design will aim to:

1. Separate pricing-rule calculations from `ShoppingCart`.
2. Introduce dedicated classes for individual pricing rules.
3. Reduce conditional statements in the checkout and offer-handling logic.
4. Improve encapsulation of shopping cart collections.
5. Preserve existing application behavior through characterization tests.

The improved object-oriented design model will be documented separately through a UML class diagram.

## 6. Conclusion

The baseline analysis identified five code smells that affect the maintainability, readability, and extensibility of the supermarket receipt application.

The existing characterization tests provide a foundation for safely improving the design. The planned refactoring will focus on extracting pricing rules into independent components while ensuring that all existing tests continue to pass.