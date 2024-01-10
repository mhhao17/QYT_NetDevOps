import datetime

current_time = datetime.datetime.now()
fiveDaysAgo = current_time - datetime.timedelta(days=5)
formatted_time = current_time.strftime('%F_%H-%M-%S')

file_name = f"save_fivedayago_time_{formatted_time}.txt"
context_to_write = f"{fiveDaysAgo}"

with open(file_name, 'w') as f:
    f.write(context_to_write + '\n')



