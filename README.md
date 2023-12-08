# Часть 1. Запросы SQL 
# Задание 1
SELECT c.login, 
COUNT(*) AS OrdersCount
FROM "Couriers" AS C 
INNER JOIN "Orders" AS O ON c.id=o."courierId" 
WHERE o."inDelivery"=true 
GROUP BY c.login;

# Задание 2
SELECT track, 
CASE 
WHEN finished = true THEN 2 
WHEN cancelled = true THEN -1 
WHEN "inDelivery" = true THEN 1 
ELSE 0 
END AS status 
FROM "Orders";

# Часть 2. Автоматизация теста к API
# Для запуска тестов должны быть установлены пакеты pytest и requests. 
# Запуск всех тестов выполняется командой pytest.