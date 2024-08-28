def generate_rule():
    print("Welcome to Suricata and Snort Rule Generator!")
    
    # Ask for action
    action = input("Enter the action (e.g., alert, drop, pass): ").strip().lower()
    
    # Ask for protocol information
    protocol = input("Enter the protocol (e.g., tcp, udp, icmp, ip): ").strip().lower()
    
    # Source IP and Port
    src_ip = input("Enter source IP address (or 'any', '$HOME_NET', '$EXTERNAL_NET'): ").strip()
    src_port = input("Enter source port (or 'any' for any port): ").strip()
    
    # Direction
    direction = input("Enter direction (-> for src to dest or <- for dest to src): ").strip()
    
    # Destination IP and Port
    dst_ip = input("Enter destination IP address (or 'any', '$HOME_NET', '$EXTERNAL_NET'): ").strip()
    dst_port = input("Enter destination port (or 'any' for any port): ").strip()
    
    # Ask for rule options
    msg = input("Enter the rule message (short description of the rule): ").strip()
    content = input("Enter the content to match in the payload (leave blank if not needed): ").strip()
    pcre = input("Enter the PCRE to match (leave blank if not needed): ").strip()
    
    # Specific to Suricata and Snort
    classtype = input("Enter the classification type (e.g., attempted-admin, successful-admin): ").strip()
    sid = input("Enter the SID (e.g., 1000001): ").strip()
    rev = input("Enter the revision number (default is 1): ").strip()
    
    # Generate the rule
    rule = f"{action} {protocol} {src_ip} {src_port} {direction} {dst_ip} {dst_port} (msg:\"{msg}\""
    
    if content:
        rule += f"; content:\"{content}\""
    
    if pcre:
        rule += f"; pcre:\"{pcre}\""
    
    rule += f"; classtype:{classtype}; sid:{sid}; rev:{rev};)"
    
    print("\nGenerated Rule for Suricata/Snort:")
    print(rule)

# Run the rule generator
if __name__ == "__main__":
    generate_rule()
