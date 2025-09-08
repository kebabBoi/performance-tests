# Импорт фабрики для создания сидера на gRPC-клиентах
from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result

# Импорт схемы плана сида — описывает, какие сущности и в каком количестве нужно создать
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan

# создаём билдер с использованием gRPC-протокола
builder = build_grpc_seeds_builder()

# вызываем метод .build(), передаём в него план генерации данных
result = builder.build(
    SeedsPlan(
        users=SeedUsersPlan(
            count=100,  # Нужно создать 100 пользователей
            credit_card_accounts=SeedAccountsPlan(
                count=1,  # У каждого пользователя — один кредитный счёт  
                physical_cards=SeedCardsPlan(count=1),  # На счёте одна физическая карта
            )
        ),
    )
)

save_seeds_result(result=result, scenario="test_scenario")

# выводим результат — структура, содержащая идентификаторы созданных пользователей, счетов, карт и операций
print(load_seeds_result(scenario="test_scenario"))
