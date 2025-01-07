# CodeGenie🧞

このライブラリはAIエージェントを用いた次世代のコーディング体験を提供します。

Other Language README  
[English](README.md)

## インストール方法

GitHubリポジトリからインストールできます。

```sh
python -m pip install git+https://github.com/drago-suzuki58/CodeGenie
```

## 使い方

CodeGenieはGoogle Gemini APIを利用します。事前にAPIキーを取得してください。

[Google AI Studio](https://aistudio.google.com/app/apikey) にアクセスし、APIキーを作成してください。

**使用例:**

```python
from codegenie import CodeGenie

code_genie = CodeGenie(api_key="YOUR_API_KEY", model="gemini-2.0-flash-exp")

code_genie.数当てゲーム(1, 100)
```

上記のコードを実行すると、CodeGenieが指定された数当てゲームのPythonコードを生成し、その場で実行します。  
生成されるコード例は以下の通りです。

```python
def 数当てゲーム(*args, **kwargs):
    import random
    if len(args) == 2:
        min_num = args[0]
        max_num = args[1]
    else:
        min_num = 1
        max_num = 100
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    print(f"数当てゲームを開始します。{min_num}から{max_num}の数字を当ててください。")

    while True:
        try:
            guess = int(input("予想を入力してください: "))
            attempts += 1

            if guess < secret_number:
                print("もっと大きい数字です。")
            elif guess > secret_number:
                print("もっと小さい数字です。")
            else:
                print(f"正解です！{attempts}回で当てました。")
                break
        except ValueError:
            print("有効な数字を入力してください。")
# 数当てゲーム(1, 100)
```

以上のように`code_genie.任意の関数名()`と呼び出すことで、様々な機能をAIに生成させることができます。

## キャッシュ機能

生成されたコードは、デフォルトで`./cache`フォルダにキャッシュされます。これにより、同じ処理を再度実行する際のAPI呼び出しを削減できます。

- **キャッシュディレクトリの変更:** CodeGenie初期化時に`cache_dir`引数で変更可能です。
- **キャッシュの削除:** 該当ファイルを削除することで可能です。

## 免責事項

このライブラリは内部で`exec()`を使用しており、AIが任意のコードを実行できる状態です。確認機構が備わっていますので、生成されたコードは、実行前に必ず内容を確認してください。
セキュリティ的に危険ですので、開発・テスト環境のみでの使用を推奨します。

このライブラリの利用によって生じたいかなる損害についても、開発者は責任を負いません。自己責任での利用をお願いいたします。
