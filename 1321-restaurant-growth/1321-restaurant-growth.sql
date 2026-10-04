-- Step 1: Aggregate daily revenue into a CTE
WITH DailyRevenue AS (
    SELECT 
        visited_on, 
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),

-- Step 2: Compute 7-day rolling sum and average using window functions
RollingWindow AS (
    SELECT 
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(
            AVG(daily_amount) OVER (
                ORDER BY visited_on 
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ), 2
        ) AS average_amount,
        -- Count how many preceding rows are included to help filter out incomplete windows
        COUNT(*) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS row_count
    FROM DailyRevenue
)

-- Step 3: Keep only the rows that have a complete 7-day window
SELECT 
    visited_on, 
    amount, 
    average_amount
FROM RollingWindow
WHERE row_count = 7
ORDER BY visited_on;