# Snake Game

Este es un juego clásico de Snake implementado usando la biblioteca `pygame` en Python.

## Instalación

Para instalar las dependencias necesarias, primero asegúrate de tener instalado Python y pip en tu sistema. Luego, ejecuta el siguiente comando en la terminal:

```
pip install -r requirements.txt
```

## Cómo jugar

1.  Ejecuta el archivo `main.py` para iniciar el juego.
2.  Usa las teclas W, A, S, D o las flechas del teclado para controlar la dirección de la serpiente.
3.  Come la comida para crecer.
4.  ¡Evita chocar contigo mismo!

## Exportar la aplicación como .exe

Si deseas exportar este juego como un archivo ejecutable `.exe` para Windows, sigue estos pasos:

1.  Asegúrate de tener `pyinstaller` instalado. Si no lo está, instálalo con `pip`:

```
pip install pyinstaller
```

2.  Navega hasta el directorio del proyecto y ejecuta el siguiente comando:

```
pyinstaller --onefile main.py
```

3.  Una vez que `pyinstaller` haya terminado de procesar, encontrarás el archivo `.exe` dentro de la carpeta `dist` en el directorio del proyecto.

4.  ¡Listo! Ahora puedes ejecutar el juego directamente desde el archivo `.exe` sin necesidad de tener Python instalado.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, realiza un fork del repositorio, crea una nueva rama, realiza tus cambios y envía un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles
