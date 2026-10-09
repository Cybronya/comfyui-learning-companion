# MiniMaxH3DirectorFaceRefine

## 节点类型

`MiniMaxH3DirectorFaceRefine`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `sigmas:SIGMAS`（3 次）
- `bd_grp_face_detect:BDGROUP`（3 次）
- `detector:COMBO`（3 次）
- `confidence:FLOAT`（3 次）
- `crop_factor:FLOAT`（3 次）
- `canvas_width:INT`（3 次）
- `canvas_height:INT`（3 次）
- `canvas_mode:COMBO`（3 次）
- `select:COMBO`（3 次）
- `bd_grp_face_sample:BDGROUP`（3 次）

## 输出

- `face_refine:MMX_DIR_FACE_REFINE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["脸部检测设置", "face_yolov8m.pt", 0.35, 2.5, 768, 768, "manual", "largest_face", "采样设置", 0.4, 8, "euler", "simple", "inherit`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
