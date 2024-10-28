# DV Lottery Checker

#### Video Demo: [link](https://youtu.be/dndkHV06z54)

#### Description:
The DV Lottery Checker is a Python-based application designed to manage Diversity Visa (DV) Lottery applications efficiently. This program allows users to submit their applications, validates them against the DV Lottery requirements, stores valid and invalid applications in separate CSV files, and randomly selects a winner from the pool of valid applicants.

##### **Objective:**
The primary goal of this project is to streamline the application process for the DV Lottery by providing an automated system that ensures all applications meet the necessary criteria before being considered for the lottery. Additionally, it facilitates the fair selection of winners through a random selection process.

##### **Features:**
- **User-Friendly Input Interface:** Users can easily input their personal details, including name, date of birth, nationality, education level, and contact information.
- **Comprehensive Validation:** The application validates each submission to ensure compliance with DV Lottery requirements, such as age eligibility, educational qualifications, and nationality restrictions.
- **Data Management:** Valid applications are stored in `dv_valid_entries.csv`, while invalid ones are logged in `dv_invalid_entries.csv` for record-keeping and future reference.
- **Random Winner Selection:** The system can randomly select a winner from the pool of valid applications, ensuring a fair and unbiased selection process.
- **Modular Code Structure:** The project is organized into separate modules, enhancing readability and maintainability.

##### **Usage:**
1. **Running the Application:**
   - Ensure all dependencies are installed by running:
     ```
     pip install -r requirements.txt
     ```
   - Execute the main program:
     ```
     python project.py
     ```
2. **Submitting an Application:**
   - Choose option `1` from the menu.
   - Enter the required details as prompted.
   - The system will inform you if your application is valid or invalid.
3. **Selecting a Random Winner:**
   - Choose option `2` from the menu.
   - The system will randomly select and display a winner from the valid entries.
4. **Exiting the Program:**
   - Choose option `3` to exit.
