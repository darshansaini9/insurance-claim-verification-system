import os
import time
import pandas as pd
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# =========================
# GEMINI SETUP
# =========================

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# =========================
# IMAGE OPTIMIZER
# =========================

def optimize_image(path):

    img = Image.open(path)

    if img.mode != "RGB":
        img = img.convert("RGB")

    max_size = 1600

    if img.width > max_size or img.height > max_size:
        img.thumbnail((max_size, max_size))

    return img


# =========================
# LOAD CLAIMS
# =========================

claims_df = pd.read_csv(
    "dataset/claims.csv"
)

# =========================
# LOAD EXISTING OUTPUT
# =========================

output_file = "dataset/output_debug.csv"

if os.path.exists(output_file):

    results_df = pd.read_csv(output_file)

    results = results_df.to_dict(
        orient="records"
    )

    done_keys = set(
        zip(
            results_df["user_id"],
            results_df["image_paths"]
        )
    )

    print(
        f"Loaded {len(results_df)} existing rows"
    )

else:

    results = []
    done_keys = set()

# =========================
# PROCESS CLAIMS
# =========================

for _, row in claims_df.iterrows():

    key = (
        row["user_id"],
        row["image_paths"]
    )

    if key in done_keys:
        continue

    print("\n" + "=" * 60)
    print(
        f"Processing {row['user_id']}"
    )
    print("=" * 60)

    images = []

    for path in str(
        row["image_paths"]
    ).split(";"):

        full_path = os.path.join(
            "dataset",
            path
        )

        if os.path.exists(full_path):

            try:
                images.append(
                    optimize_image(full_path)
                )
            except Exception as e:
                print(
                    "Image error:",
                    e
                )

    prompt = f"""
You are an insurance claim evaluator.

Object Type:
{row['claim_object']}

Claim:
{row['user_claim']}

Return ONLY JSON.

{{
  "issue_type":"",
  "object_part":"",
  "claim_status":"",
  "severity":""
}}
"""

    success = False

    for attempt in range(3):

        try:

            response = model.generate_content(
                [prompt] + images,
                request_options={
                    "timeout": 180
                }
            )

            print(response.text)

            results.append({
                "user_id": row["user_id"],
                "image_paths": row["image_paths"],
                "user_claim": row["user_claim"],
                "claim_object": row["claim_object"],
                "raw_response": response.text
            })

            pd.DataFrame(results).to_csv(
                output_file,
                index=False
            )

            print("Saved")

            success = True

            break

        except Exception as e:

            print(
                f"Retry {attempt+1}/3:",
                e
            )

            time.sleep(15)

    if not success:
        print(
            "Skipping claim after 3 failures"
        )

    time.sleep(5)

# =========================
# FINAL SAVE
# =========================

pd.DataFrame(results).to_csv(
    output_file,
    index=False
)

print("\nDONE")
print(
    f"Total rows saved: {len(results)}"
)
