# Benchmark History

Historical benchmark data for NVIDIA model performance tracking.

**Test Prompt:** "For men in 50s, what are the top 3 most important daily health habits?"

## Files

- **Latest:** [`latest.json`](latest.json) - Most recent benchmark results
- **Historical:** `YYYY-MM-DD.json` - Daily benchmark snapshots

## Schema

```json
{
  "timestamp": "2026-03-24T03:00:00-08:00",
  "total_models_tested": 189,
  "successful_models": 145,
  "failed_models": 44,
  "conversational_models": 179,
  "excluded_safety_models": 10,
  "benchmark_duration_minutes": 28,
  "results": [
    {
      "model": "model/id",
      "status": "success",
      "response_time": 2.7,
      "word_count": 250,
      "quality_score": 1.0,
      "response": "First 200 chars of response..."
    }
  ],
  "fast_models_selected": [
    "model/id",
    ...
  ],
  "deep_models_selected": [
    "model/id",
    ...
  ]
}
```

## Trends

Track model performance over time:

```bash
# Get all benchmark dates
ls benchmarks/*.json | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}'

# Compare response times across dates
for file in benchmarks/*.json; do
  echo "$(basename $file):"
  jq -r '.results[] | select(.model=="meta/llama-3.1-8b-instruct") | .response_time' "$file"
done
```

## Statistics

Updated daily:
- Average response time (fast models)
- Average response time (deep models)
- Model availability changes
- Success rate trends

## Retention

- Latest benchmark: Always available as `latest.json`
- Historical: 30 days of daily snapshots
- Older than 30 days: Archived (available in git history)
