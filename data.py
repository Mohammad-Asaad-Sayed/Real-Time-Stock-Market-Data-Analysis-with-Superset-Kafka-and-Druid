import yfinance as yf
import json
import time
from confluent_kafka import Producer

# --- Config ---
ticker_symbol = "AAPL"   # ✅ stable ticker
kafka_topic = "test-topic"

# --- Kafka Producer ---
producer = Producer({
    'bootstrap.servers': 'localhost:9092'
})

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered to {msg.topic()}")

# --- Initialize ticker ONCE ---
stock = yf.Ticker(ticker_symbol)

print(f"🚀 Streaming {ticker_symbol} (REAL DATA ONLY)...")

try:
    while True:
        try:
            price = None

            # --- Primary: fast_info (fast & reliable) ---
            try:
                price = stock.fast_info.get("last_price", None)
            except Exception as e:
                print(f"⚠️ fast_info error: {e}")

            # --- Fallback: history ---
            if price is None:
                try:
                    data = stock.history(period="1d", interval="1m")
                    if not data.empty:
                        latest = data["Close"].dropna()
                        if not latest.empty:
                            price = float(latest.iloc[-1])
                except Exception as e:
                    print(f"⚠️ history error: {e}")

            # --- Skip if no data ---
            if price is None:
                print("⛔ No real data available. Skipping...")
                time.sleep(30)
                continue

            payload = {
                "Price": round(price, 2),
                "Name": ticker_symbol,
                "Timestamp": int(time.time() * 1000)
            }

            producer.produce(
                kafka_topic,
                key=ticker_symbol,
                value=json.dumps(payload),
                callback=delivery_report
            )

            producer.poll(0)

            print(f"📤 {payload}")

        except Exception as e:
            print(f"❌ Loop error: {e}")

        # --- Delay (important to avoid blocking) ---
        time.sleep(30)

except KeyboardInterrupt:
    print("\n🛑 Stopped by user")

finally:
    print("🏁 Closing Kafka...")
    producer.flush()
    producer.close()
    print("✅ Kafka closed")