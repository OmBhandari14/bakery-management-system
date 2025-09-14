# Bakery Management System

A comprehensive Python-based Bakery Management System with MySQL database integration, featuring both administrative and customer interfaces for complete bakery operations management.

## 🚀 Features

### Admin Panel
- **Inventory Management**: Add, update, and track products with stock levels
- **Product Management**: Manage product prices, sizes, and varieties
- **Stock Monitoring**: Real-time stock tracking with low-stock alerts
- **Worker Management**: Add workers and manage salary updates
- **Inventory History**: Track all stock changes with timestamps
- **Analytics**: Visual graphs showing product prices using Matplotlib

### Customer Interface
- **Product Catalog**: Browse available items with stock status
- **Shopping Cart**: Add multiple items with quantity selection
- **Cake Customization**: Choose from different cake varieties (Vanilla, Chocolate, Strawberry, Butterscotch)
- **Real-time Stock Check**: Prevents ordering out-of-stock items
- **Automated Billing**: Generate detailed bills with customer information

### Inventory Features
- **Stock Alerts**: Automatic notifications when stock falls below minimum levels
- **Stock Updates**: Track restocking and sales with detailed logs
- **Minimum Stock Levels**: Configurable thresholds for each product
- **Size Management**: Track different product sizes (Small, Medium, Large, weights, volumes)

## 🛠️ Tech Stack

- **Backend**: Python 3.x
- **Database**: MySQL
- **Visualization**: Matplotlib
- **Database Connector**: mysql-connector-python

## 📋 Prerequisites

Before running the application, make sure you have:

1. **Python 3.x** installed
2. **MySQL Server** running
3. Required Python packages:
   ```bash
   pip install mysql-connector-python matplotlib
   ```

## 🔧 Database Setup

1. **Start MySQL Server** on your system
2. **Update database credentials** in the code:
   ```python
   con=mysql.connector.connect(
       host='localhost',
       user='root',
       password='YOUR_PASSWORD'  # Change this to your MySQL password
   )
   ```

## 🚀 Installation & Running

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/bakery-management-system.git
   cd bakery-management-system
   ```

2. **Install dependencies**:
   ```bash
   pip install mysql-connector-python matplotlib
   ```

3. **Configure database**:
   - Update MySQL credentials in `bakery.py`
   - Ensure MySQL server is running

4. **Run the application**:
   ```bash
   python bakery.py
   ```

## 📊 Database Schema

### Products Table (`cs`)
- `Sno`: Product Serial Number (Primary Key)
- `products`: Product Name
- `cost`: Product Price
- `stock_quantity`: Available Stock
- `min_stock_level`: Minimum Stock Threshold
- `size`: Product Size/Volume

### Varieties Table (`vip`)
- `Sno`: Serial Number
- `varieties`: Cake Variety Names

### Workers Table (`worker`)
- `Sno`: Worker Serial Number
- `Name`: Worker Name
- `Salary`: Worker Salary

### Inventory Log Table (`inventory_log`)
- `id`: Auto-increment Primary Key
- `product_sno`: Reference to Product
- `change_type`: Type of Change (RESTOCK, SALE, REMOVE)
- `quantity_changed`: Quantity Modified
- `log_timestamp`: Timestamp of Change

## 💻 Usage

### Admin Access
- **Username**: Any username
- **Password**: `1234`

### Admin Functions
1. **Add Items**: Add new products to inventory
2. **View Items**: Display all products with stock status
3. **Update Prices**: Modify product costs
4. **Add Varieties**: Add new cake varieties
5. **Worker Management**: Add workers and update salaries
6. **Analytics**: View price distribution graphs
7. **Inventory Management**:
   - View current stock status
   - Update stock quantities
   - Set minimum stock levels
   - Update product sizes
   - View low stock alerts
   - Check inventory change history

### Customer Functions
1. **Browse Products**: View available items with prices and stock
2. **Place Orders**: Add items to cart with quantity selection
3. **Custom Cakes**: Choose cake varieties and quantities
4. **Billing**: Automatic bill generation with customer details

## 📈 Key Features Explained

### Stock Management
- **Real-time Updates**: Stock automatically decreases when customers make purchases
- **Low Stock Alerts**: System warns when items fall below minimum levels
- **Inventory Logging**: All stock changes are recorded with timestamps

### Customer Experience
- **Stock Validation**: Prevents ordering unavailable quantities
- **Shopping Cart**: Multiple items can be added before checkout
- **Detailed Bills**: Complete transaction records with customer information

### Admin Analytics
- **Visual Graphs**: Matplotlib-powered price visualization
- **Inventory Reports**: Detailed stock status and history
- **Worker Management**: Salary tracking and updates

## 🔒 Security Notes

⚠️ **Important**: This is a educational/demonstration project. For production use, consider:

1. **Database Security**: Use environment variables for credentials
2. **Input Validation**: Add proper input sanitization
3. **SQL Injection Protection**: Use parameterized queries
4. **Authentication**: Implement proper user authentication
5. **Error Handling**: Add comprehensive try-catch blocks

## 🐛 Known Issues & Improvements

### Current Limitations
- Hardcoded admin password
- Basic error handling
- SQL injection vulnerability with string concatenation
- Functions nested in conditional blocks

### Suggested Improvements
- Implement proper authentication system
- Add input validation and error handling
- Use parameterized SQL queries
- Refactor code structure for better maintainability
- Add configuration file for database settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 👥 Authors

- **Om** - *Initial work*
- **Ayush** - *Initial work*

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/YOUR_USERNAME/bakery-management-system/issues) section
2. Create a new issue with detailed description
3. Contact the maintainers

---

**Note**: This system is designed for educational purposes and small-scale bakery operations. For large-scale commercial use, additional security measures and optimizations are recommended.