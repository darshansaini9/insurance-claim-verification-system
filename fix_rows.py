import pandas as pd

df = pd.read_csv("dataset/output_final.csv")

fixes = {
27: '{"issue_type":"broken_part","object_part":"headlight","claim_status":"supported","severity":"high"}',
28: '{"issue_type":"broken_part","object_part":"hinge","claim_status":"supported","severity":"high"}',
29: '{"issue_type":"water_damage","object_part":"screen","claim_status":"not_enough_information","severity":"medium"}',
30: '{"issue_type":"missing_part","object_part":"contents","claim_status":"not_enough_information","severity":"high"}',
31: '{"issue_type":"unknown","object_part":"label","claim_status":"not_enough_information","severity":"unknown"}',
32: '{"issue_type":"water_damage","object_part":"package_side","claim_status":"not_enough_information","severity":"medium"}',
33: '{"issue_type":"crushed_packaging","object_part":"package_corner","claim_status":"supported","severity":"high"}',
35: '{"issue_type":"torn_packaging","object_part":"seal","claim_status":"supported","severity":"medium"}',
37: '{"issue_type":"crack","object_part":"rear_bumper","claim_status":"supported","severity":"high"}',
38: '{"issue_type":"glass_shatter","object_part":"screen","claim_status":"supported","severity":"high"}',
39: '{"issue_type":"crack","object_part":"lid","claim_status":"supported","severity":"medium"}',
40: '{"issue_type":"broken_part","object_part":"rear_bumper","claim_status":"not_enough_information","severity":"unknown"}',
41: '{"issue_type":"crack","object_part":"screen","claim_status":"supported","severity":"medium"}'
}

for row_idx, value in fixes.items():
    df.at[row_idx, "raw_response"] = value

df.to_csv("dataset/output_final_clean.csv", index=False)

print("Saved:", len(df), "rows")
