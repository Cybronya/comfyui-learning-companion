# TopazImageEnhanceV2

## 节点类型

`TopazImageEnhanceV2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `output_width:INT`（2 次）
- `output_height:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Reimagine", "", 3, "All", true, 0, 1, true, false, false, 0, 0]`（1 次）
- `["Bloom 2", "", 3, 649, "randomize", true, false, "silver", 0.5, 1, 0.5, 0, 0]`（1 次）
- `["Wonder 3.5", "high", false, "silver", 0.5, 1, 0.5, 0, 0]`（1 次）
- `["Reimagine", "", 3, "All", true, 0, 1, true, true, false, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
