# from django.utils.deprecation import MiddlewareMixin
# from django.core.exceptions import PermissionDenied
# class BlackListIPMiddleware(MiddlewareMixin):
#     IP_BLACK_LIST = [
#         '10.10.80.123'
#     ]
#     def procress_view(self, request, *args, **kwargs):
#         ip = request.META['REMOTE_ADDR']
#         print('my ip', ip)
#         if ip in self.IP_BLACK_LIST:
#             raise PermissionDenied