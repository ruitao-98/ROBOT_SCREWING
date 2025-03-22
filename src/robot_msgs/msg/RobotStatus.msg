# 6维力/力矩分量 (单位: N 和 N·m)
float64[6] ft_vector    # xyz 方向的力和力矩
# 3维向量 (向量)
float64[3] pos_vector   
# 3x3姿态矩阵 (旋转矩阵)
float64[9] rotation_matrix    # 3x3矩阵，按行优先存储，共9个元素
# 6维向量，速度
float64[6] vel_vector