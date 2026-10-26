# MVEx_MaskToLatentSpace

## 节点类型

`MVEx_MaskToLatentSpace`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `masks:MASK`（8 次）
- `vae:VAE`（8 次）
- `compression:COMFY_DYNAMICCOMBO_V3`（8 次）
- `spatial_method:COMBO`（8 次）
- `temporal_method:COMBO`（8 次）
- `grow_spatial:INT`（8 次）
- `grow_temporal:INT`（8 次）
- `grow_temp_mode:COMBO`（8 次）

## 输出

- `mask:MASK`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "max", "max", 36, 1, "both"]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
