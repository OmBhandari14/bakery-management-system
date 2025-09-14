# 🚀 Setup Guide for Bakery Management System

This guide will help you set up and run the Bakery Management System on your local machine.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: Version 3.7 or higher
- **MySQL**: Version 5.7 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: At least 500MB free space

### Software Installation

#### 1. Install Python
- **Windows**: Download from [python.org](https://www.python.org/downloads/windows/)
- **macOS**: Download from [python.org](https://www.python.org/downloads/mac-osx/) or use `brew install python3`
- **Linux (Ubuntu/Debian)**: `sudo apt update && sudo apt install python3 python3-pip`

#### 2. Install MySQL
- **Windows**: Download MySQL Installer from [mysql.com](https://dev.mysql.com/downloads/installer/)
- **macOS**: Use Homebrew: `brew install mysql`
- **Linux (Ubuntu/Debian)**: `sudo apt install mysql-server`

## 🔧 Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/bakery-management-system.git
cd bakery-management-system
```

### Step 2: Install Python Dependencies
```bash
# Using pip
pip install -r requirements.txt

# Or install individually
pip install mysql-connector-python matplotlib
```

### Step 3: MySQL Setup

#### Start MySQL Service
- **Windows**: MySQL should start automatically after installation
- **macOS**: `brew services start mysql`
- **Linux**: `sudo systemctl start mysql`

#### Create MySQL User (Optional but recommended)
```sql
-- Connect to MySQL as root
mysql -u root -p

-- Create a dedicated user for the bakery system
CREATE USER 'bakery_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON items.* TO 'bakery_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### Step 4: Configure Database Connection

#### Option 1: Environment Variables (Recommended)
Create a `.env` file in the project directory:
```bash
# .env file
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
```

#### Option 2: Direct Code Modification
Edit the database configuration in your Python file:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',    # Change this
    'password': 'your_password', # Change this
    'database': 'items'
}
```

### Step 5: Test Database Connection
Run this simple test script to verify your database connection:

```python
import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password'
    )
    print("✅ Database connection successful!")
    connection.close()
except mysql.connector.Error as err:
    print(f"❌ Database connection failed: {err}")
```

## 🏃‍♂️ Running the Application

### Method 1: Run Original Version
```bash
python bakery.py
```

### Method 2: Run Improved Version
```bash
python improved_bakery.py
```

## 🔐 Default Credentials

### Admin Access
- **Username**: Any username (system doesn't validate)
- **Password**: `1234`

> ⚠️ **Security Note**: Change the default password in production!

## 🗃️ Database Structure

The system will automatically create these tables:

1. **cs** - Products inventory
2. **vip** - Cake varieties
3. **worker** - Employee information
4. **inventory_log** - Stock change tracking

## 🎯 First Time Setup

1. **Run the application**
2. **Login as Admin** (password: 1234)
3. **Check default products** - The system comes with sample data
4. **Add your products** if needed
5. **Test customer interface** to ensure everything works

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. MySQL Connection Error
```
Error: Access denied for user 'root'@'localhost'
```
**Solution**: 
- Verify MySQL is running: `sudo systemctl status mysql`
- Reset MySQL root password if needed
- Check username and password in configuration

#### 2. Module Not Found Error
```
ModuleNotFoundError: No module named 'mysql.connector'
```
**Solution**: 
```bash
pip install mysql-connector-python
```

#### 3. Permission Denied Error
```
Error: (1045, "Access denied for user")
```
**Solution**: 
- Create a dedicated MySQL user with proper permissions
- Verify the password is correct

#### 4. Database Creation Error
```
Error: Can't create database 'items'
```
**Solution**: 
- Ensure MySQL user has CREATE privileges
- Manually create database: `CREATE DATABASE items;`

#### 5. Matplotlib Display Issues
```
No display available for matplotlib
```
**Solution**: 
- **Linux**: `sudo apt install python3-tk`
- **macOS**: Ensure XQuartz is installed
- Use `matplotlib.use('Agg')` for headless systems

## 🔧 Advanced Configuration

### Using Environment Variables
Install python-dotenv for better environment management:
```bash
pip install python-dotenv
```

Add to your Python code:
```python
from dotenv import load_dotenv
load_dotenv()
```

### MySQL Configuration File
Create `my.cnf` file:
```ini
[client]
host = localhost
user = bakery_user
password = your_secure_password
database = items
```

### Running as Service (Linux)
Create a systemd service file:
```ini
# /etc/systemd/system/bakery.service
[Unit]
Description=Bakery Management System
After=mysql.service

[Service]
Type=simple
User=bakery
WorkingDirectory=/path/to/bakery-management-system
ExecStart=/usr/bin/python3 improved_bakery.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## 📊 Performance Tips

1. **Database Optimization**: Add indexes for frequently queried fields
2. **Connection Pooling**: Use connection pooling for high traffic
3. **Caching**: Implement caching for frequently accessed data
4. **Logging**: Add comprehensive logging for debugging

## 🚀 Production Deployment

For production deployment, consider:

1. **Use environment variables** for all configuration
2. **Set up proper logging**
3. **Implement backup strategies**
4. **Use HTTPS** if deploying with web interface
5. **Set up monitoring** and alerts
6. **Regular security updates**

## 📞 Getting Help

If you encounter issues:

1. **Check this guide first**
2. **Look at error messages carefully**
3. **Search existing GitHub issues**
4. **Create a new issue** with:
   - Operating system details
   - Python version
   - MySQL version
   - Complete error message
   - Steps to reproduce

## ✅ Verification Checklist

Before considering setup complete:

- [ ] Python 3.7+ installed
- [ ] MySQL server running
- [ ] Python dependencies installed
- [ ] Database connection successful
- [ ] Application starts without errors
- [ ] Admin login works
- [ ] Customer interface accessible
- [ ] Sample data loads correctly
- [ ] Graphs display properly

---

**Happy Baking! 🧁**
