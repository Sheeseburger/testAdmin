from models.user import User
from extensions import db
from passlib.hash import sha256_crypt 
from models.product import Product

def create_default_data():
    print('trying to create user')
    if not User.query.filter_by(username='admin').first():
        print('making user')
        default_admin = User(username="admin", password=sha256_crypt.hash("admin"))
        db.session.add(default_admin)
        db.session.commit()
        print('user created')

    print('trying to create products')
    if not Product.query.first():
        db.session.add(Product(name="product1", price=123, category="test1",offer_of_the_month=False,description="#desc1#desc3", photo_url="https://i0.wp.com/www.gktoday.in/wp-content/uploads/2016/04/Product-in-Marketing.png?w=1140&ssl=1" ))
        db.session.add(Product(name="product2", price=223, category="test2",available=False,description="#desc2#desc5", photo_url="https://i0.wp.com/www.gktoday.in/wp-content/uploads/2016/04/Product-in-Marketing.png?w=1140&ssl=1" ))
        db.session.add(Product(name="product3", price=32555553, category="test3",self_pickup=False,description="#desc11111#desc999", photo_url="https://i0.wp.com/www.gktoday.in/wp-content/uploads/2016/04/Product-in-Marketing.png?w=1140&ssl=)1" ))
        db.session.add(Product(name="product4", price=4444423, category="test4",description="#desc", photo_url="https://s.dou.ua/CACHE/images/img/static/companies/Logo_ICAP/bb07a770d2a6707ac3e5f4066be4387d.png" ))
        db.session.commit()
        print('products created')
