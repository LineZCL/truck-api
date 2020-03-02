# Truck API

Teste backend, desenvolvido em Python onde a idéia era a construção de uma API que controla, a carga e descarga em seus terminais

# Considerações iniciais

- Base com os terminais pré cadastrados

# Tecnologias escolhidas
- Framework Flask (Flask, Flask-Restful, Flask-Marshmallow, Flask-SqlAlchemy( 
- Banco de dados (SQLite) 
- Marshmallow 
- Python 3 

# Como rodar

1. Dá um GIT clone no projeto
2. Rodar o ambiente virtual do Python ( 
		 python3 -m venv TruckApp    
		. TruckApp/bin/activate
3. Entrar na pasta do projeto clonado e na raiz, executar: 
		pip install -r requirements.txt  
4. Executar o projeto 
		python run.py

# EndPoints
- /api/driver
-- POST: Cria novo motorista


		data : { "name": "João",
					"age": 30,
					"own_vehicle": false,
					"genre": "Male",
					"cnh_type": "A",
					"vehicle_type_id": 3}
					
	-- PUT: Atualiza motorista


		data : { "name": "João",
					"age": 30,
					"own_vehicle": false,
					"genre": "Male",
					"cnh_type": "A",
					"vehicle_type_id": 3}
					
- /driver/own-vehicle
	-- GET: Busca motoristas com veículos próprios 

- /driver/no-charge
	-- GET : Busca motoristas que estão sem cargas 

-/route/checkin
  -- POST: Faz checkin numa rota

	Data: {
	"is_loaded": true,
	"origin_id": 1,
	"destiny_id": 2,
	"driver_id": 7
	}

-/route/checkout/{id}
-- PUT: Faz checkout nesta rota


