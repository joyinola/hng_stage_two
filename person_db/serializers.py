from rest_framework import serializers
from person_db.models import Person,Physique,Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=[
            'area',
            'state',
            'house_no'


        ]
class PhysiqueSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=Physique
        fields=[
            'height',
            'weight',
            'complexion'
        ]

class PersonSerializer(serializers.ModelSerializer):
  
    address=AddressSerializer(allow_null=True,required=False)
   
    physique=PhysiqueSerializer(allow_null=True,required=False)
 
    class Meta:
        model=Person
        fields=[
            'name',
            'email',
            'physique',
            'address'
      
        ]

    def create(self,validated_data):
        physique_data=validated_data.pop('physique') if 'physique' in validated_data.keys() else {}
        address_data=validated_data.pop('address') if 'address' in validated_data.keys() else {}
    

        physique= Physique.objects.create(
            height=physique_data.setdefault('height'),
            weight = physique_data.setdefault('weight'),
            complexion= physique_data.setdefault('complexion'),
        )
        address=Address.objects.create(

            area=  address_data.setdefault('area'),
            state=  address_data.setdefault('state'),
            house_no=address_data.setdefault('house_no')
        )
        person = Person.objects.create(
            name=validated_data['name'],
            email=validated_data.setdefault('email'),
            physique=physique,
            address=address
         

        )

       
        return person
    def update(self,instance, validated_data):
        physique_data=validated_data.pop('physique') if 'physique' in validated_data.keys() else {}
        address_data=validated_data.pop('address') if 'address' in validated_data.keys() else {}
        instance.name=validated_data.get('name', instance.name)
        instance.email=validated_data.get('name', instance.name)
        instance.address.state=address_data.get('state',instance.address.state)
        instance.address.area=address_data.get('area',instance.address.area)
        instance.address.house_no=address_data.get('house_no',instance.address.house_no)
        instance.physique.height=physique_data.get('height',instance.physique.height)
        instance.physique.weight=physique_data.get('weight',instance.physique.weight)
        instance.physique.complexion=physique_data.get('complexion',instance.physique.complexion)
        instance.address.save()
        instance.physique.save()
        instance.save()
        return instance




        '''
        def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
'''
        pass

    def validate(self, attrs):
   
        name=attrs.get('name','')
        if not isinstance(name,str):
            raise serializers.ValidationError('name is not a string')
        return attrs