
INTRO
* SOME/IP - Scalable service oriented middleware over ip
* some/ip supports remote procedure calls, event
notifications and underlying serialization/wire format.

Application:
* SOME/IP shall be
used for inter-ECU Client/Server Serialization

Spec:
* SOME/IP provides service oriented communication over a network
* Events provide data that are sent cyclically or on change from the provider to the subscriber
* Methods provide the possibility to the subscriber to issue remote procedure calls which
are executed on provider side
* Fields are combinations of one or more of the following three
   • a notifier which sends data on change from the provider to the subscribers
   • a getter which can be called by the subscriber to explicitly query the provider for the value
   • a setter which can be called by the subscriber when it wants to change the value on provider side
* Serialization describes the way data is represented in protocol data units (PDUs) as payload of either UDP or TCP messages, transported over an IP-based automotive in-vehicle network.

Structure
* The structure of header layout shall consist of
    • Message ID (Service ID/Method ID) [32Bits]
    • Length [32Bits]
    • Request ID (Client ID/Session ID) [32Bits]
    • Protocol Version [8Bits]
    • Interface Version [8Bits]
    • Message Type [8Bits]
    • Return Code [8Bits]
* In case of E2E communication protection being applied, the E2E header is placed after Return Code, depending on the chosen Offset value for the E2E header. The default Offset value is 64 bit, which puts the E2E header exactly
between Return Code and Payload.
* Message ID [32 Bit]
    • The Message ID shall be a 32 Bit identifier that is used to identify
    • the RPC call to a method of an application
    • or to identify an event.

1. Core Purpose
• Definition: An automotive-specific middleware for control communication, supporting Remote Procedure Calls (RPC), Event Notifications, and a specific wire format (serialization).
• Goal: To provide a scalable, resource-efficient communication layer compatible with various platforms (AUTOSAR, Linux, etc.) that can be sent over IP-based networks without modifying the underlying IP standard.
2. Key Communication Patterns
• Request/Response: A client sends a request and expects a response message back from the server.
• Fire & Forget (Request-No-Return): A client sends a request but does not expect or receive a response.
• Events: Data sent cyclically or on change from provider to subscriber.
• Fields: Represents a status; supports a Getter (read), Setter (write), and Notifier (automatic update upon subscription or value change).
3. Transport Protocols
• UDP: Used for small payloads or cyclic data where low latency is critical (<100ms).
• TCP: Used for large data chunks (>1400 bytes) and "exactly once" reliability, as it handles segmentation and reordering.
• SOME/IP-TP: A transport protocol used to segment large messages over UDP (up to 32 KB) when hard latency requirements still exist.

--------------------------------------------------------------------------------
Message ID and Identification Format
The Message ID is a 32-bit identifier used to route the message to the correct application and task. It is split into two 16-bit parts:
Field                Bits      Description
Service ID           16 bits   Identifies the specific service (e.g., Climate Control).
Method ID            16 bits   Identifies the task (method) or the event.
Example Identifiers
• Recommended Ranges: It is common practice to assign methods to 0x0000–0x7FFF and events/notifications to 0x8000–0x8FFF.
• Sample IDs from the sources:
    ◦ Normal Service Call: Service ID 0x0101, Method ID 0x0009 → Message ID: 0x0101 0009.
    ◦ Magic Cookie (Client to Server): Message ID: 0xFFFF 0000.
    ◦ Magic Cookie (Server to Client): Message ID: 0xFFFF 8000. 

--------------------------------------------------------------------------------
Standard SOME/IP Header Format
Every message contains a 16-byte header before the optional payload. All header fields are encoded in network byte order (big endian).
Field Name         Size                   Purpose
Message ID         32 bits                Combined Service ID and Method/Event ID.
Length             32 bits                Total bytes from the Request ID to the end of the payload.
Request ID         32 bits                Combines Client ID (identifies the caller) and Session ID (tracks sequential requests).
Protocol Version   8 bits                 Fixed at 0x01.
Interface Version  8 bits                 Major version of the Service Interface.
Message Type       8 bits                 Defines the pattern: 0x00 (Request), 0x01 (Fire & Forget), 0x02 (Notification), 0x80 (Response), 0x81 (Error).
Return Code        8 bits                 Indicates status: 0x00 (E_OK), 0x01 (E_NOT_OK), 0x03 (E_UNKNOWN_METHOD), etc.

--------------------------------------------------------------------------------
Serialization Basics
• Order: Parameters are serialized sequentially in a depth-first traversal.
• Alignment: Padding may be inserted after variable-size data to align the next element to 8, 16, 32, or 64-bit boundaries.
• Strings: Must start with a Byte Order Mark (BOM) and end with a \0 null terminator.
• TLV (Tag-Length-Value): For extensible structs, a 2-byte Tag is used to identify members, allowing the receiver to skip unknown data.
Note: While I have focused on the provided sources, standard industry practice on the internet typically identifies specific Service IDs like 0x0001 for vehicle status, but these values are project-specific and defined by the system designer