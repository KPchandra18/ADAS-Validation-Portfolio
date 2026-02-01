
Automotive Ethernet is the backbone of the Software-Defined Vehicle (SDV). While CAN/CAN FD are excellent for control signals (steering, braking), they lack the bandwidth for ADAS cameras, LIDAR, Infotainment, and OTA (Over-the-Air) updates.

- Ethernet (100BASE-TX) uses two or four pairs of wires and is shielded. In a car, this is too heavy and expensive.

- Automotive Ethernet uses Single-Pair Unshielded Twisted Pair (UTP).
  * Weight Reduction: Up to 30% lighter than standard Ethernet cabling.
  * Full Duplex: Unlike CAN, which is half-duplex (one talker at a time), Ethernet allows simultaneous talking and listening on the same pair of wires using Echo Cancellation.
  * Bi-Directional: Data flows both ways at 100 Mbps or 1000 Mbps over a single pair of copper wires.

Speed Grades
 * 10BASE-T1S: (New) Designed to replace CAN/FlexRay for short-reach sensors.
 * 100BASE-T1: The current standard for gateways and basic ADAS.
 * 1000BASE-T1: For high-resolution cameras and "Zonal Controllers."
 * Multi-Gig (2.5G, 5G, 10G): Future-proofing for Level 4/5 Autonomous driving.

Frame :
 * Field	            Size	        Description
 * Preamble & SFD   	8 Bytes 	    Marks the start of the frame (Hardware level).
 * Destination MAC  	6 Bytes 	    MAC address of the receiving ECU (e.g., the Fusion ECU).
 * Source MAC	        6 Bytes 	    MAC address of the sender (e.g., Front Camera).
 * 802.1Q Tag (VLAN)	4 Bytes 	    CRITICAL for Automotive.
 * EtherType	        2 Bytes	        Defines the protocol (0x0800 = IPv4, 0x8100 = VLAN).
 * Payload	            46–1500B	    Contains the IP, UDP, and SOME/IP data.
 * FCS (CRC)       	    4 Bytes	        Checksum to ensure the frame isn't corrupted.