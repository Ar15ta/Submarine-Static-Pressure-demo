# -*- coding: utf-8 -*-
"""深潜器压力云图演示启动器：内置 HTTP 服务器 + 自动打开浏览器"""
import http.server, socketserver, functools, threading, webbrowser, os, sys, socket

PORT = 8765

def resource_dir():
    # PyInstaller onefile：资源解压到 sys._MEIPASS；否则用脚本所在目录
    return getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

def free_port(p):
    s = socket.socket()
    try:
        s.bind(('127.0.0.1', p)); s.close(); return p
    except OSError:
        s.close()
        s2 = socket.socket(); s2.bind(('127.0.0.1', 0)); p2 = s2.getsockname()[1]; s2.close()
        return p2

def main():
    os.chdir(resource_dir())
    port = free_port(PORT)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler)
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
        def end_headers(self):
            self.send_header('Cache-Control', 'no-store')
            super().end_headers()
    httpd = socketserver.ThreadingTCPServer(('127.0.0.1', port), Quiet)
    httpd.daemon_threads = True
    url = f'http://127.0.0.1:{port}/index.html'
    print('=' * 52)
    print('  深潜器压力云图教学演示')
    print(f'  地址: {url}')
    print('  关闭本窗口即退出演示')
    print('=' * 52)
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
