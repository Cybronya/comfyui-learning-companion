# CalligrapherImageProcesssor

## 节点类型

`CalligrapherImageProcesssor`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `source_image:IMAGE`（10 次）
- `mask_image:IMAGE`（10 次）
- `words:STRING`（10 次）
- `font:COMBO`（2 次）

## 输出

- `condtion:CalligrapherCondition`（10 次）
- `combined_image:IMAGE`（10 次）
- `combined_mask:IMAGE`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["贞贞", "Arial-Unicode-Regular.ttf"]`（7 次）
- `["贞贞", "models/fonts/fronts/07Takibi-Heavy-2.otf"]`（1 次）
- `["真的爱你", "Arial-Unicode-Regular.ttf"]`（1 次）
- `["Formula 1", "Arial-Unicode-Regular.ttf"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
