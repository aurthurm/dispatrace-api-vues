from whitenoise.middleware import WhiteNoiseMiddleware

class CustomWhiteNoiseMiddleware(WhiteNoiseMiddleware):
    def process_request(self, request):
        if self.autorefresh:
            static_file = self.find_file(request.path_info)
        else:
            static_file = self.files.get(request.path_info)
            if not static_file and not request.path_info.startswith("/api"):
                static_file = self.files.get("/")

        if static_file is not None:
            return self.serve(static_file, request)