# YCFaceAlignToCanvas

## 节点类型

`YCFaceAlignToCanvas`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `analysis_models:ANALYSIS_MODELS`（2 次）
- `image:IMAGE`（2 次）
- `canvas_width:INT`（2 次）
- `canvas_height:INT`（2 次）
- `target_face_x:INT`（2 次）
- `target_face_y:INT`（2 次）
- `target_face_width:INT`（2 次）
- `target_face_height:INT`（2 次）
- `padding:INT`（2 次）
- `keep_aspect_ratio:BOOLEAN`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `uncovered_mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, 128, 80, 400, 400, 0, true, 0, "contain", "auto", true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
