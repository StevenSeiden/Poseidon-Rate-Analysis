import sys

def parse_text_file(file_path, ip1, ip2):
    rates = {}
    seen_ips = set()
    calculate_average = False

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('Rate:'):
                srcip = line.split()[2]
                rate = float(line.split()[3])

                # Add the IP to the found list
                seen_ips.add(srcip)

                # Check if we have found all wanted IPs
                if ip1 in seen_ips and ip2 in seen_ips and not calculate_average:
                    calculate_average = True

                # Add found rate to average
                if calculate_average:
                    if srcip in rates:
                        rates[srcip].append(rate)
                    else:
                        rates[srcip] = [rate]

    return rates


def calculate_average_rate(rates):
    average_rates = {}
    for srcip, rate_list in rates.items():
        # Calculate the average rate for IPs
        average_rate = sum(rate_list) / len(rate_list)
        average_rates[srcip] = average_rate

    return average_rates


# Log file to read
file_path = sys.argv[1] # 'trace_multi_hop_congestion_small-topo_racks.txt'

# IP addresses to compare
ip1 = sys.argv[2]  # '0b002001'
ip2 = sys.argv[3]  # '0b000201'

parsed_data = parse_text_file(file_path, ip1, ip2)
average_rates = calculate_average_rate(parsed_data)


if ip1 in average_rates:
    print(f"srcip: {ip1}, average rate: {average_rates[ip1]}")

if ip2 in average_rates:
    print(f"srcip: {ip2}, average rate: {average_rates[ip2]}")
