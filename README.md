# gokart_learn 

`pip install gokart`

## とりあえずluigiのまとめ  

`requires`  
　依存関係にある別のTaskを呼ぶ。 
  ```
  Task B:
    requires(Task A)
  ``` 
  Aのrunの結果がBにかえる

`run`  
  実行内容   
  requiresのrunの結果をinputとして受け取る  
  結果をoutputにretuenする  

`output`  

  Taskの出力  

### パラメータを受け取る
`params = luigi.Parameter()`で受け取る

実行時に`python luigi_hello.py Addok --params='Yo' --local-scheduler`  
のようにしてコマンドライン引数としてパラメータを受け取れる




### 参考サイト  
<https://www.m3tech.blog/entry/2018/10/17/105115>

## Gokart

  