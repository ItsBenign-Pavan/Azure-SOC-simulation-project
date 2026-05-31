# Basic Filter - WHERE Operator

## Description
Filters records from a dataset based on a condition.

## Query
```kql
SecurityEvent
| where EventID == 4625
```

## Result (Sample Output)

| TimeGenerated        | EventID | Account | Computer  |
|---------------------|---------|---------|-----------|
| 2026-05-30 10:10    | 4625    | user1   | VM-WIN-01 |
| 2026-05-30 10:12    | 4625    | user2   | VM-WIN-01 |
```
