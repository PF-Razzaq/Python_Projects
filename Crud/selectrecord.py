import os
import pymysql as ms
import pandas as pd
import openpyxl

def fetch_and_update_excel():
    conn = ms.connect(host='localhost', user='root', password='', database='student')
    mysql = conn.cursor()

    selectdata = 'SELECT * FROM studentrecord'
    try:
        mysql.execute(selectdata)
        data = mysql.fetchall()

        # Get the column names
        columns = [desc[0] for desc in mysql.description]

        # Create a DataFrame using pandas
        new_df = pd.DataFrame(data, columns=columns)

        # Rename columns if needed
        column_mapping = {
            'st_name': 'Name',
            'st_class': 'Class',
            'st_email': 'Email',
        }
        new_df.rename(columns=column_mapping, inplace=True)

        # Check if the Excel file exists
        excel_file = 'Record_Sheet.xlsx'
        if os.path.exists(excel_file):
            # Read existing data from the Excel file
            existing_df = pd.read_excel(excel_file)
            
            # Concatenate new data with existing DataFrame
            df = pd.concat([existing_df, new_df], ignore_index=True)
        else:
            df = new_df

        # Save the updated DataFrame to the Excel file
        df.to_excel(excel_file, index=False)

        # Open the Excel file using openpyxl
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active

        # Add the 'ID' column in cell B1
        sheet['B1'] = 'ID'

        # Save the updated Excel file
        wb.save(excel_file)

        print("Excel file updated successfully.")
    except ms.Error as e:
        print(f'Error: {e}')

    finally:
        conn.close()
        mysql.close()

# Fetch and update the Excel file
fetch_and_update_excel()

# Now you can call this function whenever you want to fetch and update the Excel file
