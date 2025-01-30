# Public API for HNG Internship - Stage 0  

This is a simple FastAPI-based public API that returns basic information in JSON format.  
The API provides:  

1. My registered email address (used to register on the HNG12 Slack workspace).  
2. The current datetime as an ISO 8601 formatted timestamp (UTC).  
3. The GitHub URL of the project's codebase.  

## **Features**  
- Simple **GET** request to `/` returns a JSON-formatted response.  
- Built using **FastAPI**.  
- Handles **Cross-Origin Resource Sharing (CORS)**.  

## **Setup Instructions**  

### **Clone the repository**  
```bash
git clone https://github.com/Toluskydc/-Public-API-for-HNG-Internship---Stage-0-.git
cd your-repo
```

### **Create a virtual environment**  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **Install dependencies**  
```bash
pip install -r requirements.txt
```

### **Run the FastAPI server**  
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## **API Documentation**  

### **Endpoint URL**  
**GET** `/`

### **Request Format**  
- **Method:** `GET`  
- **Headers:**  
  ```json
  {
    "Content-Type": "application/json"
  }
  ```
- **Body:** Not required  

### **Response Format**  
- **Content-Type:** `application/json`  
- **Response Body:**  
  ```json
  {
    "email": "your-email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
  }
  ```

### **Example Usage (cURL Command)**  
```bash
curl -X GET http://127.0.0.1:8000/
```

---
https://hng.tech/hire/python-developers

---
