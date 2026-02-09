"""
Python implementation of YT11_Hinnoittelulaskuri_kauppa pricing calculator for retail businesses.

This module provides programmatic access to the pricing calculation functionality
originally implemented in the YT11_Hinnoittelulaskuri_kauppa.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class RetailPricingCalculator:
    """
    A class representing a retail pricing calculator based on the 
    YT11_Hinnoittelulaskuri_kauppa template.
    This tool helps retailers determine optimal pricing strategies by calculating costs, 
    margins, and profits based on various input parameters.
    """
    
    def __init__(self, company_name: str = "Retail Pricing Co", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.products = {}  # Product information
        self.cost_structure = {}  # Cost structure for products
        self.pricing_models = {}  # Different pricing models
        self.competitor_prices = {}  # Competitor pricing data
        self.discount_models = {}  # Discount models
        self.profitability_analysis = {}  # Profitability calculations
        self.price_elasticity = {}  # Price elasticity factors
        self.seasonal_factors = {}  # Seasonal pricing adjustments
        self.customer_segments = {}  # Customer segment pricing
        self.sales_channels = {}  # Channel-specific pricing
        self.tax_rates = {}  # Tax rates for different products
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the pricing calculator with default values."""
        # Default cost structure
        self.cost_structure = {
            "direct_materials": 0.0,
            "direct_labor": 0.0,
            "manufacturing_overhead": 0.0,
            "indirect_costs": 0.0,
            "distribution_costs": 0.0,
            "marketing_costs": 0.0,
            "administrative_costs": 0.0,
            "other_costs": 0.0
        }
        
        # Default pricing models
        self.pricing_models = {
            "cost_plus": {"markup_percentage": 0.30},  # 30% markup
            "competitive": {"price_index": 1.0},  # Same as competitors
            "value_based": {"value_multiplier": 1.5},  # 1.5x perceived value
            "penetration": {"discount_percentage": 0.10},  # 10% below market
            "premium": {"premium_percentage": 0.20}  # 20% above market
        }
        
        # Default competitor prices
        self.competitor_prices = {
            "competitor_1": {"name": "Kilpailija 1", "avg_price": 0.0},
            "competitor_2": {"name": "Kilpailija 2", "avg_price": 0.0},
            "competitor_3": {"name": "Kilpailija 3", "avg_price": 0.0}
        }
        
        # Default discount models
        self.discount_models = {
            "volume_discount": {"threshold": 100, "discount_rate": 0.05},  # 5% over 100 units
            "loyalty_discount": {"discount_rate": 0.10},  # 10% for loyal customers
            "seasonal_discount": {"discount_rate": 0.15},  # 15% seasonal discount
            "promotional_discount": {"discount_rate": 0.20}  # 20% promotional discount
        }
        
        # Default tax rates (VAT)
        self.tax_rates = {
            "standard": 0.24,  # 24% standard VAT
            "reduced": 0.14,   # 14% reduced VAT
            "super_reduced": 0.10,  # 10% super reduced VAT
            "zero": 0.0        # 0% VAT
        }
        
        # Initialize seasonal factors (monthly)
        self.seasonal_factors = {
            "January": 1.0, "February": 1.0, "March": 1.0, "April": 1.0, 
            "May": 1.0, "June": 1.1, "July": 1.15, "August": 1.1, 
            "September": 1.0, "October": 1.0, "November": 0.95, "December": 1.2
        }
        
        # Initialize customer segments
        self.customer_segments = {
            "segment_1": {"name": "Segmentti 1", "pricing_multiplier": 1.0},
            "segment_2": {"name": "Segmentti 2", "pricing_multiplier": 1.05},
            "segment_3": {"name": "Segmentti 3", "pricing_multiplier": 0.95}
        }
        
        # Initialize sales channels
        self.sales_channels = {
            "online": {"name": "Online", "margin_addition": 0.05},
            "retail": {"name": "Retail Store", "margin_addition": 0.15},
            "wholesale": {"name": "Wholesale", "margin_addition": -0.10}
        }
    
    def add_product(self, product_id: str, name: str, base_cost: float, category: str = "General"):
        """Add a product to the pricing calculator."""
        self.products[product_id] = {
            "name": name,
            "base_cost": base_cost,
            "category": category,
            "markup_percentage": 0.30,  # Default 30% markup
            "target_margin": 0.25,  # Default 25% margin
            "estimated_volume": 0,
            "vat_rate": self.tax_rates["standard"],  # Default to standard VAT
            "seasonal_factor": 1.0,
            "competitor_price": 0.0,
            "customer_segment_pricing": {},
            "channel_pricing": {}
        }
        
        # Initialize customer segment and channel pricing
        for segment_id in self.customer_segments:
            self.products[product_id]["customer_segment_pricing"][segment_id] = 1.0
        
        for channel_id in self.sales_channels:
            self.products[product_id]["channel_pricing"][channel_id] = 1.0
    
    def set_product_cost(self, product_id: str, cost_type: str, amount: float):
        """Set a specific cost component for a product."""
        if product_id in self.products:
            if cost_type in self.cost_structure:
                self.cost_structure[cost_type] = amount
            else:
                raise ValueError(f"Unknown cost type: {cost_type}")
        else:
            raise ValueError(f"Unknown product ID: {product_id}")
    
    def set_competitor_price(self, competitor_id: str, name: str, avg_price: float):
        """Set the average price for a competitor."""
        if competitor_id in self.competitor_prices:
            self.competitor_prices[competitor_id]["name"] = name
            self.competitor_prices[competitor_id]["avg_price"] = avg_price
        else:
            raise ValueError(f"Unknown competitor ID: {competitor_id}")

    def set_pricing_model(self, product_id: str, model_name: str, value: float):
        """Set a parameter for a specific pricing model."""
        if product_id in self.products:
            if model_name in self.pricing_models:
                if isinstance(self.pricing_models[model_name], dict):
                    # Find the appropriate key in the model dictionary
                    for key in self.pricing_models[model_name]:
                        if key != "name":  # Skip the name field if present
                            self.pricing_models[model_name][key] = value
                            break
                else:
                    self.pricing_models[model_name] = value
            else:
                raise ValueError(f"Unknown pricing model: {model_name}")
        else:
            raise ValueError(f"Unknown product ID: {product_id}")
    
    def calculate_cost_plus_price(self, product_id: str) -> float:
        """Calculate price using cost-plus pricing model."""
        if product_id not in self.products:
            raise ValueError(f"Unknown product ID: {product_id}")
        
        product = self.products[product_id]
        total_cost = product["base_cost"]
        
        # Apply markup percentage
        markup_percentage = self.pricing_models["cost_plus"]["markup_percentage"]
        price_excl_vat = total_cost * (1 + markup_percentage)
        
        # Apply VAT
        vat_rate = product["vat_rate"]
        price_incl_vat = price_excl_vat * (1 + vat_rate)
        
        return price_incl_vat
    
    def calculate_competitive_price(self, product_id: str) -> float:
        """Calculate price based on competitive pricing model."""
        if product_id not in self.products:
            raise ValueError(f"Unknown product ID: {product_id}")
        
        product = self.products[product_id]
        base_cost = product["base_cost"]
        
        # Determine competitive price based on competitor data
        avg_competitor_price = np.mean([
            comp["avg_price"] for comp in self.competitor_prices.values() 
            if comp["avg_price"] > 0
        ]) if any(comp["avg_price"] > 0 for comp in self.competitor_prices.values()) else base_cost * 1.5
        
        # Apply competitive pricing index
        price_index = self.pricing_models["competitive"]["price_index"]
        competitive_price = avg_competitor_price * price_index
        
        # Ensure minimum profitability
        min_price = base_cost * (1 + product["target_margin"])
        final_price = max(competitive_price, min_price)
        
        # Apply VAT
        vat_rate = product["vat_rate"]
        price_incl_vat = final_price * (1 + vat_rate)
        
        return price_incl_vat
    
    def calculate_value_based_price(self, product_id: str, perceived_value: float = 1.0) -> float:
        """Calculate price based on value-based pricing model."""
        if product_id not in self.products:
            raise ValueError(f"Unknown product ID: {product_id}")
        
        product = self.products[product_id]
        base_cost = product["base_cost"]
        
        # Apply value multiplier
        value_multiplier = self.pricing_models["value_based"]["value_multiplier"]
        value_based_price = base_cost * value_multiplier * perceived_value
        
        # Apply VAT
        vat_rate = product["vat_rate"]
        price_incl_vat = value_based_price * (1 + vat_rate)
        
        return price_incl_vat
    
    def calculate_penetration_price(self, product_id: str) -> float:
        """Calculate price using market penetration pricing model."""
        if product_id not in self.products:
            raise ValueError(f"Unknown product ID: {product_id}")
        
        product = self.products[product_id]
        base_cost = product["base_cost"]
        
        # Calculate competitive price as baseline
        competitive_price = self.calculate_competitive_price(product_id)
        
        # Apply penetration discount
        discount_percentage = self.pricing_models["penetration"]["discount_percentage"]
        penetration_price = competitive_price * (1 - discount_percentage)
        
        # Ensure minimum profitability
        min_price = base_cost * (1 + product["target_margin"])
        final_price = max(penetration_price, min_price)
        
        # Apply VAT
        vat_rate = product["vat_rate"]
        price_incl_vat = final_price * (1 + vat_rate)
        
        return price_incl_vat
    
    def calculate_premium_price(self, product_id: str) -> float:
        """Calculate price using premium pricing model."""
        if product_id not in self.products:
            raise ValueError(f"Unknown product ID: {product_id}")
        
        product = self.products[product_id]
        base_cost = product["base_cost"]
        
        # Calculate competitive price as baseline
        competitive_price = self.calculate_competitive_price(product_id)
        
        # Apply premium percentage
        premium_percentage = self.pricing_models["premium"]["premium_percentage"]
        premium_price = competitive_price * (1 + premium_percentage)
        
        # Apply VAT
        vat_rate = product["vat_rate"]
        price_incl_vat = premium_price * (1 + vat_rate)
        
        return price_incl_vat
    
    def calculate_final_price(self, product_id: str, pricing_model: str = "cost_plus", 
                            quantity: int = 1, customer_segment: str = "segment_1", 
                            sales_channel: str = "online", month: str = "January",
                            perceived_value: float = 1.0) -> Dict:
        """Calculate the final price considering all factors."""
        if product_id not in self.products:
            raise ValueError(f"Unknown product ID: {product_id}")
        
        # Calculate base price based on selected pricing model
        if pricing_model == "cost_plus":
            base_price = self.calculate_cost_plus_price(product_id)
        elif pricing_model == "competitive":
            base_price = self.calculate_competitive_price(product_id)
        elif pricing_model == "value_based":
            base_price = self.calculate_value_based_price(product_id, perceived_value)
        elif pricing_model == "penetration":
            base_price = self.calculate_penetration_price(product_id)
        elif pricing_model == "premium":
            base_price = self.calculate_premium_price(product_id)
        else:
            raise ValueError(f"Unknown pricing model: {pricing_model}")
        
        # Apply customer segment pricing
        if customer_segment in self.customer_segments:
            segment_multiplier = self.products[product_id]["customer_segment_pricing"][customer_segment]
            base_price *= segment_multiplier
        else:
            raise ValueError(f"Unknown customer segment: {customer_segment}")
        
        # Apply sales channel pricing
        if sales_channel in self.sales_channels:
            channel_addition = self.sales_channels[sales_channel]["margin_addition"]
            base_price *= (1 + channel_addition)
        else:
            raise ValueError(f"Unknown sales channel: {sales_channel}")
        
        # Apply seasonal factor
        if month in self.seasonal_factors:
            seasonal_factor = self.seasonal_factors[month]
            base_price *= seasonal_factor
        else:
            raise ValueError(f"Unknown month: {month}")
        
        # Apply volume discount if applicable
        volume_threshold = self.discount_models["volume_discount"]["threshold"]
        volume_discount_rate = self.discount_models["volume_discount"]["discount_rate"]
        
        if quantity >= volume_threshold:
            base_price *= (1 - volume_discount_rate)
        
        # Calculate profitability metrics
        product = self.products[product_id]
        cost = product["base_cost"]
        revenue = base_price * quantity
        total_cost = cost * quantity
        profit = revenue - total_cost
        profit_margin = profit / revenue if revenue != 0 else 0
        
        return {
            "product_id": product_id,
            "product_name": product["name"],
            "pricing_model": pricing_model,
            "base_price_per_unit": base_price,
            "quantity": quantity,
            "total_revenue": revenue,
            "total_cost": total_cost,
            "total_profit": profit,
            "profit_margin": profit_margin,
            "customer_segment": customer_segment,
            "sales_channel": sales_channel,
            "month": month
        }
    
    def calculate_break_even_volume(self, product_id: str, fixed_costs: float) -> int:
        """Calculate the break-even volume for a product."""
        if product_id not in self.products:
            raise ValueError(f"Unknown product ID: {product_id}")
        
        product = self.products[product_id]
        base_cost = product["base_cost"]
        
        # Calculate price using default pricing model (cost_plus)
        price_per_unit = self.calculate_cost_plus_price(product_id)
        
        # Calculate contribution margin per unit
        contribution_margin_per_unit = price_per_unit - base_cost
        
        if contribution_margin_per_unit <= 0:
            raise ValueError("Contribution margin is zero or negative, cannot calculate break-even")
        
        # Calculate break-even volume
        break_even_volume = fixed_costs / contribution_margin_per_unit
        
        return int(np.ceil(break_even_volume))
    
    def calculate_price_elasticity_impact(self, product_id: str, price_change_percentage: float) -> Dict:
        """Calculate the impact of price change on demand based on elasticity."""
        if product_id not in self.products:
            raise ValueError(f"Unknown product ID: {product_id}")
        
        # For simplicity, assume a default elasticity of -1.5 (demand decreases 1.5% for every 1% price increase)
        elasticity = -1.5
        
        # Calculate demand change based on elasticity
        demand_change_percentage = elasticity * price_change_percentage
        
        # Calculate new volume based on demand change
        current_volume = self.products[product_id]["estimated_volume"]
        new_volume = current_volume * (1 + demand_change_percentage / 100)
        
        # Calculate new revenue
        current_price = self.calculate_cost_plus_price(product_id)
        new_price = current_price * (1 + price_change_percentage / 100)
        new_revenue = new_price * new_volume
        
        # Calculate current revenue
        current_revenue = current_price * current_volume
        
        return {
            "price_change_percentage": price_change_percentage,
            "demand_change_percentage": demand_change_percentage,
            "current_volume": current_volume,
            "new_volume": new_volume,
            "current_revenue": current_revenue,
            "new_revenue": new_revenue,
            "revenue_change": new_revenue - current_revenue,
            "revenue_change_percentage": (new_revenue - current_revenue) / current_revenue * 100 if current_revenue != 0 else 0
        }
    
    def generate_pricing_report(self) -> Dict:
        """Generate a comprehensive pricing report."""
        report = {
            "company_name": self.company_name,
            "year": self.year,
            "products": {},
            "pricing_models": self.pricing_models,
            "competitor_analysis": self.competitor_prices,
            "cost_structure": self.cost_structure,
            "profitability_metrics": {},
            "break_even_analysis": {},
            "price_elasticity_analysis": {}
        }
        
        # Calculate metrics for each product
        for product_id, product in self.products.items():
            # Calculate prices using different models
            prices = {}
            for model in self.pricing_models:
                try:
                    if model == "value_based":
                        prices[model] = self.calculate_value_based_price(product_id)
                    else:
                        # Temporarily set model as active and calculate
                        original_models = self.pricing_models.copy()
                        active_model = {k: v for k, v in original_models.items() if isinstance(v, dict) and k == model}
                        if active_model:
                            prices[model] = self.calculate_final_price(product_id, model)["base_price_per_unit"]
                except:
                    # If calculation fails for any model, use cost plus as fallback
                    prices[model] = self.calculate_cost_plus_price(product_id)
            
            report["products"][product_id] = {
                "name": product["name"],
                "base_cost": product["base_cost"],
                "prices_by_model": prices,
                "recommended_price": self.calculate_cost_plus_price(product_id),
                "competitor_price": product["competitor_price"],
                "target_margin": product["target_margin"],
                "estimated_volume": product["estimated_volume"]
            }
            
            # Calculate profitability metrics
            recommended_price = report["products"][product_id]["recommended_price"]
            cost = product["base_cost"]
            revenue = recommended_price
            profit = revenue - cost
            profit_margin = profit / revenue if revenue != 0 else 0
            
            report["profitability_metrics"][product_id] = {
                "revenue_per_unit": revenue,
                "cost_per_unit": cost,
                "profit_per_unit": profit,
                "profit_margin": profit_margin
            }
            
            # Calculate break-even analysis
            try:
                fixed_costs = sum(self.cost_structure.values())  # Using total costs as proxy for fixed costs
                break_even_vol = self.calculate_break_even_volume(product_id, fixed_costs)
                report["break_even_analysis"][product_id] = {
                    "fixed_costs": fixed_costs,
                    "break_even_volume": break_even_vol,
                    "break_even_revenue": break_even_vol * recommended_price
                }
            except ValueError as e:
                report["break_even_analysis"][product_id] = {
                    "error": str(e)
                }
        
        return report
    
    def save_to_json(self, filepath: str):
        """Save the pricing calculator data to a JSON file."""
        report = self.generate_pricing_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load pricing calculator data from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.year = data.get("year", self.year)
        self.products = data.get("products", self.products)
        self.pricing_models = data.get("pricing_models", self.pricing_models)
        self.competitor_prices = data.get("competitor_analysis", self.competitor_prices)
        self.cost_structure = data.get("cost_structure", self.cost_structure)


def create_sample_calculator() -> RetailPricingCalculator:
    """Create a sample retail pricing calculator with example data."""
    calc = RetailPricingCalculator(company_name="Sample Retail Pricing Oy", year=2026)
    
    # Add some example products
    calc.add_product("product_1", "Esimerkkituote 1", 50.0, "Category A")
    calc.add_product("product_2", "Esimerkkituote 2", 75.0, "Category B")
    calc.add_product("product_3", "Esimerkkituote 3", 100.0, "Category C")
    
    # Set example competitor prices
    calc.competitor_prices["competitor_1"]["avg_price"] = 75.0
    calc.competitor_prices["competitor_2"]["avg_price"] = 80.0
    calc.competitor_prices["competitor_3"]["avg_price"] = 70.0
    
    # Set example cost structure
    calc.cost_structure["direct_materials"] = 20.0
    calc.cost_structure["direct_labor"] = 15.0
    calc.cost_structure["manufacturing_overhead"] = 10.0
    calc.cost_structure["distribution_costs"] = 5.0
    calc.cost_structure["marketing_costs"] = 8.0
    calc.cost_structure["administrative_costs"] = 7.0
    
    # Set example target margins for products
    calc.products["product_1"]["target_margin"] = 0.30  # 30% target margin
    calc.products["product_2"]["target_margin"] = 0.25  # 25% target margin
    calc.products["product_3"]["target_margin"] = 0.35  # 35% target margin
    
    # Set estimated volumes
    calc.products["product_1"]["estimated_volume"] = 1000
    calc.products["product_2"]["estimated_volume"] = 800
    calc.products["product_3"]["estimated_volume"] = 600
    
    # Set competitor prices for products
    calc.products["product_1"]["competitor_price"] = 75.0
    calc.products["product_2"]["competitor_price"] = 100.0
    calc.products["product_3"]["competitor_price"] = 140.0
    
    # Set customer segment pricing multipliers
    calc.products["product_1"]["customer_segment_pricing"]["segment_2"] = 1.05  # 5% premium for segment 2
    calc.products["product_1"]["customer_segment_pricing"]["segment_3"] = 0.95  # 5% discount for segment 3
    
    # Set channel pricing additions
    calc.products["product_1"]["channel_pricing"]["retail"] = 1.15  # 15% addition for retail
    calc.products["product_1"]["channel_pricing"]["wholesale"] = 0.90  # 10% reduction for wholesale
    
    return calc


if __name__ == "__main__":
    # Example usage
    print("YT11 Hinnoittelulaskuri kauppa - Retail Pricing Calculator")
    print("=" * 60)
    
    # Create a sample pricing calculator
    sample_calc = create_sample_calculator()
    
    # Generate and display the pricing report
    report = sample_calc.generate_pricing_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Year: {report['year']}")
    
    print(f"\nProducts and Pricing:")
    for prod_id, prod_info in list(report['products'].items())[:3]:  # Limit to first 3 products
        print(f"\nProduct: {prod_info['name']}")
        print(f"  Base Cost: €{prod_info['base_cost']:.2f}")
        print(f"  Recommended Price: €{prod_info['recommended_price']:.2f}")
        print(f"  Competitor Price: €{prod_info['competitor_price']:.2f}")
        print(f"  Target Margin: {prod_info['target_margin']:.1%}")
        print(f"  Estimated Volume: {prod_info['estimated_volume']}")
        
        print(f"  Prices by Model:")
        for model, price in prod_info['prices_by_model'].items():
            print(f"    {model}: €{price:.2f}")
        
        if prod_id in report['profitability_metrics']:
            metrics = report['profitability_metrics'][prod_id]
            print(f"  Profitability:")
            print(f"    Revenue per unit: €{metrics['revenue_per_unit']:.2f}")
            print(f"    Cost per unit: €{metrics['cost_per_unit']:.2f}")
            print(f"    Profit per unit: €{metrics['profit_per_unit']:.2f}")
            print(f"    Profit margin: {metrics['profit_margin']:.1%}")
        
        if prod_id in report['break_even_analysis']:
            be_info = report['break_even_analysis'][prod_id]
            if 'error' not in be_info:
                print(f"  Break-even:")
                print(f"    Volume: {be_info['break_even_volume']}")
                print(f"    Revenue: €{be_info['break_even_revenue']:,.2f}")
    
    print(f"\nPricing Models:")
    for model_name, model_info in report['pricing_models'].items():
        if isinstance(model_info, dict):
            print(f"  {model_name}: {model_info}")
        else:
            print(f"  {model_name}: {model_info}")
    
    print(f"\nCompetitor Analysis:")
    for comp_id, comp_info in report['competitor_analysis'].items():
        print(f"  {comp_info['name']}: €{comp_info['avg_price']:.2f}")
    
    # Calculate a specific price example
    print(f"\nSpecific Price Calculation Example:")
    price_result = sample_calc.calculate_final_price(
        product_id="product_1",
        pricing_model="cost_plus",
        quantity=50,
        customer_segment="segment_2",
        sales_channel="retail",
        month="June"
    )
    
    print(f"Product: {price_result['product_name']}")
    print(f"Pricing Model: {price_result['pricing_model']}")
    print(f"Base Price per Unit: €{price_result['base_price_per_unit']:.2f}")
    print(f"Quantity: {price_result['quantity']}")
    print(f"Total Revenue: €{price_result['total_revenue']:.2f}")
    print(f"Total Cost: €{price_result['total_cost']:.2f}")
    print(f"Total Profit: €{price_result['total_profit']:.2f}")
    print(f"Profit Margin: {price_result['profit_margin']:.1%}")
    print(f"Customer Segment: {price_result['customer_segment']}")
    print(f"Sales Channel: {price_result['sales_channel']}")
    print(f"Month: {price_result['month']}")
    
    # Calculate break-even example
    print(f"\nBreak-even Analysis Example:")
    try:
        fixed_costs_example = 50000  # Example fixed costs
        be_volume = sample_calc.calculate_break_even_volume("product_1", fixed_costs_example)
        recommended_price = sample_calc.calculate_cost_plus_price("product_1")
        be_revenue = be_volume * recommended_price
        
        print(f"Fixed Costs: €{fixed_costs_example:,.2f}")
        print(f"Break-even Volume: {be_volume} units")
        print(f"Break-even Revenue: €{be_revenue:,.2f}")
    except ValueError as e:
        print(f"Error in break-even calculation: {e}")
    
    # Calculate price elasticity example
    print(f"\nPrice Elasticity Analysis Example:")
    elasticity_result = sample_calc.calculate_price_elasticity_impact("product_1", 5.0)  # 5% price increase
    print(f"Price Change: {elasticity_result['price_change_percentage']:.1f}%")
    print(f"Demand Change: {elasticity_result['demand_change_percentage']:.1f}%")
    print(f"Current Volume: {elasticity_result['current_volume']}")
    print(f"New Volume: {elasticity_result['new_volume']:.0f}")
    print(f"Current Revenue: €{elasticity_result['current_revenue']:,.2f}")
    print(f"New Revenue: €{elasticity_result['new_revenue']:,.2f}")
    print(f"Revenue Change: €{elasticity_result['revenue_change']:,.2f} ({elasticity_result['revenue_change_percentage']:.1f}%)")
    
    # Save the calculator to a JSON file
    sample_calc.save_to_json("sample_retail_pricing_calculator.json")
    print(f"\nRetail pricing calculator saved to 'sample_retail_pricing_calculator.json'")