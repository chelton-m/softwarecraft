#!/usr/bin/env python3
"""
Script to generate a comprehensive permission table showing which permissions each email has.
This script reads the group_user_map.json file and creates a table with emails as rows and permissions as columns.
The results are saved to an Excel file for easy tracking and analysis.
"""

import json
import os
from collections import defaultdict
from typing import Dict, Set
import pandas as pd
from datetime import datetime


def load_group_user_map():
    """Load the group user mapping from JSON file."""
    config_path = "apps/common/config/group_user_map.json"
    if not os.path.exists(config_path):
        print(f"Error: Config file not found at {config_path}")
        return {}

    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_permissions_for_group(group_name: str, group_data: Dict) -> Set[str]:
    """Extract permissions for a specific group."""
    permissions = set()

    if "modules" not in group_data:
        return permissions

    for module_name, module_data in group_data["modules"].items():
        if "models" in module_data and "permissions" in module_data:
            permission_type = module_data["permissions"]
            models = module_data["models"]

            for model in models:
                if permission_type == "view_only":
                    permissions.add(f"{module_name}.view_{model}")
                elif permission_type == "own_crud":
                    permissions.add(f"{module_name}.view_{model}")
                    permissions.add(f"{module_name}.add_{model}")
                elif permission_type == "full_crud":
                    permissions.add(f"{module_name}.view_{model}")
                    permissions.add(f"{module_name}.add_{model}")
                    permissions.add(f"{module_name}.change_{model}")
                    permissions.add(f"{module_name}.delete_{model}")

    return permissions


def generate_permission_table():
    """Generate the permission table and save to Excel."""
    group_user_map = load_group_user_map()

    # Collect all emails and their permissions
    email_permissions = defaultdict(set)
    all_permissions = set()

    for group_name, group_data in group_user_map.items():
        # Skip UI-only groups that don't have actual permissions
        ui_only_groups = {
            "SalesDailyReport_FieldUserOptions",
            "SalesCardReport_FieldUserOptions", 
            "GADailyReport_FieldUserOptions",
            "DashboardViewer"
        }

        if group_name in ui_only_groups:
            # For UI-only groups, just mark them as having access
            permissions = {f"UI_ACCESS_{group_name}"}
        else:
            permissions = get_permissions_for_group(group_name, group_data)

        all_permissions.update(permissions)

        # Add permissions to each email in the group
        if "emails" in group_data:
            for email in group_data["emails"]:
                email_permissions[email].update(permissions)

    # Sort permissions for consistent output
    sorted_permissions = sorted(all_permissions)

    # Create DataFrame for Excel
    data = []
    for email in sorted(email_permissions.keys()):
        row = [email]
        for perm in sorted_permissions:
            row.append("✓" if perm in email_permissions[email] else "✗")
        data.append(row)

    # Create DataFrame
    df = pd.DataFrame(data, columns=["Email"] + sorted_permissions)

    # Create email to groups mapping
    email_groups = defaultdict(set)
    for group_name, group_data in group_user_map.items():
        if "emails" in group_data:
            for email in group_data["emails"]:
                email_groups[email].add(group_name)

    # Create groups DataFrame
    groups_data = []
    for email in sorted(email_groups.keys()):
        groups = ", ".join(sorted(email_groups[email]))
        groups_data.append([email, groups])

    groups_df = pd.DataFrame(groups_data, columns=["Email", "Groups"])

    # Create group permissions summary
    group_permissions_data = []
    for group_name, group_data in group_user_map.items():
        if group_name in {"SalesDailyReport_FieldUserOptions", "SalesCardReport_FieldUserOptions", "GADailyReport_FieldUserOptions", "DashboardViewer"}:
            group_permissions_data.append([group_name, "UI Access Group (no specific permissions)"])
        else:
            permissions = get_permissions_for_group(group_name, group_data)
            if permissions:
                group_permissions_data.append([group_name, ", ".join(sorted(permissions))])
            else:
                group_permissions_data.append([group_name, "No permissions defined"])

    group_permissions_df = pd.DataFrame(group_permissions_data, columns=["Group", "Permissions"])

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"permission_table_{timestamp}.xlsx"

    # Save to Excel with multiple sheets
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Permission_Table', index=False)
        groups_df.to_excel(writer, sheet_name='Email_to_Groups', index=False)
        group_permissions_df.to_excel(writer, sheet_name='Group_Permissions', index=False)

        # Add summary statistics
        summary_data = [
            ["Total unique emails", len(email_permissions)],
            ["Total unique permissions", len(sorted_permissions)],
            ["Generated on", datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            ["Source file", "apps/common/config/group_user_map.json"]
        ]
        summary_df = pd.DataFrame(summary_data, columns=["Metric", "Value"])
        summary_df.to_excel(writer, sheet_name='Summary', index=False)

    print(f"✅ Permission table saved to: {filename}")
    print(f"📊 Total unique emails: {len(email_permissions)}")
    print(f"🔑 Total unique permissions: {len(sorted_permissions)}")
    print()
    print("📋 Excel file contains the following sheets:")
    print("   - Permission_Table: Main table with emails vs permissions")
    print("   - Email_to_Groups: Mapping of emails to their groups")
    print("   - Group_Permissions: Summary of permissions for each group")
    print("   - Summary: Statistics and metadata")

    # Also print to console for immediate viewing
    print()
    print("=" * 120)
    print("PERMISSION TABLE PREVIEW (first 5 rows)")
    print("=" * 120)
    print(df.head().to_string(index=False))

    return filename


if __name__ == "__main__":
    generate_permission_table() 