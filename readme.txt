s2i build . seldonio/seldon-core-s2i-python3:1.15.0 s2i_torch:0.8

docker run -p 9007:9000 --rm s2i_torch:0.8

docker exec -it elegant_lewin /bin/bash

# 9000不能動
# 9007是對外監聽的窗口可以自己設