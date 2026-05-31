# WHERE Operator - Multiple Conditions

## Description
Filters records using multiple conditions combined with logical operators like `and`, `or`, and parentheses for complex filtering.

## Query
```kql
SecurityEvent
| where EventID == 4625 and AccountType == "User"
```

## Query (Multiple Variations)

### AND Condition
```kql
SecurityEvent
| where EventID == 4625 and AccountType == "User"
```

### OR Condition
```kql
SecurityEvent
| where EventID == 4625 or EventID == 4624
```

### Combined Conditions
```kql
SecurityEvent
| where (EventID == 4625 or EventID == 4624) and AccountType == "User"
```

### String + Numeric Filter
```kql
SecurityEvent
| where EventID == 4625 and Account contains "admin"
```

## Result (Sample Output)

| TimeGenerated        | EventID | Account   | AccountType | Computer  |
|---------------------|---------|-----------|-------------|-----------|
| 2026-05-30 10:10    | 4625    | user1     | User        | VM-WIN-01 |
| 2026-05-30 10:12    | 4624    | admin01   | User        | VM-WIN-01 |
