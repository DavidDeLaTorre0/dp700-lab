import logging
logging.basicConfig(
level=logging.INFO,
format="%(asctime)s %(levelname)s %(message)s"
)
logging.info("Inicio")
logging.warning("Fila rechazada")
logging.error("No se pudo abrir el fichero")