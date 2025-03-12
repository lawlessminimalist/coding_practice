from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os
import mimetypes

class KubernetesFileServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        if path == '/':
            self.send_response(200)
            self.send_header("Content-type","text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, world")
        elif path == '/list-files':
            try:
                self.send_response(200)
                self.send_header("Content-type","text/plain")
                self.end_headers()
                response = self.list_files()
                self.wfile.write(response.encode())
            except Exception as e:
                self.send_error(500,f"There was an issue on the server listing files:{e}")
        elif path == '/get-file':
            try:
                self.get_file()
            except Exception as e:
                self.send_error(500,f"There was an issue on the server listing files:{e}")
        else:
            self.send_error(404,f"Route not found")


    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        if path.startswith('/upload'):
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            response = self.upload_file()
            self.wfile.write(response.encode())


        else:
            self.send_error(404, f"{path} not found")

    

    def get_file(self):
        parsed_url = urllib.parse.urlparse(self.path)
        
        query_params = urllib.parse.parse_qs(parsed_url.query)
        file_id = query_params.get('file_id')
        if file_id is None:
            self.send_error(300, "Invalid request, file id not provided")
            return
        file_id = file_id[0]

        file_path = f"./files/{file_id}"
        if not os.path.exists(file_path):
            self.send_error(404, "File requested does not exist")
            return
        
        content_type,_ = mimetypes.guess_type(file_path)

        try:
            if not content_type:
                content_type = "application/octet-stream"

            self.send_response(200)
            self.send_header('Content-type',content_type)
            self.end_headers()

            with open(file_path,'rb') as file:
                self.wfile.write(file.read())
            
            
        except Exception as e:
            self.send_error(500,"Error returning file in server")

    def list_files(self) -> str:
        # Ensure the directory exists to avoid an error
        directory = './files'
        if not os.path.exists(directory):
            return "Directory not found."
        files = os.listdir(directory)
        # Use "\n" for a newline, not "/n"
        response = "\n".join(files)
        if response == "":
            return "No files found in files directory"
        return response

    def upload_file(self) -> str:
        directory = './files'
        if not os.path.exists(directory):
            return "Upload directory not found."
        
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            self.send_error(400, "No file data received")
            return
        
        # check if file_id is provided
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)

        file_id = query_params.get('file_id')
        if file_id is None:
            return f"Error uploading file: please provide a valid file_id header"
        file_id = file_id[0]

        # read contents into memory
        content = self.rfile.read(content_length)

        content_type = self.headers.get("Content-Type")
        if not content_type:
            # Default to binary if no content type is provided
            content_type = "application/octet-stream"
    
        extension = mimetypes.guess_extension(content_type)
        if not extension:
            extension = ""  
        file_path = os.path.join(directory, f"{file_id}{extension}")


        try:
            # save contents to file in directory under file id
            if os.path.exists(file_path):
                return 'File not saved, matching file already exists'
            with open(file_path,'xb') as file:
                file.write(content)
            return f"{file_id} has been saved successfully"
        # return with success or error message
        except Exception as e:
            return f"Error uploading file: {e}"
        


        







def run(server_class=HTTPServer,handler_class=KubernetesFileServerHandler,port=8080):
    server_address = ("",port)
    httpd = server_class(server_address,handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()