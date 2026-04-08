# Real-Time-Stock-Market-Data-Ingestion+Streaming-with-Superset-Kafka-and-Druid

<img width="1024" height="548" alt="image" src="https://github.com/user-attachments/assets/145fd867-5d39-4265-9a8e-aed5efec18be" />

# VizStockStreamer: Real-Time Apple (AAPL) Stock Visualization

Apache Kafka  
Apache Druid  
Apache Superset  
Python

A **real-time stock market data visualization** pipeline for **Apple Inc. (AAPL)**, built using **Apache Kafka, Apache Druid, and Apache Superset**. This project fetches live AAPL stock data via the **Yahoo Finance API (yfinance)**, streams it through Kafka, ingests it into Druid, and visualizes it in Superset dashboards.

---

## 📌 **Features**

- **Real-time AAPL stock data ingestion** from Yahoo Finance.
- **Kafka-based streaming** for scalable, low-latency data transfer.
- **Druid for OLAP** (real-time analytics and aggregations).
- **Superset dashboards** for interactive visualizations.
- **Modular architecture** for easy extension (e.g., adding Apache Spark).

---

## 🛠 **Tech Stack**


| Component         | Technology Stack                                                   |
| ----------------- | ------------------------------------------------------------------ |
| **Data Source**   | [yfinance](https://pypi.org/project/yfinance/) (Yahoo Finance API) |
| **Streaming**     | [Apache Kafka](https://kafka.apache.org/)                          |
| **OLAP Database** | [Apache Druid](https://druid.apache.org/)                          |
| **Visualization** | [Apache Superset](https://superset.apache.org/)                    |
| **Language**      | Python (Jupyter Notebooks, Scripts)                                |


---

## 🚀 **Getting Started**

### **Prerequisites**

- Python 3.8+
- Docker (for Kafka, Druid, Superset)
- Basic knowledge of Kafka, Druid, and Superset

### **Installation**

1. **Clone the repository:**
  ```bash
   git clone https://github.com/your-username/VizStockStreamer.git
   cd VizStockStreamer
  ```
2. **Install dependencies:**
  ```bash
   pip install -r requirements.txt
  ```
3. **Set up Kafka, Druid, and Superset:**
  - Follow the official documentation for each tool (links in the [Tech Stack](#-tech-stack) section).
  - Alternatively, use Docker Compose for local deployment (sample `docker-compose.yml` provided in `/docker`).
4. **Run the data producer:**
  ```bash
   jupyter notebook DataProducer.ipynb
  ```
  - Execute the notebook to fetch and preprocess **AAPL stock data**.
5. **Stream data to Kafka:**
  - Configure the Kafka producer (see `/kafka/producer.py`).
  - Start the producer to push **AAPL data** to your Kafka topic.
6. **Ingest data into Druid:**
  - Set up a Druid datasource to consume from Kafka (sample config in `/druid/config`).
7. **Visualize in Superset:**
  - Connect Superset to Druid and create dashboards for **AAPL stock trends** (sample queries in `/superset`).

---

## 📂 **Project Structure**

```
VizStockStreamer/
├── DataProducer.ipynb       # AAPL data extraction & preprocessing
├── kafka/
│   ├── producer.py          # Kafka producer script (AAPL data)
│   └── consumer.py          # Kafka consumer script
├── druid/
│   └── config/              # Druid ingestion configs (AAPL)
├── superset/                # Superset dashboard examples (AAPL)
├── docker/                  # Docker Compose files
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🔧 **Configuration**

- **Kafka**: Update `bootstrap.servers` and `topic` in `/kafka/producer.py` for **AAPL data**.
- **Druid**: Modify `/druid/config/ingestion.json` for your Kafka topic (AAPL).
- **Superset**: Configure the Druid connection in Superset’s UI for **AAPL visualizations**.

---

## 🌟 **Future Enhancements**

- Add **Apache Spark** for advanced analytics (e.g., predictive modeling for AAPL).
- Support **multiple stocks** (e.g., TSLA, MSFT) and custom time intervals.
- Deploy on **cloud platforms** (AWS, GCP) for scalability.

---

## 🤝 **Contributing**

Contributions are welcome! Open an issue or submit a PR for:

- Bug fixes
- New features (e.g., additional data sources for AAPL)
- Documentation improvements

---

