from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

# 创建数据库表和添加初始书籍的逻辑移到这里
def add_initial_books():
    pass


with app.app_context():
    db.create_all()
    add_initial_books()


def add_initial_books():
    initial_books = [
        {"book_name": "Python编程", "book_authors": "李文博", "book_publisher": "人民邮电出版社",
         "book_publication_date": "2021-01-01", "book_price": "59.00",
         "book_img_url": "https://example.com/book1.jpg"},
        {"book_name": "Flask Web开发", "book_authors": "王晨", "book_publisher": "机械工业出版社",
         "book_publication_date": "2020-02-01", "book_price": "76.00", "book_img_url": "https://example.com/flask.jpg"},
        {"book_name": "数据库系统概论", "book_authors": "黄洪奇", "book_publisher": "高等教育出版社",
         "book_publication_date": "2019-03-01", "book_price": "78.00",
         "book_img_url": "https://example.com/database.jpg"},
        {"book_name": "计算机网络", "book_authors": "林子雨", "book_publisher": "清华大学出版社",
         "book_publication_date": "2018-04-01", "book_price": "68.00",
         "book_img_url": "https://example.com/network.jpg"},
        {"book_name": "数据结构", "book_authors": "张伟", "book_publisher": "电子工业出版社",
         "book_publication_date": "2017-05-01", "book_price": "55.00",
         "book_img_url": "https://example.com/data_structure.jpg"},
        {"book_name": "人工智能基础", "book_authors": "刘洋", "book_publisher": "北京大学出版社",
         "book_publication_date": "2021-06-01", "book_price": "89.00", "book_img_url": "https://example.com/ai.jpg"},
        {"book_name": "机器学习", "book_authors": "赵敏", "book_publisher": "高等教育出版社",
         "book_publication_date": "2020-07-01", "book_price": "65.00", "book_img_url": "https://example.com/ml.jpg"},
        {"book_name": "算法导论", "book_authors": "吴鹏", "book_publisher": "机械工业出版社",
         "book_publication_date": "2019-08-01", "book_price": "99.00",
         "book_img_url": "https://example.com/algorithms.jpg"},
        {"book_name": "操作系统", "book_authors": "孙涛", "book_publisher": "清华大学出版社",
         "book_publication_date": "2018-09-01", "book_price": "79.50", "book_img_url": "https://example.com/os.jpg"},
        {"book_name": "编译原理", "book_authors": "周丽", "book_publisher": "高等教育出版社",
         "book_publication_date": "2017-10-01", "book_price": "72.00",
         "book_img_url": "https://example.com/compiler.jpg"},
        {"book_name": "计算机组成原理", "book_authors": "杨帆", "book_publisher": "机械工业出版社",
         "book_publication_date": "2021-11-01", "book_price": "85.00",
         "book_img_url": "https://example.com/computer_architecture.jpg"},
        {"book_name": "软件工程", "book_authors": "刘明", "book_publisher": "电子工业出版社",
         "book_publication_date": "2020-12-01", "book_price": "63.00",
         "book_img_url": "https://example.com/software_engineering.jpg"},
        {"book_name": "计算机体系结构", "book_authors": "李华", "book_publisher": "高等教育出版社",
         "book_publication_date": "2019-01-01", "book_price": "71.00",
         "book_img_url": "https://example.com/system_architecture.jpg"},
        {"book_name": "数据挖掘", "book_authors": "王刚", "book_publisher": "清华大学出版社",
         "book_publication_date": "2018-02-01", "book_price": "83.00",
         "book_img_url": "https://example.com/data_mining.jpg"},
        {"book_name": "深度学习", "book_authors": "赵伟", "book_publisher": "电子工业出版社",
         "book_publication_date": "2017-03-01", "book_price": "62.50",
         "book_img_url": "https://example.com/deep_learning.jpg"},
        {"book_name": "计算机视觉", "book_authors": "孙燕", "book_publisher": "高等教育出版社",
         "book_publication_date": "2021-04-01", "book_price": "80.00",
         "book_img_url": "https://example.com/computer_vision.jpg"},
        {"book_name": "自然语言处理", "book_authors": "张瑞", "book_publisher": "清华大学出版社",
         "book_publication_date": "2020-05-01", "book_price": "76.50", "book_img_url": "https://example.com/nlp.jpg"},
        {"book_name": "编程珠玑", "book_authors": "林学文", "book_publisher": "机械工业出版社",
         "book_publication_date": "2019-06-01", "book_price": "71.00", "book_img_url": "https://example.com/gems.jpg"},
        {"book_name": "算法竞赛入门", "book_authors": "周亮", "book_publisher": "高等教育出版社",
         "book_publication_date": "2018-07-01", "book_price": "86.00",
         "book_img_url": "https://example.com/algorithm_competition.jpg"},
        {"book_name": "Linux内核设计与实现", "book_authors": "杨柳", "book_publisher": "机械工业出版社",
         "book_publication_date": "2017-08-01", "book_price": "95.00",
         "book_img_url": "https://example.com/linux_kernel.jpg"},
        {"book_name": "计算机科学导论", "book_authors": "孙明", "book_publisher": "清华大学出版社",
         "book_publication_date": "2021-09-01", "book_price": "88.00",
         "book_img_url": "https://example.com/introduction_to_cs.jpg"},
        {"book_name": "Python核心技术", "book_authors": "周晓", "book_publisher": "高等教育出版社",
         "book_publication_date": "2020-10-01", "book_price": "87.50",
         "book_img_url": "https://example.com/core_python.jpg"}
    ]

    for book_info in initial_books:
        new_book = Book(
            book_name=book_info['book_name'],
            book_authors=book_info['book_authors'],
            book_publisher=book_info['book_publisher'],
            book_publication_date=book_info['book_publication_date'],
            book_price=book_info['book_price'],
            book_img_url=book_info['book_img_url']
        )
        db.session.add(new_book)
    db.session.commit()

    with app.app_context():
        db.create_all()
        add_initial_books()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add', methods=['POST'])
def add_book():
    book_name = request.form.get('book_name')
    book_authors = request.form.get('book_authors')
    book_publisher = request.form.get('book_publisher')
    book_publication_date = request.form.get('book_publication_date')
    book_price = request.form.get('book_price')
    book_img_url = request.form.get('book_img_url')

    new_book = Book(
        book_name=book_name,
        book_authors=book_authors,
        book_publisher=book_publisher,
        book_publication_date=book_publication_date,
        book_price=book_price,
        book_img_url=book_img_url
    )
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:book_id>', methods=['POST'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book.book_name = request.form.get('book_name')
        book.book_authors = request.form.get('book_authors')
        book.book_publisher = request.form.get('book_publisher')
        book.book_publication_date = request.form.get('book_publication_date')
        book.book_price = request.form.get('book_price')
        book.book_img_url = request.form.get('book_img_url')
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:book_id>', methods=['GET'])
def edit_book(book_id):
    book = Book.query.get(book_id)
    return render_template('update_book.html', book=book)

@app.route('/add_form')
def add_form():
    return render_template('add_book.html')

@app.route('/book')
def book():
    books = Book.query.all()
    return render_template('book.html', books=books)


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/manage_books')
def manage_books():
    books = Book.query.all()
    return render_template('manage_books.html', books=books)

# 搜索页面路由
@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')

# 搜索结果处理路由
@app.route('/search_books', methods=['POST'])
def search_books():
    book_name = request.form.get('book_name')
    book_id = request.form.get('book_id')

    query = Book.query

    if book_id:
        try:
            book_id = int(book_id)
            query = query.filter(Book.id == book_id)
        except ValueError:
            pass

    if book_name:
        query = query.filter(Book.book_name.like(f'%{book_name}%'))

    books = query.all()
    return render_template('search_results.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)