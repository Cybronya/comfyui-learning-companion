# RH_Tripo3d_Multiview2Model

## 节点类型

`RH_Tripo3d_Multiview2Model`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image_front:IMAGE`（2 次）
- `image_left:IMAGE`（2 次）
- `image_back:IMAGE`（2 次）
- `image_right:IMAGE`（2 次）
- `model_version:COMBO`（2 次）
- `model_seed:INT`（2 次）
- `texture:BOOLEAN`（2 次）
- `pbr:BOOLEAN`（2 次）
- `texture_seed:INT`（2 次）
- `texture_quality:COMBO`（2 次）

## 输出

- `model_file:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["v3.0-20250812", -1, true, true, -1, "standard", "original_image", -1, false, false, false, "default", false, false, "s`（1 次）
- `["v3.0-20250812", -1, true, true, -1, "standard", "original_image", 16000, true, false, false, "default", false, false, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
