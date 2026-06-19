# Evaluation Report

## Model
Gemini 2.5 Flash

## Dataset

- Sample claims: 20
- Test claims: 44
- Total images processed: ~70

## Model Calls

- Approximate sample calls: 20
- Approximate test calls: 44
- Total calls: 64

## Token Usage

Estimated:
- Input: ~80k tokens
- Output: ~8k tokens

## Runtime

- Average latency per claim: 5–20 seconds
- Total runtime: approximately 20–40 minutes

## Cost Assumptions

Used Gemini 2.5 Flash free tier during development.

Estimated paid cost would be low because only short text outputs were generated per image set.

## Rate Limiting Strategy

- Incremental saving after each processed claim
- Retry handling for 429 errors
- Retry handling for 504 timeout errors
- Resume processing from existing output file
- Duplicate removal before final export

## Operational Notes

Images were treated as primary evidence.
Claim conversations were used to identify claimed damage.
User history was considered only as contextual risk information.
