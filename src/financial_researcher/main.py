#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """Run the finacnial researcher crew"""
    inputs = {
        'company': 'Swiggy'
    }
    
    result = FinancialResearcher().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()