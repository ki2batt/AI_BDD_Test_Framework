from behave.__main__ import main as behave_main
import os
import shutil

def clean_and_create_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True) #Ensure the folder exists

if __name__ =="__main__":
    # Define the paths to the folders
    allure_results_folder = "reports"
    screenshot_folder = "screenshots"

    #Clean and recreate the necessary folders
    clean_and_create_folder(allure_results_folder)
    clean_and_create_folder(screenshot_folder)


    behave_main(
        [
            "--tags", "@regression",
            "--format", "allure_behave.formatter:AllureFormatter",
            "--outfile", "reports/allure-results"
        ]
    )
#allure generate reports/allure-results -o reports/allure-report --clean
#allure open reports/allure-report