# ✈️ Flight Aggregator API

A high-performance FastAPI-based flight search aggregator that queries multiple flight providers, caches results, and stores search history in PostgreSQL.

## 🌟 Features

- **Multi-Provider Search**: Aggregates flight data from multiple providers simultaneously
- **Smart Caching**: Redis-based caching to improve response times and reduce API calls
- **Price Comparison**: Automatically identifies the cheapest flight option
- **Search History**: Stores all searches in PostgreSQL for analytics and tracking
- **Async Operations**: Built with async/await for optimal performance
- **Docker Support**: Fully containerized with Docker Compose
- **RESTful API**: Clean, well-documented API endpoints

## 🏗️ Architecture

```
flight-aggregator/
├── app/
│   ├── cache/          # Redis caching logic
│   ├── db/             # Database models and session management
│   ├── providers/      # Flight provider integrations
│   ├── schemas/        # Pydantic models for request/response
│   ├── services/       # Business logic and aggregation
│   └── main.py         # FastAPI application entry point
├── docker-compose.yaml # Container orchestration
├── dockerfile          # API container definition
├── requirements.txt    # Python dependencies
└── .env               # Environment variables
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker & Docker Compose
- PostgreSQL 16
- Redis 7

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Raunak1627/flight-aggregator.git
   cd flight-aggregator
   ```

2. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   POSTGRES_USER=your_user
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=flight_db
   DATABASE_URL=postgresql://your_user:your_password@postgres:5432/flight_db
   REDIS_URL=redis://redis:6379
   ```

3. **Start with Docker Compose**
   ```bash
   docker-compose up --build
   ```

   This will start:
   - PostgreSQL database on port `5432`
   - Redis cache on port `6379`
   - FastAPI application on port `8000`

### Local Development (Without Docker)

1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## 📡 API Endpoints

### Health Check
```http
GET /
```

**Response:**
```json
{
  "message": "Flight Aggregator API is running"
}
```

### Search Flights
```http
POST /search-flights
```

**Request Body:**
```json
{
  "origin": "DEL",
  "destination": "BLR",
  "travel_date": "2025-12-25",
  "passengers": 1,
  "cabin_class": "economy"
}
```

**Response:**
```json
{
  "search_id": "550e8400-e29b-41d4-a716-446655440000",
  "results": [
    {
      "provider": "Provider A",
      "price": 4500.00,
      "currency": "INR",
      "duration_minutes": 150,
      "stops": 0
    },
    {
      "provider": "Provider B",
      "price": 5200.00,
      "currency": "INR",
      "duration_minutes": 180,
      "stops": 1
    }
  ],
  "cheapest": {
    "provider": "Provider A",
    "price": 4500.00,
    "currency": "INR",
    "duration_minutes": 150,
    "stops": 0
  }
}
```

## 🔧 Technology Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL 16
- **Cache**: Redis 7
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Containerization**: Docker & Docker Compose

## 📊 Database Schema

### FlightSearch Table
- `id`: Primary key
- `origin`: Departure airport code
- `destination`: Arrival airport code
- `travel_date`: Date of travel
- `passengers`: Number of passengers
- `cabin_class`: Class of travel (economy, business, first)
- `cheapest_price`: Lowest price found
- `provider`: Provider offering the cheapest price
- `created_at`: Timestamp of search

## 🔄 Caching Strategy

The application uses Redis to cache flight search results based on:
- Origin airport
- Destination airport
- Travel date
- Number of passengers
- Cabin class

Cache keys are generated using a hash of these parameters, ensuring identical searches return cached results instantly.

## 🧪 Testing

Access the interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📝 Development

### Adding New Flight Providers

1. Create a new provider file in `app/providers/`
2. Implement the provider-specific search logic
3. Register the provider in `app/services/flight_aggregator.py`

### Database Migrations

The database is automatically initialized on startup. For schema changes, update the models in `app/db/models.py`.

## 🐳 Docker Commands

```bash
# Start all services
docker-compose up

# Start in detached mode
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild containers
docker-compose up --build
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Raunak**
- GitHub: [@Raunak1627](https://github.com/Raunak1627)

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- PostgreSQL and Redis for robust data storage
- Docker for seamless containerization

---

⭐ Star this repository if you find it helpful!
