# EsesImageEffectLevels

## 节点类型

`EsesImageEffectLevels`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `preset:COMBO`（2 次）
- `channel:COMBO`（2 次）
- `all_levels_json:STRING`（2 次）
- `auto_levels:BOOLEAN`（2 次）
- `auto_color:BOOLEAN`（2 次）
- `auto_sensitivity:FLOAT`（2 次）

## 输出

- `adjusted_image:IMAGE`（2 次）
- `adjusted_mask:MASK`（2 次）
- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", "RGB", "{\"r\":{\"black_point\":0,\"mid_point\":1,\"output_white\":255,\"white_point\":1,\"output_black\":0},\"`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
