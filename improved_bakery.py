import matplotlib.pyplot as plt
import mysql.connector
from datetime import datetime
import os

# Database configuration - Use environment variables for security
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '123456'),  # Change this!
    'database': 'items'
}

class BakeryManagementSystem:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_database()
        self.setup_database()

    def connect_database(self):
        """Establish database connection with error handling"""
        try:
            self.connection = mysql.connector.connect(
                host=DB_CONFIG['host'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password']
            )
            self.cursor = self.connection.cursor()
            print("Database connection established successfully!")
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}")
            exit(1)

    def setup_database(self):
        """Initialize database and tables"""
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS items")
            self.cursor.execute("USE items")
            
            # Create tables
            self.create_tables()
            self.insert_default_data()
            
        except mysql.connector.Error as err:
            print(f"Database setup error: {err}")

    def create_tables(self):
        """Create all necessary tables"""
        # Products table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cs(
                Sno INT PRIMARY KEY,
                products VARCHAR(20),
                cost INT,
                stock_quantity INT DEFAULT 100,
                min_stock_level INT DEFAULT 10,
                size VARCHAR(10) DEFAULT 'Regular'
            )
        """)
        
        # Varieties table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vip(
                Sno INT,
                varieties VARCHAR(20)
            )
        """)
        
        # Workers table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS worker(
                Sno INT,
                Name VARCHAR(20),
                Salary INT
            )
        """)
        
        # Inventory log table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory_log(
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_sno INT,
                change_type VARCHAR(20),
                quantity_changed INT,
                log_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    def insert_default_data(self):
        """Insert default data if tables are empty"""
        # Check and insert products
        self.cursor.execute("SELECT * FROM cs")
        if not self.cursor.fetchall():
            products_data = [
                (1, 'Cake', 300, 50, 5, 'Regular'),
                (2, 'Pastry', 20, 100, 10, 'Small'),
                (3, 'Milk', 60, 80, 8, '1L'),
                (4, 'Butter', 20, 60, 6, '200g'),
                (5, 'Cheese', 30, 40, 4, '250g'),
                (6, 'Kitkat Waffle', 110, 30, 3, 'Large')
            ]
            self.cursor.executemany(
                "INSERT INTO cs VALUES (%s, %s, %s, %s, %s, %s)", 
                products_data
            )
        
        # Check and insert varieties
        self.cursor.execute("SELECT * FROM vip")
        if not self.cursor.fetchall():
            varieties_data = [
                (1, 'Vanilla'), (2, 'Chocolate'), 
                (3, 'Strawberry'), (4, 'Butter_Scotch')
            ]
            self.cursor.executemany(
                "INSERT INTO vip VALUES (%s, %s)", 
                varieties_data
            )
        
        # Check and insert workers
        self.cursor.execute("SELECT * FROM worker")
        if not self.cursor.fetchall():
            workers_data = [
                (1, 'Mukesh', 10000), (2, 'Kunj', 10000),
                (3, 'Suresh', 10000), (4, 'Raju', 10000)
            ]
            self.cursor.executemany(
                "INSERT INTO worker VALUES (%s, %s, %s)", 
                workers_data
            )
        
        self.connection.commit()

    def safe_execute(self, query, params=None):
        """Execute query with error handling"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Query execution error: {err}")
            return None

    def display_banner(self):
        """Display welcome banner"""
        print("=" * 90)
        print("                        🧁 BAKERY MANAGEMENT SYSTEM 🧁")
        print("                           Made by: Om, Ayush")
        print("                           Session: 2024-2025")
        print("=" * 90)

    def admin_login(self):
        """Handle admin authentication"""
        username = input("USERNAME: ")
        try:
            password = int(input("ENTER PASSWORD: "))
            return password == 1234
        except ValueError:
            print("Invalid password format!")
            return False

    def display_items(self):
        """Display all items in formatted table"""
        query = "SELECT * FROM cs ORDER BY sno"
        items = self.safe_execute(query)
        
        if items:
            print(f"{'S.No':<5} {'Product':<15} {'Cost':<8} {'Stock':<8} {'Min Stock':<10} {'Size':<10}")
            print("-" * 70)
            for sno, products, cost, stock, min_stock, size in items:
                status = "⚠️ LOW" if stock <= min_stock else "✅ OK"
                print(f"{sno:<5} {products:<15} {cost:<8} {stock:<8} {min_stock:<10} {size:<10} {status}")

    def add_item(self):
        """Add new item to inventory"""
        try:
            sno = int(input("Enter S.No: "))
            product = input("Enter product name: ")
            cost = int(input("Enter the cost: "))
            stock = int(input("Enter initial stock quantity: "))
            min_stock = int(input("Enter minimum stock level: "))
            size = input("Enter product size: ") or 'Regular'
            
            query = "INSERT INTO cs VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (sno, product, cost, stock, min_stock, size))
            self.connection.commit()
            print(f"✅ Item '{product}' added successfully!")
            
        except (ValueError, mysql.connector.Error) as e:
            print(f"❌ Error adding item: {e}")

    def update_cost(self):
        """Update product cost"""
        try:
            self.display_items()
            sno = int(input("Enter S.No of product to update: "))
            new_cost = int(input("Enter new cost: "))
            
            query = "UPDATE cs SET cost = %s WHERE sno = %s"
            self.cursor.execute(query, (new_cost, sno))
            self.connection.commit()
            print("✅ Cost updated successfully!")
            self.display_items()
            
        except (ValueError, mysql.connector.Error) as e:
            print(f"❌ Error updating cost: {e}")

    def view_graph(self):
        """Display product price graph"""
        try:
            query = "SELECT products, cost FROM cs"
            data = self.safe_execute(query)
            
            if data:
                products = [item[0] for item in data]
                prices = [item[1] for item in data]
                
                plt.figure(figsize=(12, 6))
                bars = plt.bar(products, prices, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'])
                
                # Add value labels on bars
                for bar, price in zip(bars, prices):
                    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                            f'₹{price}', ha='center', va='bottom', fontweight='bold')
                
                plt.xlabel('Products')
                plt.ylabel('Price (₹)')
                plt.title('📊 Product Price Analysis')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
        except Exception as e:
            print(f"❌ Error displaying graph: {e}")

    def check_low_stock(self):
        """Display low stock alerts"""
        query = "SELECT * FROM cs WHERE stock_quantity <= min_stock_level ORDER BY stock_quantity"
        low_stock_items = self.safe_execute(query)
        
        if low_stock_items:
            print("\n🚨 LOW STOCK ALERT 🚨")
            print("-" * 60)
            print(f"{'Product':<15} {'Size':<10} {'Current':<8} {'Min Level':<10}")
            print("-" * 60)
            for item in low_stock_items:
                sno, products, cost, stock, min_stock, size = item
                print(f"{products:<15} {size:<10} {stock:<8} {min_stock:<10}")
            print("\n⚠️ URGENT: Restock these items immediately!")
        else:
            print("✅ All products have sufficient stock!")

    def customer_interface(self):
        """Handle customer operations"""
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        
        cart = []
        total_cost = 0
        
        print("\n🛒 Welcome to our Bakery! Here's what we have:")
        
        continue_shopping = True
        while continue_shopping:
            # Display available items
            query = "SELECT sno, products, cost, stock_quantity, size FROM cs WHERE stock_quantity > 0 ORDER BY sno"
            items = self.safe_execute(query)
            
            if not items:
                print("😔 Sorry! No items are currently in stock.")
                break
            
            print(f"\n{'S.No':<5} {'Product':<15} {'Size':<10} {'Cost':<8} {'Stock':<8}")
            print("-" * 50)
            for sno, products, cost, stock, size in items:
                print(f"{sno:<5} {products:<15} {size:<10} ₹{cost:<7} {stock:<8}")
            
            try:
                choice = int(input("\nEnter S.No of item to buy: "))
                
                # Validate choice
                valid_items = [item[0] for item in items]
                if choice not in valid_items:
                    print("❌ Invalid choice or item out of stock!")
                    continue
                
                # Get item details
                item_query = "SELECT * FROM cs WHERE sno = %s"
                item_info = self.safe_execute(item_query, (choice,))[0]
                sno, product_name, unit_price, stock, min_stock, size = item_info
                
                # Handle cake varieties
                if choice == 1:  # Cake
                    variety_query = "SELECT * FROM vip ORDER BY sno"
                    varieties = self.safe_execute(variety_query)
                    
                    print("\n🍰 Available Cake Varieties:")
                    for v_sno, variety in varieties:
                        print(f"{v_sno}: {variety}")
                    
                    try:
                        variety_choice = int(input("Choose variety: "))
                        if 1 <= variety_choice <= len(varieties):
                            variety_name = varieties[variety_choice-1][1]
                            product_name = f"{variety_name} Cake"
                        else:
                            print("❌ Invalid variety choice!")
                            continue
                    except ValueError:
                        print("❌ Invalid input!")
                        continue
                
                # Get quantity
                print(f"Available stock: {stock}")
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity > stock:
                        print(f"❌ Sorry! Only {stock} units available.")
                        continue
                    elif quantity <= 0:
                        print("❌ Invalid quantity!")
                        continue
                except ValueError:
                    print("❌ Invalid quantity!")
                    continue
                
                # Add to cart
                item_total = quantity * unit_price
                cart.append({
                    'sno': sno,
                    'product': product_name,
                    'quantity': quantity,
                    'unit_price': unit_price,
                    'total': item_total
                })
                total_cost += item_total
                
                print(f"✅ Added {quantity} {product_name} to cart!")
                
                # Ask to continue
                more = input("\nAdd another item? (Y/N): ").upper()
                if more != 'Y':
                    continue_shopping = False
                    
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        # Process order
        if cart:
            # Update stock and generate bill
            print("\n" + "="*70)
            print("                           🧾 YOUR BILL")
            print("="*70)
            print(f"Customer: {name}")
            print(f"Phone: {phone}")
            print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("-"*70)
            print(f"{'Item':<25} {'Qty':<5} {'Price':<8} {'Total':<8}")
            print("-"*70)
            
            for item in cart:
                print(f"{item['product']:<25} {item['quantity']:<5} ₹{item['unit_price']:<7} ₹{item['total']:<7}")
                
                # Update stock
                update_query = "UPDATE cs SET stock_quantity = stock_quantity - %s WHERE sno = %s"
                self.cursor.execute(update_query, (item['quantity'], item['sno']))
                
                # Log transaction
                log_query = "INSERT INTO inventory_log (product_sno, change_type, quantity_changed) VALUES (%s, %s, %s)"
                self.cursor.execute(log_query, (item['sno'], 'SALE', item['quantity']))
            
            self.connection.commit()
            
            print("-"*70)
            print(f"{'TOTAL AMOUNT:':<35} ₹{total_cost}")
            print("="*70)
            print("         🙏 Thank you for shopping with us! 🙏")
            print("="*70)
        else:
            print("🛒 No items purchased.")

    def admin_menu(self):
        """Display admin menu and handle admin operations"""
        print("\n🔧 ADMIN PANEL")
        print("-" * 50)
        menu_options = {
            1: "Add Item", 2: "View Items", 3: "Update Cost",
            4: "Add Cake Variety", 5: "View Price Graph",
            6: "Check Low Stock", 7: "Exit Admin"
        }
        
        for key, value in menu_options.items():
            print(f"{key}. {value}")
        
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                self.add_item()
            elif choice == 2:
                self.display_items()
            elif choice == 3:
                self.update_cost()
            elif choice == 4:
                self.add_variety()
            elif choice == 5:
                self.view_graph()
            elif choice == 6:
                self.check_low_stock()
            elif choice == 7:
                return False
            else:
                print("❌ Invalid choice! Please select 1-7.")
                
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        
        return True

    def add_variety(self):
        """Add new cake variety"""
        try:
            sno = int(input("Enter S.No: "))
            variety = input("Enter variety name: ")
            
            query = "INSERT INTO vip VALUES (%s, %s)"
            self.cursor.execute(query, (sno, variety))
            self.connection.commit()
            print(f"✅ Variety '{variety}' added successfully!")
            
        except (ValueError, mysql.connector.Error) as e:
            print(f"❌ Error adding variety: {e}")

    def run(self):
        """Main application loop"""
        self.display_banner()
        
        while True:
            print("\n🏪 MAIN MENU")
            print("1. Admin Login")
            print("2. Customer")
            print("3. Exit")
            
            try:
                choice = int(input("\nEnter your choice: "))
                
                if choice == 1:
                    if self.admin_login():
                        print("✅ Admin login successful!")
                        admin_active = True
                        while admin_active:
                            admin_active = self.admin_menu()
                    else:
                        print("❌ Invalid password!")
                        
                elif choice == 2:
                    self.customer_interface()
                    
                elif choice == 3:
                    print("👋 Thank you for using Bakery Management System!")
                    break
                    
                else:
                    print("❌ Invalid choice! Please select 1-3.")
                    
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break

    def __del__(self):
        """Clean up database connections"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# Run the application
if __name__ == "__main__":
    try:
        bakery = BakeryManagementSystem()
        bakery.run()
    except Exception as e:
        print(f"Application error: {e}")
