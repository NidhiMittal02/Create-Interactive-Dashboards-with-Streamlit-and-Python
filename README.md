# Sentiment-Analysis-of-Tweets-about-US-Airlines-using-Streamlit

## Abstract
This project focuses on building an interactive **Data Analysis and Visualization web application** using **Streamlit** to analyze the **sentiment of tweets about US Airlines**.

The application allows users to explore tweet sentiment, visualize sentiment distributions, analyze airline-specific opinions, observe tweet activity by time, and generate word clouds for textual insight.

The project integrates:

- Tweet sentiment analysis dataset exploration
- Interactive dashboard development using Streamlit
- Data visualization using charts and maps
- Text analysis using Word Cloud

---

## 1. Problem Statement
Social media platforms such as Twitter contain a large volume of public opinions about airlines, including customer experiences, complaints, and feedback. Understanding these sentiments can help identify overall public perception and service-related issues.

However, manually analyzing thousands of tweets is time-consuming and inefficient. Therefore, there is a need for an **interactive dashboard** that can help users quickly analyze and visualize airline-related tweet sentiments.

This project aims to:

1. Load and preprocess tweet sentiment data
2. Analyze positive, neutral, and negative tweets
3. Visualize sentiment distribution interactively
4. Build a Streamlit-based dashboard for easy exploration

---
### **Application URL**
- **Local Deployment (runs on your machine):** [http://localhost:8502/](http://localhost:8502/)

## 2. Simulation / Development Tool

**Web Framework:** `Streamlit`  
**Programming Language:** `Python`  
**Visualization Libraries:** `Plotly`, `Matplotlib`  
**Text Visualization:** `WordCloud`

### Why Streamlit?

- Easy conversion of Python scripts into web apps
- Interactive user interface without advanced frontend coding
- Fast dashboard development
- Seamless integration with Python data libraries

### Additional Libraries Used

- `pandas` → Data loading and preprocessing
- `numpy` → Numerical operations
- `plotly.express` → Interactive chart plotting
- `matplotlib` → Word cloud rendering
- `wordcloud` → Text-based visualization

---

## 3. Methodology

### Step 1: Dataset Loading
The tweet dataset is loaded from a CSV file (`Tweets.csv`).

The dataset contains tweet-related information such as:

- Tweet text
- Airline name
- Sentiment label
- Tweet creation time
- Location / coordinates (if available)

The target sentiment categories are:

- **Positive**
- **Neutral**
- **Negative**

---

### Step 2: Data Preprocessing
Basic preprocessing is performed before visualization and analysis.

#### Preprocessing Steps:

1. Load dataset using **Pandas**
2. Convert tweet timestamp column to **datetime format**
3. Filter tweets by sentiment, time, and airline
4. Prepare data for visualization and text analysis

---

### Step 3: Dashboard Components
The dashboard includes the following interactive components:

1. **Random Tweet Display**
2. **Sentiment Distribution Visualization**
3. **Tweet Activity by Hour**
4. **Tweet Location Mapping**
5. **Airline-wise Sentiment Breakdown**
6. **Word Cloud Generation**

---

### Step 4: Visualization Methods
The application uses multiple visual techniques to explore tweet sentiment:

| Visualization | Purpose |
|--------------|---------|
| Histogram | Shows number of tweets by sentiment |
| Pie Chart | Displays sentiment distribution proportion |
| Map | Shows tweet locations based on time |
| Word Cloud | Highlights frequently used words |
| Airline Sentiment Breakdown | Compares tweet sentiment across airlines |

---

### Step 5: Streamlit Web Application
The project is deployed as an interactive **Streamlit web app** where the user can:

1. Select a tweet sentiment
2. View random tweets
3. Choose chart type
4. Filter tweets by hour
5. Analyze airline-specific tweet sentiment
6. Generate word clouds for textual analysis

---

## 4. Application Workflow

### Input
The user interacts with the Streamlit dashboard and selects:

- Tweet sentiment
- Visualization type
- Hour of day
- Airline(s)
- Word cloud category

### Processing
The application filters and processes tweet data dynamically based on user input.

### Output
The dashboard displays:

- Random tweets
- Sentiment charts
- Tweet location map
- Airline-wise sentiment graphs
- Word cloud visualization

---

## 5. Features Implemented

### 1. Random Tweet Display
Users can select a sentiment and view a random tweet from that category.

### 2. Sentiment Visualization
The dashboard provides:

- **Histogram**
- **Pie Chart**

to visualize tweet sentiment distribution.

### 3. Time-based Tweet Analysis
Users can select an hour of the day to analyze tweet activity during that time period.

### 4. Tweet Location Mapping
Tweets can be displayed on a map (if location data is available in the dataset).

### 5. Airline-wise Sentiment Breakdown
Users can compare sentiment across different airlines such as:

- US Airways
- United
- American
- Southwest
- Delta
- Virgin America

### 6. Word Cloud
The dashboard generates word clouds for:

- Positive tweets
- Neutral tweets
- Negative tweets

This helps identify commonly used words in each sentiment category.

---

## 6. Results

### Observed Results

- The dashboard successfully loads and displays tweet sentiment data
- Interactive charts effectively visualize sentiment distribution
- Airline-wise analysis provides better comparison between airlines
- Word clouds highlight commonly occurring sentiment-specific words
- The application offers a user-friendly interface for tweet exploration

### Insights

- Negative tweets often dominate airline-related feedback datasets
- Word clouds reveal frequently discussed service-related issues
- Different airlines show varying sentiment distributions

---

## 7. Result Graphs
The application can display the following visual outputs:

- **Histogram**
- **Pie Chart**
- **Map Visualization**
- **Airline-wise Sentiment Histogram**
- **Word Cloud**

These graphs help in understanding:

- Overall sentiment trends
- Airline-specific feedback
- Tweet posting activity
- Common discussion themes

---

## 8. Discussion

- Streamlit simplifies the process of building interactive dashboards.
- Sentiment-based tweet analysis provides meaningful customer feedback insights.
- Visualization techniques improve understanding of large text-based datasets.
- Word clouds are useful for discovering frequently occurring sentiment words.
- Time and airline filters make the dashboard more insightful and interactive.

This project demonstrates how **data analysis + visualization + web deployment** can be combined into a practical and user-friendly application.

---

## 9. Conclusion
This project successfully demonstrates:

- Tweet sentiment analysis dashboard development
- Data filtering and preprocessing using Python
- Interactive visualizations using Plotly and Streamlit
- Text visualization using Word Cloud

The project shows that dashboard applications can effectively transform raw tweet data into understandable and meaningful insights.

Overall, this project is a practical example of applying **Python + Streamlit + Data Visualization** to analyze real-world social media data.

---
