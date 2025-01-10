import logging
import flask
import pathlib
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter
import python_avatars as pa

# Primero crea la aplicación Flask
app = flask.Flask("avatars-api")

# Inicializa las métricas de Prometheus con la app definida
metrics = PrometheusMetrics(app)

# Contador de visitas totales
visit_counter = Counter('site_visits', 'Total visits to the site')

# Contador de solicitudes por IP
user_requests_counter = Counter(
    'user_requests',
    'Number of requests per user',
    ['ip']
)

# Middleware para rastrear visitas y solicitudes por IP
@app.before_request
def track_visits():
    # Incrementa el contador de visitas totales
    visit_counter.inc()

    # Obtén la IP del cliente
    user_ip = flask.request.remote_addr

    # Incrementa el contador para la IP específica
    user_requests_counter.labels(ip=user_ip).inc()

# Métrica de información estática
info = metrics.info('random_metric', 'This is a random metric')
info.set(1234)

# Configura el nivel de log para werkzeug (para evitar logs innecesarios)
logging.getLogger('werkzeug').setLevel(logging.WARN)

# Habilita CORS para la aplicación
CORS(app)

# Definición de grupos y mapeos para las partes del avatar
part_groups = {
    'facial_features': ['eyebrows', 'eyes', 'mouth', 'skin_color'],
    'hair': ['top', 'hair_color', 'facial_hair', 'facial_hair_color'],
}

part_mapping = {
    'top': 'HairType',
    'hat_color': 'ClothingColor',
    'eyebrows': 'EyebrowType',
    'eyes': 'EyeType',
    'nose': 'NoseType',
    'mouth': 'MouthType',
    'facial_hair': 'FacialHairType',
    'skin_color': 'SkinColor',
    'hair_color': 'HairColor',
    'facial_hair_color': 'HairColor',
    'accessory': 'AccessoryType',
}

docker_blue = '#086DD7'
tilt_green = '#20BA31'

# Inicializa las partes de ropa antes de que la aplicación maneje cualquier solicitud
@app.before_first_request
def initialize():
    try:
        pa.ClothingType.DOCKER_SHIRT
    except AttributeError:
        pa.install_part(str(pathlib.Path(__file__).parent.joinpath('docker_shirt.svg')), pa.ClothingType)
    try:
        pa.ClothingType.TILT_SHIRT
    except AttributeError:
        pa.install_part(str(pathlib.Path(__file__).parent.joinpath('tilt_shirt.svg')), pa.ClothingType)

# Ruta principal para generar un avatar basado en los parámetros proporcionados
@app.route('/api/avatar')
def avatar():
    params = dict(flask.request.args)
    for p in params:
        if p not in part_mapping:
            params.pop(p, None)
            continue
        part_enum = getattr(pa, part_mapping[p])
        try:
            # Enum por nombre, ejemplo: `BLACK`
            params[p] = part_enum[params[p]]
        except KeyError:
            # Enum por valor, ejemplo: `#262E33`
            params[p] = part_enum(params[p])

    # Se elige el tipo de ropa y color (puedes cambiar esto según tu lógica)
    clothing = 'tilt_shirt'
    clothing_color = tilt_green

    # Para activar el Docker Shirt, descomenta esta línea
    # clothing = 'docker_shirt'
    # clothing_color = docker_blue

    # Se genera el avatar con las partes y el estilo definido
    svg = pa.Avatar(
        style=pa.AvatarStyle.CIRCLE,
        background_color='#03C7D3',
        clothing=clothing,
        clothing_color=clothing_color,
        **params
    ).render()
    
    # Se devuelve el avatar generado como una respuesta SVG
    return flask.Response(svg, mimetype='image/svg+xml')

# Ruta para obtener la especificación de las partes del avatar
@app.route('/api/avatar/spec')
def avatar_spec():
    resp = {
        'parts': part_mapping,
        'groups': part_groups,
        'exclusions': {
            'facial_hair_color': {
                'part': 'facial_hair',
                'key': 'NONE'
            },
            'hair_color': {
                'part': 'top',
                'key': 'NONE'
            }
        },
        'values': {}
    }

    # Para cada parte del avatar, se obtiene un diccionario con las opciones disponibles
    for part_type in set(resp['parts'].values()):
        values_enum = getattr(pa, part_type)
        resp['values'][part_type] = {x.name: x.value for x in values_enum}

    # Se devuelve la especificación como un JSON
    return flask.jsonify(resp)

# Ruta para indicar que la aplicación está lista
@app.route('/ready')
def ready():
    return flask.Response('', status=204)

# Corre la aplicación en el puerto 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
