from flask import Flask, render_template, request
import dao

from saleapp.dao import load_catagories, load_products

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    cates = load_catagories()
    products = load_products(q=q,cate_id=cate_id)
    return render_template("index.html", cates = cates, products = products)

@app.route("/products/<int:id>")
def details(id):

    return render_template("product-details.html", products= dao.get_product_by_id(id))

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)