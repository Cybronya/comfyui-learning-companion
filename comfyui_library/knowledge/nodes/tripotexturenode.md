# TripoTextureNode

## 节点类型

`TripoTextureNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `model_task_id:MODEL_TASK_ID,SEGMENT_TASK_ID`（7 次）
- `style_image:IMAGE`（7 次）

## 输出

- `model_file:STRING`（7 次）
- `model task_id:MODEL_TASK_ID`（7 次）
- `GLB:FILE_3D_GLB`（7 次）
- `FBX:FILE_3D_FBX`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, 42, "standard", "original_image", "", "v3.0-20250812", "none", ""]`（7 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
