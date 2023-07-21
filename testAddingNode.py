import sys

def parse(file, ip1, ip2):
    ratesBefore = []
    ratesAfter = []
    seenIPs = set()
    beginAveraging = False
    ip2Seen = False

    with open(file, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('Rate:'):
                srcip = line.split()[2]
                rate = float(line.split()[3])

                # Add the IP to the found list
                seenIPs.add(srcip)

                # Check if we have found all wanted IPs
                if ip1 in seenIPs and not beginAveraging:
                    beginAveraging = True

                # Add found rate to average
                if srcip == ip2:
                    ip2Seen = True

                if beginAveraging:
                    if srcip == ip1:
                        if ip2Seen:
                            ratesAfter.append(rate)
                        else:
                            ratesBefore.append(rate)

    return ratesBefore, ratesAfter


def calcAvg(rateList):
    if not rateList:
        return None
    average_rate = sum(rateList) / len(rateList)
    return average_rate


# Log file to read
file = sys.argv[1]  # 'trace_multi_hop_congestion_small-topo_racks.txt'

# IP addresses to compare
ip1 = sys.argv[2]  # '0b002001'
ip2 = sys.argv[3]  # '0b000201'

ratesBefore, ratesAfter = parse(file, ip1, ip2)

rateBeforeNodeAdded = calcAvg(ratesBefore)
rateAfterNodeAdded = calcAvg(ratesAfter)

print(f"{ip1}\'s average rate before {ip2}: {rateBeforeNodeAdded}")
print(f"{ip1}\'s average rate after {ip2}: {rateAfterNodeAdded}")
