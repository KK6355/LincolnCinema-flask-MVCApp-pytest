from models.Admin import Admin
from models.Booking import Booking


def test_admin():
    admin = Admin("test admin","123456")    
    assert admin.adminInfo() == "admin user: test admin"
    assert admin.role == "admin"



def test_refNum():
    booking = Booking(1,1)
    assert booking.refNum == 8000