Выбрал дефолтную балансировку round robin, так как для простой выдачи хтмлной статики нет смысла использовать что-то более продвинутое. Если бы раздавали видео или что-то потяжелее, можно было бы использовать least connections, или ip hash для удержания сессий, но тут простая статика.

запуск:
ansible-playbook localhost_webapp_playbook.yml -i inventories/localhost/hosts --vault-password-file vaultpass
