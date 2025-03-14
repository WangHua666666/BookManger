**# BookManger - 图书管理应用**

**## 项目概述**

BookManger是一个基于Flask和SQLAlchemy的简单图书管理应用。它允许用户管理图书信息，包括书名、作者、出版社、出版日期、价格和图书封面图片链接等。

**## 项目结构**

book-management-system/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── images/
├── templates/
│   ├── add_book.html
│   ├── update_book.html
│   ├── manage_books.html
│   ├── search.html
│   ├── search_results.html
│   └── index.html
├── app.py
├── models.py
├── requirements.txt
└── init_db.py


**## 安装与运行**

**### 克隆项目**

首先，将项目克隆到本地：

```bash
git clone [https://github.com/WangHua666666/BookManger.git]
cd BookManger
```

**### 创建虚拟环境并激活**

```bash
python -m venv venv
source venv/bin/activate  # 对于Windows用户，使用 `venv\Scripts\activate````
```

**### 安装依赖库**

```bash
pip install -r requirements.txt
```

**### 配置数据库**

本项目使用 SQLite 作为数据库，数据库文件名为books.db。数据库连接信息在app.py中配置：

``` python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
```

**### 运行应用**

在项目根目录下，使用以下命令启动 Flask 应用：

```bash
flask run
```
应用将在本地的http://127.0.0.1:5000地址运行。

**### 功能介绍**

#### 初始化数据库和添加初始书籍

在应用启动时，会自动创建数据库表并添加一些初始书籍数据。初始书籍数据在app.py的add_initial_books函数中定义。

#### 主要功能

1. 显示图书列表
2. 添加新图书
3. 编辑图书信息
4. 删除图书

**### 代码说明**

app.py
- 该文件是 Flask 应用的入口文件，主要包含以下内容：
    - Flask 应用初始化。 
    -     app = Flask(__name__)：创建一个 Flask 应用实例。
    -     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'：配置数据库连接 URI，使用 SQLite 数据库。
    -     db.init_app(app)：初始化 SQLAlchemy 扩展，将其与 Flask 应用关联。
    - 数据库操作。 
    -     db.create_all()：在应用上下文环境中创建数据库中所有定义的表。
    -     add_initial_books()：向数据库中添加初始书籍数据。
    - 路由定义。
    -     @app.route('/')：定义根路由，用于显示所有书籍的列表。
    -     @app.route('/add', methods=['POST'])：处理添加书籍的 POST 请求。
    -     @app.route('/update/<int:book_id>', methods=['POST'])：处理更新书籍信息的 POST 请求。
    -     @app.route('/delete/<int:book_id>')：处理删除书籍的 GET 请求。
    -     @app.route('/edit/<int:book_id>', methods=['GET'])：处理编辑书籍信息的 GET 请求。
    -     @app.route('/search', methods=['GET'])：显示搜索页面。
    -     @app.route('/search_books', methods=['POST'])：处理搜索请求的 POST 路由。
    - 模板渲染。 
    -     return render_template('index.html', books=books)：渲染 HTML 模板，并将数据传递给模板。

models.py
- 该文件定义了数据库模型，使用 SQLAlchemy 来操作数据库。

requirements.txt
- 该文件列出了项目所需的依赖库。

**### 总结**      

本项目是一个基于Flask和SQLAlchemy的简单图书管理应用，它允许用户管理图书信息，包括书名、作者、出版社、出版日期、价格和图书封面图片链接等。项目结构清晰，代码规范，功能完整，适合作为学习和实践Flask和SQLAlchemy的项目。   
