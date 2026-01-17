def process_wallets_to_csv(gtd_input, fcfs_input):
    gtd_data = {}
    fcfs_data = {}

    try:
        with open(gtd_input, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().replace(':', ' ').replace(',', ' ').split()
                if len(parts) >= 2:
                    addr = parts[0].lower()
                    amount = int(parts[1])
                    gtd_data[addr] = gtd_data.get(addr, 0) + amount
    except FileNotFoundError:
        print(f"Файл {gtd_input} не найден!")

    try:
        with open(fcfs_input, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().replace(':', ' ').replace(',', ' ').split()
                if len(parts) >= 2:
                    addr = parts[0].lower()
                    amount = int(parts[1])

                    if addr not in gtd_data:
                        fcfs_data[addr] = fcfs_data.get(addr, 0) + amount
    except FileNotFoundError:
        print(f"Файл {fcfs_input} не найден!")

    with open('gtd_final.csv', 'w', encoding='utf-8') as f:
        for addr, amount in gtd_data.items():
            f.write(f"{addr},{amount}\n")

    with open('fcfs_final.csv', 'w', encoding='utf-8') as f:
        for addr, amount in fcfs_data.items():
            f.write(f"{addr},{amount}\n")

    print("--- Успешно сохранено в .csv ---")
    print(f"GTD: {len(gtd_data)} уникальных адресов")
    print(f"FCFS: {len(fcfs_data)} уникальных адресов")


process_wallets_to_csv('gtd.txt', 'fcfs.txt')