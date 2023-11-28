## 起動方法
1. データベースの作成（最初とモデル更新時のみ）
```
python manage.py makemigrations
python manage.py migrate
```
2. サーバーの起動
```
python manage.py runserver
```
3. [http://127.0.0.1:8000/](http://127.0.0.1:8000/) にアクセス

## データベースの確認方法
1. スーパーユーザーの作成（最初とモデル更新時のみ）
```
python manage.py createsuperuser
```
ユーザー名とパスワードを入力。自分で考えたものでOK。  
メールは入力なしでOK（そのままエンターキー）

2. [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) にアクセス
3. 登録したユーザー名とパスワードを入力
