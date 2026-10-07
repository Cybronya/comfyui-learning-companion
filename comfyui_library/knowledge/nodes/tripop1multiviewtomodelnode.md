# TripoP1MultiviewToModelNode

## 节点类型

`TripoP1MultiviewToModelNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `image_left:IMAGE`（1 次）
- `image_back:IMAGE`（1 次）
- `image_right:IMAGE`（1 次）

## 输出

- `model_file:STRING`（1 次）
- `model task_id:MODEL_TASK_ID`（1 次）
- `GLB:FILE_3D_GLB`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Textured", true, "detailed", "original_image", "default", 42, -1, 42, false, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
