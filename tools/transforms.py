"""Offline coordinate math. Column vectors, row-major storage, metres."""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROTATION_TOLERANCE = 5e-5  # Source matrices contain rounded decimal rotations.


def validate_matrix(matrix):
    """Validate a finite, approximately rigid, right-handed 4x4 transform."""
    if not isinstance(matrix, list) or len(matrix) != 4:
        raise ValueError('Expected a 4x4 matrix')
    for row in matrix:
        if not isinstance(row, list) or len(row) != 4:
            raise ValueError('Expected a 4x4 matrix')
        if any(type(v) not in (int, float) or not math.isfinite(v) for v in row):
            raise ValueError('Matrix values must be finite numbers')
    if any(abs(matrix[3][j] - expected) > 1e-9
           for j, expected in enumerate([0, 0, 0, 1])):
        raise ValueError('Homogeneous last row must be [0, 0, 0, 1]')
    for i in range(3):
        for j in range(3):
            dot = sum(matrix[k][i] * matrix[k][j] for k in range(3))
            if abs(dot - (1 if i == j else 0)) > ROTATION_TOLERANCE:
                raise ValueError('Rotation is not orthonormal within source rounding')
    a, b, c = [row[:3] for row in matrix[:3]]
    determinant = (a[0] * (b[1]*c[2] - b[2]*c[1])
                   - a[1] * (b[0]*c[2] - b[2]*c[0])
                   + a[2] * (b[0]*c[1] - b[1]*c[0]))
    if abs(determinant - 1) > ROTATION_TOLERANCE:
        raise ValueError('Rotation must have determinant +1')


def load_transform(product, side='right', allow_unvalidated=False):
    """Load an available calibration; never manufacture a missing hand."""
    catalog = json.loads((ROOT / 'catalog/products.json').read_text(encoding='utf-8'))
    products = {p['id']: p for p in catalog['products']}
    if product not in products:
        raise ValueError('Unknown product: ' + product)
    if side not in ('left', 'right'):
        raise ValueError('Hand must be left or right')
    if side == 'left':
        path = products[product]['left_transform']
    else:
        path = products[product]['transform']
    if path is None:
        raise ValueError(f'No {side}-hand calibration is available for {product}')
    data = json.loads((ROOT / path).read_text(encoding='utf-8'))
    if data['status'] != 'verified' and not allow_unvalidated:
        raise ValueError('Calibration is unvalidated; use --allow-unvalidated for offline review')
    if (data.get('translation_unit') != 'm'
            or data.get('vector_convention') != 'column'
            or data.get('storage') != 'row-major'
            or data.get('transform_name') != 'T_mount_tracker'
            or data.get('target_frame') != f'{side}_hand_mount_frame'
            or data.get('product') != product or data.get('side') != side):
        raise ValueError('Unexpected frame, product, hand, storage or unit contract')
    validate_matrix(data['matrix'])
    return data


def multiply(a, b):
    """Multiply two 4x4 matrices; operands are already validated by callers."""
    return [[sum(a[i][k] * b[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


def inverse(matrix):
    """Invert the preserved rounded matrix instead of approximating R^-1 by R^T."""
    validate_matrix(matrix)
    augmented = [list(map(float, row)) + [float(i == j) for j in range(4)]
                 for i, row in enumerate(matrix)]
    for col in range(4):
        pivot = max(range(col, 4), key=lambda r: abs(augmented[r][col]))
        if abs(augmented[pivot][col]) < 1e-12:
            raise ValueError('Singular matrix')
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        scale = augmented[col][col]
        augmented[col] = [v / scale for v in augmented[col]]
        for row in range(4):
            if row == col:
                continue
            factor = augmented[row][col]
            augmented[row] = [augmented[row][j] - factor * augmented[col][j]
                              for j in range(8)]
    return [row[4:] for row in augmented]


def transform_point(matrix, point):
    """Map a 3D point in metres, including translation (homogeneous w=1)."""
    validate_matrix(matrix)
    if len(point) != 3 or any(type(v) not in (int, float) or not math.isfinite(v) for v in point):
        raise ValueError('Point must contain three finite numbers in metres')
    return [sum(matrix[i][j] * point[j] for j in range(3)) + matrix[i][3]
            for i in range(3)]


def world_mount_pose(world_tracker, mount_tracker):
    """T_world_mount = T_world_tracker @ inverse(T_mount_tracker)."""
    validate_matrix(world_tracker)
    return multiply(world_tracker, inverse(mount_tracker))
