# LayerUtility: ImageReelComposit

## 节点类型

`LayerUtility: ImageReelComposit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `reel_1:Reel`（36 次）
- `reel_2:Reel`（36 次）
- `reel_3:Reel`（36 次）
- `reel_4:Reel`（36 次）
- `font_file:COMBO`（36 次）
- `font_size:INT`（36 次）
- `border:INT`（36 次）
- `color_theme:COMBO`（36 次）

## 输出

- `image1:IMAGE`（36 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Alibaba-PuHuiTi-Heavy.ttf", 40, 8, "light"]`（24 次）
- `["Alibaba-PuHuiTi-Heavy.ttf", 40, 32, "light"]`（12 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
