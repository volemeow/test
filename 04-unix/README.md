root@abruptpowder:~ # docker run -it --rm ubuntu bash
root@0db1965344a5:/# apt-get update

\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
запускаем апдейт
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

Get:1 http://archive.ubuntu.com/ubuntu noble InRelease [256 kB]
...
Get:18 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [1082 kB]
Fetched 30.0 MB in 2s (19.2 MB/s)
Reading package lists... Done
root@0db1965344a5:/# echo "nameserver 127.0.0.1" > /etc/resolv.conf

\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
меняем днс на локалхост, имена не будут резолвиться, но до айпишников все равно дойдем
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

root@0db1965344a5:/# apt-get update
Ign:1 http://security.ubuntu.com/ubuntu noble-security InRelease
...
W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/noble-security/InRelease  Temporary failure resolving 'security.ubuntu.com'
W: Some index files failed to download. They have been ignored, or old ones used instead.

\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
апдейт ожидаемо не проходит
это единственное, что получилось.
Что пробовал, но не прошло из-за минимал образа и отсутствия прав на ядро:
iptables -P OUTPUT DROP
ip route del default
была идея побить бинари вгета/курла, если бы они были
побить бинарь апта совсем чит
так что без дополнительных флагов и конфигов вне контейнера ничего больше не придумалось
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

root@0db1965344a5:/# exit