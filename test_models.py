from models.Admin import Admin
from models.Booking import Booking
from models.Customer import Customer

def test_admin():
    admin = Admin("test admin","123456")    
    assert admin.adminInfo() == "admin user: test admin"
    assert admin.role == "admin"

def test_customer():
    customer = Customer("test customer","123456")
    customer.bookingList.append(Booking(1,1))
    assert customer.customerInfo() == "customer user: test customer"
    assert customer.role == "customer"
    assert len(customer.bookingList) == 1

def test_booking():
    booking = Booking(1,1)
    assert booking.payStatus == "unpaid"
    