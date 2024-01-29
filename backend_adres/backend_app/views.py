from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.db.models import Q
from .models import Adquisicion

@csrf_exempt
@require_POST
def registrar_datos(request):
    try:
        # se regitran los datos y se valida los campos requeridos para llenar la bd
        datos_json = json.loads(request.body)
        campos_requeridos = ['presupuesto', 'unidad', 'tipo', 'cantidad', 'valorUnitario', 'fechaAdquisicion', 'proveedor', 'documentacion']
        for campo in campos_requeridos:
            if campo not in datos_json:
                raise ValueError(f'El campo "{campo}" es requerido.')
            #realiza el guardado
        nueva_adquisicion = Adquisicion.objects.create(
            presupuesto=datos_json['presupuesto'],
            unidad=datos_json['unidad'],
            tipo=datos_json['tipo'],
            cantidad=datos_json['cantidad'],
            valor_unitario=datos_json['valorUnitario'],
            valor_total=datos_json['valorTotal'],
            fecha_adquisicion=datos_json['fechaAdquisicion'],
            proveedor=datos_json['proveedor'],
            documentacion=datos_json['documentacion']
        )

        return JsonResponse({'mensaje': 'Datos registrados correctamente'}, status=201)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Error al decodificar el JSON en el cuerpo de la solicitud'}, status=400)

    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)

    except Exception as e:
        # Manejar otras excepciones
        return JsonResponse({'error': f'Error interno del servidor: {str(e)}'}, status=500)
@csrf_exempt
def actualizar_datos(request, adquisicion_id):
    try:
        datos_json = json.loads(request.body)
        print(datos_json)
        campos_requeridos = ['presupuesto', 'unidad', 'tipo', 'cantidad', 'valorUnitario', 'fechaAdquisicion', 'proveedor', 'documentacion']
        for campo in campos_requeridos:
            if campo not in datos_json:
                raise ValueError(f'El campo "{campo}" es requerido.')

        # Actualizar registro existente
        adquisicion = Adquisicion.objects.get(pk=adquisicion_id)
        adquisicion.presupuesto = datos_json['presupuesto']
        adquisicion.unidad = datos_json['unidad']
        adquisicion.tipo = datos_json['tipo']
        adquisicion.cantidad = datos_json['cantidad']
        adquisicion.valor_unitario = datos_json['valorUnitario']
        adquisicion.fecha_adquisicion = datos_json['fechaAdquisicion']
        adquisicion.proveedor = datos_json['proveedor']
        adquisicion.documentacion = datos_json['documentacion']
        adquisicion.save()

        return JsonResponse({'mensaje': 'Datos actualizados correctamente'}, status=200)

    except Adquisicion.DoesNotExist:
        return JsonResponse({'error': 'El registro especificado no existe'}, status=404)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Error al decodificar el JSON en el cuerpo de la solicitud'}, status=400)

    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)

    except Exception as e:
        return JsonResponse({'error': f'Error interno del servidor: {str(e)}'}, status=500)

def historial_adquisiciones(request):
    try:

        adquisiciones = Adquisicion.objects.all()

        # Serializar los datos a un formato JSON
        adquisiciones_json = [
            {
                'id': adq.id,
                'presupuesto': adq.presupuesto,
                'unidad': adq.unidad,
                'tipo': adq.tipo,
                'cantidad': adq.cantidad,
                'valor_unitario': adq.valor_unitario,
                'valor_total': adq.valor_total,
                'fecha_adquisicion': adq.fecha_adquisicion,
                'proveedor': adq.proveedor,
                'documentacion': adq.documentacion
            }
            for adq in adquisiciones
        ]
        # Puedes devolver una respuesta JSON si es necesario
        return JsonResponse({'historial_adquisiciones': adquisiciones_json}, status=200)

    except Exception as e:
        # Manejar otras excepciones
        return JsonResponse({'error': f'Error interno del servidor: {str(e)}'}, status=500)