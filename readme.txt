s2i build . seldonio/seldon-core-s2i-python3:1.15.0 sentiment-example-model:0.1

docker run -p 9007:9000 --rm sentiment-example-model:0.1

# 9000不能動
# 9007是對外監聽的窗口可以自己設