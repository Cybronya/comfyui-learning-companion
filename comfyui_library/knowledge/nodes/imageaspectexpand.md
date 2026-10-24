# ImageAspectExpand

## 节点类型

`ImageAspectExpand`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `aspect_ratios:STRING`（3 次）
- `fill_color:STRING`（3 次）
- `alignment:COMBO`（3 次）

## 输出

- `expanded_image:IMAGE`（3 次）
- `original_mask:MASK`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `selected_ratio:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2048x2048 \n2400x1792 \n1792x2400 \n2528x1696\n1696x2528 \n1856x2304 \n2304x1856 \n2752x1536 \n1536x2752 \n3168x1344",`（1 次）
- `["2048x2048 \n2400x1792 \n1792x2400 \n2528x1696\n1696x2528 \n1856x2304 \n2304x1856 \n2752x1536 \n1536x2752 \n3168x1344",`（1 次）
- `["2048x2048 \n2400x1792 \n1792x2400 \n2528x1696\n1696x2528 \n1856x2304 \n2304x1856 \n2752x1536 \n1536x2752 \n3168x1344 "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
