CAN : Control area network
- CAN uses Bus topology
- messege type protocol
- max speed is 1 Mbps
- is a message type/ broadcast type protocol.
- can uses differential signalling has two wires can_h and can_l and has two states.
    * Dominant state(0): Can_h is ~3.5V, CAN_L is 1.5V ( diff = 2v)
    * Recessive state(1): both has same volatge 2.5v having diff of 0

- Can uses Artibitration mechanism to prioritize messages
  * if two node transmit simultaneously messege with lower id wins
  * uses CSMA ( carriar sense mutiple access with collision resolution)

- Can Frame
  [SOF(1 bit)][Artibration field(11-bit identifier + RTR bit)][Control field(IDE+reserved bit(r0)+DLC(0-8))][data fies(0-8 bytes)][CRC field(15 bit)][ACK Field][EOF{7 recessive bits}]

- CAN FD(Flexible data rate)
 * Can fd uses 2 different bitrate in single frame.
 * till arbitration it uses 1 mbps speed and change its speed when it enters the data field
 * can fd has 64 bytes per frame (8 in can)
 * High-Level Diagram (Standard 11-bit ID)
   [SOF] [Arbitration] [Control] [Data Phase (Fast)] [CRC Phase (Fast)] [ACK] [EOF]
 * 4 bit dlc is used 
   0000 - 1000 (0-8 bytes)
   1001 - 12 bytes
   1010 - 16 bytes
   1111 - 64 bytes

- to achieve high speeds single bit is divided into time quanta

- The Three States:
 * Error Active: (TEC/REC < 128). The node functions normally. If it sees an error, it screams with a Dominant Error Flag (6 dominant bits), which destroys the current frame so everyone ignores it.
 * Error Passive: (TEC/REC > 127). The node is "on probation." If it sees an error, it sends a Passive Error Flag (6 recessive bits). This does not destroy the frame for others. It also has to wait an extra 8 bits before trying to talk again (Suspend Transmission).
 * Bus Off: (TEC > 255). The node assumes its hardware is broken. It physically disconnects from the bus. Communication can only be restored by a software reset.