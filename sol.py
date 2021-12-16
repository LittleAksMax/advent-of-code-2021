main_packet = ''.join(map(lambda x: format(int(x, 16), "04b"), open("input.txt", "r").read()))


def multiply(array):
    product = 1
    for el in array:
        product *= int(el)
    return product


operations = (sum, multiply, min, max, 4, lambda x: x[0] > x[1], lambda x: x[0] < x[1], lambda x: x[0] == x[1])


def get_version_sum_B(packet):
    this_typeid = int(packet[3:6], 2)
    packet = packet[6:]
    if this_typeid == 4:
        value = ""
        while len(packet) >= 5:
            value += packet[1:5]
            start_bit = packet[0]
            packet = packet[5:]
            if start_bit == "0":
                break
        return int(value, 2), packet
    literal_sub_packets = []
    if packet[0] == "1":
        sub_packets = int(packet[1:12], 2)
        packet = packet[12:]
        for sub_packet in range(sub_packets):
            current_sub_packet_value, packet = get_version_sum_B(packet)
            literal_sub_packets.append(current_sub_packet_value)
        return operations[this_typeid](literal_sub_packets), packet
    sub_packets_length = int(packet[1:16], 2)
    packet = packet[16:]
    stop_at_len = len(packet) - sub_packets_length
    while len(packet) > stop_at_len:
        current_sub_packet_value, packet = get_version_sum_B(packet)
        literal_sub_packets.append(current_sub_packet_value)
    return operations[this_typeid](literal_sub_packets), packet


def get_version_sum_A(packet):
    this_version = int(packet[:3], 2)
    this_typeid = packet[3:6]
    packet = packet[6:]
    if this_typeid == "100":
        value = ""
        while len(packet) >= 5:
            value += packet[:5]
            start_bit = packet[0]
            packet = packet[5:]
            if start_bit == "0":
                break
        return this_version, packet  # int(value, 2)
    sub_packets_version_sum = 0
    if packet[0] == "1":
        sub_packets = int(packet[1:12], 2)
        packet = packet[12:]
        for sub_packet in range(sub_packets):
            current_sub_packet_sum, packet = get_version_sum_A(packet)
            sub_packets_version_sum += current_sub_packet_sum
        return sub_packets_version_sum + this_version, packet
    sub_packets_length = int(packet[1:16], 2)
    packet = packet[16:]
    stop_at_len = len(packet) - sub_packets_length
    while len(packet) > stop_at_len:
        current_sub_packet_sum, packet = get_version_sum_A(packet)
        sub_packets_version_sum += current_sub_packet_sum
    return sub_packets_version_sum + this_version, packet


print("***", get_version_sum_A(main_packet)[0], "***")
print("***", get_version_sum_B(main_packet)[0], "***")

