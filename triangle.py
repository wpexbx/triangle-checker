import numpy as np
import matplotlib.pyplot as plt
import os

def validate_sides(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    return a + b > c and a + c > b and b + c > a

def validate_angles(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    return a + b + c == 180

def classify_by_sides(a, b, c):
    if a == b == c:
        return 'Triângulo Equilátero'
    elif a == b or b == c or a == c:
        return 'Triângulo Isósceles'
    else:
        return 'Triângulo Escaleno'

def classify_by_angles(a, b, c):
    angles = sorted([a, b, c])
    if angles[2] == 90:
        return 'Triângulo Retângulo'
    elif angles[2] < 90:
        return 'Triângulo Acutângulo'
    else:
        return 'Triângulo Obtusângulo'

def create_triangle_image_by_sides(a, b, c):
    A = np.array([0, 0])
    B = np.array([a, 0])
    angle = np.arccos((b**2 + a**2 - c**2) / (2 * b * a))
    C = np.array([b * np.cos(angle), b * np.sin(angle)])
    
    draw_triangle(A, B, C)

def create_triangle_image_by_angles(A, B, C):
    a = 5
    b = a * np.sin(np.radians(B)) / np.sin(np.radians(C))
    c = a * np.sin(np.radians(A)) / np.sin(np.radians(C))
    
    create_triangle_image_by_sides(a, b, c)

def draw_triangle(A, B, C):
    plt.figure()
    plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'k-')
    plt.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], 'b', alpha=0.3)
    plt.xlim(-1, max(A[0], B[0], C[0]) + 1)
    plt.ylim(-1, max(A[1], B[1], C[1]) + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    
    img_path = os.path.join('static', 'triangle.png')
    plt.savefig(img_path)
    plt.close