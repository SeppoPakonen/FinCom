"""
Python implementation of L9_Maksukehotus payment demand notice template.

This module provides programmatic access to the payment demand notice functionality
originally implemented in the L9_Maksukehotus.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class PaymentDemandNotice:
    """
    A class representing a payment demand notice based on the L9_Maksukehotus template.
    This tool helps businesses create formal notices for overdue payments that have not been 
    resolved through previous reminders, indicating the next steps in the collection process 
    and potential legal consequences.
    """
    
    def __init__(self, company_name: str = "Payment Demand Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.demand_date = datetime.now().strftime('%d.%m.%Y')
        self.sender_info = {}  # Sender information
        self.recipient_info = {}  # Recipient information
        self.outstanding_invoices = []  # List of seriously overdue invoices
        self.payment_terms = {}  # Payment terms and conditions
        self.late_payment_interest = {}  # Late payment interest calculations
        self.demand_level = 1  # Level of demand (formal demand, legal notice)
        self.total_outstanding = 0.0  # Total outstanding amount
        self.total_with_interest = 0.0  # Total with late payment interest and penalties
        self.legal_compliance = {}  # Compliance with Finnish legal requirements
        self.collection_process = {}  # Collection process tracking
        self.customer_payment_history = {}  # Customer payment history
        self.interest_calculations = {}  # Detailed interest calculations
        self.penalty_fees = {}  # Penalty fees and charges
        self.legal_consequences = {}  # Potential legal consequences
        self.payment_arrangements = {}  # Potential payment arrangements
        self.accounting_integration = {}  # Integration with accounting systems
        self.reporting_metrics = {}  # Reporting and analytics metrics
        self.demand_language = {}  # Formal legal language for demands
        self.legal_proceedings_info = {}  # Information for potential legal proceedings
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the payment demand notice with default values."""
        # Default sender information
        self.sender_info = {
            "name": self.company_name,
            "address": "",
            "business_id": "",
            "contact_person": "",
            "phone": "",
            "email": "",
            "bank_account_info": {
                "iban": "",
                "bic": "",
                "account_number": ""
            }
        }
        
        # Default recipient information
        self.recipient_info = {
            "name": "",
            "address": "",
            "business_id": "",
            "contact_person": "",
            "phone": "",
            "email": ""
        }
        
        # Default payment terms
        self.payment_terms = {
            "standard_payment_period": 14,  # days
            "late_payment_interest_rate": 0.08,  # 8% per annum
            "demand_fee": 10.00  # Fixed fee per demand
        }
        
        # Default penalty fees
        self.penalty_fees = {
            "collection_fee": 25.00,  # Fixed collection fee
            "legal_proceedings_fee": 50.00,  # Fee if legal action is initiated
            "additional_penalty_rate": 0.05  # Additional penalty rate per annum
        }
        
        # Default legal consequences
        self.legal_consequences = {
            "potential_legal_action": True,
            "credit_registry_reporting": True,
            "interest_accumulation_continues": True,
            "additional_penalty_applied": True
        }
        
        # Default legal compliance
        self.legal_compliance = {
            "complies_with_finnish_law": True,
            "interest_calculation_compliant": True,
            "demand_content_compliant": True,
            "proper_severity_level": True
        }
        
        # Default customer payment history
        self.customer_payment_history = {
            "payment_frequency": "irregular",
            "average_days_overdue": 30,
            "previous_reminders_count": 2,
            "payment_behavior_notes": "Customer has not responded to previous reminders"
        }
        
        # Default collection process
        self.collection_process = {
            "status": "formal_demand_issued",
            "last_contact_date": "",
            "next_action_date": "",
            "actions_taken": []
        }
        
        # Default demand language
        self.demand_language = {
            "severity_level": "formal",
            "legal_references": ["Finnish Debt Collection Act", "Commercial Code"],
            "deadline_emphasis": "strict",
            "consequence_warnings": True
        }
        
        # Default reporting metrics
        self.reporting_metrics = {
            "days_since_original_due_date": 0,
            "payment_probability_after_demand": 0.3,  # Estimated probability of payment after formal demand
            "collection_effort_score": 0  # How much effort has been put into collection
        }
    
    def add_seriously_overdue_invoice(self, invoice_number: str, original_amount: float, 
                                      invoice_date: str, due_date: str, days_overdue: int, 
                                      interest_rate: float = 0.11, penalty_fees: float = 0.0):
        """Add a seriously overdue invoice to the demand notice."""
        # Calculate interest based on days overdue
        interest_amount = self._calculate_interest(original_amount, days_overdue, interest_rate)
        
        # Calculate total amount due with penalties
        total_due = original_amount + interest_amount + penalty_fees
        
        invoice = {
            "invoice_number": invoice_number,
            "original_amount": original_amount,
            "invoice_date": invoice_date,
            "due_date": due_date,
            "days_overdue": days_overdue,
            "interest_rate": interest_rate,
            "interest_amount": interest_amount,
            "penalty_fees": penalty_fees,
            "total_due": total_due
        }
        
        self.outstanding_invoices.append(invoice)
        return invoice
    
    def _calculate_interest(self, principal: float, days_overdue: int, interest_rate: float) -> float:
        """Calculate interest on overdue amount."""
        # Simple interest calculation: principal * rate * time
        # Assuming interest_rate is annual rate
        interest = principal * interest_rate * (days_overdue / 365)
        return interest
    
    def set_sender_info(self, name: str, address: str, business_id: str = "", 
                       contact_person: str = "", phone: str = "", email: str = "",
                       iban: str = "", bic: str = ""):
        """Set sender information."""
        self.sender_info = {
            "name": name,
            "address": address,
            "business_id": business_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email,
            "bank_account_info": {
                "iban": iban,
                "bic": bic,
                "account_number": ""
            }
        }
    
    def set_recipient_info(self, name: str, address: str, business_id: str = "", 
                          contact_person: str = "", phone: str = "", email: str = ""):
        """Set recipient information."""
        self.recipient_info = {
            "name": name,
            "address": address,
            "business_id": business_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email
        }
    
    def set_payment_terms(self, standard_period: int = 14, late_interest_rate: float = 0.08, 
                         demand_fee: float = 10.00):
        """Set payment terms."""
        self.payment_terms = {
            "standard_payment_period": standard_period,
            "late_payment_interest_rate": late_interest_rate,
            "demand_fee": demand_fee
        }
    
    def set_penalty_fees(self, collection_fee: float = 25.00, legal_proceedings_fee: float = 50.00, 
                        additional_penalty_rate: float = 0.05):
        """Set penalty fees and charges."""
        self.penalty_fees = {
            "collection_fee": collection_fee,
            "legal_proceedings_fee": legal_proceedings_fee,
            "additional_penalty_rate": additional_penalty_rate
        }
    
    def set_customer_payment_history(self, frequency: str, avg_days_overdue: int, 
                                    previous_reminders: int, notes: str = ""):
        """Set customer payment history information."""
        self.customer_payment_history = {
            "payment_frequency": frequency,
            "average_days_overdue": avg_days_overdue,
            "previous_reminders_count": previous_reminders,
            "payment_behavior_notes": notes
        }
    
    def set_collection_process(self, status: str, last_contact: str = "", next_action: str = ""):
        """Set collection process information."""
        self.collection_process = {
            "status": status,
            "last_contact_date": last_contact,
            "next_action_date": next_action,
            "actions_taken": []
        }
    
    def add_collection_action(self, action_date: str, action_type: str, description: str):
        """Add a collection action to the log."""
        action = {
            "date": action_date,
            "type": action_type,
            "description": description
        }
        self.collection_process["actions_taken"].append(action)
    
    def calculate_total_outstanding(self) -> float:
        """Calculate the total outstanding amount."""
        total = sum(inv["total_due"] for inv in self.outstanding_invoices)
        self.total_outstanding = total
        return total
    
    def calculate_total_with_penalties(self) -> float:
        """Calculate the total amount including interest and penalties."""
        total = sum(inv["total_due"] for inv in self.outstanding_invoices)
        self.total_with_interest = total
        return total
    
    def determine_demand_level(self) -> int:
        """Determine the appropriate demand level based on days overdue and previous actions."""
        if not self.outstanding_invoices:
            return 0
        
        # Use the maximum days overdue to determine level
        max_days_overdue = max(inv["days_overdue"] for inv in self.outstanding_invoices)
        prev_reminders = self.customer_payment_history["previous_reminders_count"]
        
        if max_days_overdue <= 30 and prev_reminders <= 1:
            return 1  # First formal demand
        elif max_days_overdue <= 60 and prev_reminders <= 2:
            return 2  # Second demand with stronger language
        elif max_days_overdue <= 90 and prev_reminders <= 3:
            return 3  # Final demand before legal action
        else:
            return 4  # Legal proceedings initiated
    
    def generate_demand_message(self) -> str:
        """Generate a formal demand message based on the template."""
        level = self.determine_demand_level()
        
        if level == 1:
            level_text = "Maksukehotus"
            severity = "muodollinen"
        elif level == 2:
            level_text = "Toinen maksukehotus"
            severity = "vahvempi"
        elif level == 3:
            level_text = "Viimeinen maksukehotus"
            severity = "viimeinen ennen oikeustoimia"
        else:
            level_text = "Lopullinen maksukehotus"
            severity = "oikeustoimiin siirtyminen"
        
        message = f"""
{level_text}
{datetime.now().strftime('%d.%m.%Y')}

{self.sender_info['name']}
{self.sender_info['address']}

{self.recipient_info['name']}
{self.recipient_info['address']}

Hei,

Maksumuistutuksestamme huolimatta saatavamme on kirjanpitomme mukaan edelleen avoimena.
Saamisemme tulee suorittaa välittömästi tai viimeistään alla mainittuna eräpäivänä yhtiömme tilille.
Muussa tapauksessa perimme saatavamme oikeudenkäyntiteitse, josta teille aiheutuu merkittäviä lisäkuluja ja lisäksi merkintä maksuhäiriörekisteriin.

Seuraavat erääntyneet saatavamme ovat edelleen avoimena:

{"Laskun numero":<15} {"Alkuperäinen summa":<20} {"Eräpäivä":<12} {"Viivästyskorko":<15} {"Maksamaton saldo":<20}
"""
        
        for invoice in self.outstanding_invoices:
            message += f"{invoice['invoice_number']:<15} {invoice['original_amount']:<20.2f} {invoice['due_date']:<12} {invoice['interest_amount']:<15.2f} {invoice['total_due']:<20.2f}\n"
        
        total = self.calculate_total_with_penalties()
        message += f"\nSaamisemme yhteensä: {total:.2f} €"
        
        message += f"""

Maksuviite:
{self.sender_info['bank_account_info']['iban']}
{self.sender_info['bank_account_info']['bic']}

Yrityksen nimi: {self.sender_info['name']}
Y-tunnus: {self.sender_info['business_id']}
Puhelin: {self.sender_info['phone']}
Sähköposti: {self.sender_info['email']}

Tämä on virallinen maksukehotus. Pyydämme Teitä hoitamaan maksun mahdollisimman pian.
"""
        
        return message
    
    def generate_demand_report(self) -> Dict:
        """Generate a comprehensive payment demand report."""
        level = self.determine_demand_level()
        
        report = {
            "company_name": self.company_name,
            "demand_date": self.demand_date,
            "sender_info": self.sender_info,
            "recipient_info": self.recipient_info,
            "outstanding_invoices": self.outstanding_invoices,
            "payment_terms": self.payment_terms,
            "demand_level": level,
            "total_outstanding": self.calculate_total_outstanding(),
            "total_with_interest": self.calculate_total_with_penalties(),
            "customer_payment_history": self.customer_payment_history,
            "collection_process": self.collection_process,
            "interest_calculations": self.interest_calculations,
            "penalty_fees": self.penalty_fees,
            "legal_consequences": self.legal_consequences,
            "legal_compliance": self.legal_compliance,
            "demand_language": self.demand_language,
            "reporting_metrics": {
                **self.reporting_metrics,
                "demand_level": level,
                "max_days_overdue": max([inv["days_overdue"] for inv in self.outstanding_invoices]) if self.outstanding_invoices else 0,
                "payment_probability_after_demand": self._estimate_payment_probability(level)
            }
        }
        
        return report
    
    def _estimate_payment_probability(self, demand_level: int) -> float:
        """Estimate the probability of payment based on demand level."""
        # Simplified estimation - in reality, this would be based on historical data
        if demand_level == 1:
            return 0.40  # 40% chance after first formal demand
        elif demand_level == 2:
            return 0.25  # 25% chance after second demand
        elif demand_level == 3:
            return 0.15  # 15% chance after final notice
        else:
            return 0.05  # 5% chance after legal proceedings initiated
    
    def generate_collection_strategy(self) -> Dict:
        """Generate a collection strategy based on the current situation."""
        level = self.determine_demand_level()
        total_amount = self.calculate_total_with_penalties()
        
        strategy = {
            "recommended_action": self._get_recommended_action(level),
            "negotiation_options": self._get_negotiation_options(total_amount),
            "follow_up_schedule": self._get_follow_up_schedule(level),
            "escalation_recommendation": self._get_escalation_recommendation(level),
            "payment_probability": self._estimate_payment_probability(level)
        }
        
        return strategy
    
    def _get_recommended_action(self, level: int) -> str:
        """Get recommended action based on demand level."""
        if level == 1:
            return "Send formal payment demand with clear payment deadline"
        elif level == 2:
            return "Increase pressure with stronger language and mention potential legal consequences"
        elif level == 3:
            return "Issue final notice with explicit legal action timeline"
        else:
            return "Initiate legal proceedings or refer to collection agency"
    
    def _get_negotiation_options(self, total_amount: float) -> List[str]:
        """Get potential negotiation options."""
        options = []
        
        if total_amount > 10000:  # For larger amounts
            options.append("Offer payment plan with monthly installments")
            options.append("Negotiate partial payment with settlement discount")
        
        if total_amount > 5000:
            options.append("Accept partial payment toward outstanding balance")
        
        options.append("Extend payment terms with additional interest")
        options.append("Waive penalty fees if full payment made within 7 days")
        
        return options
    
    def _get_follow_up_schedule(self, level: int) -> List[Dict]:
        """Get recommended follow-up schedule."""
        schedule = []
        
        if level == 1:
            schedule.append({"days": 7, "action": "Follow up with phone call"})
            schedule.append({"days": 14, "action": "Send certified letter if no response"})
        elif level == 2:
            schedule.append({"days": 3, "action": "Direct phone contact"})
            schedule.append({"days": 7, "action": "Prepare for legal action"})
        elif level == 3:
            schedule.append({"days": 1, "action": "Final demand via certified mail"})
            schedule.append({"days": 7, "action": "Initiate legal proceedings if no response"})
        else:
            schedule.append({"days": 0, "action": "Proceed with legal action"})
        
        return schedule
    
    def _get_escalation_recommendation(self, level: int) -> str:
        """Get escalation recommendation."""
        if level == 1:
            return "Continue with formal collection process"
        elif level == 2:
            return "Escalate to final notice with legal consequences warning"
        elif level == 3:
            return "Prepare for legal action or collection agency referral"
        else:
            return "Proceed with legal action or collection agency"
    
    def save_to_json(self, filepath: str):
        """Save the payment demand notice to a JSON file."""
        report = self.generate_demand_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a payment demand notice from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.demand_date = data.get("demand_date", self.demand_date)
        self.sender_info = data.get("sender_info", self.sender_info)
        self.recipient_info = data.get("recipient_info", self.recipient_info)
        self.outstanding_invoices = data.get("outstanding_invoices", self.outstanding_invoices)
        self.payment_terms = data.get("payment_terms", self.payment_terms)
        self.demand_level = data.get("demand_level", self.demand_level)
        self.total_outstanding = data.get("total_outstanding", self.total_outstanding)
        self.total_with_interest = data.get("total_with_interest", self.total_with_interest)


def create_sample_demand() -> PaymentDemandNotice:
    """Create a sample payment demand notice with example data."""
    demand = PaymentDemandNotice(company_name="Sample Payment Demand Oy", year=2026)
    
    # Set sender information
    demand.set_sender_info(
        name="Sample Payment Demand Oy",
        address="Kehotuskatu 15, 33100 Tampere",
        business_id="1234567-8",
        contact_person="Kehotus: Kari Kehotus",
        phone="0500 123 456",
        email="kari.kehotus@samplepaymentdemand.fi",
        iban="FI0000000012345678",
        bic="SAMPLEBIC"
    )
    
    # Set recipient information
    demand.set_recipient_info(
        name="Maksaja Oy",
        address="Maksajankatu 20, 00100 Helsinki",
        business_id="8765432-1",
        contact_person="Maksaja: Maija Maksaja",
        phone="0400 987 654",
        email="maija.maksaja@maksaja.fi"
    )
    
    # Add example seriously overdue invoices
    demand.add_seriously_overdue_invoice(
        invoice_number="INV-123465",
        original_amount=10000.00,
        invoice_date="2025-10-01",
        due_date="2025-11-01",
        days_overdue=94,  # As of Feb 3, 2026
        interest_rate=0.11,  # 11% interest rate from the spreadsheet
        penalty_fees=25.00  # Collection fee
    )
    
    demand.add_seriously_overdue_invoice(
        invoice_number="INV-123466",
        original_amount=5000.00,
        invoice_date="2025-11-15",
        due_date="2025-12-15",
        days_overdue=49,  # As of Feb 3, 2026
        interest_rate=0.11,
        penalty_fees=25.00
    )
    
    demand.add_seriously_overdue_invoice(
        invoice_number="INV-123467",
        original_amount=2500.00,
        invoice_date="2025-12-20",
        due_date="2026-01-20",
        days_overdue=14,  # As of Feb 3, 2026
        interest_rate=0.11,
        penalty_fees=15.00
    )
    
    # Set payment terms
    demand.set_payment_terms(
        standard_period=14,
        late_interest_rate=0.11,
        demand_fee=10.00
    )
    
    # Set penalty fees
    demand.set_penalty_fees(
        collection_fee=25.00,
        legal_proceedings_fee=50.00,
        additional_penalty_rate=0.05
    )
    
    # Set customer payment history
    demand.set_customer_payment_history(
        frequency="irregular",
        avg_days_overdue=45,
        previous_reminders=2,
        notes="Customer has not responded to previous payment reminders"
    )
    
    # Set collection process
    demand.set_collection_process(
        status="formal_demand_issued",
        last_contact="2026-01-28",
        next_action="2026-02-10"
    )
    
    # Add a collection action
    demand.add_collection_action(
        action_date="2026-01-28",
        action_type="formal_demand",
        description="Sent formal payment demand notice via certified mail"
    )
    
    return demand


if __name__ == "__main__":
    # Example usage
    print("L9 Maksukehotus - Payment Demand Notice Tool")
    print("=" * 50)
    
    # Create a sample payment demand notice
    sample_demand = create_sample_demand()
    
    # Generate and display the payment demand report
    report = sample_demand.generate_demand_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Demand Date: {report['demand_date']}")
    print(f"Recipient: {report['recipient_info']['name']}")
    print(f"Recipient Address: {report['recipient_info']['address']}")
    print(f"Demand Level: {report['demand_level']}")
    print(f"Total Outstanding: €{report['total_outstanding']:,.2f}")
    print(f"Total with Interest: €{report['total_with_interest']:,.2f}")
    
    print(f"\nOutstanding Invoices:")
    for i, invoice in enumerate(report['outstanding_invoices'], 1):
        print(f"  {i}. Invoice #{invoice['invoice_number']}")
        print(f"     Original Amount: €{invoice['original_amount']:,.2f}")
        print(f"     Invoice Date: {invoice['invoice_date']}")
        print(f"     Due Date: {invoice['due_date']}")
        print(f"     Days Overdue: {invoice['days_overdue']}")
        print(f"     Interest Rate: {invoice['interest_rate']:.1%}")
        print(f"     Interest Amount: €{invoice['interest_amount']:,.2f}")
        print(f"     Penalty Fees: €{invoice['penalty_fees']:,.2f}")
        print(f"     Total Due: €{invoice['total_due']:,.2f}")
    
    print(f"\nPayment Terms:")
    terms = report['payment_terms']
    print(f"  Standard Payment Period: {terms['standard_payment_period']} days")
    print(f"  Late Payment Interest Rate: {terms['late_payment_interest_rate']:.1%}")
    print(f"  Demand Fee: €{terms['demand_fee']:.2f}")
    
    print(f"\nPenalty Fees:")
    penalties = report['penalty_fees']
    print(f"  Collection Fee: €{penalties['collection_fee']:.2f}")
    print(f"  Legal Proceedings Fee: €{penalties['legal_proceedings_fee']:.2f}")
    print(f"  Additional Penalty Rate: {penalties['additional_penalty_rate']:.1%}")
    
    print(f"\nCustomer Payment History:")
    history = report['customer_payment_history']
    print(f"  Payment Frequency: {history['payment_frequency']}")
    print(f"  Average Days Overdue: {history['average_days_overdue']}")
    print(f"  Previous Reminders: {history['previous_reminders_count']}")
    print(f"  Notes: {history['payment_behavior_notes']}")
    
    print(f"\nCollection Process:")
    collection = report['collection_process']
    print(f"  Status: {collection['status']}")
    print(f"  Last Contact: {collection['last_contact_date']}")
    print(f"  Next Action: {collection['next_action_date']}")
    print(f"  Actions Taken: {len(collection['actions_taken'])}")
    
    print(f"\nLegal Consequences:")
    legal_cons = report['legal_consequences']
    print(f"  Potential Legal Action: {legal_cons['potential_legal_action']}")
    print(f"  Credit Registry Reporting: {legal_cons['credit_registry_reporting']}")
    print(f"  Interest Continues to Accumulate: {legal_cons['interest_accumulation_continues']}")
    
    print(f"\nReporting Metrics:")
    metrics = report['reporting_metrics']
    print(f"  Max Days Overdue: {metrics['max_days_overdue']}")
    print(f"  Estimated Payment Probability After Demand: {metrics['payment_probability_after_demand']:.1%}")
    print(f"  Demand Level: {metrics['demand_level']}")
    
    # Generate and display collection strategy
    print(f"\nGenerating collection strategy...")
    strategy = sample_demand.generate_collection_strategy()
    print(f"\nCollection Strategy:")
    print(f"  Recommended Action: {strategy['recommended_action']}")
    print(f"  Payment Probability: {strategy['payment_probability']:.1%}")
    
    print(f"\nNegotiation Options:")
    for option in strategy['negotiation_options']:
        print(f"  - {option}")
    
    print(f"\nFollow-up Schedule:")
    for item in strategy['follow_up_schedule']:
        print(f"  In {item['days']} days: {item['action']}")
    
    print(f"\nEscalation Recommendation: {strategy['escalation_recommendation']}")
    
    # Generate and display the demand message
    print(f"\nGenerated Demand Message:")
    print("-" * 40)
    message = sample_demand.generate_demand_message()
    print(message)
    
    # Save the demand to a JSON file
    sample_demand.save_to_json("sample_payment_demand_notice.json")
    print(f"\nPayment demand notice saved to 'sample_payment_demand_notice.json'")