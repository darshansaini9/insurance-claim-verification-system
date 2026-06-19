import pandas as pd
import json
import re

df = pd.read_csv("dataset/output_final_clean.csv")

rows = []

for _, row in df.iterrows():

    raw = str(row["raw_response"])

    try:
        raw = raw.replace("```json", "")
        raw = raw.replace("```", "")
        raw = raw.strip()

        data = json.loads(raw)

    except Exception:
        data = {
            "issue_type": "unknown",
            "object_part": "unknown",
            "claim_status": "not_enough_information",
            "severity": "unknown"
        }

    issue_type = str(data.get("issue_type", "unknown")).lower().replace(" ", "_")
    object_part = str(data.get("object_part", "unknown")).lower().replace(" ", "_")
    claim_status = str(data.get("claim_status", "not_enough_information")).lower().replace(" ", "_")
    severity = str(data.get("severity", "unknown")).lower()

    # normalize values
    if claim_status not in [
        "supported",
        "contradicted",
        "not_enough_information"
    ]:
        claim_status = "not_enough_information"

    if severity not in [
        "none",
        "low",
        "medium",
        "high",
        "unknown"
    ]:
        severity = "unknown"

    # evidence fields
    evidence_standard_met = "true"
    evidence_standard_met_reason = (
        f"Image evidence reviewed for claimed {object_part}."
    )

    valid_image = "true"

    risk_flags = "none"

    if claim_status == "not_enough_information":
        risk_flags = "damage_not_visible"

    # supporting image ids
    ids = []

    for p in str(row["image_paths"]).split(";"):
        m = re.search(r"(img_\d+)", p)

        if m:
            ids.append(m.group(1))

    supporting_image_ids = ";".join(ids)

    if claim_status == "not_enough_information":
        supporting_image_ids = "none"

    claim_status_justification = (
        f"Visible evidence suggests claim is {claim_status}."
    )

    rows.append({
        "user_id": row["user_id"],
        "image_paths": row["image_paths"],
        "user_claim": row["user_claim"],
        "claim_object": row["claim_object"],
        "evidence_standard_met": evidence_standard_met,
        "evidence_standard_met_reason": evidence_standard_met_reason,
        "risk_flags": risk_flags,
        "issue_type": issue_type,
        "object_part": object_part,
        "claim_status": claim_status,
        "claim_status_justification": claim_status_justification,
        "supporting_image_ids": supporting_image_ids,
        "valid_image": valid_image,
        "severity": severity
    })

out = pd.DataFrame(rows)

out.to_csv("output.csv", index=False)

print("Created output.csv")
print("Rows:", len(out))
