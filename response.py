response1 = {
  "analysis": "#### Analysis of Online Purchasing Habits and Book Information\n\nThis analysis combines information about online purchasing habits across different store locations with data on books and their authors. The purchasing habits data includes total items sold and average customer satisfaction for each store location, specifically for online purchases where the total number of individual items sold online is greater than 15. The book data includes book titles, author names, and author birth years. Current age of the authors is calculated based on the current year.\n\n* *Online Purchasing Habits:* The table \"Un-Joined Data (1)\" provides insights into online purchasing habits. Denver has the highest number of total items sold online (11485), followed by Seattle (7096). The average customer satisfaction scores are relatively consistent across all store locations, ranging from 3.61 to 3.83.\n* *Book Information:* The table \"Un-Joined Data (2)\" lists five books along with their authors and the authors' birth years. The birth years range from 1922 to 1960.\n* *Author Ages (as of 2025):* Based on the provided data and the current year (2025), the approximate ages of the authors are as follows:\n    * Ursula K. Le Guin: 96 years old\n    * Kurt Vonnegut: 103 years old\n    * Kazuo Ishiguro: 71 years old\n    * Alice Walker: 81 years old\n    * Neil Gaiman: 65 years old",
  "generated_query": {
    "queries": [
      {
        "query_id": 1,
        "db_id": "1",
        "query_type": "aggregate",
        "query": {
          "collection": "sales",
          "pipeline": [
            {
              "$match": {
                "purchaseMethod": "Online"
              }
            },
            {
              "$unwind": "$items"
            },
            {
              "$group": {
                "_id": "$storeLocation",
                "totalItemsSold": {
                  "$sum": "$items.quantity"
                },
                "averageSatisfaction": {
                  "$avg": "$customer.satisfaction"
                }
              }
            },
            {
              "$match": {
                "totalItemsSold": {
                  "$gt": 15
                }
              }
            }
          ]
        }
      },
      {
        "query_id": 2,
        "db_id": "2",
        "query_type": "select",
        "query": "SELECT b.title, a.first_name, a.last_name, a.birth_year FROM authors AS a JOIN books AS b ON a.author_id = b.author_id LIMIT 5"
      }
    ],
    "join_on": []
  },
  "execution_time_ms": 15090,
  "data": [
    {
      "table_name": "Un-Joined Data (1)",
      "columns": [
        {
          "name": "_id",
          "type": "str"
        },
        {
          "name": "totalItemsSold",
          "type": "int"
        },
        {
          "name": "averageSatisfaction",
          "type": "float"
        }
      ],
      "rows": [
        {
          "_id": "London",
          "totalItemsSold": 5262,
          "averageSatisfaction": 3.8271028037383177
        },
        {
          "_id": "Austin",
          "totalItemsSold": 5001,
          "averageSatisfaction": 3.6184640522875817
        },
        {
          "_id": "New York",
          "totalItemsSold": 3488,
          "averageSatisfaction": 3.774078478002378
        },
        {
          "_id": "San Diego",
          "totalItemsSold": 2582,
          "averageSatisfaction": 3.609230769230769
        },
        {
          "_id": "Denver",
          "totalItemsSold": 11485,
          "averageSatisfaction": 3.748496639547223
        },
        {
          "_id": "Seattle",
          "totalItemsSold": 7096,
          "averageSatisfaction": 3.7571103526734926
        }
      ],
      "row_count": 6
    },
    {
      "table_name": "Un-Joined Data (2)",
      "columns": [
        {
          "name": "title",
          "type": "UNKNOWN"
        },
        {
          "name": "first_name",
          "type": "UNKNOWN"
        },
        {
          "name": "last_name",
          "type": "UNKNOWN"
        },
        {
          "name": "birth_year",
          "type": "UNKNOWN"
        }
      ],
      "rows": [
        {
          "title": "Pride and Prejudice",
          "first_name": "Ursula K.",
          "last_name": "Le Guin",
          "birth_year": 1929
        },
        {
          "title": "1984",
          "first_name": "Kurt",
          "last_name": "Vonnegut",
          "birth_year": 1922
        },
        {
          "title": "And Then There Were None",
          "first_name": "Kazuo",
          "last_name": "Ishiguro",
          "birth_year": 1954
        },
        {
          "title": "The Hobbit",
          "first_name": "Alice",
          "last_name": "Walker",
          "birth_year": 1944
        },
        {
          "title": "Mrs Dalloway",
          "first_name": "Neil",
          "last_name": "Gaiman",
          "birth_year": 1960
        }
      ],
      "row_count": 5
    }
  ],
  "visualization": {
    "Un-Joined Data (1)": {
      "chart_desc": "Bar chart of total items sold online for each store location",
      "chart_type": "BAR",
      "x_axis_column": "_id",
      "y_axis_column": "totalItemsSold"
    },
    "Un-Joined Data (2)": {
      "chart_desc": "Bar chart showing the publication year of each book's author.",
      "chart_type": "BAR",
      "x_axis_column": "title",
      "y_axis_column": "birth_year"
    }
  },
  "table_desc": {
    "Un-Joined Data (1)": "Total items sold and average customer satisfaction for each store location",
    "Un-Joined Data (2)": "Book title, author name, and author birth year for five books"
  },
  "error_message": "null"
}

response2 = {
    "success": 'true',
    "response_type": "analysis_result",
    "analysis": "#### Global Tech Corp. Quarterly Performance Review\n\nThis report provides a comprehensive overview of the company's performance across key areas including regional revenue, market penetration, employee satisfaction, user engagement, and marketing effectiveness. Each section is supported by a specific data visualization to provide clear, actionable insights.\n\n*   *Revenue Performance:* The bar chart in 'Quarterly Revenue by Region' clearly shows that North America remains the top-performing region, contributing over $150M in revenue. The LATAM region shows potential for growth but currently lags behind.\n*   *Market Share:* The 'OS Market Share' pie chart illustrates our dominant position in the mobile market, with Android and iOS combined accounting for 75% of new device activations.\n*   *Employee Morale:* The 'Employee Satisfaction Scores' histogram is encouraging, revealing a strong concentration of scores in the 7.0-9.0 range, indicating high overall employee morale.\n*   *User Engagement:* The 'Monthly Active Users' line chart highlights a positive year-over-year growth trend, with a significant seasonal spike in December, likely tied to holiday promotions.\n*   *Marketing Effectiveness:* The scatter plot correlating marketing spend with acquisitions shows a general positive trend. However, several outliers suggest that some high-spend campaigns are underperforming, warranting further investigation.\n\nOverall, the quarter was strong, with solid growth and market leadership. Key focus areas for the next quarter should be optimizing marketing spend and fostering growth in the LATAM region.",
    "generated_query": {
        "queries": [
            { "query_id": 1, "db_id": "1", "query_type": "aggregate", "query": "SELECT region, SUM(revenue) AS revenue_millions FROM sales_q4 GROUP BY region" },
            { "query_id": 2, "db_id": "2", "query_type": "aggregate", "query": "SELECT os, COUNT() / (SELECT COUNT() FROM activations) * 100 AS market_share FROM activations GROUP BY os" },
            { "query_id": 3, "db_id": "3", "query_type": "select", "query": "SELECT score FROM employee_surveys WHERE survey_date > '2023-10-01'" },
            { "query_id": 4, "db_id": "1", "query_type": "aggregate", "query": "SELECT STRFTIME('%Y-%m', event_date) AS month, COUNT(DISTINCT user_id) AS active_users FROM user_events GROUP BY month LIMIT 12" },
            { "query_id": 5, "db_id": "4", "query_type": "select", "query": "SELECT daily_spend, new_users FROM marketing_campaigns WHERE campaign_id = 'X-75'" },
            { "query_id": 6, "db_id": "3", "query_type": "select", "query": "SELECT ticket_id, product, summary, days_open FROM support_tickets WHERE priority = 'High' AND status = 'Open'" }
        ],
        "join_on": []
    },
    "execution_time_ms": 28450,
    "data": [
        {
            "table_name": "Quarterly Revenue by Region",
            "columns": [
                { "name": "region", "type": "string" },
                { "name": "revenue_millions", "type": "float" }
            ],
            "rows": [
                { "region": "North America", "revenue_millions": 152.5 },
                { "region": "Europe", "revenue_millions": 110.2 },
                { "region": "APAC", "revenue_millions": 95.8 },
                { "region": "LATAM", "revenue_millions": 45.1 },
                { "region": "MEA", "revenue_millions": 55.7 }
            ]
        },
        {
            "table_name": "OS Market Share on New Devices",
            "columns": [
                { "name": "operating_system", "type": "string" },
                { "name": "market_share", "type": "float" }
            ],
            "rows": [
                { "operating_system": "Android", "market_share": 45.0 },
                { "operating_system": "iOS", "market_share": 30.0 },
                { "operating_system": "Windows", "market_share": 12.0 },
                { "operating_system": "macOS", "market_share": 8.0 },
                { "operating_system": "Linux", "market_share": 3.0 },
                { "operating_system": "Other", "market_share": 2.0 }
            ]
        },
        {
            "table_name": "Employee Satisfaction Scores",
            "columns": [
                { "name": "satisfaction_score", "type": "float" }
            ],
            "rows": [
                { "satisfaction_score": 8.5 }, { "satisfaction_score": 7.2 }, { "satisfaction_score": 9.1 },
                { "satisfaction_score": 6.8 }, { "satisfaction_score": 7.5 }, { "satisfaction_score": 8.9 },
                { "satisfaction_score": 9.5 }, { "satisfaction_score": 7.8 }, { "satisfaction_score": 8.2 },
                { "satisfaction_score": 7.1 }, { "satisfaction_score": 6.5 }, { "satisfaction_score": 8.6 },
                { "satisfaction_score": 9.0 }, { "satisfaction_score": 7.7 }, { "satisfaction_score": 8.3 },
                { "satisfaction_score": 5.4 }, { "satisfaction_score": 7.9 }, { "satisfaction_score": 8.8 },
                { "satisfaction_score": 9.2 }, { "satisfaction_score": 7.0 }, { "satisfaction_score": 8.1 },
                { "satisfaction_score": 6.9 }, { "satisfaction_score": 9.8 }, { "satisfaction_score": 8.4 },
                { "satisfaction_score": 7.6 }, { "satisfaction_score": 8.7 }, { "satisfaction_score": 9.3 },
                { "satisfaction_score": 4.5 }, { "satisfaction_score": 7.3 }, { "satisfaction_score": 8.0 }
            ]
        },
        {
            "table_name": "Monthly Active Users (Last 12 Months)",
            "columns": [
                { "name": "month", "type": "string" },
                { "name": "active_users", "type": "integer" }
            ],
            "rows": [
                { "month": "Jan", "active_users": 1200000 },
                { "month": "Feb", "active_users": 1250000 },
                { "month": "Mar", "active_users": 1300000 },
                { "month": "Apr", "active_users": 1280000 },
                { "month": "May", "active_users": 1350000 },
                { "month": "Jun", "active_users": 1400000 },
                { "month": "Jul", "active_users": 1380000 },
                { "month": "Aug", "active_users": 1420000 },
                { "month": "Sep", "active_users": 1500000 },
                { "month": "Oct", "active_users": 1550000 },
                { "month": "Nov", "active_users": 1600000 },
                { "month": "Dec", "active_users": 1850000 }
            ]
        },
        {
            "table_name": "Marketing Campaign Effectiveness",
            "columns": [
                { "name": "daily_ad_spend_usd", "type": "float" },
                { "name": "new_customers_acquired", "type": "integer" }
            ],
            "rows": [
                { "daily_ad_spend_usd": 1500, "new_customers_acquired": 350 },
                { "daily_ad_spend_usd": 1800, "new_customers_acquired": 410 },
                { "daily_ad_spend_usd": 1200, "new_customers_acquired": 280 },
                { "daily_ad_spend_usd": 2500, "new_customers_acquired": 550 },
                { "daily_ad_spend_usd": 2200, "new_customers_acquired": 480 },
                { "daily_ad_spend_usd": 3000, "new_customers_acquired": 620 },
                { "daily_ad_spend_usd": 1000, "new_customers_acquired": 210 },
                { "daily_ad_spend_usd": 3500, "new_customers_acquired": 710 },
                { "daily_ad_spend_usd": 4000, "new_customers_acquired": 850 },
                { "daily_ad_spend_usd": 2800, "new_customers_acquired": 590 },
                { "daily_ad_spend_usd": 500, "new_customers_acquired": 150 },
                { "daily_ad_spend_usd": 4500, "new_customers_acquired": 920 },
                { "daily_ad_spend_usd": 3200, "new_customers_acquired": 650 },
                { "daily_ad_spend_usd": 2000, "new_customers_acquired": 430 },
                { "daily_ad_spend_usd": 5000, "new_customers_acquired": 880 }
            ]
        },
        {
            "table_name": "Open High-Priority Support Tickets",
            "columns": [
                { "name": "ticket_id", "type": "string" },
                { "name": "product", "type": "string" },
                { "name": "issue_summary", "type": "string" },
                { "name": "days_open", "type": "integer" }
            ],
            "rows": [
                { "ticket_id": "TICK-8B1A2C", "product": "Pro Suite", "issue_summary": "User cannot login with SSO", "days_open": 5 },
                { "ticket_id": "TICK-9F4D7E", "product": "Mobile App", "issue_summary": "App crashes on startup on Android 14", "days_open": 2 },
                { "ticket_id": "TICK-A3C6B8", "product": "Cloud Storage", "issue_summary": "File upload fails with large files (>1GB)", "days_open": 8 },
                { "ticket_id": "TICK-C5E9F0", "product": "Pro Suite", "issue_summary": "Export to PDF function is corrupting data", "days_open": 3 }
            ]
        }
    ],
    "visualization": {
        "Quarterly Revenue by Region": { "chart_type": "BAR", "x_axis_column": "region", "y_axis_column": "revenue_millions" },
        "OS Market Share on New Devices": { "chart_type": "PIE", "x_axis_column": "operating_system", "y_axis_column": "market_share" },
        "Employee Satisfaction Scores": { "chart_type": "HISTOGRAM", "x_axis_column": "satisfaction_score", "y_axis_column": 'null' },
        "Monthly Active Users (Last 12 Months)": { "chart_type": "LINE", "x_axis_column": "month", "y_axis_column": "active_users" },
        "Marketing Campaign Effectiveness": { "chart_type": "SCATTER", "x_axis_column": "daily_ad_spend_usd", "y_axis_column": "new_customers_acquired" },
        "Open High-Priority Support Tickets": { "chart_type": "TABLE", "x_axis_column": 'null', "y_axis_column": 'null' }
    },
    "table_desc": {
        "Quarterly Revenue by Region": "A summary of total revenue in millions USD for each major sales region in the last quarter.",
        "OS Market Share on New Devices": "Distribution of operating systems across all new devices activated this quarter.",
        "Employee Satisfaction Scores": "Raw data from the recent anonymous employee satisfaction survey (scores out of 10).",
        "Monthly Active Users (Last 12 Months)": "A 12-month trend of monthly active users for our flagship application.",
        "Marketing Campaign Effectiveness": "A scatter plot correlating daily marketing spend with the number of new customers acquired.",
        "Open High-Priority Support Tickets": "A list of currently open support tickets with the highest priority."
    },
    "error_message": 'null'
}