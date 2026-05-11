# Import the logic from your demographic_data_analyzer file
import demographic_data_analyzer

# The following block ensures the code only runs when this specific file is executed
if __name__ == "__main__":
    
    # Call the calculation function 
    # This will perform all the Pandas operations and print the results
    demographic_data_analyzer.calculate_demographic_data()
    
    # Note: If you want to run the automated unit tests, 
    # you can also import and run test_module.py here.