def calculate_z(s):

    n = len(s)  # Length of the input string
    z = [0] * n  # Initialize Z-array with zeros
    l, r, k = 0, 0, 0  # Initialize left and right boundary of Z-box

    for i in range(1, n):

       # Case 1: i is outside the current Z-box
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1

            # Case 2: i is inside the current Z-box
        else:
            k = i - l

            # Case 2a: Value does not stretch outside the Z-box
            if z[k] < r - i + 1:
                z[i] = z[k]

                # Case 2b: Value stretches outside the Z-box
            else:

               # Case 2b: Value stretches outside the Z-box
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z


def z_algorithm(pattern, text):

         # Concatenate pattern, delimiter, and text
    combined = pattern + "$" + text

    # Calculate Z-array for the combined string
    z = calculate_z(combined)

    # Length of the pattern
    pattern_length = len(pattern)

    # List to store the result indices
    result = []

    for i in range(len(z)):

      # If Z-value equals pattern length, pattern is found
        if z[i] == pattern_length:

          # Append starting index to result
            result.append(i - pattern_length - 1)

    return result

# Example usage:
pattern = "abc"
text = "ababcabc"
result = z_algorithm(pattern, text)
print("Pattern found at indices:", result)  # Output should be [2, 5]
