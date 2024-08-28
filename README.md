# Suricata/Snort Rule Generator

## Overview

This Python script, `rule_generator.py`, allows users to generate Suricata or Snort IDS/IPS rules based on user input. It prompts the user for various rule components and constructs a rule suitable for Suricata or Snort.

## Features

- **Generate IDS/IPS Rules**: Create rules for Suricata and Snort with customizable actions, protocols, IP addresses, ports, and messages.
- **Flexible IP Options**: Support for `$HOME_NET` and `$EXTERNAL_NET` for source and destination IP addresses.
- **Easy to Use**: Simple command-line interface to input rule parameters and generate the rule.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sudous3r/suricata-snort-rule-generator.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd suricata-snort-rule-generator
    ```

## Usage

1. Run the script:
    ```bash
    python rule_generator.py
    ```

2. Follow the prompts to input the following:
    - Action (e.g., `alert`, `drop`, `pass`)
    - Protocol (e.g., `tcp`, `udp`, `icmp`, `ip`)
    - Source IP address (or `any`, `$HOME_NET`, `$EXTERNAL_NET`)
    - Source port (or `any`)
    - Destination IP address (or `any`, `$HOME_NET`, `$EXTERNAL_NET`)
    - Destination port (or `any`)
    - Message for the rule
    - SID (e.g., `1000001`)
    - Revision number (default is `1`)

3. The script will output the generated rule based on the provided inputs.

## Example

```plaintext
Enter the action (alert, drop, pass): alert
Enter the protocol (tcp, udp, icmp, ip): tcp
Enter the source IP address (or 'any', '$HOME_NET', '$EXTERNAL_NET'): $HOME_NET
Enter the source port (or 'any'): any
Enter the destination IP address (or 'any', '$HOME_NET', '$EXTERNAL_NET'): $EXTERNAL_NET
Enter the destination port (or 'any'): 443
Enter the message for the rule: "HTTPS traffic detected"
Enter the SID (e.g., 1000001): 1000002
Enter the revision number (default is 1): 

Generated Rule:
alert tcp $HOME_NET any -> $EXTERNAL_NET 443 (msg:"HTTPS traffic detected"; sid:1000002; rev:1;)
