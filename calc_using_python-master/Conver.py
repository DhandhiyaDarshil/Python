# Bits to Bytes
def bytes_to_bits(bytes):
  return bytes * 8

print(bytes_to_bits(1))
print(bytes_to_bits(1024))


# Bytes to Kilobytes
def bytes_to_kilobytes(bytes):
  return bytes / 1024
print(bytes_to_kilobytes(1024))
print(bytes_to_kilobytes(1048576))



# Kilobytes to Bytes
def kilobytes_to_bytes(kilobytes):
  return kilobytes * 1024

print(kilobytes_to_bytes(1))
print(kilobytes_to_bytes(1024))


# Kilobytes to Megabytes
def kilobytes_to_megabytes(kilobytes):
  return kilobytes / 1048576

print(kilobytes_to_megabytes(1024))
print(kilobytes_to_megabytes(1073741824))


# Megabytes to Kilobytes
def megabytes_to_kilobytes(megabytes):
  return megabytes * 1048576

print(megabytes_to_kilobytes(1))
print(megabytes_to_kilobytes(1024))
