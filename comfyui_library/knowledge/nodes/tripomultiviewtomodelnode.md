# TripoMultiviewToModelNode

## 节点类型

`TripoMultiviewToModelNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `image_left:IMAGE`（2 次）
- `image_back:IMAGE`（2 次）
- `image_right:IMAGE`（2 次）

## 输出

- `model_file:STRING`（2 次）
- `model task_id:MODEL_TASK_ID`（2 次）
- `GLB:FILE_3D_GLB`（2 次）
- `FBX:FILE_3D_FBX`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["v3.1-20260211", "default", true, true, 42, 42, "standard", "original_image", -1, false, "standard", false, false]`（1 次）
- `["v2.5-20250123", "default", true, true, 42, 42, "standard", "original_image", -1, false, "standard", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
