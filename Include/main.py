import cv2
import socket

server_ip = "124.56.50.42"
server_port = 9573
server_addr_port = (server_ip, server_port)


if __name__ == "__main__":
    capture = cv2.VideoCapture(0)
    
    while cv2.waitKey(33) < 0:
        ret, frame = capture.read()
        udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        udp_client_socket.sendto(frame.tobytes(), server_addr_port)

    capture.release()