"""
Python implementation of Excel_harjoituspaketti_1 Excel exercise package.

This module provides programmatic access to the Excel exercise functionality
originally implemented in the Excel_harjoituspaketti_1.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class ExcelExercisePackage:
    """
    A class representing an Excel exercise package based on the 
    Excel_harjoituspaketti_1 template.
    This tool provides exercises and examples to help users practice and improve 
    their Excel skills, covering different aspects from basic operations to advanced features.
    """
    
    def __init__(self, package_name: str = "Excel Exercise Package", year: int = 2026):
        self.package_name = package_name
        self.year = year
        self.exercises = {}  # Different exercises in the package
        self.exercise_solutions = {}  # Solutions to exercises
        self.user_progress = {}  # User progress tracking
        self.learning_objectives = {}  # Learning objectives for each exercise
        self.difficulty_levels = {}  # Difficulty ratings for exercises
        self.time_estimates = {}  # Time estimates for completing exercises
        self.validation_functions = {}  # Functions to validate exercise solutions
        self.performance_metrics = {}  # Performance metrics
        self.best_practices = {}  # Best practices and tips
        self.common_mistakes = {}  # Common mistakes and how to avoid them
        self.efficiency_techniques = {}  # Efficiency techniques and shortcuts
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the Excel exercise package with default values."""
        # Define exercises with different topics
        self.exercises = {
            "exercise_1": {
                "name": "Basic Operations",
                "topic": "Basic Excel operations and functions",
                "instructions": [
                    "Change the header font to Times New Roman, size 18 pt",
                    "Fill month names horizontally with fill handle",
                    "Calculate sums for the 'Yhteensä' row",
                    "Bold the month names and calculated sums",
                    "Format all numbers in the table as currency with no decimals (e.g., 290 €)"
                ],
                "data": {
                    "categories": ["Asunto", "Ruoka", "Vaatteet", "Opiskelu", "Matkat", "Harrastukset", "Muut"],
                    "tammikuu": [290, 350, 120, 20, 55, 9, 62],
                    "helmikuu": [290, 500, 60, 50, 100, 10, 40],
                    "maaliskuu": [290, 400, 60, 50, 50, 15, 15],
                    "huhtikuu": [290, 400, 25, 40, 80, 10, 240]
                },
                "solution": {},
                "difficulty": "Beginner",
                "time_estimate_minutes": 30
            },
            "exercise_2": {
                "name": "Text Formatting",
                "topic": "Text formatting and cell alignment",
                "instructions": [
                    "Enter years 2000-2003 as column headers in cells B10:E10",
                    "Add an apostrophe before the year to format as text",
                    "Center-align the year values in cells",
                    "Calculate the sum of employee counts",
                    "Make all text in the table italic"
                ],
                "data": {
                    "locations": ["Forssa", "Helsinki", "Tampere", "Oulu"],
                    "employees_2000": [210, 345, 298, 121],
                    "employees_2001": [190, 356, 241, 142],
                    "employees_2002": [185, 360, 255, 154],
                    "employees_2003": [190, 359, 280, 200]
                },
                "solution": {},
                "difficulty": "Beginner",
                "time_estimate_minutes": 25
            },
            "exercise_3": {
                "name": "Column Manipulation",
                "topic": "Renaming columns and data entry",
                "instructions": [
                    "Rename the 'Sarakkeet' table to 'Fruits'",
                    "Remove the hash symbols (#) from cells",
                    "Calculate totals in the 'Yhteensä' column and row",
                    "Insert a new row after 'Mustikka' with: 'Puolukka', 60.23, 86.50, 120.06",
                    "Format all numbers as euros"
                ],
                "data": {
                    "fruits": ["Omena", "Banaani", "Appelsiini", "Ananas", "Mustikka"],
                    "price_1": [25.50, 40.20, 35.75, 55.00, 65.30],
                    "price_2": [28.00, 42.50, 37.20, 52.00, 68.90],
                    "price_3": [30.00, 45.00, 38.50, 58.00, 70.50]
                },
                "solution": {},
                "difficulty": "Intermediate",
                "time_estimate_minutes": 40
            },
            "exercise_4": {
                "name": "Advanced Functions",
                "topic": "Pivot tables, VLOOKUP, and complex formulas",
                "instructions": [
                    "Create a pivot table showing sales by product and month",
                    "Use VLOOKUP to match product codes with descriptions",
                    "Apply conditional formatting to highlight values above average",
                    "Create a chart showing sales trends over time"
                ],
                "data": {},
                "solution": {},
                "difficulty": "Advanced",
                "time_estimate_minutes": 60
            },
            "exercise_5": {
                "name": "Financial Modeling",
                "topic": "Financial calculations and modeling",
                "instructions": [
                    "Build a simple financial model with revenue, costs, and profit projections",
                    "Use formulas to calculate growth rates and profit margins",
                    "Create scenarios with different assumptions",
                    "Perform sensitivity analysis on key variables"
                ],
                "data": {},
                "solution": {},
                "difficulty": "Advanced",
                "time_estimate_minutes": 75
            }
        }
        
        # Define learning objectives
        self.learning_objectives = {
            "exercise_1": [
                "Master basic formatting operations",
                "Learn to use fill handle effectively",
                "Practice formula creation for sum calculations",
                "Understand currency formatting options"
            ],
            "exercise_2": [
                "Learn text formatting techniques",
                "Understand cell alignment options",
                "Practice sum calculations across rows/columns",
                "Apply formatting to entire tables"
            ],
            "exercise_3": [
                "Manipulate column names and data",
                "Insert new rows with data",
                "Format numbers as currency",
                "Practice data entry techniques"
            ],
            "exercise_4": [
                "Create and manipulate pivot tables",
                "Use VLOOKUP and other lookup functions",
                "Apply conditional formatting",
                "Create charts and visualize data"
            ],
            "exercise_5": [
                "Build financial models with Excel",
                "Use advanced formulas for financial calculations",
                "Create multiple scenarios",
                "Perform sensitivity analysis"
            ]
        }
        
        # Define difficulty levels
        self.difficulty_levels = {
            "exercise_1": "Beginner",
            "exercise_2": "Beginner",
            "exercise_3": "Intermediate",
            "exercise_4": "Advanced",
            "exercise_5": "Advanced"
        }
        
        # Define time estimates
        self.time_estimates = {
            "exercise_1": 30,  # minutes
            "exercise_2": 25,
            "exercise_3": 40,
            "exercise_4": 60,
            "exercise_5": 75
        }
        
        # Initialize user progress tracking
        for ex_id in self.exercises:
            self.user_progress[ex_id] = {
                "started": False,
                "completed": False,
                "completion_date": None,
                "score": 0,
                "attempts": 0,
                "time_taken": 0  # in minutes
            }
        
        # Define validation functions for exercises
        self.validation_functions = {
            "exercise_1": self.validate_basic_operations_exercise,
            "exercise_2": self.validate_text_formatting_exercise,
            "exercise_3": self.validate_column_manipulation_exercise,
            "exercise_4": self.validate_advanced_functions_exercise,
            "exercise_5": self.validate_financial_modeling_exercise
        }
        
        # Define performance metrics
        self.performance_metrics = {
            "total_exercises": len(self.exercises),
            "completed_exercises": 0,
            "average_completion_time": 0,
            "overall_score": 0,
            "time_spent": 0  # in minutes
        }
        
        # Define best practices
        self.best_practices = {
            "general": [
                "Use keyboard shortcuts to improve efficiency",
                "Organize data in tables for better management",
                "Use named ranges for important data",
                "Apply consistent formatting throughout the workbook"
            ],
            "formulas": [
                "Use absolute vs relative references appropriately",
                "Test formulas with sample data before applying to full dataset",
                "Document complex formulas with comments",
                "Use Excel's formula auditing tools to troubleshoot"
            ],
            "charts": [
                "Choose the right chart type for your data",
                "Keep charts simple and focused on key insights",
                "Use consistent colors and formatting",
                "Include titles, labels, and legends for clarity"
            ]
        }
        
        # Define common mistakes
        self.common_mistakes = {
            "formula_errors": [
                "Incorrect cell reference types (absolute vs relative)",
                "Dividing by zero",
                "Circular references",
                "Not updating ranges when copying formulas"
            ],
            "formatting_errors": [
                "Inconsistent number formatting",
                "Not formatting dates properly",
                "Using too many fonts or colors",
                "Poor alignment of data"
            ],
            "data_errors": [
                "Not validating data entry",
                "Mixing data types in columns",
                "Not removing duplicates",
                "Incorrect data types causing calculation errors"
            ]
        }
    
    def start_exercise(self, exercise_id: str):
        """Mark an exercise as started."""
        if exercise_id in self.user_progress:
            self.user_progress[exercise_id]["started"] = True
            self.user_progress[exercise_id]["attempts"] += 1
        else:
            raise ValueError(f"Unknown exercise ID: {exercise_id}")
    
    def complete_exercise(self, exercise_id: str, score: float, time_taken: float):
        """Mark an exercise as completed with a score and time taken."""
        if exercise_id in self.user_progress:
            self.user_progress[exercise_id]["completed"] = True
            self.user_progress[exercise_id]["completion_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.user_progress[exercise_id]["score"] = score
            self.user_progress[exercise_id]["time_taken"] = time_taken
        else:
            raise ValueError(f"Unknown exercise ID: {exercise_id}")
    
    def calculate_progress_percentage(self) -> float:
        """Calculate the overall progress percentage."""
        total_exercises = len(self.exercises)
        completed_exercises = sum(1 for progress in self.user_progress.values() if progress["completed"])
        return (completed_exercises / total_exercises) * 100 if total_exercises > 0 else 0
    
    def calculate_average_completion_time(self) -> float:
        """Calculate the average time taken to complete exercises."""
        completed_exercises = [ex for ex_id, ex in self.user_progress.items() if ex["completed"]]
        if not completed_exercises:
            return 0
        total_time = sum(ex["time_taken"] for ex in completed_exercises)
        return total_time / len(completed_exercises)
    
    def calculate_overall_score(self) -> float:
        """Calculate the overall score across all exercises."""
        completed_exercises = [ex for ex_id, ex in self.user_progress.items() if ex["completed"]]
        if not completed_exercises:
            return 0
        total_score = sum(ex["score"] for ex in completed_exercises)
        return total_score / len(completed_exercises) if len(completed_exercises) > 0 else 0
    
    def validate_basic_operations_exercise(self, user_solution: Dict) -> bool:
        """Validate the solution for the basic operations exercise."""
        # This would contain specific validation logic for the exercise
        # For now, we'll return True as a placeholder
        return True
    
    def validate_text_formatting_exercise(self, user_solution: Dict) -> bool:
        """Validate the solution for the text formatting exercise."""
        # This would contain specific validation logic for the exercise
        # For now, we'll return True as a placeholder
        return True
    
    def validate_column_manipulation_exercise(self, user_solution: Dict) -> bool:
        """Validate the solution for the column manipulation exercise."""
        # This would contain specific validation logic for the exercise
        # For now, we'll return True as a placeholder
        return True
    
    def validate_advanced_functions_exercise(self, user_solution: Dict) -> bool:
        """Validate the solution for the advanced functions exercise."""
        # This would contain specific validation logic for the exercise
        # For now, we'll return True as a placeholder
        return True
    
    def validate_financial_modeling_exercise(self, user_solution: Dict) -> bool:
        """Validate the solution for the financial modeling exercise."""
        # This would contain specific validation logic for the exercise
        # For now, we'll return True as a placeholder
        return True
    
    def generate_exercise_report(self) -> Dict:
        """Generate a comprehensive report of the exercise package."""
        completed_count = sum(1 for progress in self.user_progress.values() if progress["completed"])
        
        report = {
            "package_name": self.package_name,
            "year": self.year,
            "total_exercises": len(self.exercises),
            "completed_exercises": completed_count,
            "progress_percentage": self.calculate_progress_percentage(),
            "average_completion_time": self.calculate_average_completion_time(),
            "overall_score": self.calculate_overall_score(),
            "exercises": self.exercises,
            "learning_objectives": self.learning_objectives,
            "difficulty_levels": self.difficulty_levels,
            "time_estimates": self.time_estimates,
            "user_progress": self.user_progress,
            "best_practices": self.best_practices,
            "common_mistakes": self.common_mistakes,
            "performance_metrics": {
                "total_exercises": len(self.exercises),
                "completed_exercises": completed_count,
                "progress_percentage": self.calculate_progress_percentage(),
                "average_completion_time": self.calculate_average_completion_time(),
                "overall_score": self.calculate_overall_score()
            }
        }
        
        return report
    
    def generate_exercise_instructions(self, exercise_id: str) -> str:
        """Generate detailed instructions for a specific exercise."""
        if exercise_id not in self.exercises:
            raise ValueError(f"Unknown exercise ID: {exercise_id}")
        
        exercise = self.exercises[exercise_id]
        instructions_text = f"Exercise: {exercise['name']}\n"
        instructions_text += f"Topic: {exercise['topic']}\n"
        instructions_text += f"Difficulty: {exercise['difficulty']}\n"
        instructions_text += f"Estimated Time: {exercise['time_estimate_minutes']} minutes\n\n"
        instructions_text += "Instructions:\n"
        for i, instruction in enumerate(exercise['instructions'], 1):
            instructions_text += f"{i}. {instruction}\n"
        
        return instructions_text
    
    def save_to_json(self, filepath: str):
        """Save the exercise package to a JSON file."""
        report = self.generate_exercise_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load an exercise package from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.package_name = data.get("package_name", self.package_name)
        self.year = data.get("year", self.year)
        self.exercises = data.get("exercises", self.exercises)
        self.user_progress = data.get("user_progress", self.user_progress)
        self.learning_objectives = data.get("learning_objectives", self.learning_objectives)
        self.difficulty_levels = data.get("difficulty_levels", self.difficulty_levels)
        self.time_estimates = data.get("time_estimates", self.time_estimates)


def create_sample_package() -> ExcelExercisePackage:
    """Create a sample Excel exercise package with example data."""
    package = ExcelExercisePackage(package_name="Sample Excel Exercise Package", year=2026)
    
    # Mark some exercises as completed to simulate progress
    package.complete_exercise("exercise_1", 85.0, 28.5)  # Completed with 85% score in 28.5 minutes
    package.complete_exercise("exercise_2", 90.0, 22.0)  # Completed with 90% score in 22 minutes
    package.start_exercise("exercise_3")  # Started but not completed
    
    # Update the data for exercise 1 with actual values from the spreadsheet
    package.exercises["exercise_1"]["data"] = {
        "categories": ["Asunto", "Ruoka", "Vaatteet", "Opiskelu", "Matkat", "Harrastukset", "Muut"],
        "tammikuu": [290, 350, 120, 20, 55, 9, 62],
        "helmikuu": [290, 500, 60, 50, 100, 10, 40],
        "maaliskuu": [290, 400, 60, 50, 50, 15, 15],
        "huhtikuu": [290, 400, 25, 40, 80, 10, 240],
        "sums": [1160, 1650, 265, 160, 285, 44, 397]  # Row sums
    }
    
    # Update the data for exercise 2 with actual values from the spreadsheet
    package.exercises["exercise_2"]["data"] = {
        "locations": ["Forssa", "Helsinki", "Tampere", "Oulu"],
        "employees_2000": [210, 345, 298, 121],
        "employees_2001": [190, 356, 241, 142],
        "employees_2002": [185, 360, 255, 154],
        "employees_2003": [190, 359, 280, 200],
        "row_totals": [975, 1420, 1174, 617]  # Row totals
    }
    
    # Update the data for exercise 3 with actual values from the spreadsheet
    package.exercises["exercise_3"]["data"] = {
        "fruits": ["Omena", "Banaani", "Appelsiini", "Ananas", "Mustikka", "Puolukka"],
        "price_1": [25.50, 40.20, 35.75, 55.00, 65.30, 60.23],
        "price_2": [28.00, 42.50, 37.20, 52.00, 68.90, 86.50],
        "price_3": [30.00, 45.00, 38.50, 58.00, 70.50, 120.06],
        "column_totals": [83.50, 127.70, 111.45, 165.00, 204.70, 266.79]  # Column totals
    }
    
    return package


if __name__ == "__main__":
    # Example usage
    print("Excel harjoituspaketti 1 - Excel Exercise Package Tool")
    print("=" * 60)
    
    # Create a sample Excel exercise package
    sample_package = create_sample_package()
    
    # Generate and display the exercise report
    report = sample_package.generate_exercise_report()
    
    print(f"\nPackage: {report['package_name']}")
    print(f"Year: {report['year']}")
    print(f"Total Exercises: {report['total_exercises']}")
    print(f"Completed Exercises: {report['completed_exercises']}")
    print(f"Progress: {report['progress_percentage']:.1f}%")
    print(f"Overall Score: {report['overall_score']:.1f}%")
    print(f"Average Completion Time: {report['average_completion_time']:.1f} minutes")
    
    print(f"\nExercise List:")
    for ex_id, ex in report['exercises'].items():
        status = "Completed" if report['user_progress'][ex_id]['completed'] else "In Progress" if report['user_progress'][ex_id]['started'] else "Not Started"
        print(f"  {ex['name']} ({ex['difficulty']}) - {status}")
        if report['user_progress'][ex_id]['completed']:
            print(f"    Score: {report['user_progress'][ex_id]['score']:.1f}%, Time: {report['user_progress'][ex_id]['time_taken']:.1f}min")
    
    print(f"\nLearning Objectives for Exercise 1:")
    for obj in report['learning_objectives']['exercise_1']:
        print(f"  - {obj}")
    
    print(f"\nBest Practices:")
    for category, practices in list(report['best_practices'].items())[:2]:  # Show first 2 categories
        print(f"  {category.title()}:")
        for practice in practices[:3]:  # Show first 3 practices
            print(f"    • {practice}")
    
    print(f"\nCommon Mistakes:")
    for category, mistakes in list(report['common_mistakes'].items())[:2]:  # Show first 2 categories
        print(f"  {category.replace('_', ' ').title()}:")
        for mistake in mistakes[:2]:  # Show first 2 mistakes
            print(f"    • {mistake}")
    
    print(f"\nDetailed Instructions for Exercise 1:")
    instructions = sample_package.generate_exercise_instructions("exercise_1")
    print(instructions)
    
    # Save the package to a JSON file
    sample_package.save_to_json("sample_excel_exercise_package.json")
    print(f"\nExcel exercise package saved to 'sample_excel_exercise_package.json'")