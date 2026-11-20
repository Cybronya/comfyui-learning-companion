# ArchAi3D_Solid_Color_Image

## 节点类型

`ArchAi3D_Solid_Color_Image`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `reference_image:IMAGE`（3 次）
- `preset_dimensions:COMBO`（3 次）
- `color_mode:COMBO`（3 次）
- `rgb_r:INT`（3 次）
- `rgb_g:INT`（3 次）
- `rgb_b:INT`（3 次）
- `hex_color:STRING`（3 次）
- `debug_mode:BOOLEAN`（3 次）

## 输出

- `solid_image:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2:1 - 768 (1536×768)", "hex", 128, 128, 128, "808080", false]`（2 次）
- `["2:1 - 768 (1536×768)", "hex", 91, 190, 97, "808080", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
