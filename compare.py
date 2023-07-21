import sys

def parse(file, ip1, ip2):
    rates = {}
    seenIPs = set()
    beginAveraging = False

    with open(file, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('Rate:'):
                srcip = line.split()[2]
                rate = float(line.split()[3])

                # Add the IP to the found list
                seenIPs.add(srcip)

                # Check if we have found all wanted IPs
                if ip1 in seenIPs and ip2 in seenIPs and not beginAveraging:
                    beginAveraging = True

                # Add found rate to average
                if beginAveraging:
                    if srcip in rates:
                        rates[srcip].append(rate)
                    else:
                        rates[srcip] = [rate]

    return rates


def calcAvg(rates):
    averages = {}
    for srcip, rateList in rates.items():
        # Calculate the average rate for IPs
        averageRate = sum(rateList) / len(rateList)
        averages[srcip] = averageRate

    return averages


# Log file to read
file = sys.argv[1] # 'trace_multi_hop_congestion_small-topo_racks.txt'

# IP addresses to compare
ip1 = sys.argv[2]  # '0b002001'
ip2 = sys.argv[3]  # '0b000201'

parsedData = parse(file, ip1, ip2)
averages = calcAvg(parsedData)


if ip1 in averages:
    print(f"srcip: {ip1}, average rate: {averages[ip1]}")

if ip2 in averages:
    print(f"srcip: {ip2}, average rate: {averages[ip2]}")
