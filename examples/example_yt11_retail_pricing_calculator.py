#!/usr/bin/env python
"""
Example script demonstrating the use of the YT11 retail pricing calculator.

This script shows how to use the RetailPricingCalculator class to perform
retail pricing calculations based on the YT11_Hinnoittelulaskuri_kauppa.xlsx template.
"""

from yt11_hinnoittelulaskuri_kauppa import RetailPricingCalculator


def main():
    print("YT11 Hinnoittelulaskuri kauppa - Retail Pricing Calculator Example")
    print("=" * 70)
    
    # Create a new retail pricing calculator instance
    calc = RetailPricingCalculator(company_name="Example Retail Co", year=2026)
    
    # Add a product to the calculator
    calc.add_product(
        product_id="example_product",
        name="Esimerkkiproducti",
        base_cost=50.0,  # Base cost of the product
        category="Electronics",
        target_margin=0.30,  # 30% target margin
        estimated_volume=1000,
        competitor_price=75.0
    )
    
    # Set competitor prices
    calc.set_competitor_price("competitor_1", "Kilpailija 1", 70.0)
    calc.set_competitor_price("competitor_2", "Kilpailija 2", 80.0)
    calc.set_competitor_price("competitor_3", "Kilpailija 3", 75.0)
    
    # Calculate price using different pricing models
    print("\nCalculating prices using different pricing models:")
    print("-" * 50)
    
    # Cost-plus pricing
    cost_plus_price = calc.calculate_cost_plus_price("example_product")
    print(f"Cost-plus pricing: €{cost_plus_price:.2f}")
    
    # Competitive pricing
    competitive_price = calc.calculate_competitive_price("example_product")
    print(f"Competitive pricing: €{competitive_price:.2f}")
    
    # Value-based pricing
    value_based_price = calc.calculate_value_based_price("example_product", perceived_value=1.2)
    print(f"Value-based pricing: €{value_based_price:.2f}")
    
    # Penetration pricing
    penetration_price = calc.calculate_penetration_price("example_product")
    print(f"Penetration pricing: €{penetration_price:.2f}")
    
    # Premium pricing
    premium_price = calc.calculate_premium_price("example_product")
    print(f"Premium pricing: €{premium_price:.2f}")
    
    # Calculate final price considering various factors
    print("\nCalculating final price with all factors considered:")
    print("-" * 50)
    
    final_price = calc.calculate_final_price(
        product_id="example_product",
        pricing_model="cost_plus",
        quantity=100,
        customer_segment="segment_1",
        sales_channel="online",
        month="January",
        perceived_value=1.0
    )
    
    print(f"Product: {final_price['product_name']}")
    print(f"Base Price per Unit: €{final_price['base_price_per_unit']:.2f}")
    print(f"Quantity: {final_price['quantity']}")
    print(f"Total Revenue: €{final_price['total_revenue']:.2f}")
    print(f"Total Cost: €{final_price['total_cost']:.2f}")
    print(f"Total Profit: €{final_price['total_profit']:.2f}")
    print(f"Profit Margin: {final_price['profit_margin']:.2%}")
    print(f"Customer Segment: {final_price['customer_segment']}")
    print(f"Sales Channel: {final_price['sales_channel']}")
    print(f"Month: {final_price['month']}")
    
    # Generate and display a full pricing report
    print("\nGenerating full pricing report:")
    print("-" * 50)
    
    report = calc.generate_pricing_report()
    
    print(f"Company: {report['company_name']}")
    print(f"Year: {report['year']}")
    print(f"Number of products: {len(report['products'])}")
    
    # Show profitability metrics for the example product
    if "example_product" in report['profitability_metrics']:
        metrics = report['profitability_metrics']["example_product"]
        print(f"\nProfitability Metrics for Example Product:")
        print(f"  Revenue per unit: €{metrics['revenue_per_unit']:.2f}")
        print(f"  Cost per unit: €{metrics['cost_per_unit']:.2f}")
        print(f"  Profit per unit: €{metrics['profit_per_unit']:.2f}")
        print(f"  Profit margin: {metrics['profit_margin']:.2%}")
    
    # Calculate break-even analysis
    print(f"\nBreak-even Analysis:")
    try:
        fixed_costs = 25000  # Example fixed costs
        be_volume = calc.calculate_break_even_volume("example_product", fixed_costs)
        recommended_price = cost_plus_price  # Using cost-plus price as example
        be_revenue = be_volume * recommended_price
        
        print(f"Fixed Costs: €{fixed_costs:,.2f}")
        print(f"Break-even Volume: {be_volume} units")
        print(f"Break-even Revenue: €{be_revenue:,.2f}")
    except ValueError as e:
        print(f"Error in break-even calculation: {e}")
    
    # Calculate price elasticity impact
    print(f"\nPrice Elasticity Impact Analysis:")
    elasticity_result = calc.calculate_price_elasticity_impact("example_product", 10.0)  # 10% price change
    print(f"Price Change: {elasticity_result['price_change_percentage']:.1f}%")
    print(f"Demand Change: {elasticity_result['demand_change_percentage']:.1f}%")
    print(f"Current Volume: {elasticity_result['current_volume']}")
    print(f"New Volume: {elasticity_result['new_volume']:.0f}")
    print(f"Revenue Change: €{elasticity_result['revenue_change']:,.2f} ({elasticity_result['revenue_change_percentage']:.1f}%)")
    
    # Save the calculator to a JSON file
    calc.save_to_json("example_retail_pricing_calculator.json")
    print(f"\nRetail pricing calculator saved to 'example_retail_pricing_calculator.json'")


if __name__ == "__main__":
    main()