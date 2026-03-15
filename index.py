import http.server
import socketserver
import urllib.request

PORT = 80


def get_public_ip():
    try:
        return urllib.request.urlopen("https://api.ipify.org", timeout=5).read().decode()
    except Exception:
        return "unavailable"


with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    ip = get_public_ip()
    print(f"Public IP: {ip}")
    print(f"Serving at http://{ip}:{PORT}")
    httpd.serve_forever()
