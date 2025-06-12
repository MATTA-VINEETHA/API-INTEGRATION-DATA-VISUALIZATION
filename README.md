**Company**: CODTECH IT SOLUTIONS

**Name**: MATTA VINEETHA

**Intern ID**: CT04DN1454

**Domain**: Python Programming

**Duration**: 4 weeks

**Mentor**: NEELA SANTHOSH


API INTEGRATION AND DATA VISUALIZATION
--
A Python script that fetches real-time weather data and generates visualizations using OpenWeatherMap API.
![weather_dashboard](https://github.com/user-attachments/assets/c120370d-1ea2-4e07-a21e-d257bbefb1c3)

🚀 **Features**
- Fetches **5-day forecast** for any city
- Visualizes:
  - Temperature trends (°C/°F)
  - Humidity levels (%)
  - Wind speed (m/s)
  - Weather conditions (sunny/rainy/etc.)
- Exports dashboard as **PNG image**

## ⚙️ **Setup**
1. **Get an API key** from [OpenWeatherMap](https://openweathermap.org/api)
2. **Install dependencies**:
   ```bash
   pip install requests matplotlib pandas
   ```
3. **Configure**:
   - Add your API key in `task1.py`:
     ```python
     API_KEY = "your_api_key_here"
     ```

## 🖥️ **Usage**
```bash
python task1.py
```
*Enter a city name when prompted (e.g., "Paris" or "Hyderabad,IN")*

## 📂 **Files**
| File | Purpose |
|------|---------|
| `task1.py` | Main Python script |
| `weather_dashboard.png` | Sample output |
| `.gitignore` | Excludes API keys/cache |

## 📝 **License**
[MIT](LICENSE) *(Optional - create a `LICENSE` file if needed)*



