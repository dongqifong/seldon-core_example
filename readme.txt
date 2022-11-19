s2i build . seldonio/seldon-core-s2i-python3:1.15.0 s2i_torch:0.9

docker run --name web01 -p 9007:9000 --rm s2i_torch:0.9

docker exec -it eb01 /bin/bash

# 9000不能動
# 9007是對外監聽的窗口可以自己設