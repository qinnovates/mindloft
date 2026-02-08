
## Runemate Forge: Compression Benchmark Results

| File | Original | Staves | Ratio | PQ Overhead | Net | PQ Offset? |
|------|----------|--------|-------|-------------|-----|-----------|
| bci-alert.html | 2,393 B | 911 B | 61.9% | +20,278 B | -18,796 B | NO |
| bci-dashboard.html | 20,633 B | 4,784 B | 76.8% | +20,278 B | -4,429 B | NO |
| bci-settings.html | 10,500 B | 3,509 B | 66.6% | +20,278 B | -13,287 B | NO |

### Total Transmission Comparison

| File | Classical+HTML | PQ+HTML | PQ+Staves | vs Classical |
|------|---------------|---------|-----------|-------------|
| bci-alert.html | 3,232 B | 23,510 B | 22,028 B | +18,796 B |
| bci-dashboard.html | 21,472 B | 41,750 B | 25,901 B | +4,429 B |
| bci-settings.html | 11,339 B | 31,617 B | 24,626 B | +13,287 B |