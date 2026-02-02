def test_can_fd_extended_frame():
    """Vector India: CAN FD 29-bit + 64-byte payload"""
    can_fd_frame = {
        'SOF': 1,
        'ID_Extended': 29,          # Same as CAN 2.0B
        'RTR_SRR': 1,
        'IDE': 1,
        'FDF': 1,                   # CAN FD flag!
        'Reserved': 1,
        'BRS': 1,                   # Bit Rate Switch
        'ESI': 1,                   # Error State Indicator
        'DLC': 1,                   # Flexible DLC encoding
        'Data_64bytes': 512,        # 64 bytes = 512 bits!
        'CRC': 21,                  # Bigger CRC
        'CRC_Del': 1,
        'ACK_Slot': 1,
        'ACK_Del': 1,
        'EOF': 7,
        'IFS': 3
    }
    total_bits = sum(can_fd_frame.values())
    assert total_bits == 594, f"CAN FD FAILED: {total_bits} != 594 bits"
    print("✅ CAN FD Extended: PASSED ✓ | 594 bits (64B payload)")

if __name__ == "__main__":
    test_can_fd_extended_frame()
