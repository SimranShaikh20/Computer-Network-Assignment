def bit_stuffing(data, flag="01111110"):
    stuffed_data = ""
    count = 0
    zero_added = 0  # Counter for added '0's

    # Iterate through each bit in the data
    for bit in data:
        stuffed_data += bit
        if bit == '1':
            count += 1
        else:
            count = 0

        # If five consecutive '1's are found, stuff a '0'
        if count == 5:
            stuffed_data += '0'
            zero_added += 1  # Increment counter for added '0'
            count = 0  # Reset the counter

    # Add the flag at the beginning and end of the frame
    stuffed_data = flag + stuffed_data + flag

    return stuffed_data, zero_added


def bit_destuffing(stuffed_data, flag="01111110"):
    destuffed_data = ""
    count = 0
    zero_removed = 0  # Counter for removed '0's

    # Remove the flag from the beginning and end
    stuffed_data = stuffed_data[len(flag):-len(flag)]

    i = 0
    while i < len(stuffed_data):
        destuffed_data += stuffed_data[i]
        if stuffed_data[i] == '1':
            count += 1
        else:
            count = 0

        # If five consecutive '1's are followed by a '0', remove the '0'
        if count == 5 and i + 1 < len(stuffed_data) and stuffed_data[i + 1] == '0':
            zero_removed += 1  # Increment counter for removed '0'
            i += 1  # Skip the next bit ('0')
            count = 0  # Reset the counter

        i += 1  # Move to the next bit

    return destuffed_data, zero_removed


# Example usage
if __name__ == "__main__":
    flag = "01111110"
    choice = int(input("Enter choice (1 for stuffing, 2 for destuffing): "))

    if choice == 1:
        data = input("Enter data to be stuffed (binary string, e.g., 011111110111110): ")
        stuffed_data, zero_added = bit_stuffing(data, flag)
        print(f"Original Data: {data}")
        print(f"Stuffed Data: {stuffed_data}")
        print(f"Number of '0's added: {zero_added}")
        
    elif choice == 2:
        stuffed_data = input("Enter data to be destuffed (binary string, e.g., 011111100111110): ")
        destuffed_data, zero_removed = bit_destuffing(stuffed_data, flag)
        print(f"Destuffed Data: {destuffed_data}")
        print(f"Number of '0's removed: {zero_removed}")
