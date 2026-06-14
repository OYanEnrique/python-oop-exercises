'''Crie uma classe capaz de calcular frete
de veículos diferentes:

*Transporte (abstract)
-distancia
-frete
-calc_frete() (abstract)

*Moto
-fator=0.50
-calc_frete()

*Caminhao
-fator=1.20
-calc_frete() -> min 50km

*Drone
fator=9.50
-calc_frete() -> max 10km
'''

from moto import Moto
from caminhao import Caminhao
from drone import Drone


def main():
    """Função principal que executa o programa"""
    moto = Moto(20)
    print(f"Frete Moto (20 km): R$ {moto.calc_frete():.2f}")
    
    caminhao = Caminhao(50)
    print(f"Frete Caminhão (50 km): R$ {caminhao.calc_frete():.2f}")
    
    drone = Drone(10)
    print(f"Frete Drone (10 km): R$ {drone.calc_frete():.2f}")


if __name__ == "__main__":
    main()
