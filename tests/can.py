def test_can_frame_structure():
 frame_bits = {
        'SOF': 1, 'ID_Std': 11, 'RTR': 1, 'IDE': 1, 'r0': 1,
        'DLC': 4, 'Data_8bytes': 64, 'CRC': 15, 'CRC_Delimiter': 1,
        'ACK_Slot': 1, 'ACK_Delimiter': 1, 'EOF': 7, 'Interframe_Space': 3
    }
 total_bits = sum(frame_bits.values())
 assert total_bits == 111, f"CAN frame validation FAILED: {total_bits} != 111 bits"
 print("✅ CAN 2.0B frame test: PASSED ✓")

# EXECUTE YOUR FIRST ADAS TEST
if __name__ == "__main__":
    test_can_frame_structure()