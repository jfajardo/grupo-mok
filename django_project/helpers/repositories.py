class GenericRepository:
    """
    Clase que implementa un repositorio genérico para realizar operaciones comunes de CRUD en modelos de Django.
    """

    def __init__(self, model_class):
        """
        Inicializa una instancia del repositorio genérico.

        :param model_class: Clase del modelo asociado al repositorio.
        """
        self.model_class = model_class

    def get_all(self):
        """
        Obtiene todos los objetos del modelo asociado al repositorio.

        :return: QuerySet con todos los objetos del modelo.
        """
        return self.model_class.objects.all()

    def get_by_id(self, id):
        """
        Obtiene un objeto del modelo por su ID.

        :param id: ID del objeto a obtener.
        :return: Objeto del modelo con el ID especificado.
        :raises: DoesNotExist si el objeto no existe.
        """
        return self.model_class.objects.get(id=id)

    def create(self, data):
        """
        Crea un nuevo objeto del modelo con los datos proporcionados.

        :param data: Diccionario con los datos del objeto a crear.
        :return: Objeto del modelo recién creado.
        """
        return self.model_class.objects.create(**data)

    def update(self, instance, data):
        """
        Actualiza un objeto existente del modelo con los datos proporcionados.

        :param instance: Instancia del objeto a actualizar.
        :param data: Diccionario con los datos actualizados.
        :return: Objeto del modelo actualizado.
        """
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, instance):
        """
        Elimina un objeto existente del modelo.

        :param instance: Instancia del objeto a eliminar.
        """
        instance.delete()
