from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .permissions import IsAdminOrReadOnly
from .models import *
from .serializers import *
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken



class APIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2

class JewelryAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            jewelry = get_object_or_404(Jewelry, pk=pk)
            serializer = JewelrySerializer(jewelry)
            return Response(serializer.data)
        else:
            jewelries = Jewelry.objects.all()
            serializer = JewelrySerializer(jewelries, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = JewelrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        jewelry = get_object_or_404(Jewelry, pk=pk)
        serializer = JewelrySerializer(jewelry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        jewelry = get_object_or_404(Jewelry, pk=pk)
        jewelry.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)
    permission_classes = (IsAuthenticated, )

class ClientAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            client = get_object_or_404(Client, pk=pk)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        else:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        client = get_object_or_404(Client, pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        client = get_object_or_404(Client, pk=pk)
        client.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)
    permission_classes = (IsAdminOrReadOnly, )
class MaterialAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            material = get_object_or_404(Material, pk=pk)
            serializer = MaterialSerializer(material)
            return Response(serializer.data)
        else:
            materials = Material.objects.all()
            serializer = MaterialSerializer(materials, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        material = get_object_or_404(Material, pk=pk)
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        material = get_object_or_404(Material, pk=pk)
        material.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class OrderStatusAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            order_status = get_object_or_404(OrderStatus, pk=pk)
            serializer = OrderStatusSerializer(order_status)
            return Response(serializer.data)
        else:
            order_statuses = OrderStatus.objects.all()
            serializer = OrderStatusSerializer(order_statuses, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = OrderStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        order_status = get_object_or_404(OrderStatus, pk=pk)
        serializer = OrderStatusSerializer(order_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        order_status = get_object_or_404(OrderStatus, pk=pk)
        order_status.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class OrderAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            order = get_object_or_404(Order, pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class ReviewAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            review = get_object_or_404(Review, pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            reviews = Review.objects.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class JewelryTypeAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            jewelry_type = get_object_or_404(JewelryType, pk=pk)
            serializer = JewelryTypeSerializer(jewelry_type)
            return Response(serializer.data)
        else:
            jewelry_types = JewelryType.objects.all()
            serializer = JewelryTypeSerializer(jewelry_types, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = JewelryTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        jewelry_type = get_object_or_404(JewelryType, pk=pk)
        serializer = JewelryTypeSerializer(jewelry_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        jewelry_type = get_object_or_404(JewelryType, pk=pk)
        jewelry_type.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class OrderCompositionAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            order_composition = get_object_or_404(OrderComposition, pk=pk)
            serializer = OrderCompositionSerializer(order_composition)
            return Response(serializer.data)
        else:
            order_compositions = OrderComposition.objects.all()
            serializer = OrderCompositionSerializer(order_compositions, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = OrderCompositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        order_composition = get_object_or_404(OrderComposition, pk=pk)
        serializer = OrderCompositionSerializer(order_composition, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        order_composition = get_object_or_404(OrderComposition, pk=pk)
        order_composition.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class SpecializationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            specialization = get_object_or_404(Specialization, pk=pk)
            serializer = SpecializationSerializer(specialization)
            return Response(serializer.data)
        else:
            specializations = Specialization.objects.all()
            serializer = SpecializationSerializer(specializations, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        specialization = get_object_or_404(Specialization, pk=pk)
        serializer = SpecializationSerializer(specialization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        specialization = get_object_or_404(Specialization, pk=pk)
        specialization.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class MasterAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            master = get_object_or_404(Master, pk=pk)
            serializer = MasterSerializer(master)
            return Response(serializer.data)
        else:
            masters = Master.objects.all()
            serializer = MasterSerializer(masters, many=True)
            return Response(serializer.data)


    def post(self, request):
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        master = get_object_or_404(Master, pk=pk)
        serializer = MasterSerializer(master, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        master = get_object_or_404(Master, pk=pk)
        master.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class ProductionAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            production = get_object_or_404(Production, pk=pk)
            serializer = ProductionSerializer(production)
        else:
            productions = Production.objects.all()
            serializer = ProductionSerializer(productions, many=True)
        return Response({'posts': serializer.data})


    def post(self, request):
        serializer = ProductionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Production.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ProductionSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        production = get_object_or_404(Production, pk=pk)
        production.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class MaterialUsageAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            material_usage = get_object_or_404(MaterialUsage, pk=pk)
            serializer = MaterialUsageSerializer(material_usage)
            return Response(serializer.data)
        else:
            material_usages = MaterialUsage.objects.all()
            serializer = MaterialUsageSerializer(material_usages, many=True)
            return Response(serializer.data)


    def post(self, request):
        serializer = MaterialUsageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        material_usage = get_object_or_404(MaterialUsage, pk=pk)
        serializer = MaterialUsageSerializer(material_usage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        material_usage = get_object_or_404(MaterialUsage, pk=pk)
        material_usage.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)
class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)



    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод PUT не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "Объект успешно удален"}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAdminOrReadOnly,)