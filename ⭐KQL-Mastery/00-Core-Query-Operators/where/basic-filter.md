# Basic Filter - WHERE Operator

## Description
Filters records from a dataset based on conditions using the `where` operator. It supports numeric, string, and time-based filtering.

## Query
```kql
SecurityEvent
| where EventID == 4625
```

## Query (Multiple Variations)

### Numeric Filter
```kql
SecurityEvent
| where EventID == 4625
```

### Multiple Conditions
```kql
SecurityEvent
| where EventID == 4625 and AccountType == "User"
```

### Time-Based Filter
```kql
SecurityEvent
| where TimeGenerated > ago(1h)
```

### String Filter
```kql
SecurityEvent
| where Account contains "admin"
```

## Result (Sample Output)

| TimeGenerated        | EventID | Account   | Computer  |
|---------------------|---------|-----------|-----------|
| 2026-05-30 10:10    | 4625    | user1     | VM-WIN-01 |
| 2026-05-30 10:11    | 4625    | admin01   | VM-WIN-01 |
| 2026-05-30 10:12    | 4625    | user2     | VM-WIN-01 |
