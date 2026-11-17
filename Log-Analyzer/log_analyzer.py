"""
Simple Failed-Login Log Analyzer
Author: Enzu Piechaczek

Parses a Linux auth.log-style file (or any log with similar SSH failed-login
lines) and flags IP addresses with repeated failed login attempts,
a common early indicator of brute-force attacks.

Only matches "Failed password" lines with IPv4 addresses. Use it only on logs
you are authorised to analyse.

Usage:
    python log_analyzer.py sample_auth.log
    python log_analyzer.py sample_auth.log --threshold 5
"""

import argparse
import re
import sys
from collections import Counter
from datetime import datetime

FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

DEFAULT_THRESHOLD = 3  # flag IPs with this many failed attempts or more


def parse_log(filepath):
    ip_counter = Counter()
    user_counter = Counter()

    with open(filepath, "r", errors="ignore") as f:
        for line in f:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                ip_counter[match.group("ip")] += 1
                user_counter[match.group("user")] += 1

    return ip_counter, user_counter


def report(ip_counter, user_counter, threshold=DEFAULT_THRESHOLD):
    print("=== Failed Login Analysis Report ===")
    print(f"Generated: {datetime.now().isoformat()}\n")

    print("Top targeted usernames:")
    for user, count in user_counter.most_common(5):
        print(f"  {user:<15} {count} attempts")

    print("\nSuspicious IPs (>= {} failed attempts):".format(threshold))
    flagged = [(ip, c) for ip, c in ip_counter.items() if c >= threshold]
    if not flagged:
        print("  No IPs met the brute-force threshold.")
    else:
        for ip, count in sorted(flagged, key=lambda x: -x[1]):
            print(f"  {ip:<15} {count} failed attempts  -> Recommend firewall block / rate-limit review")


def main():
    parser = argparse.ArgumentParser(description="Flag IPs with repeated failed SSH logins.")
    parser.add_argument("logfile", help="path to an auth.log-style file")
    parser.add_argument(
        "--threshold",
        type=int,
        default=DEFAULT_THRESHOLD,
        help="flag IPs with at least this many failed attempts (default: %(default)s)",
    )
    args = parser.parse_args()
    if args.threshold < 1:
        parser.error("--threshold must be 1 or more")

    try:
        ip_counts, user_counts = parse_log(args.logfile)
    except FileNotFoundError:
        print(f"File not found: {args.logfile}")
        sys.exit(1)
    report(ip_counts, user_counts, args.threshold)


if __name__ == "__main__":
    main()
