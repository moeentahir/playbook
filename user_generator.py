import csv
import random
import string

def generate_random_staff_number(length=8):
    return ''.join(random.choices(string.digits, k=length))

def main():
    # Predefined access values
    access_options = ["Admin", "User", "Viewer", "Editor", "Auditor"]
    
    # Display options
    print("Available access types:")
    for idx, access in enumerate(access_options, 1):
        print(f"{idx}. {access}")

    selected_indices = input("Select access types by entering numbers separated by space (e.g., 1 3 4): ").strip().split()
    try:
        selected_access = [access_options[int(i) - 1] for i in selected_indices if 1 <= int(i) <= len(access_options)]
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        return

    if not selected_access:
        print("No valid access types selected. Exiting.")
        return

    # Get other user inputs
    first_name = input("Enter first name: ").strip()
    base_last_name = input("Enter base last name (will be sequenced): ").strip()
    try:
        num_rows = int(input("Enter the number of rows to generate: "))
    except ValueError:
        print("Invalid number. Exiting.")
        return

    filename = 'generated_users.csv'

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['First name', 'Last name', 'Email address', 'Staff number', 'Access', 'Delivery unit', 'All_required']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, num_rows + 1):
            last_name = f"{base_last_name}{i}"
            email = f"{first_name.lower()}.{last_name.lower()}@example.com"
            staff_number = generate_random_staff_number()
            access = random.choice(selected_access)
            delivery_unit = "Unit A"  # You can customize this
            all_required = "Yes"

            writer.writerow({
                'First name': first_name,
                'Last name': last_name,
                'Email address': email,
                'Staff number': staff_number,
                'Access': access,
                'Delivery unit': delivery_unit,
                'All_required': all_required
            })

    print(f"{num_rows} rows written to {filename}")

if __name__ == '__main__':
    main()
