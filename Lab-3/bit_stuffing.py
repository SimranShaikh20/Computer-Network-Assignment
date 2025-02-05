def bit_stuffing(data, flag="01111110"):
    stuffed_data = ""
    count = 0

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
            count = 0  # Reset the counter

    # Add the flag at the beginning and end of the frame
    return flag + stuffed_data + flag


def bit_destuffing(stuffed_data, flag="01111110"):
    destuffed_data = ""
    count = 0

    # Remove the flag from the beginning and end
    stuffed_data = stuffed_data[len(flag):-len(flag)]

    # Iterate through each bit in the stuffed data
    for bit in stuffed_data:
        destuffed_data += bit
        if bit == '1':
            count += 1
        else:
            count = 0

        # If five consecutive '1's are followed by a '0', remove the '0'
        if count == 5:
            stuffed_data = stuffed_data[1:]  # Skip the next bit ('0')
            count = 0  # Reset the counter

    return destuffed_data


# Example usage
if __name__ == "__main__":
    # Input data
    data = "011111110111110"
    flag = "01111110"

    # Perform bit stuffing
    stuffed_data = bit_stuffing(data, flag)
    print(f"Original Data: {data}")
    print(f"Stuffed Data: {stuffed_data}")

    # Perform bit destuffing
    destuffed_data = bit_destuffing(stuffed_data, flag)
    print(f"Destuffed Data: {destuffed_data}")