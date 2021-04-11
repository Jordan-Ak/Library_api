class GetSerializerClassMixin(object): #Class used to choose the seriailizer to use in viewsets

    def get_serializer_class(self):

        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
            
            #This mixin is resuable and if a serializer isn't in action classes uses default serial...