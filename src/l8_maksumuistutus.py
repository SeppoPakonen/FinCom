"""
Python implementation of L8_Maksumuistutus payment reminder template.

This module provides programmatic access to the payment reminder functionality
originally implemented in the L8_Maksumuistutus.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class PaymentReminder:
    """
    A class representing a payment reminder based on the L8_Maksumuistutus template.
    This tool helps businesses create professional reminders for overdue invoices, 
    following up with customers who have not paid by the due date, and maintaining 
    healthy cash flow.
    """
    
    def __init__(self, company_name: str = "Payment Reminder Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.reminder_date = datetime.now().strftime('%d.%m.%Y')
        self.sender_info = {}  # Sender information
        self.recipient_info = {}  # Recipient information
        self.outstanding_invoices = []  # List of overdue invoices
        self.payment_terms = {}  # Payment terms and conditions
        self.late_payment_interest = {}  # Late payment interest calculations
        self.reminder_level = 1  # Level of reminder (1st, 2nd, final notice)
        self.total_outstanding = 0.0  # Total outstanding amount
        self.total_with_interest = 0.0  # Total with late payment interest
        self.escalation_rules = {}  # Rules for escalating reminders
        self.collection_process = {}  # Collection process tracking
        self.customer_payment_history = {}  # Customer payment history
        self.interest_calculations = {}  # Detailed interest calculations
        self.legal_compliance = {}  # Compliance with Finnish regulations
        self.communication_log = []  # Log of communications with customer
        self.payment_arrangements = {}  # Potential payment arrangements
        self.accounting_integration = {}  # Integration with accounting systems
        self.reporting_metrics = {}  # Reporting and analytics metrics
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the payment reminder with default values."""
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
            "reminder_fee": 5.00  # Fixed fee per reminder
        }
        
        # Default escalation rules
        self.escalation_rules = {
            "level_1_days_overdue": 7,
            "level_2_days_overdue": 14,
            "final_notice_days_overdue": 30,
            "collection_referral_days_overdue": 60
        }
        
        # Default interest calculations
        self.interest_calculations = {
            "interest_calculation_method": "simple_interest",
            "interest_base": "euribor_plus",  # Base rate for interest calculation
            "additional_interest_rate": 0.07  # Additional rate on top of base
        }
        
        # Default legal compliance
        self.legal_compliance = {
            "complies_with_finnish_law": True,
            "interest_calculation_compliant": True,
            "reminder_content_compliant": True
        }
        
        # Default customer payment history
        self.customer_payment_history = {
            "payment_frequency": "regular",
            "average_days_overdue": 5,
            "payment_behavior_notes": ""
        }
        
        # Default collection process
        self.collection_process = {
            "status": "pre_reminder",
            "last_contact_date": "",
            "next_action_date": "",
            "actions_taken": []
        }
        
        # Default reporting metrics
        self.reporting_metrics = {
            "days_since_invoice": 0,
            "payment_probability": 0.8,  # Estimated probability of payment
            "collection_effort_score": 0  # How much effort has been put into collection
        }
    
    def add_outstanding_invoice(self, invoice_number: str, original_amount: float, 
                               invoice_date: str, due_date: str, days_overdue: int, 
                               interest_rate: float = 0.11, additional_charges: float = 0.0):
        """Add an outstanding invoice to the reminder."""
        # Calculate interest based on days overdue
        interest_amount = self._calculate_interest(original_amount, days_overdue, interest_rate)
        
        # Calculate total amount due
        total_due = original_amount + interest_amount + additional_charges
        
        invoice = {
            "invoice_number": invoice_number,
            "original_amount": original_amount,
            "invoice_date": invoice_date,
            "due_date": due_date,
            "days_overdue": days_overdue,
            "interest_rate": interest_rate,
            "interest_amount": interest_amount,
            "additional_charges": additional_charges,
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
                         reminder_fee: float = 5.00):
        """Set payment terms."""
        self.payment_terms = {
            "standard_payment_period": standard_period,
            "late_payment_interest_rate": late_interest_rate,
            "reminder_fee": reminder_fee
        }
    
    def set_customer_payment_history(self, frequency: str, avg_days_overdue: int, notes: str = ""):
        """Set customer payment history information."""
        self.customer_payment_history = {
            "payment_frequency": frequency,
            "average_days_overdue": avg_days_overdue,
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
    
    def calculate_total_with_interest(self) -> float:
        """Calculate the total amount including interest."""
        total = sum(inv["total_due"] for inv in self.outstanding_invoices)
        self.total_with_interest = total
        return total
    
    def determine_reminder_level(self) -> int:
        """Determine the appropriate reminder level based on days overdue."""
        if not self.outstanding_invoices:
            return 0
        
        # Use the maximum days overdue to determine level
        max_days_overdue = max(inv["days_overdue"] for inv in self.outstanding_invoices)
        
        if max_days_overdue <= self.escalation_rules["level_1_days_overdue"]:
            return 1
        elif max_days_overdue <= self.escalation_rules["level_2_days_overdue"]:
            return 2
        elif max_days_overdue <= self.escalation_rules["final_notice_days_overdue"]:
            return 3  # Final notice
        else:
            return 4  # Refer to collection agency
    
    def generate_reminder_message(self) -> str:
        """Generate a standard reminder message based on the template."""
        level = self.determine_reminder_level()
        
        if level == 1:
            level_text = "Ensimmäinen maksumuistutus"
        elif level == 2:
            level_text = "Toinen maksumuistutus"
        elif level == 3:
            level_text = "Viimeinen maksumuistutus"
        else:
            level_text = "Lopullinen maksumuistutus"
        
        message = f"""
{level_text}
{datetime.now().strftime('%d.%m.%Y')}

{self.sender_info['name']}
{self.sender_info['address']}

{self.recipient_info['name']}
{self.recipient_info['address']}

Hei,

Kirjanpitomme mukaan emme ole saaneet suoritustanne tähän päivään mennessä.
Maksumuistutuksemme on aiheeton, mikäli olette suorittaneet maksun me.

Mikäli teillä on huomautettavaa laskumme johdosta, pyydämme Teitä ottamaan yhteyttä 7 päivän kuluessa.
Muussa tapauksessa katsomme, että Teillä ei ole saatavastamme huomautettavaa.

Seuraavat erääntyneet saatavamme ovat edelleen avoimena:

{"Laskun numero":<15} {"Alkuperäinen summa":<20} {"Eräpäivä":<12} {"Viivästyskorko":<15} {"Maksamaton saldo":<20}
"""
        
        for invoice in self.outstanding_invoices:
            message += f"{invoice['invoice_number']:<15} {invoice['original_amount']:<20.2f} {invoice['due_date']:<12} {invoice['interest_amount']:<15.2f} {invoice['total_due']:<20.2f}\n"
        
        total = self.calculate_total_with_interest()
        message += f"\nSaamisemme yhteensä: {total:.2f} €"
        
        message += f"""

Maksuviite:
{self.sender_info['bank_account_info']['iban']}
{self.sender_info['bank_account_info']['bic']}

Yrityksen nimi: {self.sender_info['name']}
Y-tunnus: {self.sender_info['business_id']}
Puhelin: {self.sender_info['phone']}
Sähköposti: {self.sender_info['email']}

Kiitämme ymmärtäväisyydestänne ja pyydämme Teitä hoitamaan maksun mahdollisimman pian.
"""
        
        return message
    
    def generate_payment_reminder_report(self) -> Dict:
        """Generate a comprehensive payment reminder report."""
        level = self.determine_reminder_level()
        
        report = {
            "company_name": self.company_name,
            "reminder_date": self.reminder_date,
            "sender_info": self.sender_info,
            "recipient_info": self.recipient_info,
            "outstanding_invoices": self.outstanding_invoices,
            "payment_terms": self.payment_terms,
            "reminder_level": level,
            "total_outstanding": self.calculate_total_outstanding(),
            "total_with_interest": self.calculate_total_with_interest(),
            "escalation_rules": self.escalation_rules,
            "customer_payment_history": self.customer_payment_history,
            "collection_process": self.collection_process,
            "interest_calculations": self.interest_calculations,
            "legal_compliance": self.legal_compliance,
            "reporting_metrics": {
                **self.reporting_metrics,
                "reminder_level": level,
                "max_days_overdue": max([inv["days_overdue"] for inv in self.outstanding_invoices]) if self.outstanding_invoices else 0,
                "payment_probability": self._estimate_payment_probability(level)
            }
        }
        
        return report
    
    def _estimate_payment_probability(self, reminder_level: int) -> float:
        """Estimate the probability of payment based on reminder level."""
        # Simplified estimation - in reality, this would be based on historical data
        if reminder_level == 1:
            return 0.85  # 85% chance for first reminder
        elif reminder_level == 2:
            return 0.70  # 70% chance for second reminder
        elif reminder_level == 3:
            return 0.40  # 40% chance for final notice
        else:
            return 0.15  # 15% chance after referral to collection agency
    
    def generate_collection_strategy(self) -> Dict:
        """Generate a collection strategy based on the current situation."""
        level = self.determine_reminder_level()
        total_amount = self.calculate_total_with_interest()
        
        strategy = {
            "recommended_action": self._get_recommended_action(level),
            "negotiation_options": self._get_negotiation_options(total_amount),
            "follow_up_schedule": self._get_follow_up_schedule(level),
            "escalation_recommendation": self._get_escalation_recommendation(level),
            "payment_probability": self._estimate_payment_probability(level)
        }
        
        return strategy
    
    def _get_recommended_action(self, level: int) -> str:
        """Get recommended action based on reminder level."""
        if level == 1:
            return "Send friendly reminder and confirm receipt of invoice"
        elif level == 2:
            return "Make direct contact with customer to discuss payment"
        elif level == 3:
            return "Issue final notice with clear consequences of non-payment"
        else:
            return "Refer to collection agency or legal action"
    
    def _get_negotiation_options(self, total_amount: float) -> List[str]:
        """Get potential negotiation options."""
        options = []
        
        if total_amount > 10000:  # For larger amounts
            options.append("Offer payment plan with monthly installments")
            options.append("Negotiate partial payment with settlement discount")
        
        if total_amount > 5000:
            options.append("Accept partial payment toward outstanding balance")
        
        options.append("Extend payment terms with additional interest")
        options.append("Waive interest charges if full payment made within 7 days")
        
        return options
    
    def _get_follow_up_schedule(self, level: int) -> List[Dict]:
        """Get recommended follow-up schedule."""
        schedule = []
        
        if level == 1:
            schedule.append({"days": 7, "action": "Follow up with phone call"})
            schedule.append({"days": 14, "action": "Send second reminder"})
        elif level == 2:
            schedule.append({"days": 3, "action": "Direct phone contact"})
            schedule.append({"days": 7, "action": "Send certified letter"})
        elif level == 3:
            schedule.append({"days": 1, "action": "Final reminder via certified mail"})
            schedule.append({"days": 14, "action": "Consider legal action"})
        else:
            schedule.append({"days": 0, "action": "Refer to collection agency"})
        
        return schedule
    
    def _get_escalation_recommendation(self, level: int) -> str:
        """Get escalation recommendation."""
        if level == 1:
            return "Continue with standard collection process"
        elif level == 2:
            return "Increase contact frequency and consider personal visit"
        elif level == 3:
            return "Prepare for legal action or collection agency referral"
        else:
            return "Proceed with collection agency or legal action"
    
    def save_to_json(self, filepath: str):
        """Save the payment reminder to a JSON file."""
        report = self.generate_payment_reminder_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a payment reminder from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.reminder_date = data.get("reminder_date", self.reminder_date)
        self.sender_info = data.get("sender_info", self.sender_info)
        self.recipient_info = data.get("recipient_info", self.recipient_info)
        self.outstanding_invoices = data.get("outstanding_invoices", self.outstanding_invoices)
        self.payment_terms = data.get("payment_terms", self.payment_terms)
        self.reminder_level = data.get("reminder_level", self.reminder_level)
        self.total_outstanding = data.get("total_outstanding", self.total_outstanding)
        self.total_with_interest = data.get("total_with_interest", self.total_with_interest)


def create_sample_reminder() -> PaymentReminder:
    """Create a sample payment reminder with example data."""
    reminder = PaymentReminder(company_name="Sample Payment Reminder Oy", year=2026)
    
    # Set sender information
    reminder.set_sender_info(
        name="Sample Payment Reminder Oy",
        address="Perintökatu 15, 33100 Tampere",
        business_id="1234567-8",
        contact_person="Perintö: Pekka Perintö",
        phone="0500 123 456",
        email="pekka.perinto@samplepaymentreminder.fi",
        iban="FI0000000012345678",
        bic="SAMPLEBIC"
    )
    
    # Set recipient information
    reminder.set_recipient_info(
        name="Maksaja Oy",
        address="Maksajankatu 20, 00100 Helsinki",
        business_id="8765432-1",
        contact_person="Maksaja: Maija Maksaja",
        phone="0400 987 654",
        email="maija.maksaja@maksaja.fi"
    )
    
    # Add example outstanding invoices
    reminder.add_outstanding_invoice(
        invoice_number="INV-123465",
        original_amount=10000.00,
        invoice_date="2025-10-01",
        due_date="2025-11-01",
        days_overdue=94,  # As of Feb 3, 2026
        interest_rate=0.11,  # 11% interest rate from the spreadsheet
        additional_charges=5.00  # Reminder fee
    )
    
    reminder.add_outstanding_invoice(
        invoice_number="INV-123466",
        original_amount=5000.00,
        invoice_date="2025-11-15",
        due_date="2025-12-15",
        days_overdue=49,  # As of Feb 3, 2026
        interest_rate=0.11,
        additional_charges=5.00
    )
    
    reminder.add_outstanding_invoice(
        invoice_number="INV-123467",
        original_amount=2500.00,
        invoice_date="2025-12-20",
        due_date="2026-01-20",
        days_overdue=14,  # As of Feb 3, 2026
        interest_rate=0.11,
        additional_charges=5.00
    )
    
    # Set payment terms
    reminder.set_payment_terms(
        standard_period=14,
        late_interest_rate=0.11,
        reminder_fee=5.00
    )
    
    # Set customer payment history
    reminder.set_customer_payment_history(
        frequency="occasional",
        avg_days_overdue=25,
        notes="Customer has history of delayed payments but eventually pays"
    )
    
    # Set collection process
    reminder.set_collection_process(
        status="second_reminder_sent",
        last_contact="2026-01-28",
        next_action="2026-02-10"
    )
    
    # Add a collection action
    reminder.add_collection_action(
        action_date="2026-01-28",
        action_type="email_reminder",
        description="Sent first payment reminder via email"
    )
    
    return reminder


if __name__ == "__main__":
    # Example usage
    print("L8 Maksumuistutus - Payment Reminder Tool")
    print("=" * 45)
    
    # Create a sample payment reminder
    sample_reminder = create_sample_reminder()
    
    # Generate and display the payment reminder report
    report = sample_reminder.generate_payment_reminder_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Reminder Date: {report['reminder_date']}")
    print(f"Recipient: {report['recipient_info']['name']}")
    print(f"Recipient Address: {report['recipient_info']['address']}")
    print(f"Reminder Level: {report['reminder_level']}")
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
        print(f"     Additional Charges: €{invoice['additional_charges']:,.2f}")
        print(f"     Total Due: €{invoice['total_due']:,.2f}")
    
    print(f"\nPayment Terms:")
    terms = report['payment_terms']
    print(f"  Standard Payment Period: {terms['standard_payment_period']} days")
    print(f"  Late Payment Interest Rate: {terms['late_payment_interest_rate']:.1%}")
    print(f"  Reminder Fee: €{terms['reminder_fee']:.2f}")
    
    print(f"\nCustomer Payment History:")
    history = report['customer_payment_history']
    print(f"  Payment Frequency: {history['payment_frequency']}")
    print(f"  Average Days Overdue: {history['average_days_overdue']}")
    print(f"  Notes: {history['payment_behavior_notes']}")
    
    print(f"\nCollection Process:")
    collection = report['collection_process']
    print(f"  Status: {collection['status']}")
    print(f"  Last Contact: {collection['last_contact_date']}")
    print(f"  Next Action: {collection['next_action_date']}")
    print(f"  Actions Taken: {len(collection['actions_taken'])}")
    
    print(f"\nReporting Metrics:")
    metrics = report['reporting_metrics']
    print(f"  Max Days Overdue: {metrics['max_days_overdue']}")
    print(f"  Estimated Payment Probability: {metrics['payment_probability']:.1%}")
    print(f"  Reminder Level: {metrics['reminder_level']}")
    
    # Generate and display collection strategy
    print(f"\nGenerating collection strategy...")
    strategy = sample_reminder.generate_collection_strategy()
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
    
    # Generate and display the reminder message
    print(f"\nGenerated Reminder Message:")
    print("-" * 40)
    message = sample_reminder.generate_reminder_message()
    print(message)
    
    # Save the reminder to a JSON file
    sample_reminder.save_to_json("sample_payment_reminder.json")
    print(f"\nPayment reminder saved to 'sample_payment_reminder.json'")