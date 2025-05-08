def main():
    display_main_menu()
    float_list = get_user_input()
    average = calc_average_temperature(float_list)
    min_max = calc_min_max_temperature(float_list)
    print(f"Average Temperature: {average:.2f}")
    print(f"Minimum Temperature: {min_max[0]}")
    print(f"Maximum Temperature: {min_max[1]}")
    
 
def display_main_menu():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    print("Hello world")

def get_user_input():
    input_str = input("Enter numbers separated by commas (e.g., 12.5, 45.3, 67): ")
    str_list = input_str.split(",")
    float_list = [float(num.strip()) for num in str_list]
    return float_list

def calc_average_temperature(float_list):
    if not float_list:
        return 0.0 
    return sum(float_list) / len(float_list)

def calc_min_max_temperature(float_list):
    if not float_list:
        return [0, 0]
    return [int(min(float_list)), int(max(float_list))]

main()


